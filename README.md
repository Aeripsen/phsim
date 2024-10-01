# Physics Simulations

This project is a physics simulation platform, starting with a **double pendulum simulation**. It is designed to be modular and scalable, allowing for easy extension with new physics simulations and visualization methods.

## Features:
- **Double Pendulum Simulation**: Models the chaotic motion of a double pendulum.
- **Real-Time Visualization**: Displays the simulation in real-time using `matplotlib`.
- **Modular Design**: Easily add new simulations by implementing the `PhysicsSimulation` base class.

## How to Run:
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the simulation:
    ```bash
    python run_simulation.py
    ```

## Future Development:
- Add more complex systems like **fluid dynamics** or **chaotic systems**.
- Implement **GUI controls** for interactive parameter adjustment.
- Improve performance using **GPU acceleration**.
