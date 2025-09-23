from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node

URDF = "/home/samrb-dev/Desktop/Projects/scoutbot/src/scoutbot_design/urdf/urdf.xacro"

def generate_launch_description():
    start_gz = ExecuteProcess(
        cmd=['gz', 'sim', '-v', '4', 'empty.sdf'],  # omit 'empty.sdf' to get default world
        output='screen'
    )

    spawn = TimerAction(
        period=2.0,
        actions=[Node(
            package='ros_gz_sim',
            executable='create',
            arguments=['-name', 'scoutbot',
                       '-file', URDF,
                       '-z', '0.05'],
            output='screen'
        )]
    )

    return LaunchDescription([start_gz, spawn])
