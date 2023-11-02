# Tasks

The **`nmk-doc`** plugin defines the tasks described below.

## Setup tasks

All tasks in this chapter are dependencies of the base [**`setup`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#setup-task) task.

### **`doc.config`** -- doc configuration file generation

This tasks generates the [sphinx](https://www.sphinx-doc.org/) configuration file.

| Property | Value/description |
|-         |-
| builder  | {py:class}`nmk_doc.builders.NmkDocConfigBuilder`
| input    | **[${gitVersion}](https://nmk-base.readthedocs.io/en/stable/config.html#gitversion-git-version)** value (current git version)
| output   | {ref}`${docConfig}<docconfig>` file
| if       | enabled only if {ref}`${docInputs}<docinputs>` config item is not empty

### **`doc.rtd`** -- Read The Docs build configuration file generation

This tasks generates the [Read The Docs](https://readthedocs.org/) automated build configuration file.

| Property | Value/description |
|-         |-
| builder  | {py:class}`nmk_doc.builders.NmkDocConfigBuilder`
| input    | {ref}`${docConfig}<docconfig>` doc config file
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
