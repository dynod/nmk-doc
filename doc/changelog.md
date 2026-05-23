# Changelog

Here are listed all the meaningfull changes done on **`nmk-doc`** since version 1.0

```{note}
Only interface and important behavior changes are listed here.

The fully detailed changelog is also available on [Github](https://github.com/dynod/nmk-doc/releases)
```

## Release 1.2.0

- Config items update:
  - added {ref}`config items<snippetsConfig>` related to snippets generation
  - updated {ref}`${docInputs}<docInputs>` to include generated **PlantUml** diagrams and doc snippets as inputs
- Tasks behaviors:
  - added {ref}`doc.snippets<doc.snippets>` task to handle snippets generation

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
