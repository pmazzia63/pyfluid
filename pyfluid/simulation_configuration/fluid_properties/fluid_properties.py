class FluidProperties:
    def __init__(self,
                 temperature: float,
                 pressure: float,
                 speed: float
                 ) -> None:
        """
        Initializes the FluidProperties class with the given parameters.

        :param temperature: The temperature of the fluid.
        :type temperature: float
        :param pressure: The pressure of the fluid.
        :type pressure: float
        :param speed: The speed of the fluid.
        :type speed: float
        """
        self.temperature = temperature
        self.pressure = pressure
        self.speed = speed
