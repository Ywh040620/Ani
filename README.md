# 最会跳舞的Grok_Ani
 
## 项目简介
基于本地部署的Qwen3模型，内嵌多种舞蹈动作，通过对话触发不同的舞蹈动作，支持长期记忆。

## 功能特性
- 🎵 高质量中文语音合成
- 🎨 简洁美观的用户界面
- ⚡ 实时语音播放
- 📱 响应式设计
- 🔇 多种动作设计

## 使用说明
```bash
# 下载Qwen3，安装依赖
pip install -U huggingface_hub
# 设置环境变量
#Linux
export HF_ENDPOINT=https://hf-mirror.com
#Windows
$env:HF_ENDPOINT = "https://hf-mirror.com"
#下载模型
huggingface-cli download --resume-download Qwen/Qwen3-0.6B --local-dir ./Qwen3-0.6B
#或者
huggingface-cli download --resume-download Qwen/Qwen3-4B --local-dir ./Qwen3-0.6B
huggingface-cli download --resume-download Qwen/Qwen3-8B --local-dir ./Qwen3-0.6B
#效果更好，但需要更大的显存
```
```bash
# 进入项目目录
cd Ani
#推荐使用python3.12
pip install flask
pip install torch
pip install transformers
#运行
python app.py
#点击http://127.0.0.1:5000
#推荐使用edge浏览器，内置的语音效果更好
```

## 许可证声明
本项目采用非商业性使用许可。

### 你可以：
- 个人学习和研究使用
- 在开源社区分享和讨论
- 克隆和修改代码以供个人使用
### 你不可以：
- 将本项目或其衍生作品用于任何商业目的
- 销售本项目或其部分代码
- 在商业产品或服务中使用本项目
- 以盈利为目的使用本项目
- 重新分发用于商业用途


# 版权声明
© 2025 Ywh. 保留所有权利。

### 免责声明
本项目仅供学习交流使用，作者不对使用本项目产生的任何后果承担责任。

联系方式
- GitHub: @Ywh
- 邮箱: 
### 贡献说明
欢迎提交Issue和Pull Request来改进项目，但请确保贡献的内容也遵守相同的非商业使用许可。