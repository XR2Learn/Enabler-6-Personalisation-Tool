# XR2Learn Enabler 6: Personalisation Tool
This repository implements Enabler 6 for the XR2Learn project, the personalisation tool. 
The personalisation tool automatically provides suggestions for the adjustment of an activity level based on emotions classified by the other Enablers components. 

# Install 
1. Clone the repository

2. Create a configuration.json file by copying from example.configuration.json by running:
  
   `cp example.configuration.json configuration.json`

# Development
## Local run

1. Run Redis docker 

      `docker compose up redis -d`

   2. To stop Redis docker 

       `docker compose down`
   
2. Run 

   `python personalisation_tool/suggest_activity_level.py`

3. Run (in another terminal tab) 

   `python personalisation_tool/simulate_input_output.py`

## Run inside docker image

1. Enter docker image with bash entrypoint

    `REDIS_HOST=redis docker compose run --rm personalisation-tool /bin/bash`
2. Run the simulate input/output script in background

`python personalisation_tool/simulate_input_output.py > out.txt &`

3. Run suggest activity level script

`python personalisation_tool/suggest_activity_level.py`


## Run DemoUI + Personalisation tool 

`docker compose up -d`

Go to `http://172.22.0.3:8000/` to access DemoUI. 