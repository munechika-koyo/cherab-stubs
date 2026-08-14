from .efit import EFITEquilibrium

def plot_equilibrium(
    equilibrium: EFITEquilibrium,
    detail: bool = False,
    resolution: float = 0.025,
) -> None:
    """
    Generates some overview plots of a given EFIT equilibrium.

    :param equilibrium: The input EFIT equilibrium object.
    :param detail: If true, prints additional information about the equilibrium.
    :param float resolution: Spatial resolution for sampling (default=0.025).

    .. code-block:: pycon

       >>> from cherab.tools.equilibrium import example_equilibrium, plot_equilibrium
       >>>
       >>> equilibrium = example_equilibrium()
       >>> plot_equilibrium(equilibrium, detail=False, resolution=0.001)
    """
