import numpy as np
from pyquaternion import Quaternion
import xml.etree.ElementTree as ET

#root = ET.parse("/root/Desktop/studying/flyBattle/code/data.xml").getroot()
#rocket = root.find('Rocket')
#d = rocket.find('x')
#d = float(d.text)
#print((d))
#a = d + 60
#print(a)
#itemlist = xmldoc.getElementsByTagName('item')
#print(len(itemlist))
#print(itemlist[0].attributes['name'].value)

x = 5
y = 5
z = 5
v = np.array([1 , 1, 1])

q1 = Quaternion(axis = [0, 0, 1], angle = np.arctan2(y, x))
qv = q1.rotate([0, 1, 0])
q2 = Quaternion(axis= qv, angle = np.arctan2(z, np.sqrt(x**2 + y**2)))
q3 = q2.conjugate * q1

print(q3.rotate(v))
#print(qv)