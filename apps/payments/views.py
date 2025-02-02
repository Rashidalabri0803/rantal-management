from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Payment
from .forms import PaymentForm

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payments/payment_list.html', {'payments': payments})

def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            payment = form.save()
            messages.success(request, 'تم تسجيل الدفع بنجاح!')
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'payments/create_payment.html', {'form': form})