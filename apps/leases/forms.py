from django import forms
from .models import Lease

class LeaseForm(forms.ModelForm):
    agreement = forms.BooleanField(required=False, label="أوافق على جميع الشروط والأحكام واتعهد بدفع جميع المبالغ المستحقة للكهرباء والمياه واعادة العقار كما استلكته")

    class Meta:
        model = Lease
        fields = ['tenant', 'unit', 'start_date', 'end_date', 'contract_file', 'landlord_signature', 'tenant_signature']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date >= end_date:
            raise forms.ValidationError("يجب ان يكون تاريخ انتهاء العقد بعد تاريخ البدء")
        return cleaned_data