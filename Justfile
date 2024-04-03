# a justfile that makes running the crews easier

# run a the crew
project NAME *ARGS:
    @echo "Running project: {{NAME}}"
    python aicrew/projects/{{NAME}}/team.py {{ARGS}}
