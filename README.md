# nmk-doc
Documentation handling plugin for nmk build system

<!-- NMK-BADGES-BEGIN -->
[![License: MIT License](https://img.shields.io/github/license/dynod/nmk-doc)](https://github.com/dynod/nmk-doc/blob/main/LICENSE)
[![Checks](https://img.shields.io/github/actions/workflow/status/dynod/nmk-doc/build.yml?branch=main&label=build%20%26%20u.t.)](https://github.com/dynod/nmk-doc/actions?query=branch%3Amain)
[![Issues](https://img.shields.io/github/issues-search/dynod/nmk?label=issues&query=is%3Aopen+is%3Aissue+label%3Aplugin%3Adoc)](https://github.com/dynod/nmk/issues?q=is%3Aopen+is%3Aissue+label%3Aplugin%3Adoc)
[![Supported python versions](https://img.shields.io/badge/python-3.9%20--%203.13-blue)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/nmk-doc)](https://pypi.org/project/nmk-doc/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://astral.sh/ruff)
[![Code coverage](https://img.shields.io/codecov/c/github/dynod/nmk-doc)](https://app.codecov.io/gh/dynod/nmk-doc)
[![Documentation Status](https://readthedocs.org/projects/nmk-doc/badge/?version=stable)](https://nmk-doc.readthedocs.io/)
<!-- NMK-BADGES-END -->

This plugin provide tasks to build documentation using the [Sphinx tool](https://www.sphinx-doc.org/).

## Usage

To use this plugin in your **`nmk`** project, insert this reference:
```yaml
refs:
    - pip://nmk-doc!plugin.yml
```

## Documentation

This plugin documentation is available [here](https://nmk-doc.readthedocs.io/)

## Issues

Issues for this plugin shall be reported on the [main  **`nmk`** project](https://github.com/dynod/nmk/issues), using the **plugin:doc** label.
