使用或调试 fr5_moveit_config 功能包中遇到的一些问题以及处理
## 将 Python 脚本设置为可执行文件

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

## Pose 服务通信
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

## MoveIt API 问题

对于如下 API：
```python
(plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.01)
move_group.execute(plan, wait=True)
```
`fraction` 的数值代表规划出的笛卡尔路径占预期路径的比例。它的范围在 `0.0` 到 `1.0` 之间，表示成功规划的路径占所有路径点的比例。`fraction` 越接近 `1.0`，表示规划的路径越完整。例如：

- `fraction = 1.0` 表示 MoveIt 成功规划了整个路径，没有丢失任何路径点。
- `fraction < 1.0` 表示 MoveIt 只规划了部分路径，可能因为某些路径点无法到达或超出规划器的限制。

`fraction` 的数值会受到多个因素的影响，主要包括以下几点：

- **目标点的可达性**：如果某些路径点超出了机械臂的运动范围或机械臂姿态超出了关节限制，MoveIt 就无法规划完整路径，导致 `fraction` 降低。

- **轨迹的分辨率**：`compute_cartesian_path` 中的第二个参数（步长，如 `0.01`）定义了路径分辨率。步长越小，路径点越多，也可能增加路径规划失败的风险。如果步长太大，路径可能会不够平滑。因此，步长的选择会影响 `fraction`。

- **避障要求**：如果启用了避障，机械臂可能会避开障碍物，导致某些路径点无法规划成功，减少了 `fraction`。

- **逆解（IK）求解器的精度**：逆解求解器负责找到每个路径点对应的关节角度组合。如果逆解求解器对某些点求解失败，路径就会中断，从而降低 `fraction`。

- **时间限制和运动规划的配置**：MoveIt 规划器的时间限制、迭代次数等设置都会影响路径规划的完成度。如果设置的时间较短，可能导致路径规划未完成，`fraction` 也会偏低。
