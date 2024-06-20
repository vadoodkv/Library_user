
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import addin

# Create your views here.

def print_addi(request):
    if request.POST:
        bkid=request.POST.get('book_id')
        bknm=request.POST.get('book_name')
        brid=request.POST.get('borrowee_id')
        name=request.POST.get('name')
        address=request.POST.get('address')
        phno=request.POST.get('phone_no')
        addin_obj=addin(Book_id=bkid,Book_name=bknm,Borr_id=brid,Name=name,Address=address,Phone=phno)
        addin_obj.save()
   
    return render(request,'adding.html')



def print_land(request):
    
    return render(request,'landing.html')


def print_sear(request):
    if request.method=='GET':
     query=request.GET.get('bookid')
     data=addin.objects.filter(Book_id=query)
     
   
    return render(request,'searching.html',{'data':data})

   
            
            
    
    


