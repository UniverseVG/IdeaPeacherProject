from django.shortcuts import redirect, render
from ideapeacher.forms import CreateUserForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.http import HttpResponse
from . models import sponser
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def registerSponser(request):
    form = CreateUserForm()
    if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                if not Group.objects.filter(name="sponser").exists():
                    group = Group.objects.create(name="sponser")
                    addtogroup = Group.objects.get(name='sponser')
                    user.groups.add(addtogroup)

                    sponser.objects.create(user=user, name=user.username)
                    messages.success(
                    request, 'Account was created for ' + username)
                    return redirect('/login_request1/')

                else:
                    group = Group.objects.get(name='sponser')
                    user.groups.add(group)
                    sponser.objects.create(user=user, name=user.username)
                    messages.success(
                    request, 'Account was created for ' + username)
                    return redirect('/login_request1/')

    context = {'form': form}

    return render(request, 'main/register.html', context)

