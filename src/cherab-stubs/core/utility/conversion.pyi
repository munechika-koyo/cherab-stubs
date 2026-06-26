class EvAmuToMS:
    """Converts from eV/amu to velocity (m/s)"""

    conversion_factor: float
    @classmethod
    def to(cls, x: float) -> float:
        """Direct conversion"""
    @classmethod
    def inv(cls, x: float) -> float:
        """Inverse conversion"""

class PhotonToJ:
    """Converts from photon to Jules"""

    conversion_factor: float
    @classmethod
    def to(cls, x: float, wavelength: float) -> float:
        """Direct conversion; wavelength in nm"""
    @classmethod
    def inv(cls, x: float, wavelength: float) -> float:
        """Inverse conversion; wavelength in nm"""

class BaseFactorConversion:
    """Base class for conversion based on factor"""
    @classmethod
    def to(cls, x: float) -> float:
        """Direct conversion"""
    @classmethod
    def inv(cls, x: float) -> float:
        """Inverse conversion"""

class AmuToKg(BaseFactorConversion):
    """Converts from amu to kg"""

    conversion_factor: float

class EvToJ(BaseFactorConversion):
    """Converts from eV to Jules"""

    conversion_factor: float

class Cm3ToM3(BaseFactorConversion):
    """Converts from cm3 to m3"""

    conversion_factor: float = 1e-6

class PerCm3ToPerM3(BaseFactorConversion):
    """Converts from cm-3 to m-3"""

    conversion_factor: float = 1e6

class AngstromToNm(BaseFactorConversion):
    """Converts from Angstroms to nm."""

    conversion_factor: float = 0.1
