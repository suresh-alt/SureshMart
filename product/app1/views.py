from django.shortcuts import render,redirect
from app1.form import Custerform,Productform
from django.contrib import messages
from app1.models import productmodel,Customer
from django.core.paginator import Paginator

def show(req):
    return render(req,"index.html")

def home(req):
    return render(req,"registration.html",{"form":Custerform()})
def save(req):
    fm=Custerform(req.POST)
    if fm.is_valid():
        fm.save()
        messages.success(req,"Registration completed successfully")
        return redirect('home')
    else:
        return render(req,"registration.html",{"form":fm})

def admin(req):
    return render(req,"admin.html")

def adlogin(req):
    un=req.POST.get("t1")
    pa=req.POST.get("t2")

    if un == 'raju' and pa == '12345':
        return render(req,"welcomeadmin.html")
    else:
        return render(req,"admin.html",{"error":"invalid details"})

def addp(req):
    return render(req,"addproduct.html",{"form":Productform()})
def savep(req):
    fm=Productform(req.POST,req.FILES)
    if fm.is_valid():
        fm.save()
        messages.success(req,'product is saved')
        return redirect('addp')
    else:
        return render(req,"addproduct.html",{"form":fm})

def viewall(req):
    return render(req,"viewallpro.html",{"data":productmodel.objects.all()})

def updatepro(req):
   no= req.GET.get("pn")
   return render(req,"update.html",{"data":productmodel.objects.get(pno=no)})
def ud(req):
    n=req.POST.get("u1")
    na = req.POST.get("u2")
    p = req.POST.get("u3")
    q = req.POST.get("u4")
    img= req.POST.get("u5")
    res=productmodel.objects.filter(pno=n).update(pname=na,price=p,quantity=q)



    return redirect('viewall')
def delete(req):
    no=req.GET.get("pn")
    productmodel.objects.filter(pno=no).delete()
    return redirect('viewall')
def clogin(req):
    return render(req,"customerlogin.html")
def c(req):
    try:
         un=req.POST.get("t1")
         pa=req.POST.get("t2")
         Customer.objects.get(username=un,password=pa)
         return render(req,"welcomecustomer.html")
    except Customer.DoesNotExist:
        return render(req,"customerlogin.html",{"error":"invalid details"})

def h1(req):
    return render(req,"welcomecustomer.html")
def vpro(req):
    res=productmodel.objects.all()

    pa = Paginator(res, 2)
    pageno = req.GET.get("pno", 1)
    pg = pa.page(pageno)
    return render(req,"vpro.html", {"data":pg,"cdata":len(req.COOKIES)})
def cart(req):
    no=req.GET.get("no")
    nam=req.GET.get("na")
    response=redirect('vpro')
    response.set_cookie(no,nam)
    return response

def cartview(req):
    return render(req,"cartview.html",{"data":req.COOKIES})
def cartdelete(req):
    no = req.GET.get("pn")
    response = redirect('vpro')
    response.delete_cookie(no)
    return response


