from django.forms import ModelForm
from django.template import Context, loader
from django.shortcuts import render
from public.models import Purchase, Product, UserProfile
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json


# MPOWER PAYMENT DETAILS
URL = "https://app.mpowerpayments.com/sandbox-api/v1/checkout-invoice/create"
HEADER = {
    "Content-Type": "application/json",
    "MP-Master-Key": "dd6f2c90-f075-012f-5b69-00155d866600",
    "MP-Private-Key": "test_private_amOI11Gb0SIo6NSLZr1xkfOYSuE",
    "MP-Token": "d25e1f4ddc053779d526"
}


# Create your views here.
class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase


def helping_hand_lp(request):
    t = loader.get_template('broadcast/helping_hand_lp.html')
    c = Context(dict())
    return HttpResponse(t.render(c))


def purchase_product(request, id):
    purchases = Purchase.objects.filter()
    if request.method == 'POST':
        purchase = Purchase()
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            print form['name'].value(), form['name']
            user = UserProfile.objects.create(name=form['name'].value(), phone=form['phone'].value(),
                                              email=form['email'].value())
            data = {"invoice":
                        {"total_amount": purchase.product.price,
                         "description": purchase.product.description},
                    "store":
                        {"name": "H4P Crew Store"}
                    }

            r = requests.post(URL, data, headers=HEADER)
            response = json.loads(r.text)
            if (r.status_code == 200) and (response['response_code'] == '00'):
                return HttpResponseRedirect('/confirmation/'+str(purchase.id))
            else:
                return HttpResponseRedirect('/error/'+str(purchase.id))
    else:
        form = PurchaseForm()
    t = loader.get_template('broadcast/purchase.html')
    c = Context({'form':form.as_p()})
    return HttpResponse(t.render(c))


def home(request):
    t = loader.get_template('broadcast/home.html')
    c = Context(dict())
    return HttpResponse(t.render(c))
