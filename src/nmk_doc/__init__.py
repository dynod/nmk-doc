"""
Python module for **nmk-doc** plugin code.
"""

from configparser import ConfigParser
from pathlib import Path

from nmk_base.version import VersionResolver
from pkg_resources import DistributionNotFound, get_distribution

__title__ = "nmk-doc"
"""
Module name
"""

try:
    __version__ = get_distribution(__title__).version
    """
    Module version, dynamically resolved from installed package
    """
except DistributionNotFound:  # pragma: no cover
    # For debug
    try:
        with (Path(__file__).parent.parent.parent / "setup.cfg").open("r") as f:
            c = ConfigParser()
            c.read_file(f.readlines())
            __version__ = c.get("metadata", "version")
    except Exception:
        __version__ = "unknown"


class NmkDocVersionResolver(VersionResolver):
    """
    Version resolver for **${nmkDocPluginVersion}**
    """

    def get_version(self) -> str:
        """
        Module version accessor

        :return: current module version
        """

        return __version__
