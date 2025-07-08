from datetime import date
from django.shortcuts import render
from .forms import PriceEntryForm
from .models import PriceEntry

def price_entry_view(request):
    message = ""
    existing_entries = None

    default_initial = {
        'isin': 'us0000001',
        'quotation_date': date.today().strftime('%Y-%m-%d'),
        'price': 100,
        'currency': 'EUR',
        'source': 'BBG',
        'entered_by': 'Philippe',
    }

    if request.method == 'POST':
        form = PriceEntryForm(request.POST)
        if form.is_valid():
            isin = form.cleaned_data['isin']
            quotation_date = form.cleaned_data['quotation_date']
            existing_entries = PriceEntry.objects.filter(isin=isin, quotation_date=quotation_date)
            if existing_entries.exists():
                message = "⚠️ Cet ISIN existe déjà pour cette date de cotation."
                # On laisse l'utilisateur corriger, donc on garde sa saisie
                today_entries = PriceEntry.objects.filter(quotation_date=date.today())
            else:
                form.save()
                message = "✅ Saisie enregistrée !"
                # Remet le formulaire à zéro AVEC les valeurs par défaut
                form = PriceEntryForm(initial=default_initial)
                # On recharge bien la liste après ajout !
                today_entries = PriceEntry.objects.filter(quotation_date=date.today())
        else:
            # Form non valide, on garde la saisie utilisateur
            today_entries = PriceEntry.objects.filter(quotation_date=date.today())
    else:
        form = PriceEntryForm(initial=default_initial)
        today_entries = PriceEntry.objects.filter(quotation_date=date.today())

    return render(request, 'pricemaker_app/price_entry.html', {
        'form': form,
        'message': message,
        'existing_entries': existing_entries,
        'today_entries': today_entries,
    })
