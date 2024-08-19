# Import all models
from .aufgabe import Aufgabe
from .aufgabematerial import Aufgabematerial
from .datei import Datei
from .fortschritt import Fortschritt
from .kategorie import Kategorie
from .material import Material
from .prioritaet import Prioritaet


# Define what should be accessible when `from models import *` is used
__all__ = ['Aufgabe', 'Aufgabematerial', 'Datei', 'Fortschritt', 'Kategorie', 'Material', 'Prioritaet']