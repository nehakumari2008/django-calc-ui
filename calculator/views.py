import json

from django.http import HttpResponse
# from django.shortcuts import render
#
# Create your views here.
from calculator.models import Operation

from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'base.html')


def addition(request, number1, number2):
    sum = (number1 + number2)
    processed_data = {"num1": number1, "num2": number2, "sum": sum}
    json_object = json.dumps(processed_data, indent=4)
    calculate = Operation(First_number=number1, Second_number=number2, operator='+', Result=sum)
    calculate.save()
    return HttpResponse(json_object)


def subtraction(request, number1, number2):
    diff = (number1 - number2)
    processed_data = {"num1": number1, "num2": number2, "difference": diff}
    json_object = json.dumps(processed_data, indent=4)
    calculate = Operation(First_number=number1, Second_number=number2, operator='-', Result=diff)
    calculate.save()
    return HttpResponse(json_object)


def multiplication(request, number2, number1):
    mul = (number1 * number2)
    processed_data = {"num1": number1, "num2": number2, "Multiplication": mul}
    json_object = json.dumps(processed_data, indent=4)
    calculate = Operation(First_number=number1, Second_number=number2, operator='*', Result=mul)
    calculate.save()
    return HttpResponse(json_object)


def division(request, number1, number2):
    try:
        div = (number1 / number2)
        processed_data = {"num1": number1, "num2": number2, "division": div}
        json_object = json.dumps(processed_data, indent=4)
        calculate = Operation(First_number=number1, Second_number=number2, operator='/', Result=div)
        calculate.save()
        return HttpResponse(json_object)
    except:
        return HttpResponse("Cannot be divide by 0")

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
# def history_view(request):
#     show_history = Operation.objects.all().values()
#     return render(request, 'history.html', {'show history': show_history})

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
