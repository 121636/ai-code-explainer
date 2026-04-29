# AI 代码解释工具（AI Code Explainer）

## 项目简介
这是一个基于 GPT API 的 AI 工具（AI-powered tool），用于自动分析和解释代码逻辑，帮助开发者更高效地理解陌生代码。

## 项目背景
在学习编程或阅读开源项目时，理解复杂代码往往需要花费大量时间。本项目尝试通过大模型能力，对代码进行语义分析并生成解释，从而提升学习和开发效率。

## 核心功能
- 输入任意代码片段
- 自动生成代码解释
- 输出结构化分析结果

## 工作流程（Agent Workflow）
1. 用户输入代码
2. 系统构建 Prompt
3. 调用 GPT 模型进行分析
4. 输出解释结果

该流程包含多步推理（multi-step reasoning），包括代码语义理解、逻辑拆解和自然语言重构。

## 技术栈
- Python
- GPT API
- Prompt Engineering

## 使用场景
- 编程学习
- 阅读 GitHub 开源项目
- 快速理解历史代码（legacy code）

## 使用情况
目前已在个人日常学习中使用，在阅读代码和调试过程中提供辅助支持，平均每日消耗约 5万 Token。

## 后续计划
- 引入多 Agent 协作（解释 + Debug + 优化）
- 支持多轮对话（multi-turn interaction）
- 集成到 Cursor / IDE 等开发工具中
