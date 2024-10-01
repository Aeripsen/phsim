import numpy as np
from simulations.double_pendulum import DoublePendulum
from visualization.visualizer import Visualizer
from utils.chaos_plotter import plot_chaos_sensitivity


def main():
    # Parameters
    l1, l2 = 1.0, 1.0
    m1, m2 = 1.0, 1.0
    g = 9.81
    t = np.linspace(0, 20, 1000)
    initial_conditions = [np.pi / 4, 0, np.pi / 2,
                          0]  # [theta1, omega1, theta2, omega2]

    # Run Simulation for Double Pendulum
    pendulum = DoublePendulum(l1, l2, m1, m2, g)
    solution = pendulum.simulate(initial_conditions, t)

    # Visualize the results
    visualizer = Visualizer(l1, l2)
    visualizer.visualize(solution, t)

    # Plot chaos sensitivity (small change in theta1)
    small_change = 0.01
    plot_chaos_sensitivity(initial_conditions, small_change, t, l1, l2, m1, m2,
                           g)


if __name__ == "__main__":
    main()
