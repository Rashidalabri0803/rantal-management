from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from tinycss2.color4 import parse_color
from weasyprint import HTML

from .forms import LeaseForm
from .models import Lease


def lease_list(request):
    leases = Lease.objects.all()
    return render(request, 'leases/lease_list.html', {'leases': leases})

def lease_detail(request, lease_id):
    lease = get_object_or_404(Lease, id=lease_id)
    return render(request, 'leases/lease_detail.html', {'lease': lease})

def create_lease(request):
    if request.method == 'POST':
        form = LeaseForm(request.POST, request.FILES)
        if form.is_valid():
            lease = form.save()
            messages.success(request, 'تم إنشاء عقد الإيجار بنجاح!')
            return redirect('lease_list')
    else:
        form = LeaseForm()
    return render(request, 'leases/lease_create.html', {'form': form})

def generate_lease_pdf(request, lease_id):
    lease = get_object_or_404(Lease, id=lease_id)
    context = {'lease': lease}
    html_context = render_to_string('leases/lease_template.html', context)
    pdf_file = HTML(string=html_context).write_pdf()
    color = parse_color('rgba(255, 99, 71, 0.5)')
    print(color)
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'filename="lease_{lease.id}.pdf'
    return response