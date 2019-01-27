from django.shortcuts import render, redirect
from django.contrib import messages
from apps.products.models import *

def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/index.html', context)

def purchase(request):

    if request.method == 'POST':
        purchase = request.POST
        # Form validation
        errors = Product.objects.validate(purchase)
        if errors:
            for error in errors:
                messages.error(request,error)
            return redirect('products:index')
        else:
            
            # Determine total price and remove the amount purchased from available inventory numbers.
            purchasedItem = Product.objects.get(id=int(purchase['id']))
            purchasedItemPrice = float(purchasedItem.price)
            numPurchase = float(purchase['numPurchase'])

            request.session['priceCharged'] = purchasedItemPrice * numPurchase
            
            numAvail = purchasedItem.numAvail
            numAvail -= numPurchase
            purchasedItem.numAvail = numAvail
            purchasedItem.save()
            
            # Create or add to session-stored information of total purchases.  This would be more suited to the database if the project were fully developed.
            if 'totalCharged' not in request.session:
                request.session['totalCharged'] = request.session['priceCharged']
            else:
                chargeThisPurchase = request.session['priceCharged']
                totalCharged = request.session['totalCharged']
                totalCharged += chargeThisPurchase
                totalCharged = round(totalCharged, 2)
                request.session['totalCharged'] = totalCharged
            
            # Create or add to total number of items purchased for this session.
            if 'numItemsPurchased' not in request.session:
                request.session['numItemsPurchased'] = int(numPurchase)
            else:
                numItemsPurchased = int(request.session['numItemsPurchased'])
                numItemsPurchased += int(numPurchase)
                request.session['numItemsPurchased'] = numItemsPurchased
            return redirect('products:thankyou')
    else: 
        return redirect('products:index')

def thankyou(request):
    return render(request, 'products/thankyou.html')