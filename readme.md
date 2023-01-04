
## How to use it

```shell
$ git clone https://github.com/nehakumari2008/django-calc-ui
$ cd django-calc-ui
$ python3 -m virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver
```

## APIs /api
### /api/add, /api/subtract, /api/multiply, /api/divide
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
/ For main page
<img width="840" alt="Screenshot 2023-01-04 at 9 44 50 PM" src="https://user-images.githubusercontent.com/69853711/210600121-0da08748-529f-47b8-be62-9322d5f014e0.png">
