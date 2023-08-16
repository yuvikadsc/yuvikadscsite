from django.shortcuts import render,redirect
from .models import CustomerData
from django.contrib import messages
from django.db.models import Q
import time

# Create your views here.

def index(request):
    customers = CustomerData.objects.all()
    query = ""

    if request.method == "POST":
        if "add" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            CustomerData.objects.create(
                name=name,
                email=email
            )
            messages.success(request,"Customer added successfully....!!")

        elif "delete" in request.POST:
            id = request.POST.get("id")
            CustomerData.objects.get(id=id).delete()
            messages.error(request,"Customer deleted successfully....!!")
        
        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")

            update_customer = CustomerData.objects.get(id=id)
            update_customer.name = name
            update_customer.email = email
            update_customer.save()
            messages.info(request,"Customer updated successfully....!!")

        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            customers = CustomerData.objects.filter(Q(name__icontains=query))
        

    context = {"customers" : customers, "query" : query}
    return render(request, "crudapp/index.html", context=context)