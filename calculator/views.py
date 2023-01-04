import json

from django.http import HttpResponse
# from django.shortcuts import render
#
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from calculator.models import Operation

from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'base.html')


@csrf_exempt
def addition(request):
    if request.method == "POST":
        data = json.loads(request.body)
        number1 = data['num1']
        number2 = data['num2']
        sum = (number1 + number2)
        processed_data = {"num1": number1, "num2": number2, "sum": sum}
        json_object = json.dumps(processed_data, indent=4)
        # Saving operation log in DB
        calculate = Operation(first_number=number1, second_number=number2, operator='+', Result=sum)
        calculate.save()
        return HttpResponse(json_object)


@csrf_exempt
def subtraction(request):
    if request.method == "POST":
        data = json.loads(request.body)
        number1 = data['num1']
        number2 = data['num2']
        diff = (number1 - number2)
        processed_data = {"num1": number1, "num2": number2, "diff": diff}
        json_object = json.dumps(processed_data, indent=4)
        calculate = Operation(first_number=number1, second_number=number2, operator='-', Result=diff)
        calculate.save()
        return HttpResponse(json_object)


@csrf_exempt
def multiplication(request):
    if request.method == "POST":
        data = json.loads(request.body)
        number1 = data['num1']
        number2 = data['num2']
        mul = (number1 * number2)
        processed_data = {"num1": number1, "num2": number2, "Multiplication": mul}
        json_object = json.dumps(processed_data, indent=4)
        calculate = Operation(first_number=number1, second_number=number2, operator='*', Result=mul)
        calculate.save()
        return HttpResponse(json_object)


@csrf_exempt
def division(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            number1 = data['num1']
            number2 = data['num2']
            div = (number1 / number2)
            processed_data = {"num1": number1, "num2": number2, "division": div}
            json_object = json.dumps(processed_data, indent=4)
            calculate = Operation(first_number=number1, second_number=number2, operator='/', Result=div)
            calculate.save()
            return HttpResponse(json_object)
        except ZeroDivisionError:
            return HttpResponse(ZeroDivisionError)




# def addition(request):
#     input1 = int(request.POST['num1'])
#     input2 = int(request.POST['num2'])
#     res = input1 + input2
#     calculate = Operation(First_number=input1, Second_number=input2, operator='+', Result=res)
#     calculate.save()
#
#     return render(request, 'result.html', {"result": res})
#
#
# def subtraction(request):
#     input1 = int(request.POST['num1'])
#     input2 = int(request.POST['num2'])
#     res = input1 - input2
#     calculate = Operation(First_number=input1, Second_number=input2, operator='-', Result=res)
#     calculate.save()
#
#     return render(request, 'result.html', {"result": res})
#
#
# def multiplication(request):
#     input1 = int(request.POST['num1'])
#     input2 = int(request.POST['num2'])
#     res = input1 * input2
#     calculate = Operation(First_number=input1, Second_number=input2, operator='*', Result=res)
#     calculate.save()
#
#     return render(request, 'result.html', {"Result": res})
#
#
# def division(request):
#     try:
#         input1 = int(request.POST['num1'])
#         input2 = int(request.POST['num2'])
#         res = input1 / input2
#         calculate = Operation(First_number=input1, Second_number=input2, operator='/', Result=res)
#         calculate.save()
#
#         return render(request, 'result.html', {"result": res})
#     except:
#         return render(request, 'result.html', {"result": "Cannot be divide by 0"})
#
#


# def viewAdd(request):
#     return render(request, 'add.html')
#
# def viewSub(request):
#     return render(request, 'sub.html')
#
#
# def viewMul(request):
#     return render(request, 'multiply.html')
#
#
# def viewDiv(request):
#     return render(request, 'div.html')
