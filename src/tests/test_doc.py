from pathlib import Path

from nmk.tests.tester import NmkBaseTester


class TestDocPlugin(NmkBaseTester):
    @property
    def templates_root(self) -> Path:
        return Path(__file__).parent / "templates"

    def prepare_doc_project(self) -> Path:
        # Build a sample project with doc files
        return self.prepare_project("ref_doc.yml")

    def test_version(self):
        self.nmk(self.prepare_doc_project(), extra_args=["version"])
