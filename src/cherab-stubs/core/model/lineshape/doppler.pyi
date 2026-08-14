from raysect.core.math import Vector3D

def doppler_shift(wavelength: float, observation_direction: Vector3D, velocity: Vector3D) -> float:
    """
    Calculates the Doppler shifted wavelength for a given velocity and observation direction.

    :param wavelength: The wavelength to Doppler shift in nanometers.
    :param observation_direction: A Vector defining the direction of observation.
    :param velocity: A Vector defining the relative velocity of the emitting source in m/s.
    :return: The Doppler shifted wavelength in nanometers.
    """

def thermal_broadening(wavelength: float, temperature: float, atomic_weight: float) -> float:
    """
    Returns the line width for a gaussian line as a standard deviation.

    :param wavelength: Central wavelength.
    :param temperature: Temperature in eV.
    :param atomic_weight: Atomic weight in AMU.
    :return: Standard deviation of gaussian line.
    """
