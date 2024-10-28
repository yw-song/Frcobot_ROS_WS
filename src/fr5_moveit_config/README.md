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
