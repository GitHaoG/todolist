## 描述

用来学习langchain和tinker的项目，要做什么暂时没想好

### 简单设计一下

- config 提供程序配置 像是 Api什么的
- ui 可视化部分
- tool Agent调用
- ai的一些工作流设计
- orm 查本地数据库

### 程序流程设计

桌面程序启动 -> 等待用户输入 -> 输入对话内容 -> 发送信息给API去调用工具


#### 接口设计

#### 数据库

任务 先设定下面几个字段：

id name description startTime expectTime endTime taskLevel IsCompleted IsDeleted

#### ui设计
