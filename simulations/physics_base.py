class PhysicsSimulation:
    def __init__(self):
        pass

    def equations_of_motion(self, *args):
        raise NotImplementedError("Subclasses must implement equations_of_motion method.")

    def simulate(self, y0, t, params):
        raise NotImplementedError("Subclasses must implement simulate method.")
