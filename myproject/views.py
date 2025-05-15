from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import usersForm



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
          dummy = n1+n2
          print(dummy)
          data={
            "n1":n1,
            "n2":n2,
            "output":dummy
          }
          return HttpResponse(dummy)
   except:
        pass

   return render(request, 'result.html')
   
# def userForm(request):
#     dummy=0 
#     data={}
#     try:
#         # if request.method =="GET":
#         if request.method == "POST":
#         # n1 = request.GET['name']
#         # n2 = request.GET['email']
#         # n1=int(request.GET.get("name"))
#         # n2=int(request.GET.get("email"))
#             n1=int(request.POST.get("name"))
#             n2=int(request.POST.get("email"))
#             dummy = n1+n2
#         print(dummy)
#         data={
#             "n1":n1,
#             "n2":n2,
#             "output":dummy
#         }

#         url = "/product/?output={}".format(dummy)
#         return HttpResponseRedirect(url)
#     except : 
#         pass
#     return render(request, "userform.html",data)

def userForm(request):
    data = {}
    if request.method == "POST":
        form = usersForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data['num1']
            n2 = form.cleaned_data['num2']
            output = n1 + n2
            return redirect(f"/product/?output={output}")
    else:
        form = usersForm()

    data['form'] = form
    return render(request, "userform.html", data)

def calculator(request):
    c=""
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == "+":
                c= n1+n2
            elif opr == "-":
                c= n1-n2
            elif opr =="*":
                c= n1*n2
            elif opr == "/":
                c = n1 / n2
    except:
        c = "Invalid opr......"               

    return render(request,"calculator.html",{'c':c})

def evenodd(request):
    c=""
    if request.method == "POST":
        if request.POST.get("num1") == "":
           return render(request,"evenodd.html",{"error":True})
        n = eval(request.POST.get("num1"))
        if n%2 ==0:
            c = "Even number"
        else:
            c="odd number"
    

    return render(request,"evenodd.html",{"c":c})

def marksheet(request):
    c=""
    if request.method == "POST":
        n1 = eval(request.POST.get("num1"))
        n2 = eval(request.POST.get("num2"))
        n3 = eval(request.POST.get("num3"))
        n4 = eval(request.POST.get("num4"))
        n5 = eval(request.POST.get("num5"))
        c = n1+n2+n3+n4+n5
        p = c*100/500
        if p >= 90:
            d = "A+ Grade"
        elif p >= 80:
            d = "A Grade"
        elif p >= 60:
            d = "B Grade"
        elif p >= 50:
            d = "C Grade"
        else:
            d = "Fail"    
        data={
            "total":c,
            "per":p,
            "div":d
        }
        return render(request,"marksheet.html",data)
    return render(request, "marksheet.html")