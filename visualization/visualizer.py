import matplotlib.pyplot as plt
import numpy as np


class Visualizer:
    def __init__(self, simulation):
        self.simulation = simulation

    def visualize(self, solution, t, l1, l2):
        theta1, theta2 = solution[:, 0], solution[:, 2]

        x1 = l1 * np.sin(theta1)
        y1 = -l1 * np.cos(theta1)
        x2 = x1 + l2 * np.sin(theta2)
        y2 = y1 - l2 * np.cos(theta2)

        fig, ax = plt.subplots()
        for i in range(0, len(t),
                       5):  # Plot every 5th frame for smoother animation
            ax.clear()
            ax.set_xlim([-2, 2])
            ax.set_ylim([-2, 2])
            ax.plot([0, x1[i]], [0, y1[i]], 'o-', lw=2)
            ax.plot([x1[i], x2[i]], [y1[i], y2[i]], 'o-', lw=2)
            plt.pause(0.01)

        plt.show()
