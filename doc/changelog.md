# Changelog

Here are listed all the meaningfull changes done on **`nmk-doc`** since version 1.0

```{note}
Only interface and important behavior changes are listed here.

The fully detailed changelog is also available on [Github](https://github.com/dynod/nmk-doc/releases)
```

## Release 1.1.0

- Config items update:
  - added {ref}`${docIndex}<docIndex>`: resolved path to main **index.md** documentation index file
  - updated {ref}`${docHtmlTheme}<docHtmlTheme>`: switched default theme to **furo**
- Tasks behaviors:
  - all {ref}`doc.config<doc.config>`, {ref}`doc.rtd<doc.rtd>` and {ref}`doc.build<doc.build>` tasks are now only enabled only if {ref}`${docIndex}<docIndex>` file exists
  - add version information when building documentation with {ref}`doc.build<doc.build>` task
