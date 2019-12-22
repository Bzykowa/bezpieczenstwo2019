from django.shortcuts import render, redirect
from AwesomeBank.forms import TransferForm
from AwesomeBank.models import PreparedTransfer, Transfer


# Create your views here.

#@csrf_exempt
def transfer_sending(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            form.save(sender=request.user)
            return redirect('transfer_confirm')
    else:
        form = TransferForm()

    context = {
        'form': form
    }

    return render(request, 'transfer_sending.html', context)

#@csrf_exempt
def transfer_confirmed(request):
    prepared_transfers = []

    for item in PreparedTransfer.objects.all():
        if item.sender_id == request.user.id:
            prepared_transfers.append(item)

    if request.method == 'POST':

        for t in prepared_transfers:
            Transfer.objects.create(recipient_name=t.recipient_name, recipient_account=t.recipient_account,
                                    title=t.title, amount=t.amount, sender=t.sender, approved=t.approved)
            t.delete()
        return redirect('transfer_sent')

    context = {
        'transfers': prepared_transfers
    }
    return render(request, 'transfer_confirm.html', context)

#@csrf_exempt
def transfer_sent(request):
    transfers = []
    for item in Transfer.objects.all():
        if item.sender_id == request.user.id:
            transfers.append(item)

    transfers = [transfers[-1]]

    context = {
        'transfers': transfers
    }

    return render(request, 'transfer_sent.html', context)

#@csrf_exempt
def transfers_history(request):
    transfers = []
    for item in Transfer.objects.all():
        if item.sender_id == request.user.id:
            transfers.append(item)

    context = {
        'transfers': transfers
    }
    return render(request, 'transfers_history.html', context)

def approve_panel(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect("/")

    context = {
        'transfers': Transfer.objects.filter(approved = False)
    }
    return render(request, 'WebPage1.html', context)

def approve_transaction(request, transid):
    print(type(transid))
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect("/")

    transaction = Transfer.objects.get(id=transid)
    transaction.approved = True
    transaction.save()

    return redirect("/approve_panel")
