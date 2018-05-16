from django.shortcuts import render, redirect, HttpResponse
def index(request):
    return render(request, "survey/index.html")

def process(request):
    full_name = request.form['full_name']
    comment = request.form['comment']
    language = request.form.get('language',None)
    place = request.form.get('location',None)
    return render(request,'survey/result.html',full_name=full_name,comment=comment,language=language,place=place)
