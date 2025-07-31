from flask import Flask, render_template, send_from_directory, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)


# AI聊天机器人类
class QwenChatbot:
    def __init__(self, model_name="./Qwen3-0.6B"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.history = []
        f = open("./promet.txt", "r", encoding="utf-8")
        for line in f:
            self.history.append({"role": "user", "content": line})
        f.close()
        print("AI模型加载完成")

    def generate_response(self, user_input):
        # 将用户输入添加到历史记录
        self.history.append({"role": "user", "content": user_input})

        # 使用历史记录构建对话上下文
        text = self.tokenizer.apply_chat_template(
            self.history,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False
        )

        # 编码输入
        inputs = self.tokenizer(text, return_tensors="pt")

        # 生成回复
        response_ids = self.model.generate(
            **inputs,
            max_new_tokens=500,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.1

        )[0][len(inputs.input_ids[0]):].tolist()

        response = self.tokenizer.decode(response_ids, skip_special_tokens=True)
        response = response.replace('```json', '').replace('```', '').strip()

        # 将AI回复添加到历史记录
        self.history.append({"role": "assistant", "content": response})

        return response

    def clear_history(self):
        """清空对话历史"""
        self.history = []


# 全局AI聊天机器人实例
chatbot = None

# 忽略 favicon 请求错误
@app.route('/favicon.ico')
def favicon():
    return '', 204  # 返回空内容，状态码 204 (No Content)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/model/<path:filename>')
def serve_model(filename):
    return send_from_directory('model', filename)


@app.route('/action/<path:filename>')
def serve_action(filename):
    return send_from_directory('action', filename)


@app.route('/music/<path:filename>')
def serve_music(filename):
    return send_from_directory('music', filename)


@app.route('/api/chat', methods=['POST'])
def chat_with_ai():
    global chatbot

    try:
        # 获取 JSON 数据
        data = request.get_json()

        if not data or 'message' not in data:
            return jsonify({'error': '缺少消息内容'}), 400

        user_message = data['message']

        # 初始化AI模型（如果还没有初始化）
        if chatbot is None:
            chatbot = QwenChatbot()

        # 生成AI回复
        ai_response = chatbot.generate_response(user_message)

        return jsonify({'response': ai_response}), 200

    except Exception as e:
        print(f"AI聊天时出错: {str(e)}")
        return jsonify({'error': 'AI回复生成失败'}), 500


@app.route('/api/clear_chat_history', methods=['POST'])
def clear_chat_history():
    global chatbot

    try:
        if chatbot is not None:
            chatbot.clear_history()

        return jsonify({'message': '对话历史已清空'}), 200

    except Exception as e:
        print(f"清空对话历史时出错: {str(e)}")
        return jsonify({'error': '清空失败'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)