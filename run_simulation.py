import numpy as np
from simulations.double_pendulum import DoublePendulum
from visualization.visualizer import Visualizer


def main():
    # Initialize the Double Pendulum simulation
    pendulum = DoublePendulum(l1=1.0, l2=1.0, m1=1.0, m2=1.0, g=9.81)

    # Initial conditions: [theta1, theta1_dot, theta2, theta2_dot]
    y0 = [np.pi / 2, 0, np.pi / 4, 0]

    # Time points for simulation
    t = np.linspace(0, 10, 1000)

    # Simulate the system
    solution = pendulum.simulate(y0, t)

    # Visualize the result
    visualizer = Visualizer(pendulum)
    visualizer.visualize(solution, t, pendulum.l1, pendulum.l2)


if __name__ == "__main__":
    main()
