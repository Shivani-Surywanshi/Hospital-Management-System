from django.shortcuts import render, redirect
from paymentapp.forms import DischargeSummaryForm
from paymentapp.models import DischargeSummary


def discharge(request):
    if request.method == 'POST':
        form = DischargeSummaryForm(request.POST)

        if form.is_valid():
            obj = form.save()
            return redirect('final_bill', obj.id)

    else:
        form = DischargeSummaryForm()

    return render(request, 'paymentapp/discharge_summary.html', {
        'form': form
    })


def final_bill(request, id):
    data = DischargeSummary.objects.get(id=id)

    room_charges = {
        'Common Ward': {
            'bed': 250,
            'nursing': 300,
            'doctor': 250,
            'misc': 100,
            'medicine_percent': 10
        },

        'Semi Private': {
            'bed': 1000,
            'nursing': 1000,
            'doctor': 550,
            'misc': 250,
            'medicine_percent': 12
        },

        'Private AC': {
            'bed': 1550,
            'nursing': 1250,
            'doctor': 650,
            'misc': 350,
            'medicine_percent': 15
        },

        'Private Non AC': {
            'bed': 1250,
            'nursing': 1150,
            'doctor': 650,
            'misc': 350,
            'medicine_percent': 13
        },

        'Deluxe': {
            'bed': 2000,
            'nursing': 1500,
            'doctor': 850,
            'misc': 500,
            'medicine_percent': 20
        }
    }

    charges = room_charges[data.room_type]

    # Per Day Total
    daily_total = (
        charges['bed'] +
        charges['nursing'] +
        charges['doctor'] +
        charges['misc']
    )

    # Room Charges
    room_total = daily_total * data.total_days

    # Food Charges
    food_per_day = 480

    if data.food_required:
        food_total = food_per_day * data.total_days
    else:
        food_total = 0

    # Medicine Charges
    medicine_charge = (room_total * charges['medicine_percent']) / 100

    # Final Total
    total = room_total + food_total + medicine_charge

    return render(request, 'paymentapp/final_bill.html', {
        'data': data,

        'bed_charge': charges['bed'],
        'nursing_charge': charges['nursing'],
        'doctor_charge': charges['doctor'],
        'misc_charge': charges['misc'],

        'room_total': room_total,
        'food_total': food_total,

        'medicine_percent': charges['medicine_percent'],
        'medicine_charge': medicine_charge,

        'total': total
    })