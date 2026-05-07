# DeepSeek 自动化系统

> 🤖 自动调用 DeepSeek 专家模式 + 深度思考 + 联网搜索

## ✨ 功能特点

- ✅ **专家模式** - 使用 DeepSeek-R1 模型
- ✅ **深度思考** - 启用深度思考功能  
- ✅ **联网搜索** - 自动搜索最新信息
- ✅ **代码提取** - 自动提取代码块
- ✅ **打包下载** - 生成跨平台代码包

## 🚀 快速开始

### 环境要求

- Python 3.8+
- 浏览器（Chrome）

### 安装步骤

```bash
# 1. 下载并解压项目
git clone https://github.com/g11ma20230417/deepseek-automation.git
cd deepseek-automation

# 2. 安装依赖
pip install -r requirements.txt
playwright install chromium
```

### 使用方法

```bash
# 方式1：交互模式
python main.py

# 方式2：直接传任务
python main.py "帮我写一个Python爬虫"
```

### 使用示例

```bash
# 示例1：写代码
python main.py "帮我写一个Python爬虫，爬取豆瓣电影Top250"

# 示例2：分析问题
python main.py "解释什么是人工智能"

# 示例3：生成网页
python main.py "创建一个简单的登录页面"
```

## 📁 项目结构

```
deepseek-automation/
├── main.py                    # 主程序入口
├── requirements.txt           # 依赖列表
├── scripts/
│   ├── deepseek_controller.py    # DeepSeek浏览器控制器
│   ├── code_generator.py         # 代码生成器
│   └── cross_platform_deployer.py # 跨平台部署器
└── config/
    └── deepseek-config.yaml      # 配置文件
```

## 🎯 工作流程

```
用户提问
    ↓
打开 DeepSeek 网页
    ↓
激活专家模式 + 深度思考 + 联网搜索
    ↓
发送问题
    ↓
获取响应
    ↓
提取代码并打包
    ↓
提供下载链接
```

## ⚠️ 注意事项

1. **首次运行需要登录** - 只需登录一次
2. **需要网络连接** - 要访问 DeepSeek
3. **浏览器会自动打开** - 不要关闭

## 📄 更新日志

### v1.0.0 (2026-05-07)
- ✨ 初始版本发布
- ✅ 支持专家模式
- ✅ 支持深度思考
- ✅ 支持联网搜索
- ✅ 自动代码提取和打包

## 📬 反馈

如有问题或建议，请在 Issues 中提出！

---

Made with ❤️ by AI Assistant
