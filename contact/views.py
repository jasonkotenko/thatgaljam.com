from forms import ContactForm
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponseRedirect

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            #cc_myself = form.cleaned_data['cc_myself']
            subject = "[thatgaljam] Contact Form - " + subject
            
            recipients = ['jamglam@gmail.com']
            #if cc_myself:
            #    recipients.append(sender)
                
            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
    
    return render_to_response('contact.html', {'form':form,},
                context_instance=RequestContext(request))
