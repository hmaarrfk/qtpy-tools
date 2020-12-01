# qtpy-uic

qtpy ui compiler: qtpy-uic

Based on the pyside2-uic tool.

The main advantage of this tool is that it does not require any installation of
PySide2, PyQt5, or qtpy to function, but generates code compatible with
qtpy.

## Usage

```
qtpy-uic --help
qtpy-uic -o myui.py myui.ui
```


### Notes from the PySide2 Tools repository

This repository is the tools for PySide2. If you would like to install PySide2, please go to [pyside2-setup](https://github.com/PySide/pyside2-setup) for instructions.

Resources:

* [PySide2-setup](https://github.com/PySide/pyside2-setup)
  The container-project with the setup.py script. It contains the following sub-projects:
  * [PySide2 Wiki](https://github.com/PySide/pyside2/wiki)
    Developer information
  * [PySide2](https://github.com/PySide/pyside2)
    The PySide2 project
  * [Shiboken2](https://github.com/PySide/shiboken2)
    The Shiboken2 project
  * [PySide2-tools](https://github.com/PySide/pyside2-examples)
    The PySide2-tools project
  * [PySide2-examples](https://github.com/PySide/pyside2-examples)
    The PySide2 example scripts

### Changes

#### 0.2.5
- Support for Python 3.9.
