from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from django.db.models import Sum
# Create your views here.


def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('ammount')
        
        if description is None:
            messages.info(request, "Description is Blank!!!")
            return redirect('/')
        
        
        try:
            amount = float(amount)
        except(TypeError , ValueError):
            messages.info(request, "Account must be a number!!!")
            return redirect('/')
        
        Transaction.objects.create(
            discription = description,
            ammount = amount,
        )
        
        return redirect('/')
    
    context = {'transections' : Transaction.objects.all(),
               'balance' : Transaction.objects.aggregate(total_balace = Sum('ammount'))['total_balace'],
               'income' :  Transaction.objects.filter(ammount__gte = 0).aggregate(income = Sum('ammount'))['income'] or 0,
               'expense' : Transaction.objects.filter(ammount__lte = 0).aggregate(expense = Sum('ammount'))['expense'] or 0
               }
    
    return render(request,'index.html', context)


def deleteHistory(request , uuid):
    Transaction.objects.get(uuid = uuid).delete()
    return redirect('/')