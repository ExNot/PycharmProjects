from django.http import HttpResponse
from django.shortcuts import render

#/home/
def index(request):
    evenNumberList = [item for item in range(2,45,2)]
    return render(request, 'home/index.html', {'evenNumberList': evenNumberList})

 # def detail(request, detailNumber):
 #     return HttpResponse(f'{detailNumber} You are in details page')


def archive(response, archiveNumber):
    return HttpResponse(f'Arşiv numarası {archiveNumber}')
