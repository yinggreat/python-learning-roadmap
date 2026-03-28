# Python 学习路线图

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-teaching--ready-16A34A?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-0F766E?style=flat-square)

![cover](assets/cover.svg)

一套面向初学者、转行者和进阶开发者的 Python 成长路线图，帮助你从基础语法一路走到自动化、公开数据采集、数据分析和 AI 应用项目。

## 这个仓库适合谁

- 想系统学习 Python，但总是东学一点西学一点的人
- 想从零开始做出作品集的大学生和转行者
- 已经会写基础代码，但不知道下一步如何进阶的人

## 你能从这里得到什么

- 一条清晰的 Python 学习路径，而不是碎片化资料
- 每个阶段该学什么、为什么学、学完做什么
- 可直接生成的 12 周学习计划
- 一套更适合自动化、数据和 AI 方向的项目成长框架

## 仓库亮点

- 路线图按真实项目能力设计，而不是只按语法章节堆知识点
- 同时覆盖自动化、数据采集、数据分析、AI 应用 4 条高价值方向
- 附带学习计划生成脚本，适合训练营、训练营助教和自学者直接使用

## 仓库结构

- `data/roadmap.json`：学习阶段定义
- `data/study_profiles.json`：不同学习者画像模板
- `scripts/show_roadmap.py`：按阶段浏览路线图
- `scripts/generate_study_plan.py`：生成个性化学习计划
- `examples/career_switcher_plan.md`：示例学习计划输出

## 快速开始

```bash
python scripts/show_roadmap.py
python scripts/show_roadmap.py --phase automation
python scripts/generate_study_plan.py --track career-switcher --focus automation --weeks 12 --weekly-hours 10 --output examples/career_switcher_plan.md
```

## 推荐学习顺序

1. Foundations：补齐 Python 基础语法和程序思维
2. Automation：先做能提升效率的小项目，建立成就感
3. Public Data Collection：学习公开数据采集、解析和清洗
4. Data Analysis：学会用数据做表达，而不是只会抓数据
5. AI Applications：把 Python 和大模型结合到实际工作流中

## 为什么这个仓库值得 Star

- 它不是空泛的“学习建议”，而是可以落成项目作品的路线图
- 它适合你做 GitHub 作品集的总入口
- 它也适合你做课程大纲、训练营路径、社群打卡计划

## 作者定位

这个仓库服务于这样一种教学理念：

> 把复杂技术拆成可执行步骤，让学习者从“知道”走向“做到”。

## 仓库维护

- 开源协议：`MIT`
- 更新记录见 `CHANGELOG.md`
- 贡献方式见 `CONTRIBUTING.md`
