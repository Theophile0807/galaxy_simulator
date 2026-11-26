from importlib.metadata import version
from src.galaxy_simulator import CelestialObject

__version__ = version("galaxy_simulator")
__all__ = ["CelestialObject"]