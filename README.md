# API REST Example with Flask

## Created with
* Flask
* Flask-SQLAlchemy

### How to install
1. Clone this repository
```
$ git clone [repo-url]
```
2. Install requirements
```
$ pip install -r requirements.txt
```
3. Run server
```
$ flask --app main.py run
```

3. Run the following code in python. TRANSACTION_ID is the ID to evaluate, MODEL is the department that owns the model, VERSION is the version of the model and SERVER is the server address.
```
import requests

TRANSACTION_ID = 3
MODEL = 'fraud'
VERSION = '1.0.0'
SERVER = 'http://127.0.0.1:5000'

evaluations = requests.get(f'{SERVER}/api/v1/model_decision/{TRANSACTION_ID}')
if evaluations.json()['evaluations'] == []:
    transactions = requests.get(f'{SERVER}/api/v1/raw_data/{TRANSACTION_ID}')
    features = requests.post('{SERVER}/api/v1/compute_features/', 
                             json=(transactions.json()["transactions"]))
    scoring = requests.post(f'{SERVER}/api/v1/model_decision/{MODEL}/{VERSION}/', 
                            json=features.json()['features'])
    evaluations = requests.get(f'{SERVER}/api/v1/model_decision/{TRANSACTION_ID}')

evaluations.json()
```

### API Spec

---
#### `GET` `api/v1/test`
Test that API is running
**Response**: A message
```json
{
    "message": "hello from api v1!"
}
```

### Links of interest
* [Create an API in Flask](https://codigofacilito.com/articulos/api-flask)
* [Flask and SQLAlchemy](https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application)
* [Deploy Flask App as Azure Fuction](https://www.youtube.com/watch?v=ldFJBzSH5cM)