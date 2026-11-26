from importlib.metadata import version

from galaxy_simulator.galaxy import Galaxy
from galaxy_simulator.celestial_object import CelestialObject


__version__ = version("galaxy_simulator")
__all__ = ["CelestialObject","Galaxy"]