"""
Python module for **nmk-doc** plugin builders.
"""

from nmk.model.builder import NmkTaskBuilder
from nmk.utils import run_with_logs


class NmkDocSphinxBuilder(NmkTaskBuilder):
    """
    Builder used to trigger **sphinx** documentation build
    """

    def build(self, source_folder: str, output_folder: str, version: str = ""):  # type: ignore
        """
        Called by the **doc.build** task, to build the **sphinx** documentation

        :param source_folder: doc source folder
        :param output_folder: doc output folder
        :param version: project version
        """

        # Invoke sphinx
        run_with_logs(["sphinx-build", source_folder, output_folder] + (["-D", f"release={version}"] if version else []))

        # Touch main output index (for incremental build)
        self.main_output.touch()


class PlantUmlBuilder(NmkTaskBuilder):
    """
    Builder used to trigger **plantuml** diagram generation
    """

    def build(self, jar: str, java_runtime: str, input_folder: str, output_folder: str, formats: list[str], extra_options: str):  # type: ignore
        """
        Called by the **puml.generate** task, to generate diagrams

        :param jar: path to the PlantUML JAR file
        :param java_runtime: path to the Java runtime
        :param input_folder: input folder containing the diagram source files
        :param output_folder: output folder for the generated diagrams
        :param formats: list of output formats
        :param extra_options: extra options for the PlantUML command
        """

        # Invoke plantuml
        args = [
            java_runtime,
            "-jar",
            jar,
            "--output-dir",
            output_folder,
            *[eo.strip() for eo in extra_options.split() if eo.strip()],  # Split extra options by space and filter out empty ones
            *[f"--{fmt}" for fmt in formats if fmt],  # Add format options (e.g., --png, --svg) if formats are specified
            input_folder,
        ]
        run_with_logs(args)

        # Touch all output files
        for output_file in filter(lambda of: of.is_file(), self.outputs):
            output_file.touch()
