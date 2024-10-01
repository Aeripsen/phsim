import numpy as np
import matplotlib.pyplot as plt
from simulations.double_pendulum import DoublePendulum

def plot_chaos_sensitivity(initial_conditions, small_change, t, l1, l2, m1, m2, g):
    pendulum = DoublePendulum(l1, l2, m1, m2, g)

    # Simulate for original initial condition
    solution_1 = pendulum.simulate(initial_conditions, t)

    # Simulate for slightly changed initial condition (small change in angle)
    modified_conditions = initial_conditions.copy()
    modified_conditions[0] += small_change  # Change in theta1
    solution_2 = pendulum.simulate(modified_conditions, t)

    # Plot difference between the two trajectories
    plt.figure()
    plt.plot(t, solution_1[:, 0] - solution_2[:, 0], label='Difference in Theta1')
    plt.plot(t, solution_1[:, 2] - solution_2[:, 2], label='Difference in Theta2')
    plt.xlabel('Time (s)')
    plt.ylabel('Difference in Angle (radians)')
    plt.title('Sensitivity to Initial Conditions (Chaos)')
    plt.legend()
    plt.savefig('results/chaos_sensitivity.png')
    plt.show()
