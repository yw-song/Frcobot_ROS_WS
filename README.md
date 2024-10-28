# frcobot_ros

该项目为法奥机器人ROS API接口，基于法奥SDK库，简化了参数并提供了service接口，用户可以发送字符串指令到接口实现对应的功能。

API函数的介绍见 `API说明.md` 文件

安装教程及说明可以参考法奥文档平台的内容: https://fr-documentation.readthedocs.io/zh-cn/latest/ROSGuide/ros1guide.html

## 测试是否与机器人连接成功

待机械臂第六轴光圈绿色常量之后运行：

```bash
ping 192.168.57.2
```
