import ast

import weasyprint
from django.conf import settings
from django.core.mail import EmailMessage
from django.dispatch import receiver
from django.http import HttpResponse
from django.template.loader import render_to_string
from paypal.standard.ipn.signals import valid_ipn_received, payment_was_flagged
from paypal.standard.models import ST_PP_COMPLETED


@receiver(valid_ipn_received)
def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    # Undertake some action depending upon `ipn_obj`.
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        print('Payment is completed')
        user_infor = ast.literal_eval(ipn_obj.custom)
        if ipn_obj.receiver_email == settings.PAYPAL_RECEIVER_EMAIL:
            print('And Payment is valid')
            # generate and send an email with pdf certificate file to the user's email
            user_infor = ast.literal_eval(ipn_obj.custom)
            user_info = {
                "name": user_infor['name'],
                "hours": user_infor['hours'],
                "taggedArticles": user_infor['taggedArticles'],
                "email": user_infor['email'],
                "date": user_infor['date'],
            }
            html = render_to_string('users/certificate_template.html',
                                    {'user': user_info})
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'filename=certificate_{}'.format(user_info['name']) + '.pdf'
            pdf = weasyprint.HTML(string=html, base_url=settings.host + '/users/process/').write_pdf(
                stylesheets=[weasyprint.CSS(string='body { font-family: serif}')])
            to_emails = [str(user_infor['email'])]
            subject = "Certificate from Nami Montana"
            email = EmailMessage(subject, body=pdf, from_email=settings.EMAIL_HOST_USER, to=to_emails)
            email.attach("certificate_{}".format(user_infor['name']) + '.pdf', pdf, "application/pdf")
            email.content_subtype = "pdf"  # Main content is now text/html
            email.encoding = 'us-ascii'
            email.send()
        else:
            payment_was_flagged.connect(do_not_show_me_the_money)
            # if int(user_infor['taggedArticles']) > 11:
            #     # generate and send an email with pdf certificate file to the user's email
            #     user_info = {
            #         "name": user_infor['name'],
            #         "hours": user_infor['hours'],
            #         "taggedArticles": user_infor['taggedArticles'],
            #         "email": user_infor['email'],
            #         "date": user_infor['date'],
            #     }
            #     html = render_to_string('users/certificate_template.html',
            #                             {'user': user_info})
            #     pdf = weasyprint.HTML(string=html, base_url='http://8d8093d5.ngrok.io/users/process/').write_pdf(
            #         stylesheets=[weasyprint.CSS(string='body { font-family: serif}')])
            #     to_emails = [str(user_infor['email']), 'arycloud7@gmail.com']
            #     subject = "Certificate from Nami Montana"
            #     email = EmailMessage(subject,
            #                          body=pdf,
            #                          from_email=settings.EMAIL_HOST_USER, to=to_emails)
            #     email.attach("certificate_{}".format(user_infor['name']) + '.pdf', pdf, "application/pdf")
            #     email.content_subtype = "pdf"  # Main content is now pdf
            #     email.encoding = 'us-ascii'
            #     email.send()
    # else:
    #     print('Get fail signal')
    #     user_infor = ast.literal_eval(ipn_obj.custom)
    #     to_emails = [str(user_infor['email'])]
    #     subject = "Certificate from Nami Montana"
    #     # message = 'Enjoy your certificate.'
    #     email = EmailMessage(subject, body='Unfortunately, there\'s something wrong with your payment.Check your'
    #                                        + 'paypal account, please!',
    #                          from_email=settings.EMAIL_HOST_USER, to=to_emails)
    #
    #     # email.content_subtype = "pdf"  # Main content is now text/html
    #     # email.encoding = 'us-ascii'
    #     email.send()


#
# def show_me_the_money(sender, **kwargs):
#     print('Payment is valid')


# @receiver(invalid_ipn_received)
def do_not_show_me_the_money(sender, **kwargs):
    print('And Payment is not valid')
    ipn_obj = sender
    user_infor = ast.literal_eval(ipn_obj.custom)
    to_emails = [str(user_infor['email'])]
    subject = "Certificate from Nami Montana"
    # message = 'Enjoy your certificate.'
    email = EmailMessage(subject, body='Unfortunately, there\'s something wrong with your payment as it\'s'
                                       'not validated.Check your PayPal account, please!',
                         from_email=settings.EMAIL_HOST_USER, to=to_emails)
    email.send()


valid_ipn_received.connect(show_me_the_money)
