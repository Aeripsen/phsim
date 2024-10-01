import numpy as np
from scipy.integrate import odeint
from .physics_base import PhysicsSimulation


class DoublePendulum(PhysicsSimulation):
    def __init__(self, l1=1.0, l2=1.0, m1=1.0, m2=1.0, g=9.81):
        super().__init__()
        self.l1 = l1
        self.l2 = l2
        self.m1 = m1
        self.m2 = m2
        self.g = g

    def equations_of_motion(self, y, t):
        theta1, omega1, theta2, omega2 = y
        delta = theta2 - theta1
        dydt = [omega1,
                (-self.g * (2 * self.m1 + self.m2) * np.sin(
                    theta1) - self.m2 * self.g * np.sin(theta1 - 2 * theta2)
                 - 2 * np.sin(delta) * self.m2 * (
                         omega2 ** 2 * self.l2 + omega1 ** 2 * self.l1 * np.cos(
                     delta))) / (self.l1 * (
                        2 * self.m1 + self.m2 - self.m2 * np.cos(
                    2 * delta))),
                omega2,
                (2 * np.sin(delta) * (omega1 ** 2 * self.l1 * (
                        self.m1 + self.m2) + self.g * (
                                              self.m1 + self.m2) * np.cos(
                    theta1)
                                      + omega2 ** 2 * self.l2 * self.m2 * np.cos(
                            delta))) / (self.l2 * (
                        2 * self.m1 + self.m2 - self.m2 * np.cos(
                    2 * delta)))]
        return dydt

    def simulate(self, y0, t):
        return odeint(self.equations_of_motion, y0, t)
