# ros melodic in jetson nano

```Shell
sudo apt-get update
```

```Shell
sudo apt-get upgrade
```

```Shell
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu bionic main" > /etc/apt/sources.list.d/ros-latest.list'
```

```Shell
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```

```Shell
sudo apt-get update

```

```Shell
sudo apt-get install -y python-rosdep
```

```Shell
sudo apt-get update
```

```Shell
sudo apt-get install python3-catkin-pkg
```

```Shell
sudo apt-get install python3-rosinstall
```

```Shell
sudo apt-get install python3-rosinstall-generator python3-wstool build-essential
```

```Shell
sudo apt-get install ros-melodic-desktop-full
```

or

## if we need to remove previous ros then

sudo apt-get remove ros-melodic-\*
sudo rm -rf /etc/ros /opt/ros/melodic /ros_entrypoint.sh

```Shell
sudo rosdep init
```

```Shell
rosdep update
```

```Shell
source /opt/ros/melodic/setup.bash
```

```Shell
source ~/.bashrc
```

## now make catkin workspace env

```Shell
mkdir -p ~/catkin_ws/src
```

```Shell
cd ~/catkin_ws/
```

## create package

```Shell
catkin_create_pkg duburi std_msgs rospy roscpp
```

## build

```Shell
catkin_make
```

```Shell
source devel/setup.bash
```

```Shell
source ~/catkin_ws/devel/setup.bash
```

```Shell
roscore
```

## Installing and using SMACH-ROS

```Shell
sudo apt-get install ros-melodic-smach ros-melodic-smach-ros ros-melodic-executive-smach ros-melodic-smach-viewer
```

```Shell
rosrun smach_viewer smach_viewer.py
```
