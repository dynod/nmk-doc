"""
Python module for **nmk-doc** plugin builders.
"""

import shlex
import shutil
from pathlib import Path

from nmk.model.builder import NmkTaskBuilder
from nmk.utils import is_windows, run_with_logs


class NmkDocSphinxBuilder(NmkTaskBuilder):
    """
    Builder used to trigger **sphinx** documentation build
    """

    def build(self, source_folder: str, output_folder: str, version: str = "", static_sub_folder: str = "_static", static_resources: list[str] | None = None):  # type: ignore
        """
        Called by the **doc.build** task, to build the **sphinx** documentation

        Before calling **sphinx**, this builder also copy the configured static files in the static resources directory

        :param source_folder: doc source folder
        :param output_folder: doc output folder
        :param version: project version
        :param static_sub_folder: subfolder for static resources
        :param static_resources: list of static resources to copy
        """

        # Copy static resources if provided
        if static_resources:  # pragma: no branch
            # Prepare folder (clean old resources)
            static_folder = Path(source_folder) / static_sub_folder
            if static_folder.is_dir():
                shutil.rmtree(static_folder)
            static_folder.mkdir(parents=True, exist_ok=True)

            # Copy all input files
            for src_file in map(Path, static_resources):
                if src_file.is_file():
                    shutil.copyfile(src_file, static_folder / src_file.name)
                else:
                    self.logger.warning(f"Static resource '{src_file}' was not found")

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

        # Iterate on formats
        for fmt in formats:
            # Invoke plantuml
            args = [
                java_runtime,
                "-jar",
                jar,
                "--output-dir",
                output_folder,
                *shlex.split(extra_options, posix=not is_windows()),
                f"--{fmt}",
                input_folder,
            ]
            run_with_logs(args)

        # Touch all output files
        for output_file in filter(lambda of: of.is_file(), self.outputs):
            output_file.touch()


class SnippetsBuilder(NmkTaskBuilder):
    """
    Builder used to generate documentation snippets
    """

    def build(self, snippets: dict[str, str], output_folder: str):  # type: ignore
        """
        Called by the **doc.snippets** task, to generate documentation snippets

        :param snippets: dict of snippet name to command to execute
        :param output_folder: output folder for the generated snippets
        """

        # Iterate on snippets definitions
        for snippet_name, command in snippets.items():
            # Prepare output folder if needed
            output_file = Path(output_folder) / snippet_name
            output_file.parent.mkdir(parents=True, exist_ok=True)

            # Execute command and save output to file (force linux line endings)
            cp = run_with_logs(shlex.split(command, posix=not is_windows()))
            output_file.write_text(cp.stdout, encoding="utf-8", errors="ignore", newline="\n")


class ArchiveBuilder(NmkTaskBuilder):
    """
    Builder used to generate documentation archive
    """

    def build(self, clean_pattern: str):  # type: ignore
        """
        Called by the **doc.package** task, to generate documentation archive

        :param clean_pattern: pattern for the files to clean from the output folder (glob style)
        """

        # Prepare output folder if needed
        output_folder = self.main_output.parent
        output_folder.mkdir(parents=True, exist_ok=True)

        # Clean former doc archives
        for old_archive in output_folder.glob(clean_pattern):
            old_archive.unlink()

        # Create zip archive
        shutil.make_archive(base_name=str(self.main_output.with_suffix("")), format="zip", root_dir=self.main_input.parent)
