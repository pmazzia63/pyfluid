"""
This file contains the implementation of the SimulationController class.
"""
from pyfluid.simulation_configuration.boundary_conditions.boundary_conditions \
    import BoundaryConditions
from pyfluid.simulation_configuration.fluid_properties.fluid_properties \
    import FluidProperties
from pyfluid.simulation_configuration.geometry_properties.geometry_properties \
    import GeometryProperties
from pyfluid.simulation_configuration.performance_settings \
        .performance_settings import PerformanceSettings
from pyfluid.simulation_configuration.simulation_parameters \
        .simulation_parameters import SimulationParameters
from pyfluid.simulation_configuration.solver_settings.solver_settings \
    import SolverSettings


class SimulationController:
    def __init__(self,
                 boundary_conditions: BoundaryConditions,
                 fluid_properties: FluidProperties,
                 geometry_properties: GeometryProperties,
                 performance_settings: PerformanceSettings,
                 simulation_parameters: SimulationParameters,
                 solver_settings: SolverSettings
                 ) -> None:
        """
        Create a new SimulationController instance.

        :param boundary_conditions: Boundary conditions of the simulation
        :type boundary_conditions: BoundaryConditions
        :param fluid_properties: Properties of the fluid
        :type fluid_properties: FluidProperties
        :param geometry_properties: Geometry of the simulation
        :type geometry_properties: GeometryProperties
        :param performance_settings: Settings for the performance of the
            simulation
        :type performance_settings: PerformanceSettings
        :param simulation_parameters: Parameters of the simulation
        :type simulation_parameters: SimulationParameters
        :param solver_settings: Settings of the solver
        :type solver_settings: SolverSettings
        """
        self.boundary_conditions = boundary_conditions
        self.fluid_properties = fluid_properties
        self.geometry_properties = geometry_properties
        self.performance_settings = performance_settings
        self.simulation_parameters = simulation_parameters
        self.solver_settings = solver_settings
