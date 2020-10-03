from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
"""
messages.debug
messages.info
messages.success
essages.warning
messages.error
"""

def register(request):
    # if request is trying to "post" data into database
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # if the info in form is good to go, username will get the "username" form the form.
            username = form.cleaned_data.get('username')
            # if sign up success, show this message to user, and send them to main page.
            # messages.success(request, f'Account created for {username}!')
            # return redirect('main_home')
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('login')
    else: # if info that user typed in is not valid, get them back to the register page,
          # let them try again.
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
# @sign to me, means that request who qualify the @ function, which is who login here.
# then can request the function follow.
@login_required
def profile(request):
    # this means when user click submit button, then if establish.
    # just like if you type in whatever info into the block, but don't click
    # save button, nothin won't happen.
    if request.method == 'POST':
        """
        u_form get UserUpdateForm's fields which is ['username', email]
        p_form get ProfileUpdateForm's fields which is ['image']
        the instance=request.user means get request's sender's UserUpdateForm's fields info
        which is ['username', 'email'], show in to u_form.
        if without instance=request.user, the web's form ganna be empty.
        if request is trying to "post" data into database
        """
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   # request.FILES save the image file into p_form.
                                   request.FILES,
                                   instance=request.user.profile)
        # need check if info that user put in is valid, then save it if valid.
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been update!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'username_email_form': u_form,
        'image_form': p_form
    }
    return render(request, 'users/profile.html', context)
