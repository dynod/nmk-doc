import shutil
from pathlib import Path

from nmk.tests.tester import NmkBaseTester


class TestDocPlugin(NmkBaseTester):
    @property
    def templates_root(self) -> Path:
        return Path(__file__).parent / "templates"

    @property
    def doc_folder(self) -> Path:
        doc = self.test_folder / "doc"
        doc.mkdir(exist_ok=True)
        return doc

    def prepare_doc_project(self) -> Path:
        # Build a sample project with doc files
        return self.prepare_project("ref_doc.yml")

    def test_version(self):
        # Cover version resolver
        self.nmk(self.prepare_doc_project(), extra_args=["version"])

    def test_no_doc(self):
        # Check project without documentation
        self.nmk(self.prepare_doc_project(), extra_args=["--print", "docInputs"])
        self.check_logs('Config dump: { "docInputs": [] }')

    def test_build_config(self):
        # Build config file for sphinx tool
        index_template = self.template("index.md")
        shutil.copyfile(index_template, self.doc_folder / index_template.name)
        prj = self.prepare_doc_project()
        self.nmk(prj, extra_args=["doc.config"])

        # Check config file exists
        assert (self.doc_folder / "conf.py").is_file()

        # Check rebuild
        self.nmk(prj, extra_args=["doc.config"])
        self.check_logs("[doc.config]] DEBUG 🐛 - Task skipped, nothing to do")

    def test_build_doc(self):
        # Prepare doc project
        index_template = self.template("index.md")
        shutil.copyfile(index_template, self.doc_folder / index_template.name)
        prj = self.prepare_doc_project()
        self.nmk(prj, extra_args=["doc.config", "doc.build"])

        # Check built doc index exists
        assert (self.test_folder / "out" / "doc" / "index.html").is_file()

        # Check rebuild
        self.nmk(prj, extra_args=["doc.build"])
        self.check_logs("[doc.build]] DEBUG 🐛 - Task skipped, nothing to do")

    def test_build_rtd(self):
        # Prepare doc project
        index_template = self.template("index.md")
        shutil.copyfile(index_template, self.doc_folder / index_template.name)
        prj = self.prepare_doc_project()
        self.nmk(prj, extra_args=["doc.rtd", "--config", '{"pythonSupportedVersions":["3.8"]}'])

        # Check generated ReadTheDocs file
        assert (self.test_folder / ".readthedocs.yaml").is_file()

        # Check rebuild
        self.nmk(prj, extra_args=["doc.rtd"])
        self.check_logs("[doc.rtd]] DEBUG 🐛 - Task skipped, nothing to do")

    def test_build_rtd_disabled(self):
        # Prepare doc project
        index_template = self.template("index.md")
        shutil.copyfile(index_template, self.doc_folder / index_template.name)
        prj = self.prepare_doc_project()
        self.nmk(prj, extra_args=["doc.rtd", "--config", '{"docRTDDisabled":true}'])

        # Check ReadTheDocs file is not generated
        assert not (self.test_folder / ".readthedocs.yaml").is_file()
        self.check_logs("[doc.rtd]] DEBUG 🐛 - Task skipped, nothing to do")
