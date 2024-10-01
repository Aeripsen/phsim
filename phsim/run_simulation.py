from config.simulation_config import SimulationConfig
from utils.simulation_manager import SimulationManager


def main():
    # Example: Run a single simulation
    config = SimulationConfig()
    manager = SimulationManager(config)
    manager.run_single_simulation()

    # Example: Run multiple simulations to generate chaos charts
    manager.run_multiple_simulations(small_change=0.01, num_runs=10)


if __name__ == "__main__":
    main()
