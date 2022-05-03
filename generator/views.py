from django.shortcuts import render
from random import choice
#from django.http import HttpResponse



def home(request):
    return render(request,'home.html')

def about(request):
    #return HttpResponse('<h1>hello world from DJANGOOOO</h1>')
    return render(request,'about.html')

def password(request):
    print(request.GET)

    ###agregar validaciones por las dudas en caso que el usuario tipee un valor directo en la URL
    characters = list('abcdefghijkmlnñopqrstuvwxyz')
    lenProperty = int(request.GET.get('length'))

    if 'uppercase' in request.GET:
        characters += list('ABCDEFGHIJKLMNÑOPQRSTUVWXTZ')
    
    if 'numbers' in request.GET:
        characters += list('1234567890')
    if 'special' in request.GET:
        characters += list('/*-+.-.,{}+?¡!"#$%&/()=?¡_\' ')
    

    generatedPassword=''
    for character in range(lenProperty):
        generatedPassword += choice(characters)

    return render(request,'password.html',{'password': generatedPassword})

