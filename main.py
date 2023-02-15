import numpy as np


def quaternionTransformed(n, a):
    if not isinstance(n, tuple):
        raise TypeError("Expected a tuple, received ", type(n))

    for element in n:
        if abs(element) > 1:
            # We stock the normalized vector in the variable n so its components can be used in the code right under.
            n = vectorNormalized(n)

    a = a/180 * np.pi
    w = np.cos(a/2)
    x = n[0] * np.sin(a/2)
    y = n[1] * np.sin(a/2)
    z = n[2] * np.sin(a/2)

    q = np.array([w, x, y, z])

    return q


def vectorNormalized(n):
    nMag = np.sqrt((n[0])**2 + (n[1])**2 + (n[2])**2)
    n = (n[0]/nMag, n[1]/nMag, n[2]/nMag)

    return n


def rotatePoint(q, v):
    # Since we previously normalized the vector, the quaternion is aslo normalized so the imaginary vector composing it is a unit vector.
    # So the inverse of the quaternion is equal to the conjugate of the quaternion.
    qVec = q[1:4]
    uv = np.cross(qVec, v)
    uuv = np.cross(qVec, uv)
    result = v + (((uv * q[0]) + uuv) * 2.0)

    lst = []
    for element in result:
        if '{:6f}'.format(element, 6) == '-0.000000':
            lst += ['{:6f}'.format(abs(element), 6), ]
        else:
            lst += ['{:6f}'.format(element, 6), ]

    return lst


def multiplyQuaternions(q1, q2):
    result = np.array([(q1[0]*q2[0])-(q1[1]*q2[1])-(q1[2]*q2[2])-(q1[3]*q2[3]), (q1[0]*q2[1])+(q1[1]*q2[0])+(q1[2]*q2[3])-(q1[3] *
                      q2[2]), (q1[0]*q2[2])-(q1[1]*q2[3])+(q1[2]*q2[0])+(q1[3]*q2[1]), (q1[0]*q2[3])+(q1[1]*q2[2])-(q1[2]*q2[1])+(q1[3]*q2[0])])

    return result


q1 = quaternionTransformed((1, 0, 0), 45)
q2 = quaternionTransformed((0, 1, 0), 90)
v = np.array([1, 0, 0])
q1q2 = multiplyQuaternions(q1, q2)
print(rotatePoint(q1, v), rotatePoint(q2, v), rotatePoint(q1q2, v))
