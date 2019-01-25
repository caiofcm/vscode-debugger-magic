from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic)

@magics_class
class VsCodeDebugger(Magics):

    @line_magic
    def vscodedebugger(self, line):
        import ptvsd
        # 5678 is the default attach port in the VS Code debug configurations
        print("Waiting for debugger attach from VsCode")
        ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
        ptvsd.wait_for_attach()            
        return# line