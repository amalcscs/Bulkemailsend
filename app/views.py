from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import *
import csv
import os
import uuid

def index(request):
    if request.method == "POST":
        uploaded_file = request.FILES['file']
        uploaded_fileimg = request.FILES.getlist('images')  

        if uploaded_file.name.endswith('.xls') or uploaded_file.name.endswith('.xlsx'):
            data = pd.read_excel(uploaded_file)
        attachments=[]
        for f in uploaded_fileimg:
            attachments.append((f.name, f.read(), f.content_type))

            email_col = data.get('email')
            name_col = data.get('name')

            if email_col is not None and name_col is not None:
                emails = list(email_col)
                names = list(name_col)

                message = request.POST['message']

                subject = request.POST['subject']
                from_email = 'your_email@example.com'

                for i in range(len(emails)):
                    content = f'Dear {names[i]},\n\n{message}\n\nBest regards,\nAltos technologies'

                    email = EmailMultiAlternatives(subject, content, from_email, [emails[i]],attachments=attachments)



                    email.send()

                return HttpResponse('<script>alert("MAILS HAVE BEEN SENT SUCCESSFULLY. THANK YOU FOR USING OUR SERVICE"); window.location.href = "/";</script>')

            else:
                return HttpResponse('<script>alert("The excel file must contain columns name and email"); window.location.href = "/";</script>')
        else:
            return render(request, 'error.html', {'message': 'Please upload a valid Excel file.'})

    return render(request, 'index.html')


