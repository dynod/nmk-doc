# Changelog

Here are listed all the meaningfull changes done on **`nmk-doc`** since version 1.0

```{note}
Only interface and important behavior changes are listed here.

The fully detailed changelog is also available on [Github](https://github.com/dynod/nmk-doc/releases)
```

## Release 1.4.0

- Config items update:
  - added {ref}`${docHtmlStaticPath}<docHtmlStaticPath>`, {ref}`${docHtmlStaticPaths}<docHtmlStaticPaths>` and {ref}`${docHtmlStaticFiles}<docHtmlStaticFiles>` items to handle extra static resources to be bundled in the documentation
  - added {ref}`${docHtmlJsFiles}<docHtmlJsFiles>` item to configure used scripts for generated documentation customization
- Added {ref}`customizations<customization>`:
  - open external links in a new browser tab

## Release 1.3.0

- Config items update:
  - added {ref}`${plantUmlDefaultFormat}<plantUmlDefaultFormat>` to specifically identify (and override) default output format for **PlantUml**
  - added {ref}`${docArtifacts}<docArtifacts>`, {ref}`${docArchive}<docArchive>` and {ref}`${docArtifactsCleanPattern}<docArtifactsCleanPattern>` items to configure documentation archive packaging
- Tasks update:
  - added {ref}`doc.package<doc.package>` task to bundle the built documentation in a ZIP archive

## Release 1.2.0

- Config items update:
  - added {ref}`config items<snippetsConfig>` related to snippets generation
  - updated {ref}`${docInputs}<docInputs>` to include generated **PlantUml** diagrams and doc snippets as inputs
- Tasks update:
  - added {ref}`doc.snippets<doc.snippets>` task to handle snippets generation
- Removed [Live Preview](https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server) from suggested extensions, now that HTML preview is integrated natively in VSCode (since **1.121.0**)

## Release 1.1.1

- Make {ref}`${docRTDConfig}<docRTDConfig>` config file independent of python version
- Add buildenv 2.0 install template preliminary support

## Release 1.1.0

- Config items update:
  - added {ref}`config items<plantumlConfig>` related to **PlantUml** diagrams generation
  - added {ref}`${docIndex}<docIndex>`: resolved path to main **index.md** documentation index file
  - added {ref}`${docVersion}<docVersion>`: used to configure the document version
  - updated {ref}`${docHtmlTheme}<docHtmlTheme>`: switched default theme to **furo**
- Tasks behaviors:
  - added {ref}`puml.download<puml.download>` and {ref}`puml.generate<puml.generate>` to handle **PlantUml** diagrams generation
  - all {ref}`doc.config<doc.config>`, {ref}`doc.rtd<doc.rtd>` and {ref}`doc.build<doc.build>` tasks are now only enabled only if {ref}`${docIndex}<docIndex>` file exists
  - add version information when building documentation with {ref}`doc.build<doc.build>` task
