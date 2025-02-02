from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserUpdateForm


@login_required
def profile_view(request):
  if request.method == 'POST':
    form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
    if form.is_valid():
      form.save()
      messages.success(request, 'تم تحديث بياناتك بنجاح!')
      return redirect('profile')
  else:
    form = UserUpdateForm(instance=request.user)
  return render(request, 'users/profile.html', {'form': form})
