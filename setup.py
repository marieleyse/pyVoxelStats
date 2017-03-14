from setuptools import setup

setup(
    # Application name:
    name="pyVoxelStats",

    # Version number (initial):
    version="0.1.1a2",

    # Application author details:
    author="Sulantha Mathotaarachchi",
    author_email="sulantha.ms@gmail.com",

    # Packages
    packages=["pyVS"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/pyVoxelStats_v011/",

    #
    # license="LICENSE.txt",
    description="Python implementation of the VoxelStats toolbox for neuroimage analysis",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "nibabel", "pandas", "numpy",
        "pyminc",
        "statsmodels",
        "rpy2",
        "ipyparallel",
    ],
)