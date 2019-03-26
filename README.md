# Vscode-Debugger-Magic

Attach a debugging session of visual studio code to the jupyter notebook and also for node-red (within a python-function node)

## Install

```
pip install vscode-debugger-magic
```

## Jupyter Notebook Usage

- Load the magic extension:

```
%load_ext vscode_debugger_magic
```

- Run the magic in jupyter notebook

```
%vscodedebugger
```

- Activate the debugging session in Visual studio code in the Python attached mode:

```json
{
    "name": "Python: Attach",
    "type": "python",
    "request": "attach",
    "port": 5678,
    "host": "localhost"
},
```

- Set breakpoints in vscode
- Invoke functions to be debugged

## Option:

- `--timeout`or `-t` seconds: timeout to attach debugger

```
%vscodedebugger -t 10
```

## Node-red Usage

Example of a python-function node:

```python
import hello_module

from vscode_debugger_magic import start
start()

msg['first'] = 'Caio'
msg['last'] = 'Marcellos'

m = hello_module.hello(msg)

msg['payload'] = m

return msg
```

After execution proceed to VSCode and attach to the process as in the jupyter case.
