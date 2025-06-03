import numpy as np
import math
from OpenGL.GLU import gluLookAt

class Camera:
    def __init__(self, position):
        self.position = np.array(position, dtype=np.float32)
        self.yaw = -90.0
        self.pitch = 0.0
        self.speed = 0.15
        self.sensitivity = 0.15

    def get_front(self):
        yaw_rad = math.radians(self.yaw)
        pitch_rad = math.radians(self.pitch)
        front = np.array([
            math.cos(yaw_rad) * math.cos(pitch_rad),
            math.sin(pitch_rad),
            math.sin(yaw_rad) * math.cos(pitch_rad)
        ])
        return front / np.linalg.norm(front)

    def get_right(self):
        return np.cross(self.get_front(), np.array([0, 1, 0]))

    def move(self, direction):
        front = self.get_front()
        right = self.get_right()
        if direction == 'FORWARD':
            self.position += front * self.speed
        elif direction == 'BACKWARD':
            self.position -= front * self.speed
        elif direction == 'LEFT':
            self.position -= right * self.speed
        elif direction == 'RIGHT':
            self.position += right * self.speed

    def mouse_move(self, dx, dy):
        self.yaw += dx * self.sensitivity
        self.pitch -= dy * self.sensitivity
        self.pitch = max(-89.0, min(89.0, self.pitch))

    def apply(self):
        front = self.get_front()
        center = self.position + front
        gluLookAt(*self.position, *center, 0, 1, 0)
