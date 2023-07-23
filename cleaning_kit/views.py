from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import CleaningKit,Notification
from .forms import OrderForm


@login_required
def DisplayCleaningMaterialsView(request):
    if 1==request.user.account_type:
        messages.add_message(request, messages.ERROR,  'Your Account is Seller type please create a Buyer type Account to Buy Cleaning Materials')
        return redirect('homepage') 

    context=dict()
 
    
    kits=CleaningKit.objects.all()
    context['kits']=kits
    context['loop_times']=range(1,5)
    return render(request,'display_cleaning_kit.html',context)


@login_required
def BuyKitView(request,user_id=None,kit_id=None):
    
    context=dict()
    if request.method=="POST":
        from django.utils import timezone
        from datetime import timedelta
        dalivery_date = str(timezone.now() + timedelta(days=6))
        
        form=OrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.ordered_by=user_id
            instance.product_id=kit_id
            instance.save()
            Notification.objects.create(to=user_id,desc="Your product will be delivered within "+dalivery_date)
            messages.add_message(request, messages.SUCCESS,  'Your Order Recieved Successfully')

        return redirect('homepage')

    
    else:
        kit=CleaningKit.objects.get(pk=kit_id)
        context['kit']=kit
        order_form=OrderForm()
        context['order_form']=order_form
    return render(request,'buy_kit.html',context)