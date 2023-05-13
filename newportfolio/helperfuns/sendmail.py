from django.core.mail import send_mail
from django.conf import settings


def sendmail(recipient='abdullahzamanbabar2019@gmail.com', subject='Thank You for visiting my portfolio!', message="Thank you for leaving a message on my web portfolio. I'll get back to you soon.\nRegards\nAbdullah Zaman Babar"):

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [recipient],
        fail_silently=False,
        )

    return "0"