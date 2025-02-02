from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .forms import PropertyForm
from .models import Property


@login_required
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'properties/property_list.html', {'properties': properties})
  
@login_required
def property_detail(request, property_id):
    property_obj = get_object_or_404(Property, pk=property_id)
    return render(request, 'properties/property_detail.html', {'property': property_obj})