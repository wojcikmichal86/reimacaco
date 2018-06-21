from django.shortcuts import render
from django.http import HttpResponse
import requests
from requests import request
from bs4 import BeautifulSoup
import lxml

def landing_page(request):
	return render(request, 'porta/landing_page.html', {})

def main(request):
	return render(request, 'porta/main.html', {})

def blog(request):
	return render(request, 'porta/blog.html', {})



gyms=['lea', 'mogilska', 'solvaypark', 'wadowicka', 'krakowska', 'aleksandry', 'plaza', 'zakopianska', 'nastoku', 'bratyslawska']

display='<table style="width:100%"><tr><th>Aula</th><th>Dia</th><th>Hora</th><th>Academia</th></tr>'
def gym_spider(gym):
    global display
    godziny = []
    zajecia = []
    url = 'http://fitnessplatinium.pl/'+str(gym)+'/grafik/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    dni=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


    for hour in soup.findAll('td', {'class': 'hour'}):
        if hour.contents==[]:
            hour.contents=['']
        godziny.append(hour.contents)
    for n,i in enumerate(godziny):
        if i==['']:
            godziny[n]=godziny[n-1]
    temp=[]
    for a in godziny:
        if isinstance(a, list):
            temp.extend(a)
    for aula in soup.findAll('td', {'class': 'active'}):
        if aula.contents==None:
            aula.contents=[]
        else:
            aula.contents=str(aula.findAll('h6'))[5:-6]
        zajecia.append([aula.contents])
    for c in zajecia:
        if "&amp" in c[0]:
            c[0]=c[0].replace("&amp;","&")
        c.append(dni[zajecia.index(c)%7])
        c.append(str(temp[int(zajecia.index(c)/7)]))
        c.append(gym)
    klasy=[]
    for c in zajecia:
        if c[0]!='':
            klasy.append(c)
    for klasa in klasy:
        display+='<tr>'
        for info in klasa:
            display+='<td style="text-align:center">'+str(info)+'</td>'
        display+='</tr>'
for gym in gyms:
    gym_spider(gym)


def gyms(request):
    return HttpResponse(display+'</table>')