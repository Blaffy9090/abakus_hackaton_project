from django.shortcuts import render, redirect
from .models import Event, Registration
from .forms import EventForm


def event_list(request):
    events = Event.objects.all().order_by('-time')
    context = {
        'events': events,
    }
    return render(request, 'event_list.html', context)


def event_detail(request, id):
    event = Event.objects.get(id=id)
    registrations = event.registration_set.all()
    context = {
        'event': event,
        'registrations': registrations
    }
    return render(request, 'event_detail.html', context)


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    context = {
        'form': form
    }
    return render(request, 'event_create.html', context)


def event_register(request, id):
    event = Event.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # create registration
        Registration.objects.create(event=event, name=name, email=email, password=password)
        return redirect('event_detail', id=id)
    context = {
        'event': event
    }
    return render(request, 'event_register.html', context)


def event_content(request, id):
    event = Event.objects.get(id=id)
    context = {
        'event': event,
    }
    return render(request, 'event_subpage.html', context)


def event_login(request,id):
    event = Event.objects.get(id=id)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if event.registration_set.filter(email=email, password=password).exists():
            return redirect('event_content', id=id)
        else:
            return redirect('event_detail', id=id)
    context = {
        'event': event
    }
    return render(request, 'event_login.html', context)





