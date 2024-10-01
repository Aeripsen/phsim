import matplotlib.pyplot as plt
import numpy as np


class Visualizer:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def visualize(self, solution, t):
        theta1, theta2 = solution[:, 0], solution[:, 2]
        x1 = self.l1 * np.sin(theta1)
        y1 = -self.l1 * np.cos(theta1)
        x2 = x1 + self.l2 * np.sin(theta2)
        y2 = y1 - self.l2 * np.cos(theta2)

        fig, ax = plt.subplots()
        ax.plot(x1, y1, label='Pendulum 1')
        ax.plot(x2, y2, label='Pendulum 2')
        plt.legend()
        plt.xlabel('X Position (m)')
        plt.ylabel('Y Position (m)')
        plt.title('Double Pendulum Motion')
        plt.show()
