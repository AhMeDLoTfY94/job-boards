from django.shortcuts import redirect, render
from .forms import SignUpForm,UserForm,ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.urls import reverse

def signup(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password1"]
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form=SignUpForm()
    
    context={
        'form':form
    }
    return render(request,'registration/signup.html',context)
    

def profile(request):
    profile=Profile.objects.get(user=request.user)


    context={
        'profile':profile,
    }

    return render(request,"accounts/profile.html",context)



def profile_edit(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=="POST":
        userform=UserForm(request.POST,instance=request.user)
        profilefrom=ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profilefrom.is_valid():
            userform.save()
            myprofile=profilefrom.save(commit=False)
            myprofile.user=request.user
            myprofile.save()
            return redirect(reverse('profile'))
        

    else:
        userform=UserForm(instance=request.user)
        profilefrom=ProfileForm(instance=profile)


    context={
        "userform":userform,
        "profileform":profilefrom,
    }
    return render (request,'accounts/profile_edit.html',context)