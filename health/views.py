from django.shortcuts import render, get_object_or_404, redirect
from .models import Prescription, Event
from django.contrib import messages


# Create your views here.

def dashboard(request):
    prescriptions = Prescription.objects.all()

    for prescription in prescriptions:  
        prescription.latest_event = prescription.events.first()  

    
    context = {
        'prescriptions': prescriptions, 
        'title': 'Intake Dashboard'
    }
    
    return render(request, 'health/dashboard.html', context)  # Fixed: render() not (render, ...)


def prescription_detail(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    events = prescription.events.all()

    if request.method == 'POST':
        try:
            event = Event(
                prescription=prescription,
                performed_by=request.POST.get('performed_by', '').strip(), 
                event_type=request.POST.get('event_type', 'NOTE'),  
                description=request.POST.get('description', '').strip()  
            )  # Fixed: closing parenthesis here
            event.save()  # Fixed: moved outside Event() constructor
            messages.success(request, "Event added successfully")
            return redirect('prescription_detail', pk=pk)
        except Exception as e:
            messages.error(request, f'Error adding event: {str(e)}')  
    
    context = {
        'prescription': prescription,
        'events': events,
        'title': f'Prescription - {prescription.patient_name}',  
        'event_types': Event.EVENT_TYPES,
    }

    return render(request, 'health/prescription_detail.html', context)  