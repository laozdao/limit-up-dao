# 老子道·涨停股批量归因分析 (limit-up-dao)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> 🎯 **零遗漏逐一分析** - 基于开源大模型的A股涨停股系统化归因分析工具

## ✨ 核心特性

- 📊 **批量分析**：输入日期，自动获取当日所有涨停股票
- 🔍 **逐一归因**：对每一只股票进行五维度深度分析，零遗漏
- 📈 **量化评分**：消息驱动、资金性质、封板质量、板块共振、连板位置
- 📝 **专业报告**：输出结构化Markdown分析报告
- 🤖 **AI驱动**：基于开源大模型，智能归因涨停原因

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/laozdao/limit-up-dao.git
cd limit-up-dao

# 安装依赖
pip install -r requirements.txt
```

### 使用

```bash
# 获取今日涨停数据
python scripts/fetch_limit_up.py

# 获取指定日期数据
python scripts/fetch_limit_up.py 20260521

# 输出到文件
python scripts/fetch_limit_up.py 20260521 --output
```

### 作为 Skill 使用

将 `limit-up-dao.skill` 文件导入支持 Skill 的 AI 助手，触发关键词：
- "分析今日涨停股"
- "涨停归因分析"
- "涨停板复盘"

## 📖 涨停归因分析模型

本工具基于**老子道涨停归因分析模型**，该模型是A股量化交易领域的系统性归因框架。

### 模型概要

涨停归因分析模型通过**五维评分体系**对涨停股进行全方位解析：

| 维度 | 权重 | 核心要素 |
|------|------|----------|
| **消息驱动** | 20% | 政策利好、业绩超预期、重大事件、行业催化 |
| **资金性质** | 25% | 机构席位、知名游资、量化资金、散户参与度 |
| **封板质量** | 25% | 封板时间、炸板次数、封单量、换手率 |
| **板块共振** | 20% | 同板块涨停数、梯队完整性、龙头效应 |
| **连板位置** | 10% | 首板、2-3板、4-5板、高位板 |

### 模型特点

- **零遗漏分析**：对当日所有涨停股逐一分析，不遗漏任何标的
- **量化评分**：每只股票给出1-5星的五维评分和综合评分
- **归因结论**：综合五维因素得出涨停类型和驱动逻辑
- **次日展望**：基于模型给出次日溢价预期和连板概率

📚 **详细模型文档**：[R05-04 涨停归因分析模型](https://github.com/laozdao/dao-quant-research/blob/main/articles/R05-literature/R05-04-limit-up-attribution-model.md)

## 📋 分析维度

## 📊 示例输出

```
# 20260521 涨停股归因分析报告

## [1/58]. 某某股份（000001）

| 维度 | 分析 | 评分 |
|-----|------|-----|
| 消息驱动 | 新能源汽车政策利好 | ⭐⭐⭐⭐⭐ |
| 资金性质 | 机构买入+知名游资 | ⭐⭐⭐⭐⭐ |
| 封板质量 | 9:35封板，无炸板 | ⭐⭐⭐⭐⭐ |
| 板块共振 | 新能源汽车板块8只涨停 | ⭐⭐⭐⭐⭐ |
| 连板位置 | 3连板，板块龙头 | ⭐⭐⭐⭐ |

**综合评分**: 4.6/5.0 | **涨停类型**: 强势涨停
**归因结论**: 政策驱动+机构资金+板块共振，龙头地位确立
**次日展望**: 高溢价预期，连板概率>70%
```

## 🛠️ 技术栈

- Python 3.8+
- Pandas - 数据处理
- OpenAI API / 开源大模型 - 智能分析

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 📜 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

使用本工具生成的报告需保留以下声明：

> **本报告由开源大模型Skill自动生成 | 仅供参考，不构成投资建议**
> 
> **免责声明**：本报告基于公开数据和大模型分析，**不构成任何投资建议**。市场有风险，投资需谨慎，自主决策，自负盈亏。

## 🙏 致谢

- **理论支撑**：[R05-04 涨停归因分析模型](https://github.com/laozdao/dao-quant-research/blob/main/articles/R05-literature/R05-04-limit-up-attribution-model.md) - 老子道量化研究
- 灵感来源：A股量化交易社区、实盘操作经验、道德经

## 📮 联系方式

- GitHub Issues: [提交问题](https://github.com/laozdao/limit-up-dao/issues)
- 邮箱: laozdao@126.com

---

**⚠️ 重要免责声明**

本工具仅供学习研究使用，不构成投资建议。股市有风险，投资需谨慎。使用者应独立判断并承担投资风险。
