import numpy as np
from pyquaternion import Quaternion
x = 5
y = 5
z = 5
v = np.array([1, 0, 0])

q1 = Quaternion(axis = [0, 0, 1], angle = np.arctan2(y, x))
q2 = Quaternion(axis=[0, 1, 0], angle = np.arctan2(-z, np.sqrt(x**2 + y**2)))
q3 = q1 * q2
v1 = q3.rotate(v)
v2 = q1.rotate(v)
v3 = q2.rotate(v2)
print("q1: {}\n q2:{} \n q3: {} \n v1: {}  \n v2: {} \n v3:{}".format(q1, q2, q3, v1, v2, v3))