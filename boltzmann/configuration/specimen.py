import numpy as np
from matplotlib.colors import cnames as mpl_colors


class Specimen:
    """Encapsulates all data of a single simulated specimen."""
    def __init__(self,
                 name,
                 color,
                 mass,
                 collision_rate
                 ):
        self.name = name
        self.color = color
        self.mass = mass
        self.collision_rate = collision_rate
        self.check_integrity()
        return

    #####################################
    #            Verification           #
    #####################################
    def check_integrity(self, complete_check=True):
        """Sanity Check.
        Calls :meth:`check_parameters` to check validity of all attributes.

        Parameters
        ----------
        complete_check : :obj:`bool`, optional
            If True, then all attributes must be set (not None).
            If False, then unassigned attributes are ignored.
        """
        self.check_parameters(name=self.name,
                              color=self.color,
                              mass=self.mass,
                              collision_rate=self.collision_rate,
                              complete_check=complete_check)
        # Additional Conditions on instance:
        # parameter can also be a list,
        # instance attributes must be nd.array
        assert isinstance(self.collision_rate, np.ndarray)
        # parameter can also be list/array of ints,
        # instance attribute must be nd.array of floats
        assert self.collision_rate.dtype is float
        return

    @staticmethod
    def check_parameters(name=None,
                         color=None,
                         mass=None,
                         collision_rate=None,
                         complete_check=False):
        """Sanity Check.
        Checks integrity of given parameters and their interactions.

        Parameters
        ----------
        name : :obj:`str`, optional
        color : :obj:`str`, optional
        mass : :obj:`int`, optional
        collision_rate : :obj:`np.ndarray` of :obj:`float`, optional
            Determines the collision probability between two specimen.
            Should be a row or column of :attr:`collision_rate_matrix`.
        complete_check : :obj:`bool`, optional
            If True, then all parameters must be set (not None).
            If False, then unassigned parameters are ignored.
        """
        # For complete check, assert that all parameters are assigned
        if complete_check is True:
            assert all([param is not None for param in locals().values()])
        else:
            assert isinstance(complete_check, bool)

        # check all parameters, if set
        if name is not None:
            assert type(name) is str
            assert len(name) > 0

        if color is not None:
            assert type(color) is str
            assert color in mpl_colors

        if mass is not None:
            assert type(mass) in [int, np.int64]
            assert mass > 0

        if collision_rate is not None:
            # lists are also accepted as parameters
            if isinstance(collision_rate, list):
                collision_rate = np.array(collision_rate)
            assert isinstance(collision_rate, np.ndarray)
            assert len(collision_rate.shape) == 1
            assert collision_rate.dtype in [int, float]
            assert np.all(collision_rate >= 0)
        return

    def print(self, print_collision_rate=False):
        """Prints all Properties for Debugging."""
        print("Name of Specimen  = {}".format(self.name))
        print("Color of Specimen = {}".format(self.color))
        print("Mass of Specimen = {}".format(self.mass))
        if print_collision_rate:
            print("Collision-Factors = \n{}".format(self.collision_rate))
        return