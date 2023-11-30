from time import sleep
from django.core.mail import send_mail
from celery import shared_task
from .models import *

@shared_task()
def send_email_task():
    """Sends an email when the profile has been created."""
    sleep(20)  # Simulate expensive operation(s) that freeze Django
    message="Hope you have a great day ahead!"
    all_profiles=Profiles.objects.filter(is_verified=False)
    emails_list=[]
    for item in all_profiles:
        emails_list.append(item.email)
    print(emails_list)
    send_mail(
        "Your Profile has been created.",
        f"\t{message}\n\nThank you!",
        "support@example.com",
        emails_list,
        fail_silently=False,
    )