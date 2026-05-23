from pathlib import Path

from buildenv.extension import BuildEnvRenderer
from jinja2 import Environment, PackageLoader
from nmk_base._buildenv.template import NmkBaseProjectTemplate, NmkReference

_DOC_PATH = Path("doc")
_DIAGRAMS_PATH = Path("diagrams")

_ENV = Environment(loader=PackageLoader("nmk_doc"))


class NmkDocProjectTemplate(NmkBaseProjectTemplate):
    """
    Template for **nmk-doc** plugin project
    """

    @property
    def references(self) -> list[NmkReference]:
        return super().references + [NmkReference("nmk-doc!plugin.yml", ["nmk-base!plugin.yml"])]

    @property
    def weight(self) -> int:
        return 200

    @property
    def auto_extra(self) -> bool:
        # If not selected as main template, at least used as an extra
        return True

    @property
    def description(self) -> str:
        return "project with documentation, generated using sphinx"

    @property
    def generated_files(self) -> set[Path]:
        return super().generated_files | set([_DOC_PATH / "index.md", _DOC_PATH / "subchapter.md"])

    @property
    def post_generation_tasks(self) -> list[str]:
        return super().post_generation_tasks + ["doc.config"]

    def generate_extra_files(self, renderer: BuildEnvRenderer):
        # Generate doc/index.md
        renderer.render(_ENV, "doc/index.md.jinja", sub_path=_DOC_PATH, keywords={"project_name": self.project_name})

        # Generate doc/subchapter.md
        renderer.render(_ENV, "doc/subchapter.md.jinja", sub_path=_DOC_PATH)


class NmkDocPlantUmlProjectTemplate(NmkBaseProjectTemplate):
    """
    Template for **nmk-doc** plugin project with PlantUML diagrams
    """

    @property
    def weight(self):
        # Not a main template
        return 0

    @property
    def references(self) -> list[NmkReference]:
        return super().references + [NmkReference("nmk-doc!plugin.yml", ["nmk-base!plugin.yml"])]

    @property
    def description(self) -> str:
        return "add support for PlantUML diagrams generation"

    @property
    def generated_files(self) -> set[Path]:
        return super().generated_files | set([_DIAGRAMS_PATH / "README.md", _DIAGRAMS_PATH / "example.puml"])

    def generate_extra_files(self, renderer: BuildEnvRenderer):
        # Generate diagrams/README.md
        renderer.render(_ENV, "diagrams/README.md.jinja", sub_path=_DIAGRAMS_PATH)

        # Generate diagrams/example.puml
        renderer.render(_ENV, "diagrams/example.puml.jinja", sub_path=_DIAGRAMS_PATH)
