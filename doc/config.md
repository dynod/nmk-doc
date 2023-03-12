# Configuration

The **`nmk-doc`** plugin handles the configuration items listed in this page.

All of them are initiliazed with convenient default values, so that you don't need to setup them for a default working behavior. You can anyway override them in your projet if you need to fine tune the plugin behavior.

## Paths and files

(docpath)=
### **`docPath`** -- Documentation input path

| Type | Default value |
|-     |-
| str  | ${PROJECTDIR}/doc

This is the input path where [sphinx](https://www.sphinx-doc.org/) will look for documentation files.

(docconfig)=
### **`docConfig`** -- Sphinx config file

| Type | Default value |
|-     |-
| str  | {ref}`${docPath}<docpath>`/conf.py

This is the [sphinx](https://www.sphinx-doc.org/) configuration file, that will be generated by **`nmk`**.

### **`docConfigTemplate`** -- Config file template

| Type | Default value |
|-     |-
| str  | ${BASEDIR}/templates/config.py.jinja

This item is the path to the [Jinja](https://jinja.palletsprojects.com/en/3.1.x/templates/) template used by **`nmk`** to generate the **`${docConfig}`** file.

(docstaticinputs)=
### **`docStaticInputs`** -- Documentation input files (static ones)

| Type       | Default value |
|-           |-
| list[Path] | Generated by {py:class}`nmk_doc.resolvers.NmkDocInputsResolver`

This is the list of all files contained in the {ref}`${docPath}<docpath>` folder.

(docinputs)=
### **`docInputs`** -- Documentation input files (all of them)

| Type       | Default value |
|-           |-
| list[Path] | [ {ref}`${docStaticInputs}<docstaticinputs>` ]

This is the list of all files that contribute to the documentation build.
It is used to perform documentation incremental build (i.e. **`nmk`** will rebuild documentation only if at least one of these files changed).

This item is welcomed to be extended by other plugins, typically to include source files that may be parsed for automated documentation generation.

(docoutput)=
### **`docOutput`** -- Generated documentation folder

| Type | Default value |
|-     |-
| str  | ${outputDir}/doc

This is the path where [sphinx](https://www.sphinx-doc.org/) will generate the documentation.

## Sphinx configuration

### **`docExtensions`** -- Enabled sphinx extensions

| Type       | Default value |
|-           |-
| list[str] | ["myst_parser", "sphinx_rtd_theme"]

This is the list of the [sphinx](https://www.sphinx-doc.org/) extensions to be enabled in the config file. Default enabled ones are:
* [myst_parser](https://myst-parser.readthedocs.io/en/stable/index.html): used to support markdown (*.md) files in documentation input
* [sphinx_rtd_theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html): used to enable the [ReadTheDocs](https://readthedocs.org/) HTML theme for generated documentation

### **`docHtmlTheme`** -- HTML theme

| Type | Default value |
|-     |-
| str  | sphinx_rtd_theme

This item configures the enabled HTML theme for generated documentation.

### **`docName`** -- Document name

| Type | Default value |
|-     |-
| str  | ${projectName}

This item is used to configure the main document name. Default value is the projet name.

### **`docAuthor`** -- Document author

| Type | Default value |
|-     |-
| str  | ${projectAuthor}

This item is used to configure the document author. Default value is the projet author.

(docversion)=
### **`docVersion`** -- Document version

| Type | Default value |
|-     |-
| str  | Generated by {py:class}`nmk_doc.resolvers.NmkDocVersionResolver`

This item is used to configure the document version. It is generated from the current project git version, by trying to guess the next tag version.
See {py:class}`nmk_doc.resolvers.NmkDocVersionResolver` resolver and {ref}`${docVersionIncrement}<docversionincrement>` item for more information about guessing behavior.

(docversionincrement)=
### **`docVersionIncrement`** -- Document version increment

| Type | Default value |
|-     |-
| str  | 0.1.0

This item is used to guess next tagged version, in order to get a stable resolved value for {ref}`${docVersion}<docversion>` until next version is rolled out.

The dotted version syntax allows to choose which version "segment" to be incremented. Note that when version increment is used, all segments after the identified one will be reset to 0.

Examples
| ${gitVersion}    | ${docVersionIncrement} | {ref}`${docVersion}<docversion>` |
|-                 |-                       |-
| 1.2.3            | 0.1.0                  | 1.2.3
| 1.2.3-3-g1234567 | 0.1.0                  | 1.3.0
| 1.2.3-3-g1234567 | 0.0.1                  | 1.2.4

### **`docYear`** -- Document year

| Type | Default value |
|-     |-
| str  | Generated by {py:class}`nmk_doc.resolvers.NmkDocYearResolver`

This item configures the document generation year. Default is the current one.

### **`docExtraConfig`** -- Extra configuration items

| Type | Default value |
|-     |-
| dict | {}

This item allows the projet and/or other plugins to contribute to [sphinx](https://www.sphinx-doc.org/) config file generation. All items in this dict will be added to generated config file.