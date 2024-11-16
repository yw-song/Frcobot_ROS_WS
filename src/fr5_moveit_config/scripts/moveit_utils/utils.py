import numpy as np
from scipy.spatial.transform import Rotation as R
from moveit_commander.conversions import pose_to_list
import geometry_msgs.msg

def all_close(goal, actual, tolerance):
    if type(goal) is list:
        return all(abs(a - g) < tolerance for a, g in zip(actual, goal))
    elif type(goal) is geometry_msgs.msg.PoseStamped:
        return all_close(goal.pose, actual.pose, tolerance)
    elif type(goal) is geometry_msgs.msg.Pose:
        return all_close(pose_to_list(goal), pose_to_list(actual), tolerance)
    return True

def normal_vector_to_quaternion(nx, ny, nz, ref_x=(1, 0, 0)):
    normal_vector = np.array([nx, ny, nz]) / np.linalg.norm([nx, ny, nz])
    ref_x = np.array(ref_x)
    x_axis = np.cross(normal_vector, ref_x)
    x_axis /= np.linalg.norm(x_axis) if np.linalg.norm(x_axis) > 1e-6 else 1
    y_axis = np.cross(normal_vector, x_axis)
    rotation_matrix = np.column_stack((x_axis, y_axis, normal_vector))
    return R.from_matrix(rotation_matrix).as_quat()
