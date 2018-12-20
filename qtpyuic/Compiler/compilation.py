from qtpyuic import __version__
from . import indenter
from . import compiler

_header = """# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '%s'
#
# Created: %s
#      by: qtpy-uic %s
#
# WARNING! All changes made in this file will be lost!

"""

_display_code = """
if __name__ == "__main__":
\timport sys
\tapp = QtWidgets.QApplication(sys.argv)
\t%(widgetname)s = QtWidgets.%(baseclass)s()
\tui = %(uiclass)s()
\tui.setupUi(%(widgetname)s)
\t%(widgetname)s.show()
\tsys.exit(app.exec_())
"""


def compileUiDir(dir, recurse=False, map=None, **compileUi_args):
    """compileUiDir(dir, recurse=False, map=None, **compileUi_args)

    Creates Python modules from Qt Designer .ui files in a directory or
    directory tree.

    dir is the name of the directory to scan for files whose name ends with
    '.ui'.  By default the generated Python module is created in the same
    directory ending with '.py'.
    recurse is set if any sub-directories should be scanned.  The default is
    False.
    map is an optional callable that is passed the name of the directory
    containing the '.ui' file and the name of the Python module that will be
    created.  The callable should return a tuple of the name of the directory
    in which the Python module will be created and the (possibly modified)
    name of the module.  The default is None.
    compileUi_args are any additional keyword arguments that are passed to
    the compileUi() function that is called to create each Python module.
    """

    import os

    # Compile a single .ui file.
    def compile_ui(ui_dir, ui_file):
        # Ignore if it doesn't seem to be a .ui file.
        if ui_file.endswith('.ui'):
            py_dir = ui_dir
            py_file = ui_file[:-3] + '.py'

            # Allow the caller to change the name of the .py file or generate
            # it in a different directory.
            if map is not None:
                py_dir, py_file = map(py_dir, py_file)

            # Make sure the destination directory exists.
            try:
                os.makedirs(py_dir)
            except:
                pass

            ui_path = os.path.join(ui_dir, ui_file)
            py_path = os.path.join(py_dir, py_file)

            ui_file = open(ui_path, 'r')
            py_file = open(py_path, 'w')

            try:
                compileUi(ui_file, py_file, **compileUi_args)
            finally:
                ui_file.close()
                py_file.close()

    if recurse:
        for root, _, files in os.walk(dir):
            for ui in files:
                compile_ui(root, ui)
    else:
        for ui in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, ui)):
                compile_ui(dir, ui)


def compileUi(uifile, pyfile, execute=False, indent=4, from_imports=False):
    """compileUi(uifile, pyfile, execute=False, indent=4, from_imports=False)

    Creates a Python module from a Qt Designer .ui file.

    uifile is a file name or file-like object containing the .ui file.
    pyfile is the file-like object to which the Python code will be written to.
    execute is optionally set to generate extra Python code that allows the
    code to be run as a standalone application.  The default is False.
    indent is the optional indentation width using spaces.  If it is 0 then a
    tab is used.  The default is 4.
    from_imports is optionally set to generate import statements that are
    relative to '.'.
    """

    from time import ctime

    try:
        uifname = uifile.name
    except AttributeError:
        uifname = uifile

    indenter.indentwidth = indent

    pyfile.write(_header % (uifname, ctime(), __version__))

    winfo = compiler.UICompiler().compileUi(uifile, pyfile, from_imports)

    if execute:
        indenter.write_code(_display_code % winfo)
