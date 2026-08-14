from raysect.optical.observer import Observer0D, Pipeline0D
from raysect.optical.observer import PowerPipeline0D as PowerPipeline0D

from .base import Observer0DGroup

def select_pipelines(group: Observer0DGroup, item: int | str) -> tuple[list[Pipeline0D], list[Observer0D]]:
    """
    Selects pipelines of the same type based on index or name from the provided group.

    If name is used, error is raised when more than one pipeline is found in an observer.
    An ValueError is also raised if found pipelines are not of the same type.

    :param Observer0DGroup group: Observer group from which to select pipelines.
    :param str/int item: The index or name of the pipeline to be selected.
    :return list pipelines: matching pipelines
    :return list observers: observers with matching pipelines
    """

def plot_group_total(group: Observer0DGroup, item: int | str = 0, ax: object | None = None) -> object:
    """
    Plots total (wavelength-integrated) signal for each observer in the group.

    :param Observer0DGroup group: Group class with observers holding data to be plotted.
    :param str/int item: The index or name of the pipeline. Default: 0.
    :param Axes ax: Existing matplotlib axes.
    :return Axes ax: Matplotlib axes with plotted spectra
    """

def plot_group_spectra(group: Observer0DGroup, item: int | str = 0, in_photons: bool = False, ax: object | None = None) -> object:
    """
    Plot the spectra observed by each observer in the group for a given pipeline.

    :param Observer0DGroup group: Group class with observers holding data to be plotted.
    :param str/int item: The index or name of the pipeline. Default: 0.
    :param bool in_photons: If True, plots the spectrum in photon/s/nm instead of W/nm.
                            Default is False.
    :param Axes ax: Existing matplotlib axes.
    :return Axes ax: Matplotlib axes with plotted spectra
    """
