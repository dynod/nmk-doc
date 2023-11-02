# Configuration Extension

As for all **`nmk`** projects config items, [**`nmk-doc`** ones](config.md) are all overridable by other plug-ins and project files. But the ones described on this page are specifically designed to be extended.

## Documentation inputs

Plugins which support documentation generation from source code should extend the **{ref}`${docInputs}<docinputs>`** config item, in order to trigger documentation rebuild if source code is modified.

Example:
```yaml
docInputs:
    - file.py
    - ${someVarResolvingAllPyFiles}
```

## Sphinx extensions

Plugins and/or project may want to enable [sphinx extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html), in addition to the default ones. The following items may be extended for this purpose:

* **{ref}`${docExtensions}<docExtensions>`**: List of enabled sphinx extensions.
  Example:
  ```yaml
  docExtensions:
      - breathe
  ```
* **{ref}`${docExtensionsVenvDeps}<docExtensionsVenvDeps>`**: List of python modules to be installed in the project venv in order to support the enabled extensions.
  Example:
  ```yaml
  docExtensionsVenvDeps:
      - breathe
  ```
* **{ref}`${docExtraConfig}<docExtraConfig>`**: Dictionnary of additional sphinx config parameters, to be added to the generated {ref}`configuration file<docconfig>`.
  Example:
  ```yaml
  docExtraConfig:
      configName: value
  ```
