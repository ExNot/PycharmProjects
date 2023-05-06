from django.shortcuts import render, redirect
from .models import Riddle

#Bilmece nesneleri oluşturuldu
riddles = [
    Riddle("If there are four apples and you take away three, how many do you have?", "3","0"),
    Riddle("A grandmother, two mothers, and two daughters went to a baseball game together and bought one ticket each. How many tickets did they buy in total?", "3","1"),
    Riddle("Eggs are 12 cents a dozen. How many eggs can you get for a dollar?", "100","2"),
    Riddle("A cellphone and a phone case cost $110 in total. The cell phone costs $100 more than the phone case. How much was the cellphone?", "105", "3"),
    Riddle("When Lisa was 6 years old, her sister Lucy was half her age. If Lisa is 40 years old today, how old is Lucy?","37","4"),
    Riddle("A duck was given $9, a spider was given $36, and a bee was given $27. Based on this information, how much money would be given to a cat?", "18","5")
]
def index(request):     #HomePage
    context = {'riddles': riddles} #riddles için dict oluşturuldu
    return render(request, 'home/index.html', context) #dict index.html'e gönderildi


def detail(request,riddle_id):  #riddle detail page
    riddle = riddles[riddle_id-1]   #html parametresinde bilmeceler 1 ile başladığı ve benim oluşturduğum nesnelerde riddles indis gibi düşünülerek 0dan başlatıldığı için 1 çıkarıldı
    context = {'riddle': riddle}    #dict oluşturuldu
    return render(request, 'home/detail.html',context)


def search_results(request): #Search bar
    query = request.GET.get('search_query') #ilk GET metodu request içindeki query çağırısı için 2. get metodu ise search_query değerini arıyoruz
    results = [riddle for riddle in riddles if query in riddle.question or query in riddle.answer] #results değişkenine query içindeki kelimeyi barındıran elemanları atıyoruz
    context = {'riddles':results}
    return render(request, 'home/search_results.html', context)


def check_answer(request, riddle_id):   # Cevap kontrolü
    riddle = riddles[riddle_id]     #riddles nesne dizilerinden id parametresi ile istediğimiz riddle'ı alıyoruz
    answer = request.POST.get('answer') # detail.html'deki seçtiğimiz cevabı getiriyoruz
    if answer == riddle.answer: #cevap doğruysa
        message = 'Congratulations Right Answer'
    else:   #cevap yanlışsa
        message = f'Sorry, False Answer. True Answer is: {riddle.answer}'
    return render(request, 'home/result.html', {'message': message}) #message ile result sayfasına yönlendirdik

