from django.shortcuts import render # нужно для возвращения HTML в качестве ответа
from django.http import HttpResponse # класс, который используется для формирования и отправки HTTP-ответов клиенту

# Create your views here.
# Определение view-функций - функций, 
# которые создают запрос и возвращают ответ
# request handler

#--------------------------------------------------------
# Возвращали просто текст
# def say_hello(request):
#     return HttpResponse('Hello World')
#--------------------------------------------------------

def calculate():
    x = 1
    y = 2
    return x + y

# Теперь возвращается HTML
def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Victoria'})
