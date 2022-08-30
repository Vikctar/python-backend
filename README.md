# Python Backend

[![build status](https://github.com/Vikctar/python-backend/actions/workflows/main.yml/badge.svg)](https://github.com/Vikctar/python-backend/actions/workflows/main.yml)

Api for recording trip details

## Project Set up

### Runtime

Python 3.10

### Run it locally

* Clone this repository

```
git clone git@github.com:Vikctar/python-backend.git
```

* Setup a virtual environment in project root

```                                                              
python3 -m venv env                                            
 ```                                                              

* Install dependencies with *pip* by running the following commands in succession

```                                                              
source env/bin/activate                                        
```

```
pip install -U pip
```

```                                                              
pip install -r requirements.txt                            
```                                                              

* Create a *.env* file and update entries with appropriate values

```                                                              
cp .env-example .env                                           
```                                                              

* Generate a secret key using the secrets module and copy the generated key and paste it into .env

```
python
```

```
>>> import secrets
>>> secrets.token_urlsafe(8)
```

* Migrate the database

```                                                              
flask db upgrade                                               
```

* Run the server

```                                                              
flask run                                                      
```                                                              

## Run using docker

To run the app using docker, requires two docker images to be built. A flask image and a mysql image.

* First pull the latest mysql image from docker hub

```
docker pull mysql
 ```

* Run a container from the mysql image providing an envfile that contains the following content. Name the file .env-db

 ```dotenv
MYSQL_ROOT_PASSWORD='my-password'
MYSQL_DATABASE='db-name'
```

```
docker run --name dbserver -d --env-file=.env-db --rm mysql:latest
```

* Build the flask image using the provided Dockerfile

```
docker build -t myapp .
```

* Run the flask container

```
docker run --name python-backend -d -p 8080:5000 --rm --env-file=.env --link dbserver myapp:latest
```

* Access the app locally on port 8080

## API Reference

External API reference can be found at {{base_url}}/docs

Endpoints
---------------

#### POST /record-trip?api_token=some-token

* Description:
    * Records trip details using the request payload.
    * Returns a message on successful transaction or an error


*

Sample `curl -X POST http://{{base_url}}/api/v1/record-trip?api_token=some-token -H "Content-Type: application/json" -d '{"vehicle_id": 1, "driver_id": 1, "customer_id": 1, "address_type": "PICKUP_POINT", "done_by_user_id": 1, "address": "Mombasa", "cargo_tonnage": 1000.00}'`

```
{
  "description": "Trip Recorded",
}
```