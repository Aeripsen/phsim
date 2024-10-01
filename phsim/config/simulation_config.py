import numpy as np


class SimulationConfig:
    def __init__(self, l1=1.0, l2=1.0, m1=1.0, m2=1.0, g=9.81,
                 initial_conditions=None, time_duration=20, time_steps=1000):
        if initial_conditions is None:
            initial_conditions = [np.pi / 4, 0, np.pi / 2,
                                  0]  # [theta1, omega1, theta2, omega2]
        self.l1 = l1
        self.l2 = l2
        self.m1 = m1
        self.m2 = m2
        self.g = g
        self.initial_conditions = initial_conditions
        self.time_duration = time_duration
        self.time_steps = time_steps
        self.time_array = np.linspace(0, self.time_duration, self.time_steps)
