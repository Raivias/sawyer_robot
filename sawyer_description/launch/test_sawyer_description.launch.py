import os
import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

# Params electric_gripper:=true

# Load the URDF into a parameter
sawyer_desc_dir = get_package_share_directory('saywer_description')
# compose urdf at launch
urdf_path = os.path.join(sawyer_desc_dir, 'urdf', 'sawyer_base.urdf')
urdf = open(urdf_path).read()

# Add this to your LaunchDescription
def generate_launch_description():
    robot_state_pub = Node(
        name='robot_state_publisher',
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': urdf}],
    )

    test_base_to_world = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        output='screen',
        arguments=[
            {'x': 0}, 
            {'y': 0}, 
            {'z': 0}, 
            {'qx': 0}, 
            {'qy': 0}, 
            {'qz': 0},
            {'qw': 1},
            {'frame-id': 'world'},
            {'child_frame': 'base_link'},
            ]
        )

    rviz2_node = Node(
        name="rviz2",
        package="rviz2",
        executable="rviz2",
        parameters=[{}]  # TODO(xguay)
    )

    return launch.LaunchDescription([
            robot_state_pub,
            # joint_state_node
            test_base_to_world,
            rviz2_node,
            # ros2_control_node,
        ])
