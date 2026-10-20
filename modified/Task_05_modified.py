import numpy as np

# Drone waypoints in 3D (x, y, z) metres
waypoints = np.array([
    [0.0, 0.0, 0.0],
    [10.0, 0.0, 2.0],
    [10.0, 10.0, 2.0],
    [0.0, 10.0, 2.0],
])

yaw   = np.deg2rad(30)
pitch = np.deg2rad(15)

Rz = np.array([[np.cos(yaw), -np.sin(yaw), 0],
               [np.sin(yaw),  np.cos(yaw), 0],
               [0,            0,           1]])

Ry = np.array([[ np.cos(pitch), 0, np.sin(pitch)],
               [ 0,             1, 0           ],
               [-np.sin(pitch), 0, np.cos(pitch)]])

T = Rz @ Ry
rotated = waypoints @ T.T

print("Original waypoints:\n", waypoints)
print("Combined rotation:\n", T)
print("Rotated waypoints:\n", rotated)
print("Determinant (volume scale):", np.linalg.det(T))