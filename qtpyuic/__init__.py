# This file was modified from that of the PySide Project.
# It is made to be compatible with qtpy
# Copyright (C) 2018 Mark Harfouche
#
# This file is part of the PySide project.
#
# Copyright (C) 2009-2011 Nokia Corporation and/or its subsidiary(-ies).
# Copyright (C) 2010 Riverbank Computing Limited.
# Copyright (C) 2009 Torsten Marek
#
# Contact: PySide team <pyside@openbossa.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# version 2 as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301 USA

__all__ = ("compileUi", "compileUiDir", "widgetPluginPath")

from .Compiler import compileUiDir, compileUi

# The list of directories that are searched for widget plugins.
from .objcreator import widgetPluginPath

# The script
from .main import main

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
