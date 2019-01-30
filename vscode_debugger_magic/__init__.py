"""An example magic"""
__version__ = '1.1.0'

from .vscode_debugger_magic import VsCodeDebugger

def load_ipython_extension(ipython):
    ipython.register_magics(VsCodeDebugger)
