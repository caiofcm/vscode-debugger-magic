import ptvsd

def start(timeout_sec = None):
    if not ptvsd.is_attached():
        # 5678 is the default attach port in the VS Code debug configurations
        print("Waiting for debugger attach from VsCode")
        ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
        ptvsd.wait_for_attach(timeout_sec)
    return
