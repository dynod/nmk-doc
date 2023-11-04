# Tasks

The **`nmk-doc`** plugin defines the tasks described below.

## Setup tasks

All tasks in this chapter are dependencies of the base [**`setup`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#setup-task) task.

### **`doc.config`** -- doc configuration file generation

This tasks generates the [sphinx](https://www.sphinx-doc.org/) configuration file.

| Property | Value/description |
|-         |-
| builder  | [**`nmk_base.common.TemplateBuilder`**](https://nmk-base.readthedocs.io/en/stable/autoapi/nmk_base/common/index.html#nmk_base.common.TemplateBuilder)
| input    | {ref}`${docConfigTemplate}<docConfigTemplate>` template file
| output   | {ref}`${docConfig}<docconfig>` file
| if       | enabled only if {ref}`${docInputs}<docinputs>` config item is not empty

### **`doc.rtd`** -- Read The Docs build configuration file generation

This tasks generates the [Read The Docs](https://readthedocs.org/) automated build configuration file.

| Property | Value/description |
|-         |-
| builder  | [**`nmk_base.common.TemplateBuilder`**](https://nmk-base.readthedocs.io/en/stable/autoapi/nmk_base/common/index.html#nmk_base.common.TemplateBuilder)
| inputs    | {ref}`${docConfig}<docconfig>` doc config file<br>{ref}`${docRTDConfigTemplate}<docRTDConfigTemplate>` template file
| output   | {ref}`${docRTDConfig}<docRTDConfig>` file
| if       | enabled only if {ref}`${docInputs}<docinputs>` config item is not empty

## Build tasks

All tasks in this chapter are dependencies of the base [**`build`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#build-task) task.

### **`doc.build`** -- documentation build

This tasks builds the documentation by calling the [sphinx](https://www.sphinx-doc.org/) tool.

| Property | Value/description |
|-         |-
| builder  | {py:class}`nmk_doc.builders.NmkDocSphinxBuilder`
| input    | {ref}`${docInputs}<docinputs>` files
| output   | {ref}`${docOutput}<docoutput>` folder
| if       | enabled only if {ref}`${docInputs}<docinputs>` config item is not empty
