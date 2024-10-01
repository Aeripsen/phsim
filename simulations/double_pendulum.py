import numpy as np
from scipy.integrate import odeint
from .physics_base import PhysicsSimulation


class DoublePendulum(PhysicsSimulation):
    def __init__(self, l1=1.0, l2=1.0, m1=1.0, m2=1.0, g=9.81):
        self.l1 = l1
        self.l2 = l2
        self.m1 = m1
        self.m2 = m2
        self.g = g

    def equations_of_motion(self, y, t):
        theta1, z1, theta2, z2 = y
        cos_delta = np.cos(theta1 - theta2)
        sin_delta = np.sin(theta1 - theta2)

        theta1_dot = z1
        theta2_dot = z2

        z1_dot = (-self.g * (2 * self.m1 + self.m2) * np.sin(
            theta1) - self.m2 * self.g * np.sin(theta1 - 2 * theta2)
                  - 2 * sin_delta * self.m2 * (
                              z2 ** 2 * self.l2 + z1 ** 2 * self.l1 * cos_delta)) / self.l1
        z2_dot = (2 * sin_delta * (
                    z1 ** 2 * self.l1 * (self.m1 + self.m2) + self.g * (
                        self.m1 + self.m2) * np.cos(theta1)
                    + z2 ** 2 * self.l2 * self.m2 * cos_delta)) / self.l2

        return [theta1_dot, z1_dot, theta2_dot, z2_dot]

    def simulate(self, y0, t):
        return odeint(self.equations_of_motion, y0, t)
