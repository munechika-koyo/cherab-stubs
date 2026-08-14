from .roughconductor import RToptimisedRoughConductor as RToptimisedRoughConductor

class _DataLoader(RToptimisedRoughConductor):
    def __init__(self, filename: str, roughness: float) -> None: ...

class RoughAluminium(_DataLoader):
    """Aluminium metal material."""
    def __init__(self, roughness: float) -> None: ...

class RoughBeryllium(_DataLoader):
    """Beryllium metal material."""
    def __init__(self, roughness: float) -> None: ...

class RoughCobolt(_DataLoader):
    """Cobolt metal material."""
    def __init__(self, roughness: float) -> None: ...

class RoughCopper(_DataLoader):
    """Copper metal material."""
    def __init__(self, roughness: float) -> None: ...

class RoughGold(_DataLoader):
    """Gold metal material."""
    def __init__(self, roughness: float) -> None: ...

class RoughIron(_DataLoader):
    """Iron metal material."""
    def __init__(self, roughness: float) -> None: ...

class RoughLithium(_DataLoader):
    """Lithium metal material."""
    def __init__(self, roughness: float) -> None: ...

class RoughMagnesium(_DataLoader):
    """Magnesium metal material."""
    def __init__(self, roughness: float) -> None: ...

class RoughManganese(_DataLoader):
    """Manganese metal material."""
    def __init__(self, roughness: float) -> None: ...

class RoughMercury(_DataLoader):
    """Mercury metal material."""
    def __init__(self, roughness: float) -> None: ...

class RoughNickel(_DataLoader):
    """Nickel metal material."""
    def __init__(self, roughness: float) -> None: ...

class RoughPalladium(_DataLoader):
    """Palladium metal material."""
    def __init__(self, roughness: float) -> None: ...

class RoughPlatinum(_DataLoader):
    """Platinum metal material."""
    def __init__(self, roughness: float) -> None: ...

class RoughSilicon(_DataLoader):
    """Silicon metal material."""
    def __init__(self, roughness: float) -> None: ...

class RoughSilver(_DataLoader):
    """Silver metal material."""
    def __init__(self, roughness: float) -> None: ...

class RoughSodium(_DataLoader):
    """Sodium metal material."""
    def __init__(self, roughness: float) -> None: ...

class RoughTitanium(_DataLoader):
    """Titanium metal material."""
    def __init__(self, roughness: float) -> None: ...

class RoughTungsten(_DataLoader):
    """Tungsten metal material."""
    def __init__(self, roughness: float) -> None: ...
