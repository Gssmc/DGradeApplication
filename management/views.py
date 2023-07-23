from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductUploadForm

from .models import Garbage,Cleaner,GarbageOrder
from accounts.models import MyUser


@login_required
def UploadGarbageView(request,id=None):

    context=dict()
    if request.method=="POST":
        form=ProductUploadForm(request.POST,request.FILES)

        if id!=None:
            garbag=Garbage.objects.get(pk=id)
            form=ProductUploadForm(request.POST,request.FILES,instance=garbag)

            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,'your garbage updated successfully')
                
        else:
            if form.is_valid():
                obj=form.save(commit=False)
                obj.uploaded_by=request.user.id
                obj.save()
                messages.add_message(request, messages.SUCCESS,  'Your Waste Posted successfully it will be published after acknowledgement')
        return redirect('homepage')

    else:
        if 2==request.user.account_type:
            messages.add_message(request, messages.ERROR,  'Your Account is Buyer type please create a seller type Account')
            return redirect('homepage')

        if id!=None:
            garbag=Garbage.objects.get(pk=id)
            form=ProductUploadForm(instance=garbag)
        else:
            form=ProductUploadForm()

        context['upload_form']=form
    return render(request,'publish_waste.html',context)


#display all garbage view is here

def DisplayWasteView(request):

    if not request.user.is_authenticated:
        messages.add_message(request,messages.ERROR,'please login first')
        return redirect('homepage')

    if 1==request.user.account_type:
        messages.add_message(request, messages.ERROR,  'Your Account is Seller type please create a Buyer type Account to Buy Garbage')
        return redirect('homepage') 
    context=dict()
    active_garbages=Garbage.objects.filter(status=True)
    context['garbages']=active_garbages
    context['loop_times'] = range(1, 4)
    return render(request,'display_waste.html',context)


@login_required
def BuyGarbageView(request,slug=None,id=None):

    context=dict()
    garbage=Garbage.objects.get(pk=id)
    owner=MyUser.objects.get(pk=garbage.uploaded_by)

    context['garbage']=garbage
    context['owner']=owner
    return render(request,'garbage_buy.html',context)


@login_required
def CleanerView(request):
    context=dict()
    cleaners=Cleaner.objects.all()

    times=range(1,5)
    context['cleaners']=cleaners
    context['loop_times']=times


    return render(request,'cleaner.html',context)

@login_required
def CleanerDetailView(request,id=None):
    
    context=dict()
    cleaner=Cleaner.objects.get(pk=id)
    context['cleaner']=cleaner
    return render(request,'cleaner_details.html',context)



def AboutUs(request):

    return render(request,'about.html',)

@login_required
def GarbageOrderView(request,slug=None,id=None):

    obj=Garbage.objects.get(pk=id)
    obj.status=False
    obj.save()
    if  GarbageOrder.objects.filter(ordered_by=request.user.id,ordered_garbage=obj).count()==0:
        GarbageOrder.objects.create(ordered_by=request.user.id,ordered_garbage=obj)
        messages.add_message(request, messages.SUCCESS,  'Your Order Recieved Successfully')
    return redirect('homepage')