# Tasks

The **`nmk-doc`** plugin defines the tasks described below.

---

## Setup tasks

All tasks in this chapter are dependencies of the base [**`setup`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#setup-task) task.

---

(doc.config)=

### **`doc.config`** -- doc configuration file generation

This tasks generates the [sphinx](https://www.sphinx-doc.org/) configuration file.

| Property | Value/description                                                                                                                                                                                         |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| builder  | [**`nmk_base.common.TemplateBuilder`**](https://nmk-base.readthedocs.io/en/stable/autoapi/nmk_base/common/index.html#nmk_base.common.TemplateBuilder)                                                     |
| input    | {ref}`${docConfigTemplate}<docConfigTemplate>` template file                                                                                                                                              |
| output   | {ref}`${docConfig}<docconfig>` file                                                                                                                                                                       |
| if       | enabled only if {ref}`${docIndex}<docIndex>` config item is not empty<br> <br>_<span style="color:orange">Changed in version 1.1.0</span>_ -- Previous enablement item was {ref}`${docInputs}<docInputs>` |

---

(doc.rtd)=

### **`doc.rtd`** -- Read The Docs build configuration file generation

This tasks generates the [Read The Docs](https://readthedocs.org/) automated build configuration file.

| Property | Value/description                                                                                                                                                                                         |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| builder  | [**`nmk_base.common.TemplateBuilder`**](https://nmk-base.readthedocs.io/en/stable/autoapi/nmk_base/common/index.html#nmk_base.common.TemplateBuilder)                                                     |
| inputs   | {ref}`${docConfig}<docconfig>` doc config file<br>{ref}`${docRTDConfigTemplate}<docRTDConfigTemplate>` template file                                                                                      |
| output   | {ref}`${docRTDConfig}<docRTDConfig>` file                                                                                                                                                                 |
| if       | enabled only if {ref}`${docIndex}<docIndex>` config item is not empty<br> <br>_<span style="color:orange">Changed in version 1.1.0</span>_ -- Previous enablement item was {ref}`${docInputs}<docInputs>` |

---

(puml.download)=

### **`puml.download`** -- Download the PlantUML runtime

This tasks downloads the [PlantUML](https://plantuml.com/) runtime, needed to generate image files from input diagram files.

| Property | Value/description                                                                                                                                     |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| builder  | [**`nmk_base.common.DownloadBuilder`**](https://nmk-base.readthedocs.io/en/stable/autoapi/nmk_base/common/index.html#nmk_base.common.DownloadBuilder) |
| inputs   | [**`${PROJECTFILES}`**](https://nmk.readthedocs.io/en/stable/file.html#built-in-config-items)                                                         |
| output   | {ref}`${plantUmlLocalPath}<plantUmlLocalPath>` file                                                                                                   |
| if       | {ref}`${plantUmlReady}<plantUmlReady>`                                                                                                                |

Builder is called with the following parameters:

| Parameter name   | Value                                                                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| url              | {ref}`${plantUmlDownloadUrl}<plantUmlDownloadUrl>`                                                                                    |
| request_function | [**`${requestFunction}`**](https://nmk-base.readthedocs.io/en/stable/config.html#requestfunction-request-function-for-download-tasks) |

_<span style="color:green">Added in version 1.1.0</span>_

---

## Build tasks

All tasks in this chapter are dependencies of the base [**`build.doc`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#build-doc-task) task.

_<span style="color:orange">Changed in version 1.2.0</span>_ -- previous dependency was on main [**`build`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#build-task) task.

---

(doc.build)=

### **`doc.build`** -- documentation build

This tasks builds the documentation by calling the [sphinx](https://www.sphinx-doc.org/) tool.

| Property | Value/description                                                                                                                                                                                         |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| builder  | {py:class}`nmk_doc.builders.NmkDocSphinxBuilder`                                                                                                                                                          |
| input    | {ref}`${docInputs}<docinputs>` files                                                                                                                                                                      |
| output   | {ref}`${docOutput}<docoutput>` folder                                                                                                                                                                     |
| if       | enabled only if {ref}`${docIndex}<docIndex>` config item is not empty<br> <br>_<span style="color:orange">Changed in version 1.1.0</span>_ -- Previous enablement item was {ref}`${docInputs}<docInputs>` |

Builder is called with the following parameters:

| Parameter name | Value                                                                                              |
| -------------- | -------------------------------------------------------------------------------------------------- |
| source_folder  | {ref}`${docPath}<docPath>`                                                                         |
| output_folder  | {ref}`${docOutput}<docOutput>`                                                                     |
| version        | {ref}`${docVersion}<docVersion>`<br> <br>_<span style="color:green">Added in version 1.1.0</span>_ |

---

(puml.generate)=

### **`puml.generate`** -- Generate the PlantUML diagram images

This tasks calls the [PlantUML](https://plantuml.com/) runtime to generate image files from input diagram files.

| Property | Value/description                                        |
| -------- | -------------------------------------------------------- |
| builder  | {py:class}`nmk_doc.builders.PlantUmlBuilder`             |
| inputs   | {ref}`${plantUmlDiagrams}<plantUmlDiagrams>` files       |
| output   | {ref}`${plantUmlOutputFiles}<plantUmlOutputFiles>` files |
| if       | {ref}`${plantUmlReady}<plantUmlReady>`                   |

Builder is called with the following parameters:

| Parameter name | Value                                                                                                          |
| -------------- | -------------------------------------------------------------------------------------------------------------- |
| jar            | {ref}`${plantUmlLocalPath}<plantUmlLocalPath>`                                                                 |
| java_runtime   | [${javaRuntime}](https://nmk-base.readthedocs.io/en/stable/config.html#javaruntime-resolved-java-command-path) |
| input_folder   | {ref}`${plantUmlDiagramsFolder}<plantUmlDiagramsFolder>`                                                       |
| output_folder  | {ref}`${plantUmlOutputFolder}<plantUmlOutputFolder>`                                                           |
| formats        | {ref}`${plantUmlOutputFormats}<plantUmlOutputFormats>`                                                         |
| extra_options  | {ref}`${plantUmlExtraOptions}<plantUmlExtraOptions>`                                                           |

_<span style="color:green">Added in version 1.1.0</span>_
