# Analysing reports of events involving automated vehicles with ChatGPT

In the description below, it is assumed that the repo is stored in the folder `llm-robot`. Terminal commands lower assume macOS.

## Setup
Tested with Python 3.9.12. To setup the environment run these two commands in a parent folder of the downloaded repository (replace `/` with `\` and possibly add `--user` if on Windows):
- `pip install -e llm-robot` will setup the project as a package accessible in the environment.
- `pip install -r llm-robot/requirements.txt` will install required packages.

For analysis with GPT-V, the API key of OpenAI needs to be placed in file `llm-robot/secret`. The file needs to be formatted as `llm-robot/secret example`.

### Configuration of project
Configuration of the project needs to be defined in `llm-robot/config`. Please use the `default.config` file for the required structure of the file. If no custom config file is provided, `default.config` is used. The config file has the following parameters:
* `reports`: path with reports.
* `plotly_template`: template used to make graphs in the analysis.

## Analysis
Analysis can be started by running `python llm-robot/gptevents/run.py`. A number of CSV files used for data processing are saved in `llm-robot/_output`. Visualisations of all data are saved in `llm-robot/_output/figures/`.

## Troubleshooting
### Troubleshooting setup
#### ERROR: llm-robot is not a valid editable requirement
Check that you are indeed in the parent folder for running command `pip install -e llm-robot`. This command will not work from inside of the folder containing the repo.