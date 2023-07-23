from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#from .forms import ComplainForm
from .models import Notification
# Create your views here.
'''
@login_required
def ComplainView(request,id=None):

    if request.method=="POST":
        form=ComplainForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.author=request.user
            obj.save()
            messages.add_message(request, messages.SUCCESS,  'Your Complain recieved response will be provided soon')
        return redirect('homepage')
    context=dict()
    form=ComplainForm()
    context['complain_form']=form
    return render(request,'complain.html',context)
'''


@login_required
def NotificationView(request,id=None):
    context=dict()
    notifications=Notification.objects.filter(author=request.user)
    context['notifications']=notifications
    return render(request,'notifications.html',context)


@login_required
def DeleteNotification(request,id=None):

    instance=Notification.objects.get(pk=id)
    instance.delete()
    messages.add_message(request, messages.SUCCESS,  'One notification deleted successfully')
    return redirect('homepage')


def NotificationDetails(request,id=None):
    context=dict()
    notification=Notification.objects.get(pk=id)
    context['notification']=notification
    return render(request,'notification_details.html',context)