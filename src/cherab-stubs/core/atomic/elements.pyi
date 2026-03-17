_element_index: dict[str, Element]
_isotope_index: dict[str, Isotope]

class Element:
    """
    Class representing an atomic element.

    :param str name: Element name.
    :param str symbol: Element symbol, e.g. 'H'.
    :param int atomic_number: Number of protons.
    :param float atomic_weight: average atomic weight in amu

    :ivar str name: Element name.
    :ivar str symbol: Element symbol, e.g. 'H'.
    :ivar int atomic_number: Number of protons.
    :ivar float atomic_weight: average atomic weight in amu

    .. code-block:: pycon

       >>> from cherab.core.atomic import Element
       >>> helium = Element("helium", "He", 2, 4.002602)
    """

    name: str
    symbol: str
    atomic_number: int
    atomic_weight: float

    def __init__(
        self, name: str, symbol: str, atomic_number: int, atomic_weight: float
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...
    def __richcmp__(self, other: Element, op: int) -> bool: ...

class Isotope(Element):
    """
    Class representing an atomic isotope.

    :param str name: Isotope name.
    :param str symbol: Isotope symbol, e.g. 'T'.
    :param Element element: The parent element of this isotope,
      e.g. for Tritium it would be Hydrogen.
    :param int mass_number: Atomic mass number, which is total number of protons
      and neutrons. Allows identification of specific isotopes.
    :param float atomic_weight: atomic weight in amu

    :ivar str name: Isotope name.
    :ivar str symbol: Isotope symbol, e.g. 'T'.
    :param Element element: The parent element of this isotope,
      e.g. for Tritium it would be Hydrogen.
    :ivar int atomic_number: Number of protons.
    :ivar int mass_number: Atomic mass number, which is total number of protons
      and neutrons. Allows identification of specific isotopes.
    :ivar float atomic_weight: atomic weight in amu

    .. code-block:: pycon

       >>> from cherab.core.atomic import Isotope, hydrogen
       >>> tritium = Isotope("tritium", "T", hydrogen, 3, 3.0160492777)
    """

    mass_number: int
    element: Element

    def __init__(
        self, name: str, symbol: str, element: Element, mass_number: int, atomic_weight: float
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...
    def __richcmp__(self, other: Isotope, op: int) -> bool: ...

def _build_element_index() -> None:
    """
    Populate an element search dictionary.

    Populates the element index so users can search for elements by name,
    symbol or atomic number.
    """

def _build_isotope_index() -> None:
    """
    Populate an isotope search dictionary.

    Populates the isotope index so users can search for isotopes by name or
    symbol.
    """

def lookup_element(v: str | int) -> Element:
    """
    Find an element by name, symbol or atomic number.

    .. code-block:: pycon

       >>> from cherab.core.atomic import lookup_element
       >>> hydrogen = lookup_element("hydrogen")
       >>> neon = lookup_element("Ne")
       >>> argon = lookup_element(18)

    :param v: Search string or integer.
    :return: Element object.
    """

def lookup_isotope(v: str | int, number: int | None = None) -> Isotope:
    """
    Find an isotope by name, symbol or number.

    Isotopes are uniquely determined by the element type and mass number. These
    can be specified as a single string or a combination of element and mass number.

    .. code-block:: pycon

       >>> from cherab.core.atomic import lookup_isotope
       >>> deuterium = lookup_element("deuterium")
       >>> tritium = lookup_element(1, number=3)
       >>> helium3 = lookup_element("he3")
       >>> helium4 = lookup_element("he", number=4)

    :param v: Search string, integer or element.
    :param number: Integer mass number
    :return: Element object.
    """

hydrogen: Element
helium: Element
lithium: Element
beryllium: Element
boron: Element
carbon: Element
nitrogen: Element
oxygen: Element
fluorine: Element
neon: Element
sodium: Element
magnesium: Element
aluminium: Element
silicon: Element
phosphorus: Element
sulfur: Element
chlorine: Element
argon: Element
potassium: Element
calcium: Element
scandium: Element
titanium: Element
vanadium: Element
chromium: Element
manganese: Element
iron: Element
cobalt: Element
nickel: Element
copper: Element
zinc: Element
gallium: Element
germanium: Element
arsenic: Element
selenium: Element
bromine: Element
krypton: Element
rubidium: Element
strontium: Element
yttrium: Element
zirconium: Element
niobium: Element
molybdenum: Element
# technetium: Element
ruthenium: Element
rhodium: Element
palladium: Element
silver: Element
cadmium: Element
indium: Element
tin: Element
antimony: Element
tellurium: Element
iodine: Element
xenon: Element
caesium: Element
barium: Element
lanthanum: Element
cerium: Element
praseodymium: Element
neodymium: Element
# promethium: Element
samarium: Element
europium: Element
gadolinium: Element
terbium: Element
dysprosium: Element
holmium: Element
erbium: Element
thulium: Element
ytterbium: Element
lutetium: Element
hafnium: Element
tantalum: Element
tungsten: Element
rhenium: Element
osmium: Element
iridium: Element
platinum: Element
gold: Element
mercury: Element
thallium: Element
lead: Element
bismuth: Element
# polonium: Element
# astatine: Element
# radon: Element
# francium: Element
# radium: Element
# actinium: Element
thorium: Element
protactinium: Element
uranium: Element
# neptunium: Element
# plutonium: Element
# americium: Element
# curium: Element
# berkelium: Element
# californium: Element
# einsteinium: Element
# fermium: Element
# mendelevium: Element
# nobelium: Element
# lawrencium: Element
# rutherfordium: Element
# dubnium: Element
# seaborgium: Element
# bohrium: Element
# hassium: Element
# meitnerium: Element
# darmstadtium: Element
# roentgenium: Element
# copernicium: Element
# nihonium: Element
# flerovium: Element
# moscovium: Element
# livermorium: Element
# tennessine: Element
# oganesson: Element

# isotopes
protium: Isotope
deuterium: Isotope
tritium: Isotope
helium3: Isotope
helium4: Isotope
lithium6: Isotope
lithium7: Isotope
beryllium9: Isotope
boron10: Isotope
boron11: Isotope
carbon12: Isotope
carbon13: Isotope
nitrogen14: Isotope
nitrogen15: Isotope
oxygen16: Isotope
oxygen17: Isotope
oxygen18: Isotope
fluorine19: Isotope
neon20: Isotope
neon21: Isotope
neon22: Isotope
sodium23: Isotope
magnesium24: Isotope
magnesium25: Isotope
magnesium26: Isotope
aluminium27: Isotope
silicon28: Isotope
silicon29: Isotope
silicon30: Isotope
phosphorus31: Isotope
sulfur32: Isotope
sulfur33: Isotope
sulfur34: Isotope
sulfur36: Isotope
chlorine35: Isotope
chlorine37: Isotope
argon36: Isotope
argon38: Isotope
argon40: Isotope
potassium39: Isotope
potassium40: Isotope
potassium41: Isotope
calcium40: Isotope
calcium42: Isotope
calcium43: Isotope
calcium44: Isotope
calcium46: Isotope
calcium48: Isotope
scandium45: Isotope
titanium46: Isotope
titanium47: Isotope
titanium48: Isotope
titanium49: Isotope
titanium50: Isotope
vanadium50: Isotope
vanadium51: Isotope
chromium50: Isotope
chromium52: Isotope
chromium53: Isotope
chromium54: Isotope
manganese55: Isotope
iron54: Isotope
iron56: Isotope
iron57: Isotope
iron58: Isotope
cobalt59: Isotope
nickel58: Isotope
nickel60: Isotope
nickel61: Isotope
nickel62: Isotope
nickel64: Isotope
copper63: Isotope
copper65: Isotope
zinc64: Isotope
zinc66: Isotope
zinc67: Isotope
zinc68: Isotope
zinc70: Isotope
gallium69: Isotope
gallium71: Isotope
germanium70: Isotope
germanium72: Isotope
germanium73: Isotope
germanium74: Isotope
germanium76: Isotope
arsenic75: Isotope
selenium74: Isotope
selenium76: Isotope
selenium77: Isotope
selenium78: Isotope
selenium80: Isotope
selenium82: Isotope
bromine79: Isotope
bromine81: Isotope
krypton78: Isotope
krypton80: Isotope
krypton82: Isotope
krypton83: Isotope
krypton84: Isotope
krypton86: Isotope
rubidium85: Isotope
rubidium87: Isotope
strontium84: Isotope
strontium86: Isotope
strontium87: Isotope
strontium88: Isotope
yttrium89: Isotope
zirconium90: Isotope
zirconium91: Isotope
zirconium92: Isotope
zirconium94: Isotope
zirconium96: Isotope
niobium93: Isotope
molybdenum92: Isotope
molybdenum94: Isotope
molybdenum95: Isotope
molybdenum96: Isotope
molybdenum97: Isotope
molybdenum98: Isotope
molybdenum100: Isotope
ruthenium96: Isotope
ruthenium98: Isotope
ruthenium99: Isotope
ruthenium100: Isotope
ruthenium101: Isotope
ruthenium102: Isotope
ruthenium104: Isotope
rhodium103: Isotope
palladium102: Isotope
palladium104: Isotope
palladium105: Isotope
palladium106: Isotope
palladium108: Isotope
palladium110: Isotope
silver107: Isotope
silver109: Isotope
cadmium106: Isotope
cadmium108: Isotope
cadmium110: Isotope
cadmium111: Isotope
cadmium112: Isotope
cadmium113: Isotope
cadmium114: Isotope
cadmium116: Isotope
indium113: Isotope
indium115: Isotope
tin112: Isotope
tin114: Isotope
tin115: Isotope
tin116: Isotope
tin117: Isotope
tin118: Isotope
tin119: Isotope
tin120: Isotope
tin122: Isotope
tin124: Isotope
antimony121: Isotope
antimony123: Isotope
tellurium120: Isotope
tellurium122: Isotope
tellurium123: Isotope
tellurium124: Isotope
tellurium125: Isotope
tellurium126: Isotope
tellurium128: Isotope
tellurium130: Isotope
iodine127: Isotope
xenon124: Isotope
xenon126: Isotope
xenon128: Isotope
xenon129: Isotope
xenon130: Isotope
xenon131: Isotope
xenon132: Isotope
xenon134: Isotope
xenon136: Isotope
caesium133: Isotope
barium130: Isotope
barium132: Isotope
barium134: Isotope
barium135: Isotope
barium136: Isotope
barium137: Isotope
barium138: Isotope
lanthanum138: Isotope
lanthanum139: Isotope
cerium136: Isotope
cerium138: Isotope
cerium140: Isotope
cerium142: Isotope
praseodymium141: Isotope
neodymium142: Isotope
neodymium143: Isotope
neodymium144: Isotope
neodymium145: Isotope
neodymium146: Isotope
neodymium148: Isotope
neodymium150: Isotope
samarium144: Isotope
samarium147: Isotope
samarium148: Isotope
samarium149: Isotope
samarium150: Isotope
samarium152: Isotope
samarium154: Isotope
europium151: Isotope
europium153: Isotope
gadolinium152: Isotope
gadolinium154: Isotope
gadolinium155: Isotope
gadolinium156: Isotope
gadolinium157: Isotope
gadolinium158: Isotope
gadolinium160: Isotope
terbium159: Isotope
dysprosium156: Isotope
dysprosium158: Isotope
dysprosium160: Isotope
dysprosium161: Isotope
dysprosium162: Isotope
dysprosium163: Isotope
dysprosium164: Isotope
holmium165: Isotope
erbium162: Isotope
erbium164: Isotope
erbium166: Isotope
erbium167: Isotope
erbium168: Isotope
erbium170: Isotope
thulium169: Isotope
ytterbium168: Isotope
ytterbium170: Isotope
ytterbium171: Isotope
ytterbium172: Isotope
ytterbium173: Isotope
ytterbium174: Isotope
ytterbium176: Isotope
lutetium175: Isotope
lutetium176: Isotope
hafnium174: Isotope
hafnium176: Isotope
hafnium177: Isotope
hafnium178: Isotope
hafnium179: Isotope
hafnium180: Isotope
tantalum180: Isotope
tantalum181: Isotope
tungsten180: Isotope
tungsten182: Isotope
tungsten183: Isotope
tungsten184: Isotope
tungsten186: Isotope
rhenium185: Isotope
rhenium187: Isotope
osmium184: Isotope
osmium186: Isotope
osmium187: Isotope
osmium188: Isotope
osmium189: Isotope
osmium190: Isotope
osmium192: Isotope
iridium191: Isotope
iridium193: Isotope
platinum190: Isotope
platinum192: Isotope
platinum194: Isotope
platinum195: Isotope
platinum196: Isotope
platinum198: Isotope
gold197: Isotope
mercury196: Isotope
mercury198: Isotope
mercury199: Isotope
mercury200: Isotope
mercury201: Isotope
mercury202: Isotope
mercury204: Isotope
thallium203: Isotope
thallium205: Isotope
lead204: Isotope
lead206: Isotope
lead207: Isotope
lead208: Isotope
bismuth209: Isotope
thorium230: Isotope
thorium232: Isotope
protactinium231: Isotope
uranium234: Isotope
uranium235: Isotope
uranium238: Isotope
