## Build

```bash
colcon build
```

## Visualize URDF

```bash
ros2 launch urdf_tutorial display.launch.py model:=/home/samrb-dev/Desktop/Projects/scoutbot/src/scoutbot_design/urdf/urdf.xacro
```

## Run Gazebo Launch file for URDF

```bash
ros2 launch scoutbot_design gazebo.launch.py 
```