from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    evenNumberList=[x for x in range(2,45,2)]
    return render(request, 'home/index.html', {'evenNumberList': evenNumberList})


def details(requset, detailNumber):
    return HttpResponse(f"{detailNumber} details page!")

def archive(response, archiveNumber):
    return HttpResponse(f'Archive number: {archiveNumber}')

def comment(request, commentNumber):
    return HttpResponse(f'{commentNumber}. comment!')