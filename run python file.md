# create package

```Shell
catkin_create_pkg vision rospy sd_msgs
```

```Shell
cd ~/catkin_ws/src/vision
```

```Shell
gedit my_file.py
```

Make the Python file executable by adding the following line at the beginning of the file

```Shell
chmod +x my_file.py
```

```Shell
catkin_make
```

```Shell
source ~/catkin_ws/devel/setup.bash
```

```Shell
roscore
```
