from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

def sendVerifyMail(name, address, token):
    template = get_template('email/varify.html')
    url = "127.0.0.1:8000/register/varify/?actiCode=" + token
    
    content = template.render({'name': name, 'url': url})
    fromAddr = settings.DEFAULT_FROM_EMAIL
    subject = u'【电气实践】请您确认您的邮件'
    
    print(fromAddr)
    msg = EmailMultiAlternatives(subject, content, fromAddr, [address])
    msg.send()

def sendMail(message):
    try:
        message.send()
    except:
        pass