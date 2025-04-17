from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    # data={
    #     "title":"home page",
    #     "name":"welcome to my Django webbsite",
    #     "items":["timater","oranfe","marinda"],
    #     "numbers":[10,20,30,40],
    #     "list":[{"name":"one","phone":123456},{"name":"two","phone":123456},{"name":"three","phone":123456}]
    # }
    return render(request, "index.html")

def aboutUs(request):
    return render(request, "aboutus.html")

def products(request):
    return render(request, "product.html")
# using this we can show id through dynmaic routing
def courseDetail(request,courseid):
    return HttpResponse(courseid)

def userForm(request):
    dummy =0 
    try:
        # n1 = request.GET['name']
        # n2 = request.GET['email']
        n1=int(request.GET.get("name"))
        n2=int(request.GET.get("email"))
        dummy =n1+n2
        print(dummy)
    except : 
        pass
    return render(request, "userform.html",{"output":dummy})
#we pass 3 types of value trough rdynamic routing (int,str,slug(gello-07-jhhh))