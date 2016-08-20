from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["pyVoxelStats.pyx", "pyVoxelStatsLM.pyx", "pyVoxelStatsGAM.pyx", "Util/StatsUtil.pyx", "Util/VoxelOperation.pyx"])
)