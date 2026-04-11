"""
Module containing all config item resolvers for **nmk-doc** plugin.
"""

import re
from datetime import date
from itertools import product
from pathlib import Path

from nmk.logs import NmkLogger
from nmk.model.resolver import NmkBoolConfigResolver, NmkIntConfigResolver, NmkListConfigResolver


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


# "Start UML" tag regex
_START_UML_PATTERN = re.compile(r"^@startuml\s+(.+)")


class PlantUmlOutputFilesResolver(NmkListConfigResolver):
    """
    Resolver for the list of generated PlantUML image files
    """

    def get_value(self, name: str, diagrams: list[str], output_folder: str, formats: list[str]) -> list[str]:  # type: ignore
        """
        Get the list of generated PlantUML image files.

        :param name: config item name to be resolved
        :param diagrams: list of diagram source files
        :param output_folder: output folder for the generated diagrams
        :param formats: list of output formats
        :return: list of generated image files
        """

        # Parse input inputs files to grab all diagram names
        diagram_names: list[str] = []
        for diagram in map(Path, diagrams):
            for line in diagram.read_text().splitlines():
                match = _START_UML_PATTERN.match(line.strip())
                if match:
                    diagram_names.append(match.group(1))

        # List of generated diagram files
        output_path = Path(output_folder)
        return sorted([str(output_path / f"{name}.{ext}") for name, ext in product(diagram_names, formats)])


class DiagramsReadyResolver(NmkBoolConfigResolver):
    """
    Resolver to check if diagrams are ready to be generated
    """

    def get_value(self, name: str, diagrams: list[str], java_runtime: str) -> bool:  # type: ignore
        """
        Check if diagrams are ready to be generated.

        :param name: config item name to be resolved
        :param diagrams: list of diagram source files
        :param java_runtime: path to the Java runtime
        :return: True if all diagrams are ready to be generated, False otherwise
        """

        # No java: just warn
        if not java_runtime:
            NmkLogger.warning("Java runtime not found, skipping PlantUML diagram generation")

        return (len(diagrams) > 0) and (java_runtime != "")
