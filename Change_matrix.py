import numpy as np
import math as m


def change_matrix(roll, pitch, yaw):
    roll = roll * m.pi / 180
    pitch = pitch * m.pi / 180
    yaw = yaw * m.pi / 180
    yawMatrix = np.matrix([
        [m.cos(yaw), -m.sin(yaw), 0],
        [m.sin(yaw), m.cos(yaw), 0],
        [0, 0, 1]
    ])

    pitchMatrix = np.matrix([
        [m.cos(pitch), 0, m.sin(pitch)],
        [0, 1, 0],
        [-m.sin(pitch), 0, m.cos(pitch)]
    ])

    rollMatrix = np.matrix([
        [1, 0, 0],
        [0, m.cos(roll), -m.sin(roll)],
        [0, m.sin(roll), m.cos(roll)]
    ])

    R = yawMatrix * pitchMatrix * rollMatrix

    return R
