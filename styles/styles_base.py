import reflex as rx
from enum import Enum

# CONSTANTES
WIDTH_MAX = "600px"

#tamaños
class Spacer(Enum):
    # un em = 18px
    SMALL = '0.5em'
    DEFAUL = '1em'
    BIG = '2em'