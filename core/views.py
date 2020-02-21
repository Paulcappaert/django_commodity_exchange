from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm

def home(request):
    return render(request, 'core/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account updated')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'core/profile.html', {'form': form})