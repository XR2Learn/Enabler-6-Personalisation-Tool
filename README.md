![XR2Learn](https://raw.githubusercontent.com/XR2Learn/.github/5c0fada6136915b389c1cd2151a0dd2cfc4a5aac/images/XR2Learn%20logo.png)

# Enabler 6: Personalisation Tool
This repository implements Enabler 6 for the XR2Learn project, the personalisation tool. 
The personalisation tool automatically provides suggestions for the adjustment of an activity level based on emotions classified by the other Enablers components. 

# Install 
1. Clone the repository

## Local run (Development focused)

1. Run Redis docker 

      `docker compose up redis -d`

   2. To stop Redis docker 

       `docker compose down`
   
2. Run 

   `python personalisation_tool/suggest_activity_level.py`

3. Run (in another terminal tab) 

   `python personalisation_tool/simulate_input_output.py`

## Run using docker images

1. Enter docker image with bash entrypoint

    `REDIS_HOST=redis docker compose run --rm personalisation-tool /bin/bash`
2. Run the simulate input/output script in background

`python personalisation_tool/simulate_input_output.py > out.txt &`

3. Run suggest activity level script

`python personalisation_tool/suggest_activity_level.py`


## Run DemoUI + Personalisation tool 

`docker compose up -d`

Go to `http://172.22.0.3:8000/` to access DemoUI. 

# Changelog
A list of released versions and the main changes can be found on [Changelog](CHANGELOG.md).