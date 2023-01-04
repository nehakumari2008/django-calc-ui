Calculator with following functions:

## How to use it

```shell
$ git clone https://github.com/nehakumari2008/django-calc-ui
$ cd django-calc-ui
$ python3 -m virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver
```

## APIs
### /add, /subtract, /multiply, /divide
Request format: POST with following json format
```json
{
  "num1": 500,
  "num2": 2100
}
```
### Response format
```json
{
  "num1": 500,
  "num2": 2100,
  "sum/diff/division/multiplication": 2600
}
```
# UI
/
For main page
