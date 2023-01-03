import json

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def addition(request, number1, number2):
    sum = (number1 + number2)
    processed_data = {"num1": number1, "num2": number2, "Sum": sum}
    json_object = json.dumps(processed_data, indent=4)
    return HttpResponse(json_object)


def subtraction(request, number1, number2):
    diff = (number1 - number2)
    processed_data = {"num1": number1, "num2": number2, "difference": diff}
    json_object = json.dumps(processed_data, indent=4)
    return HttpResponse(json_object)


def multiplication(request, number2, number1):
    mul = (number1 * number2)
    processed_data = {"num1": number1, "num2": number2, "Multiplication": mul}
    json_object = json.dumps(processed_data, indent=4)
    return HttpResponse(json_object)


def division(request, number1, number2):
    try:
        div = (number1 / number2)
        processed_data = {"num1": number1, "num2": number2, "division": div}
        json_object = json.dumps(processed_data, indent=4)
        return HttpResponse(json_object)
    except:
        return HttpResponse("Cannot be divide by 0")
