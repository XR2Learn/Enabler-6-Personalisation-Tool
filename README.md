![XR2Learn](https://raw.githubusercontent.com/XR2Learn/.github/5c0fada6136915b389c1cd2151a0dd2cfc4a5aac/images/XR2Learn%20logo.png)

# [XR2Learn Personalization Enablers]: Personalisation Tool

The Personalization Tool utilizes the user’s predicted emotions as the output of the Training and Inference domain,
together with contextual information, e.g., a user and activity levels, to provide personalized suggestions on the
recommended activity level for the user in educational XR applications.

The Personalization Tool exploits the Publisher/Subscriber messaging protocol implemented using Redis to provide
asynchronous, real-time communication between the Personalization Tool, Inference domain and an XR educational software
implemented using Unity.

A web-based DemoUI is also provided as a graphic interface for better visualizing the personalization tool functionality
and how it communicates with the other domain’s components, i.e., multimodal fusion layer and Unity application.

## Pre-requisites

Personalization Tool supports the three main Operational Systems (OS): Linux, MacOS, and Windows.
The two pre-requisites are:

1. Docker installed
2. Python 3.10 installed

## Installation

1. Navigate to the root directory of the downloaded project, and from the root repository, run the command to build the
   docker images:

   `docker compose build`

## For installing locally (Development focused):

### Personalization Tool

1. Navigate to the directory Personalisation_Tool
2. Prepare the virtual environment (Create and activate virtual environment with venv).

   `python -m venv ./venv`

   `source ./venv/bin/activate`
3. Install the requirements within the virtual environment

   `pip install -r requirements.txt`

### DemoUI

1. Navigate to the directory DemoUI
2. Prepare the virtual environment (Create and activate virtual environment with venv).

`python -m venv ./venv`

`source ./venv/bin/activate`

3. Install the requirements within the virtual environment

`pip install -r requirements.txt`

## Basic User Manual

Personalization Tool can be used as a standalone application or with Enablers-CLI, a command-line interface to simplify
the use of Enablers. The easiest way to access the Personalization Tool’s functionalities is by
using [Enablers-CLI](https://github.com/XR2Learn/Enablers-CLI).

However, if changing or expanding the Personalization tool’s functionalities is required, it is possible to access each
component using docker commands, as exemplified below. Thus, the instructions described below are focused on a
development environment.

A “configuration.json” file is required to provide the components with the necessary specifications for running. A
default version of “configuration.json” is provided and can be changed by the user.

### Local run
1. Run Redis docker

   `docker compose up redis -d`

    2. To stop Redis docker

       `docker compose down`

2. Run

   `python personalisation_tool/suggest_activity_level.py`

3. Run (in another terminal tab)

   `python personalisation_tool/simulate_input_output.py`

### Run using docker images

1. Enter docker image with bash entrypoint

   `REDIS_HOST=redis docker compose run --rm personalisation-tool /bin/bash`
2. Run simulate input/output script in background

`python personalisation_tool/simulate_input_output.py > out.txt &`

3. Run suggest activity level script

`python personalisation_tool/suggest_activity_level.py`

### Run DemoUI + Personalisation tool

`docker compose up -d`

Go to `http://172.22.0.3:8000/` to access DemoUI.

## License

Copyright © 2024, Maastricht University

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Pre-trained and fine-tuned models created using the RAVDESS dataset are shared under
the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en) license to
comply with the RAVDESS license, as the models are derivative works from this dataset.

Please refer to [LICENSE.md](LICENSE.md) document for more details.

## Changelog

A list of released versions and the main changes can be found on [Changelog](CHANGELOG.md).