# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

# Get the long description from the README file
with open('README.md') as f:
    long_description = f.read()

import versioneer
version = versioneer.get_version()
cmdclass = versioneer.get_cmdclass()

setup(
    name='qtpy-uic',
    version=version,
    cmdclass=cmdclass,
    description='Qt UI compiler to qtpy',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hmaarrfk/qtpy-tools/',
    author='Mark Harfouche',
    author_email='mark.harfouche@gmail.com',
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GPLv3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(),  # Required
    install_requires=[],
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    #
    # If using Python 2.6 or earlier, then these have to be included in
    # MANIFEST.in as well.
    # package_data={  # Optional
    #     'sample': ['package_data.dat'],
    # },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={  # Optional
        'console_scripts': [
            'qtpy-uic=qtpyuic:main',
        ],
    },
)
