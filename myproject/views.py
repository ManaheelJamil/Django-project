from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
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
   if request.method == "GET":
    output=request.GET.get('output')
    return render(request, "product.html",{"output":output})
    #using this we can get value from url and send on page 
def courseDetail(request,courseid):
    return HttpResponse(courseid)
# using this we can show id through dynmaic routing

def submitform(request):
   try:
        if request.method == "POST":
          n1=int(request.POST.get("name"))
          n2=int(request.POST.get("email"))
          dummy =n1+n2
          print(dummy)
          data={
            "n1":n1,
            "n2":n2,
            "output":dummy
          }
          return HttpResponse(dummy)
   except:
        pass



def userForm(request):
    dummy=0 
    data={}
    try:
        # if request.method =="GET":
        if request.method == "POST":
        # n1 = request.GET['name']
        # n2 = request.GET['email']
        # n1=int(request.GET.get("name"))
        # n2=int(request.GET.get("email"))
          n1=int(request.POST.get("name"))
        n2=int(request.POST.get("email"))
        dummy =n1+n2
        print(dummy)
        data={
            "n1":n1,
            "n2":n2,
            "output":dummy
        }
        url = "/product/?output={}".format(dummy)
        return HttpResponseRedirect(url)
    except : 
        pass
    return render(request, "userform.html",data)
#we pass 3 types of value trough rdynamic routing (int,str,slug(gello-07-jhhh))