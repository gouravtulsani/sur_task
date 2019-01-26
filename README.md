# Survaider Backend Task

### Installation

Backend Server [Python](https://docs.python.org/3.6/) v3.6+ to run.

Create python3 virtual env and install the dependencies,
migrate database, load data and start the server.

```sh
$ git clone git@github.com:gouravtulsani/sur_task.git
$ cd sur_task
$ python3 -m venv .
$ pip install -r requirments.txt
$ python src/manage.py makemigrations && python src/manage.py migrate
$ python src/manage.py load_data # This will take some time
$ python src/manage.py runserver
# In new terminal
$ {firefox|google-chrome} path/to/project/src/frontend_task/index.html
```

## APIs

### Sex Destribution
- API description:
    > This api is use to get count based on sex destribution
- Request Headers:
    - Request URL: **/sex_destribution**
    - Supported Request Methods: GET
    - Content-Type: application/json
- Response headers:
- Status ``200``:
    - Content-Type: application/json
    - Response Body: *{result: ...}*

### Relationship Destribution
- API description:
    > This api is use to get count based on Relationship destribution
- Request Headers:
    - Request URL: **/relation_destribution**
    - Supported Request Methods: GET
    - Content-Type: application/json
- Response headers:
- Status ``200``:
    - Content-Type: application/json
    - Response Body: *{result: ...}*

### Raw Data
- API description:
    > This api is use to see the raw  adult data
- Request Headers:
    - Request URL: **/raw_data**
    - Supported Request Methods: GET
    - Content-Type: application/json
- Response headers:
- Status ``200``:
    - Content-Type: application/json
    - Response Body: *{result: [[...], [...], ...]}*

