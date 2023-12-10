from typing import Dict


BOUNDARY_CONDITIONS_TYPE = ['pressure', 'speed']


class BoundaryConditions:
    def __init__(self,
                 dict_boundaries: Dict[str, str]):
        """
        Class used to save the boundary conditions of the simulation.

        :param dict_boundaries: Dictionnary of type of boundaries for each
            surface.
        :type dict_boundaries: Dict[str, str]
        """
        self.check_conditions(dict_boundaries)
        self.dict_boundaries = dict_boundaries

    def check_conditions(dict_boundaries: Dict[str, str]):
        """
        Check if the boundary conditions respects the naming imposed

        :param dict_boundaries: Dictionnary of type of boundaries for each
            surface.
        :type dict_boundaries: Dict[str, str]
        """
        if set(dict_boundaries.values) == set(BOUNDARY_CONDITIONS_TYPE):
            raise InvalidBoundaryConditionError(
                message=BOUNDARY_CONDITIONS_TYPE - set(dict_boundaries.values))


class InvalidBoundaryConditionError(Exception):
    """
    Exception raised for invalid boundary conditions in CFD simulations.
    """

    def __init__(self,
                 message: str = ''):
        """
        :param message: message of the error, defaults to "Invalid boundary
            condition provided"
        :type message: str, optional
        """
        self.message = "Invalid boundary condition provided" + message
        super().__init__(self.message)
