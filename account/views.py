from django.shortcuts import render, redirect
from.forms import RegistrationForm
from.models import account
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# email verification imports
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name'] # this cleaned_data function will get the request and 
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split('@')[0]

            user = account.object.create_user(first_name= first_name, last_name=last_name, email=email, username=username,
                                               password=password )
            user.phone_number = phone_number
            user.save()

            # due to the some terms in the account model, a new user cannot log into our sites because
            # the is_active boolean in the model is setb to false, therefore we need to verify the user b4 
            # he or she signs into my site ,, below are some verification codes i want to pass to this user via
            # email, then , when the user is verified , the boolean is automatically set to true and the user can login.

          #   mail_subject = 'please activate your account'
         #   message = render_to_string('account/verification.html',{ # find this template to see what is inside 
        #        'user': user,
         #       'domain': current_site,
         #       'uid': urlsafe_base64_encode(force_bytes(user.pk)),
           #     'token': default_token_generator.make_token(user),
        #    })
        #    to_email = email
         #   send_mail = EmailMessage(mail_subject, message, to=[to_email,])
         #   send_mail.send()

            # after this coding, inhave to go configure the smtp email configuration on the settings.py file .. down below

            messages.success(request,'Account created successfully, Login') 
            return redirect('login')
    else:
         form = RegistrationForm()
    context ={
        'form':form
    }
    return render(request, 'account/register.html',context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email'].lower()
        password = request.POST['password']#.lower()

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('dashboard')
            
        else:
            messages.error(request,'Invalid email or password')
            return redirect('login')

    return render(request, 'account/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out ')
    return redirect('login')

def activate(request, uidb64, token):
    return HttpResponse('okay')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'account/dashboard.html')