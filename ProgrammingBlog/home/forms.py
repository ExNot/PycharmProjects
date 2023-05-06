from django import forms

class SearchForm(forms.Form): #Bu form girdiğimiz metini tutması için oluşturuldu!
    search_query = forms.CharField(max_length=100)