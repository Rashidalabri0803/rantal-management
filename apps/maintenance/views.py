from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import MaintenanceForm
from .models import Maintenance


def maintenance_list(request):
    maintenances = Maintenance.objects.all()
    return render(request, 'maintenance/maintenance_list.html', {'maintenances': maintenances})

def create_maintenance(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST, request.FILES)
        if form.is_valid():
            maintenance = form.save()
            messages.success(request, 'تم تقديم طلب الصيانة!')
            return redirect('maintenance_list')
    else:
        form = MaintenanceForm()
    return render(request, 'maintenance/create_maintenance.html', {'form': form})