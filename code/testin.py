import numpy as np
from pyquaternion import Quaternion
x = 5
y = 5
z = 5
v = np.array([1, 0, 0])

q1 = Quaternion(axis = [0, 0, 1], angle = np.arctan2(y, x))
q2 = Quaternion(axis=[0, 1, 0], angle = np.arctan2(-z, np.sqrt(x**2 + y**2)))
q3 = q1 * q2
v = q3.rotate(v)
print(v)