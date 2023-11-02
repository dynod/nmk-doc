# Usage

To use this plugin in your **`nmk`** project, insert this reference in your **nmk.yml** main file:
```yaml
refs:
    - pip://nmk-doc!plugin.yml
```

Then you can start writing documentation by adding an **index.md** file in your project **doc** sub-folder. Once done, **`nmk`** build will:
* generate the [sphinx](https://www.sphinx-doc.org/) **conf.py** file in the **doc** sub-folder
* build the documentation; you can check the result by browsing the **out/doc/index.html** file

