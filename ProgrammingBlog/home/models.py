from django.db import models

class Riddle(): #Riddle class'ı oluşturuldu
    def __init__(self, question, answer, id, *args, **kwargs): #python'a constructor'ı oluşturtuldu ve ayrıca question, answer, id değişkenleri tanımlandı
        super().__init__(*args, **kwargs)
        self.question = question
        self.answer = answer
        self.id = id





