"""bioinformatics file reading, backed by duckdb"""
from importlib.metadata import PackageNotFoundError, version


try:
    __version__ = version("bioduck")
except PackageNotFoundError:
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
