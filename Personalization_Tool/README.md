# Personalisation Tool
Personalisation Tool (Enabler 6)

# Including component in Docker-compose.yml file as a service 

```yaml
personalisation-tool:
    image: some.registry.com/xr2learn-enablers/personalisation-tool:latest
    build:
      context: 'Personalization_Tool'
      dockerfile: 'Dockerfile'
    volumes:
      - "./Personalization_Tool:/app"
    working_dir: /app
    environment:
      # To include environment variables in the format below
      - KEY=${KEY}
    #    entrypoint: /bin/sh -c
    command: python <<project_slug>>/<<main_python_file>>.py
```