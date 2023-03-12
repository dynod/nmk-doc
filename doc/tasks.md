# Tasks

The **`nmk-doc`** plugin defines the tasks described below.

## Setup tasks

All tasks in this chapter are dependencies of the main **`setup`** task.

### **`doc.config`** -- doc configuration file generation

This tasks generates the [sphinx](https://www.sphinx-doc.org/) configuration file.

| Property | Value/description |
|-         |-
| builder  | {py:class}`nmk_doc.builders.NmkDocConfigBuilder`
| input    | **${gitVersion}** value (current git version)
| output   | {ref}`${docConfig}<docconfig>` file
| if       | enabled only if {ref}`${docInputs}<docinputs>` config item is not empty

## Build tasks

All tasks in this chapter are dependencies of the main **`build`** task.

### **`doc.build`** -- documentation build

This tasks builds the documentation by calling the [sphinx](https://www.sphinx-doc.org/) tool.

| Property | Value/description |
|-         |-
| builder  | {py:class}`nmk_doc.builders.NmkDocSphinxBuilder`
| input    | {ref}`${docInputs}<docinputs>` files
| output   | {ref}`${docOutput}<docoutput>` folder
| if       | enabled only if {ref}`${docInputs}<docinputs>` config item is not empty
