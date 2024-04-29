from django.shortcuts import render,redirect
from drug.models import inpatient_tbl,outpatient_tbl,inproducts_tbl,outproducts_tbl,inpayment_tbl,outpayment_tbl
from django.contrib import messages
# Create your views here.
def log(request):
    if request.method=="POST":
        emails=request.POST.get("email")
        passw=request.POST.get("password")

        obj1=inpatient_tbl.objects.filter(email=emails,password=passw)
        obj2=outpatient_tbl.objects.filter(email=emails,password=passw)

        if obj1:
            return redirect("drug1:inindex")
        
        if obj2:
            return redirect("drug1:outindex")
        

        
    return render(request,"login.html")
def reg(request):
    if request.method=="POST":
        nam=request.POST.get("name")
        numb=request.POST.get("num")
        pat=request.POST.get("patient")
        emails=request.POST.get("email")
        passw=request.POST.get("password")
        if pat=="inpatient":
            obj1=inpatient_tbl.objects.create(name=nam,num=numb,email=emails,password=passw)
            obj1.save()
        else:
            obj2=outpatient_tbl.objects.create(name=nam,num=numb,email=emails,password=passw)
            obj2.save()

            return redirect("drug1:log")

    return render(request,"reg.html")

def inindex(request):
    obj= inproducts_tbl.objects.all()
    idno=request.GET.get('idn')
    request.session['idno']=idno
    return render(request,"inindex.html",{'data':obj})

def outindex(request):
    obj= outproducts_tbl.objects.all()
    return render(request,"outindex.html",{'datas':obj})

def payment(request):
    idno=request.GET.get('idn')
    if request.method =="POST":
        nam=request.POST.get("name")
        addres=request.POST.get("address")
        num=request.POST.get("phone")

        obj=inproducts_tbl.objects.filter(id=idno)
        for m in obj:
            items=m.title
            prices=m.price

        if obj:
            obj2=inpayment_tbl.objects.create(name=nam, address=addres,numb=num,item=items,price=prices)
            obj2.save()
            if obj2:
                return redirect("drug1:inorder")
    return render(request,"payment.html")

def inorder(request):
    obj=inpayment_tbl.objects.all()
    return render(request,"inorder.html",{'dat':obj})

def outpayment(request):
    idno=request.GET.get('idn')
    
    if request.method=="POST":
        nam=request.POST.get("name")
        addres=request.POST.get("address")
        num=request.POST.get("phone")
        print(idno)
        

        obj1=outproducts_tbl.objects.filter(id=idno)
        for m in obj1:
            items=m.title
            prices=m.price
        if obj1:
            obj2=outpayment_tbl.objects.create(name=nam, address=addres,numb=num,item=items,price=prices)
            obj2.save()
            if obj2:
                return redirect("drug1:outorder") 
    return render(request,"outpayment.html")

def outorder(request):
    obj=outpayment_tbl.objects.all()
    return render(request,"outorder.html",{'datt':obj})

# views.py


    



