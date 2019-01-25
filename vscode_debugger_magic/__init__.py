"""An example magic"""
__version__ = '0.0.1'

from .abracadabra import Abracadabra

def load_ipython_extension(ipython):
    ipython.register_magics(Abracadabra)
