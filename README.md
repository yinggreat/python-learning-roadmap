# Python 学习路线图

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-teaching--ready-16A34A?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-0F766E?style=flat-square)

![cover](assets/cover.svg)

一套面向初学者、转行者和进阶开发者的 Python 成长路线图，帮助你从基础语法一路走到自动化、公开数据采集、数据分析和 AI 应用项目。

这个仓库不是“资料堆砌型导航页”，而是一个可以直接拿来做学习规划、课程大纲、训练营路径和作品集总入口的路线图仓库。

## 这个仓库适合谁

- 想系统学习 Python，但总是东学一点西学一点的人
- 想从零开始做出作品集的大学生和转行者
- 已经会写基础代码，但不知道下一步如何进阶的人
- 想把自动化、数据分析和 AI 应用串成一条成长路径的人

## 你可以立刻用它做什么

- 按阶段浏览一条完整的 Python 成长路线
- 生成 8 周、12 周或更长周期的学习计划
- 给训练营、社群或课程设计阶段化学习安排
- 把它作为 GitHub 置顶仓库中的“总入口”

## 仓库亮点

- 路线图按真实项目能力设计，而不是只按语法章节堆知识点
- 同时覆盖自动化、数据采集、数据分析、AI 应用 4 条高价值方向
- 附带学习计划生成脚本，适合训练营助教和自学者直接使用
- 能很好地支撑“我不是只会写代码，我是有教学体系的”这种讲师形象

## 当前包含内容

1. Python 五阶段成长路线
2. 不同人群的学习画像模板
3. 个性化学习计划生成脚本
4. 示例学习计划输出

## 效果预览

运行：

```bash
python scripts/generate_study_plan.py --track career-switcher --focus automation --weeks 12 --weekly-hours 10 --output examples/career_switcher_plan.md
```

会生成类似这样的阶段计划：

```md
### Week 3 | Automation
- 本周目标：Use Python to solve repetitive office and workflow problems with scripts that save time.
- 重点关键词：argparse
- 建议项目：meeting note formatter
- 建议投入：10 小时
```

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

## 推荐使用方式

- 如果你是初学者：先跑 `show_roadmap.py`，再生成自己的 12 周计划
- 如果你是讲师：把这个仓库放在置顶第一位，作为其他 5 个项目仓库的总导航
- 如果你是转行者：结合项目仓库同步推进，边学边产出作品

## 为什么这个仓库值得 Star

- 它不是空泛的“学习建议”，而是可以落成项目作品的路线图
- 它既能服务个人学习，也能服务课程设计和训练营教学
- 它非常适合强化“有体系、有方法、有教学能力”的个人品牌

## 后续更新计划

- 增加更细分的学习画像，如“大学生求职型”“在职提效型”
- 增加路线图可视化导出能力
- 增加与其他项目仓库的联动推荐

## 作者定位

这个仓库服务于这样一种教学理念：

> 把复杂技术拆成可执行步骤，让学习者从“知道”走向“做到”。

## 仓库维护

- 开源协议：`MIT`
- 更新记录见 `CHANGELOG.md`
- 贡献方式见 `CONTRIBUTING.md`
