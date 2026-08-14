from .efit import EFITEquilibrium

def import_eqdsk(file_path: str, drop_nan: bool = False) -> EFITEquilibrium:
    """
    Imports equilibrium data from an EFIT G EQDSK file.

    The file format is described at https://w3.pppl.gov/ntcc/TORAY/G_EQDSK.pdf.

    .. WARNING::
       The G EQDSK file format is unstable and unreliable. Use with caution.

    :param str file_path: Path to the EFIT eqdsk file.
    :param bool drop_nan: Drop NaN values in the f and q profiles.
    :rtype: EFITEquilibrium

    .. code-block:: pycon

       >>> from cherab.tools.equilibrium import import_eqdsk
       >>> equilibrium = import_eqdsk("equilibrium.eqdsk")
    """
