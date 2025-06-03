import numpy as np
from math import sin, cos, radians

class Camera:
    def __init__(self, position=(0, 0, 3), yaw=-90, pitch=0):
        self.position = np.array(position, dtype=np.float32)
        self.yaw = yaw
        self.pitch = pitch
        self.front = np.array([0.0, 0.0, -1.0], dtype=np.float32)
        self.up = np.array([0.0, 1.0, 0.0], dtype=np.float32)
        self.right = np.array([1.0, 0.0, 0.0], dtype=np.float32)
        self.world_up = np.array([0.0, 1.0, 0.0], dtype=np.float32)
        self.update_vectors()

    def update_vectors(self):
        front = np.array([
            cos(radians(self.yaw)) * cos(radians(self.pitch)),
            sin(radians(self.pitch)),
            sin(radians(self.yaw)) * cos(radians(self.pitch))
        ], dtype=np.float32)
        self.front = front / np.linalg.norm(front)
        self.right = np.cross(self.front, self.world_up)
        self.right = self.right / np.linalg.norm(self.right)
        self.up = np.cross(self.right, self.front)
        self.up = self.up / np.linalg.norm(self.up)

    def get_view_matrix(self):
        return self.look_at(self.position, self.position + self.front, self.up)

    def look_at(self, eye, target, up):
        f = (target - eye) / np.linalg.norm(target - eye)
        s = np.cross(f, up)
        s = s / np.linalg.norm(s)
        u = np.cross(s, f)

        view = np.identity(4, dtype=np.float32)
        view[0, 0] = s[0]
        view[0, 1] = s[1]
        view[0, 2] = s[2]
        view[1, 0] = u[0]
        view[1, 1] = u[1]
        view[1, 2] = u[2]
        view[2, 0] = -f[0]
        view[2, 1] = -f[1]
        view[2, 2] = -f[2]
        view[3, 0] = -np.dot(s, eye)
        view[3, 1] = -np.dot(u, eye)
        view[3, 2] = np.dot(f, eye)
        return view

    def process_mouse_movement(self, xoffset, yoffset, constrain_pitch=True):
        sensitivity = 0.1
        xoffset *= sensitivity
        yoffset *= sensitivity

        self.yaw += xoffset
        self.pitch += yoffset

        if constrain_pitch:
            if self.pitch > 89.0:
                self.pitch = 89.0
            if self.pitch < -89.0:
                self.pitch = -89.0

        self.update_vectors()

    def process_keyboard(self, direction, velocity):
        if direction == "FORWARD":
            self.position += self.front * velocity
        if direction == "BACKWARD":
            self.position -= self.front * velocity
        if direction == "LEFT":
            self.position -= self.right * velocity
        if direction == "RIGHT":
            self.position += self.right * velocity
