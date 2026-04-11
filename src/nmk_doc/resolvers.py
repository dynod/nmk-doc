"""
Module containing all config item resolvers for **nmk-doc** plugin.
"""

from datetime import date

from nmk.model.resolver import NmkIntConfigResolver


class NmkDocYearResolver(NmkIntConfigResolver):
    """
    Current year resolver
    """

    def get_value(self, name: str) -> int:
        """
        Get today's year.

        :param name: config item name to be resolved
        :return: current year
        """

        # Today's year
        return date.today().year
