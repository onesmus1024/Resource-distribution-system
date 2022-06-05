from django import forms
from .models import Importer, LocalSupplier, Consumer

class ImporterForm(forms.ModelForm):
    class Meta:
        model = Importer
        fields = ('name', 'email', 'amount_bought', 'product_name', 'imported_from', )


class LocalSupplierForm(forms.ModelForm):
    class Meta:
        model = LocalSupplier
        fields = ('name', 'email', 'amount_bought', 'product_name', 'location','importer' )

class ConsumerForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = ('name','amount_bought', 'product_name','LocalSupplier')