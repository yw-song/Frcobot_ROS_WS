# 将 Python 脚本设置为可执行文件

使用以下命令来将脚本设置为可执行文件：

```bash
chmod +x src/fr5_moveit_config/scripts/*.py
```

另外，确保`CMakeLists.txt`文件中包含对`scripts`目录的Python文件安装指令。可以在`CMakeLists.txt`文件的末尾添加以下内容，以确保在构建时将脚本安装为可执行文件：

```cmake
install(PROGRAMS
  scripts/move_group_test.py
  scripts/joint_motion.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

保存更改后，重新编译并运行以下命令：

```bash
catkin_make
source devel/setup.bash
```

### Pose 服务通信
service 调用命令
```bash
rosservice call /GoToPose "{p_x: -0.408007, p_y: 0.446886, p_z: 0.148634, o_x: -0.581810, o_y: -0.812146, o_z: -0.002702, o_w: 0.043688}"
rosservice call /GoToPose "{p_x: -0.4021, p_y: 0.48457, p_z: 0.155652, o_x: -1, o_y: 0, o_z: 0, o_w: 0}"
-0.4021; 0.48457; 0.055652
```

目前机器人处于初始位置的信息：
```bash
[INFO] [1730708787.640200]: 当前末端执行器位置: x=-0.407922, y=0.446886, z=0.148665
[INFO] [1730708787.641351]: 当前末端执行器位置: x=-0.581680, y=-0.812223, z=-0.002739, w=0.043974
```

### Chat with AI
你好，我在实时控制机械臂的过程中遇到了问题，我打算在一个曲面上画一个圆，这就意味着我机械臂末端执行器位置在不断变化的同时，姿态也要不断的变化。我用 ROS MoveIt 中的 move_group.set_pose_target(pose_goal) 这个函数实现的。但是这个画圆的时候就只能将圆分割成多边形然后进行轨迹规划描绘出圆的形状，并不丝滑。MoveIt 中有没有更加丝滑的 API 实现这个功能？