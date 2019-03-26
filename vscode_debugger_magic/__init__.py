"""VSCode Debugger Magic"""
__version__ = '1.3.0'

from .vscode_debugger_magic import VsCodeDebugger
from .vscode_attach import start

def load_ipython_extension(ipython):
    ipython.register_magics(VsCodeDebugger)
