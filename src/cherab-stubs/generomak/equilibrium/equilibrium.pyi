from os import PathLike

from ...tools.equilibrium import EFITEquilibrium

def load_equilibrium(file_path: str | PathLike[str] | None = None) -> EFITEquilibrium: ...
