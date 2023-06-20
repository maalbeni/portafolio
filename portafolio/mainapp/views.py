from django.shortcuts import render, redirect
from mainapp.forms import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages



# Create your views here.

def index(request):

    return render(request, 'mainapp/index.html', {
        'title' : "Inicio"
    })

def about(request):

    return render(request, 'mainapp/about.html', {
        'title' : "Sobre mi"
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Website Inquiry'
            body = {
                'nombre' : form.cleaned_data['nombre'],
                'email' : form.cleaned_data['email'],
                'mensaje' : form.cleaned_data['mensaje'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'manuelbellonino@gmail.com', ['manuelbellonino@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.add_message(request=request, level=messages.SUCCESS, message="Enviado exitosamente, Gracias.")
            return redirect ('contact')
       
    form = ContactForm()
    return render(request, 'mainapp/contact.html', {'form': form})
