from IPython.core import magic_arguments
from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic)

@magics_class
class VsCodeDebugger(Magics):

    @magic_arguments.magic_arguments()
    @magic_arguments.argument('--timeout', '-t',
        #   action='store_true',
          help='Set timeout for attachment (seconds)'
    )
    @line_magic
    def vscodedebugger(self, line):
        args = magic_arguments.parse_argstring(self.vscodedebugger, line)
        timeout_sec = None
        if args.timeout:
            try:
                timeout_sec = float(args.timeout)
            except ValueError:
                raise ValueError('Timeout should be a number')
        import ptvsd
        # 5678 is the default attach port in the VS Code debug configurations
        print("Waiting for debugger attach from VsCode")
        ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
        ptvsd.wait_for_attach(timeout_sec)
        return# line
