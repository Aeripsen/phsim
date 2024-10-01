from simulations.double_pendulum import DoublePendulum
from visualization.visualizer import Visualizer
from utils.chaos_plotter import plot_chaos_sensitivity
from config.simulation_config import SimulationConfig

class SimulationManager:
    def __init__(self, config):
        self.config = config

    def run_single_simulation(self):
        pendulum = DoublePendulum(self.config.l1, self.config.l2, self.config.m1, self.config.m2, self.config.g)
        solution = pendulum.simulate(self.config.initial_conditions, self.config.time_array)

        visualizer = Visualizer(self.config.l1, self.config.l2)
        visualizer.visualize(solution, self.config.time_array)

    def run_multiple_simulations(self, small_change, num_runs=10):
        for i in range(num_runs):
            delta = small_change * i
            new_conditions = self.config.initial_conditions.copy()
            new_conditions[0] += delta  # Small change in theta1 for chaos testing
            plot_chaos_sensitivity(self.config.initial_conditions, delta, self.config.time_array,
                                   self.config.l1, self.config.l2, self.config.m1, self.config.m2, self.config.g)
