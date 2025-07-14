from django.core.mail import send_mail,EmailMessage
from django.conf import settings



def SENDING_MAIL():
    send_mail(
    subject = 'Testing Django Mail.',
    message = 'Hi, My name is Sanu Singh....This mail is to test, how the mail is send from django project.',
    from_email = settings.EMAIL_HOST_USER,
    recipient_list=['priyanshuthapa93@gmail.com','djcosty452@gmail.com'],
    fail_silently=False
    )

# this one is a function which is used to send a Email with File Attachment with it
def SEND_EMAIL_WITH_FILE(subject,message,recipient_list,FILE_PATH):
    Mail = EmailMessage(subject=subject,body=message,from_email=settings.EMAIL_HOST_USER,to=recipient_list)
    Mail.attach_file(FILE_PATH)
    Mail.send()

