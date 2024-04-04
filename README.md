# Analysing reports of events involving automated vehicles with ChatGPT

In the description below, it is assumed that the repo is stored in the folder `chatgpt-av-events`. Terminal commands lower assume macOS.

## Setup
Tested with Python 3.9.12. To setup the environment run these two commands in a parent folder of the downloaded repository (replace `/` with `\` and possibly add `--user` if on Windows):
- `pip install -e chatgpt-av-events` will setup the project as a package accessible in the environment.
- `pip install -r chatgpt-av-events/requirements.txt` will install required packages.

### Configuration of project
Configuration of the project needs to be defined in `chatgpt-av-events/config`. Please use the `default.config` file for the required structure of the file. If no custom config file is provided, `default.config` is used. The config file has the following parameters:
* `reports`: path with reports.
* `plotly_template`: template used to make graphs in the analysis.

## Preparation of reports
The source files of the video stimuli are outputted from Unity to `config.path_source`. To prepare them for the crowdsourced setup `python chatgpt-av-events/preparation/process_videos.py`. Videos will be outputted to `config.path_stimuli`.

## Troubleshooting
### Troubleshooting setup
#### ERROR: chatgpt-av-events is not a valid editable requirement
Check that you are indeed in the parent folder for running command `pip install -e chatgpt-av-events`. This command will not work from inside of the folder containing the repo.