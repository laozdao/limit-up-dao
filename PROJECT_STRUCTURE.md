# 项目结构说明

本文档详细说明 `limit-up-dao` 项目的目录结构和每个文件的用途。

## 📁 目录结构概览

```
limit-up-dao/
├── .github/                    # GitHub 配置目录
├── references/                 # 参考文档目录
├── scripts/                    # 脚本工具目录
├── .gitignore                  # Git 忽略文件配置
├── CHANGELOG.md               # 版本更新日志
├── LICENSE                    # 开源协议文件
├── PROJECT_STRUCTURE.md       # 本文件：项目结构说明
├── README.md                  # 项目主说明文档
├── requirements.txt           # Python 依赖清单
├── setup.py                   # Python 包安装配置
├── SKILL.md                   # Skill 主定义文件
└── limit-up-dao.skill         # 打包后的 Skill 文件
```

---

## 📂 .github/ - GitHub 配置目录

存放所有与 GitHub 相关的配置文件，包括工作流和模板。

### 📁 .github/workflows/ - CI/CD 工作流

| 文件 | 说明 |
|------|------|
| `release.yml` | **自动发布工作流**：当推送 `v*` 标签时自动触发，构建 Python 包并创建 GitHub Release |
| `stale.yml` | **自动清理工作流**：每天检查一次，自动标记 30 天未活动的 Issue/PR，7 天后关闭 |

### 📁 .github/ISSUE_TEMPLATE/ - Issue 模板

| 文件 | 说明 |
|------|------|
| `bug_report.md` | **Bug 报告模板**：用户提交 Bug 时使用的标准模板，包含环境信息、复现步骤等字段 |
| `feature_request.md` | **功能请求模板**：用户提出新功能建议时使用的模板 |

### 📄 .github/PULL_REQUEST_TEMPLATE.md

**PR 模板**：贡献者提交 Pull Request 时使用的模板，包含变更类型、测试情况、检查清单等。

---

## 📂 references/ - 参考文档目录

存放 Skill 使用的参考指南和数据源说明。

| 文件 | 说明 |
|------|------|
| `attribution_guide.md` | **归因分析详细指南**：五维评分标准的详细说明，包括席位识别规则、封板质量评分细则、板块共振判断方法、涨停类型分类、典型场景与案例 |
| `web_sources.md` | **Web 数据源清单**：核心数据源（东方财富、同花顺等）、搜索关键词模板、搜索策略与预算控制、数据提取要点 |

---

## 📂 scripts/ - 脚本工具目录

存放 Python 数据采集脚本。

| 文件 | 说明 |
|------|------|
| `fetch_limit_up.py` | **涨停数据采集脚本**：使用 AkShare 获取指定日期的涨停池、龙虎榜、板块数据，输出 JSON 格式供归因分析使用。支持命令行参数指定日期和输出选项 |

---

## 📄 根目录文件说明

### .gitignore
**Git 忽略配置**：指定哪些文件/目录不应被 Git 跟踪，包括：
- Python 编译缓存（`__pycache__/`）
- 虚拟环境目录（`venv/`、`env/`）
- IDE 配置文件（`.vscode/`、`.idea/`）
- 操作系统文件（`.DS_Store`、`Thumbs.db`）
- 项目生成的数据文件（`*.json`、`*.csv`、`*.xlsx`）
- 敏感信息文件（`credentials.json`、`.env`）

### CHANGELOG.md
**版本更新日志**：记录项目的所有显著变更，遵循 [Keep a Changelog](https://keepachangelog.com/) 格式和 [语义化版本](https://semver.org/) 规范。

当前版本：
- v2.0.0 (2025-05-21)：优化开源声明与免责声明融合
- v1.0.0 (2025-05-21)：初始版本发布

### LICENSE
**开源协议文件**：MIT License

- 允许自由使用、修改、分发，包括商业用途
- 要求保留版权声明和许可声明
- 作者不承担任何责任

### PROJECT_STRUCTURE.md
**本文件**：详细说明项目的目录结构和每个文件的用途。

### README.md
**项目主说明文档**：项目的入口文档，包含：
- 项目简介和核心特性
- 快速开始指南（安装、使用）
- 分析维度说明
- 示例输出
- 技术栈
- 贡献指南
- 开源协议和免责声明

### requirements.txt
**Python 依赖清单**：列出项目运行所需的 Python 包及其版本要求。

| 包名 | 版本 | 用途 |
|------|------|------|
| akshare | >=1.10.0 | 财经数据接口 |
| pandas | >=1.5.0 | 数据处理 |
| requests | >=2.28.0 | HTTP 请求 |
| openai | >=1.0.0 | OpenAI API 调用 |
| python-dotenv | >=1.0.0 | 环境变量管理 |

### setup.py
**Python 包安装配置**：定义包的元数据和安装配置，使项目可以通过 `pip install` 安装。

包含：
- 包名、版本、作者信息
- 依赖项列表
- 入口点配置
- PyPI 分类标签

### SKILL.md
**Skill 主定义文件**：AI 助手使用的 Skill 定义文档，包含：

- **元数据**：name、version、description、author、license
- **Overview**：工具简介和核心原则
- **Workflow**：六步分析流程
- **Step 1-6**：详细的分析步骤说明
- **输出模板**：报告头部、股票卡片、报告尾部的标准格式
- **Resources**：引用的脚本和参考文档
- **注意事项**：使用时的重要提醒

### limit-up-dao.skill
**打包后的 Skill 文件**：将 `SKILL.md`、`references/`、`scripts/` 打包成的 `.skill` 文件，可直接导入支持 Skill 的 AI 助手使用。

---

## 🔄 文件关系图

```
limit-up-dao.skill (打包文件)
    ├── SKILL.md (主定义)
    ├── references/
    │   ├── attribution_guide.md (评分标准)
    │   └── web_sources.md (数据源)
    └── scripts/
        └── fetch_limit_up.py (数据采集)

GitHub 工作流
    ├── release.yml (自动发布)
    └── stale.yml (自动清理)

项目文档
    ├── README.md (用户文档)
    ├── CHANGELOG.md (版本日志)
    ├── LICENSE (开源协议)
    └── PROJECT_STRUCTURE.md (本文件)
```

---

## 📝 维护说明

### 添加新文件时的注意事项

1. **代码文件**：放在 `scripts/` 或新建 `src/` 目录
2. **文档文件**：放在 `references/` 或根目录
3. **配置文件**：放在 `.github/` 对应子目录
4. **更新本文件**：添加新文件后，同步更新 `PROJECT_STRUCTURE.md`

### 版本更新时的文件变更

1. 更新 `SKILL.md` 中的 version 字段
2. 更新 `setup.py` 中的 version 字段
3. 在 `CHANGELOG.md` 中添加新版本记录
4. 重新打包 `limit-up-dao.skill`
5. 创建 Git 标签并推送

---

*最后更新：2025-05-21*
