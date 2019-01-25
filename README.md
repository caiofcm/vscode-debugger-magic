# Vscode-Debugger-Magic

Attach a debugging session of visual studio code to the jupyter notebook 

## Install

Todo

```
pip install vscode-debugger-magic
```

## Usage

1. Run the magic in jupyter notebook

```
%vscodedebugger
```

2. Activate the debugging session in Visual studio code in the Python attached mode:

```json
{
    "name": "Python: Attach",
    "type": "python",
    "request": "attach",
    "port": 5678,
    "host": "localhost"
},
```

3. Set breakpoints
4. Invoke functions to be debugged

