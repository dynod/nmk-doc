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

    def prepare_doc_project(self, simple: bool = False) -> Path:
        # Build a sample project with doc files
        return self.prepare_project("ref_doc_simple.yml" if simple else "ref_doc.yml")

    def test_version(self):
        # Cover version resolver
        self.nmk(self.prepare_doc_project(), extra_args=["version"])

    def test_no_doc(self):
        # Check project without documentation
        self.nmk(self.prepare_doc_project(simple=True), extra_args=["--print", "docInputs"])
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

        # Check warning on missing resource
        self.check_logs("Static resource 'unknown.png' was not found")

        # Check built doc index exists (+generated static resources)
        assert (self.test_folder / "out" / "doc" / "index.html").is_file()
        assert (self.test_folder / "out" / "doc" / "_static" / "ext_links.js").is_file()

        # Touch index and rebuild (to force static resources cleaning)
        (self.doc_folder / "index.md").touch()
        fake_resource = self.doc_folder / "static" / "blabla.png"
        fake_resource.touch()
        self.nmk(prj, extra_args=["doc.config", "doc.build"])
        assert not fake_resource.is_file()

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

    def prepare_diagrams_project(self) -> Path:
        # Setup project
        p = self.prepare_doc_project()
        diagrams_dir = self.test_folder / "diagrams"
        diagrams_dir.mkdir(exist_ok=True, parents=True)
        shutil.copyfile(self.template("example.puml"), diagrams_dir / "example.puml")
        return p

    def test_diagrams(self):
        # Generate diagrams
        p = self.prepare_diagrams_project()
        self.nmk(p, extra_args=["puml.generate"])
        assert (self.test_folder / "doc" / "diagrams" / "example sequence.svg").is_file()

        # Build again (check incremental build)
        self.nmk(p, extra_args=["puml.generate"])
        self.check_logs("[puml.generate]] DEBUG 🐛 - Task skipped, nothing to do")

    def test_diagrams_multi_formats(self):
        # Generate diagrams for several formats
        p = self.prepare_diagrams_project()
        self.nmk(p, extra_args=["puml.generate", "--config", '{"plantUmlDefaultFormat":"png"}', "--config", '{"plantUmlOutputFormats":["txt"]}'])
        assert (self.test_folder / "doc" / "diagrams" / "example sequence.png").is_file()
        assert (self.test_folder / "doc" / "diagrams" / "example sequence.atxt").is_file()

    def test_diagrams_no_java(self):
        # Try to generate diagrams without Java
        p = self.prepare_diagrams_project()
        self.nmk(p, extra_args=["puml.generate", "--config", "javaRuntime="])
        self.check_logs("Java runtime not found, skipping PlantUML diagram generation")

    def jsonify(self, to_escape: Path) -> str:
        # Escape backslashes (for Windows paths in json print)
        return '"' + str(to_escape).replace("\\", "\\\\") + '"'

    def test_snippets_output(self):
        # Check snippets outputs
        p = self.prepare_doc_project()
        self.nmk(p, extra_args=["--print", "docSnippetsOutputFiles"])
        self.check_logs(f'Config dump: {{ "docSnippetsOutputFiles": [ {self.jsonify(self.test_folder / "doc" / "snippets" / "example_snippet.txt")} ] }}')

    def test_snippets_build(self):
        # Generate snippets
        p = self.prepare_doc_project()
        self.nmk(p, extra_args=["doc.snippets"])

        # Check generated file
        gen_file = self.test_folder / "doc" / "snippets" / "example_snippet.txt"
        assert gen_file.is_file()
        assert "Next-gen make-like build system" in gen_file.read_text()

        # Build again (check incremental build)
        self.nmk(p, extra_args=["doc.snippets"])
        self.check_logs("[doc.snippets]] DEBUG 🐛 - Task skipped, nothing to do")

    def test_archive_build(self):
        # Generate doc archive
        p = self.prepare_doc_project(simple=True)
        (self.test_folder / "doc").mkdir(exist_ok=True, parents=True)
        (self.test_folder / "doc" / "index.md").touch()
        (self.test_folder / "out" / "doc").mkdir(exist_ok=True, parents=True)
        (self.test_folder / "out" / "doc" / "index.html").write_text("<html><body>Sample doc</body></html>")
        self.nmk(p, extra_args=["doc.package"])

        # Check generated file
        gen_file = self.test_folder / "out" / "artifacts" / "sample-project-1.0.0-doc.zip"
        assert gen_file.is_file()

        # Build again (check incremental build)
        self.nmk(p, extra_args=["doc.package"])
        self.check_logs("[doc.package]] DEBUG 🐛 - Task skipped, nothing to do")

        # Build again with a different version (check old artifact is removed)
        self.nmk(p, extra_args=["doc.package", "--config", '{"docVersion":"1.0.1"}'])
        assert not gen_file.is_file()
        gen_file = self.test_folder / "out" / "artifacts" / "sample-project-1.0.1-doc.zip"
        assert gen_file.is_file()
