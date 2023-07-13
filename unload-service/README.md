[//]: # (Copyright \(c\) 2023 by Delphix. All rights reserved.)

# Mongo Hyperscale Compliance Unload Service

This is an unload service created for Mongo DB.

## Development:

For contributing to the project, follow the below steps:

### Pre requisites

Python 3.9 should be installed on your system.

    python3.9 -V

For creating virtual environment and installing all the dependencies:

    make env

For running the FastAPI project:

    make run

In case you want to run the app inside a docker container:
    
    make docker-run

This command will first remove the existing docker container and image if it exists,
then build a new docker image and at create and run a docker container with the app inside it.



## Testing

This will run all the unit tests and generate the pytest and coverage reports.

    make tests


## Migrations for DB changes

This will be required when we create migrations for Database Model changes

Steps:
1. Change the model file inside src/models
2. Run `alembic upgrade head` to bring the database to the current state
3. To auto generate migrations run `alembic revision --autogenerate -m "change message"`
    This will generate the migration file inside `migrations/versions`
4. Edit this migration file and update the revision number to an Integer which will be `down_revision`+1 
   
   example: 
   
   <pre>revision = '3'
   down_revision = '2'
   </pre>
