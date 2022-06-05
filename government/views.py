from django.shortcuts import redirect, render
from django.views import View, generic

from .forms import ImporterForm, LocalSupplierForm, ConsumerForm
from django.contrib import messages
from .models import Importer, LocalSupplier,Consumer


def index(request):
    context = {}
    context['imports']=Importer.objects.all()
    context['local_supplies']=LocalSupplier.objects.all()
    context['consumers']=Consumer.objects.all()
    return render(request, 'base.html', context)

class Import(generic.FormView):
    template_name = 'import.html'
    form_class = ImporterForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LocalSupplierView(generic.FormView):
    template_name = 'localsupplier.html'
    form_class = LocalSupplierForm
    success_url = '/'
    def form_valid(self, form):
        importerId = self.request.POST.get('importer')
        importer = Importer.objects.get(pk=int(importerId))
        if importer.can_supply_to_local_supplier():
            importer.amount_supplied += int(self.request.POST['amount_bought'])
            importer.remaining_amount -=int(self.request.POST['amount_bought'])
            importer.save()
            form.save()
            messages.info(self.request, 'You have successfully imported {} {} from {}'.format(self.request.POST['amount_bought'], self.request.POST['product_name'], importer))
            return redirect('info')
        else:
            messages.error(self.request, 'You cannot import more than 100 {} from {} as they have less than that'.format(self.request.POST['product_name'], importer))
            return redirect('info')
        return super().form_valid(form)



class ConsumerView(generic.FormView):
    template_name = 'consumer.html'
    form_class = ConsumerForm
    success_url = '/'
    def form_valid(self, form):
        supplierId = self.request.POST['LocalSupplier']
        sell_supplier = LocalSupplier.objects.get(pk=int(supplierId))
        if sell_supplier.can_sell():
            sell_supplier.amount_supplied += int(self.request.POST['amount_bought'])
            sell_supplier.remaining_amount -=int(self.request.POST['amount_bought'])
            sell_supplier.save()
            form.save()
            messages.info(self.request, 'You have successfully purchased {} {} from {}'.format(self.request.POST['amount_bought'], self.request.POST['product_name'], sell_supplier))
            return redirect('info')
        else:
            messages.error(self.request, 'You cannot purchase {} {} from {} as your purchase is above what is remaining'.format(self.request.POST['amount_bought'], self.request.POST['product_name'], sell_supplier))
            return redirect('info')
        return super().form_valid(form)




def info(request):
    return render(request, 'info.html')