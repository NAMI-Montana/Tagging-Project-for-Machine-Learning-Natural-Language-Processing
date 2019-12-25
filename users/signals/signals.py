import datetime

from django.http import HttpResponse
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.template.loader import get_template

from brain.util import render_to_pdf


def payment_notification(sender, **kwargs):
    ipn_obj = sender
    print(ipn_obj.payment_status)
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # payment was successful
        template = get_template('users/certificate_template.html')
        minutes = int(ipn_obj.request.user.tagging.count()) * 5
        context = {
            "fullname": ipn_obj.fullname,
            "date": datetime.date.today(),
            "hours": ipn_obj.hours,
        }
        html = template.render(context)
        pdf = render_to_pdf('users/certificate_template.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % "12341231"
            content = "inline; filename='%s'" % filename
            download = ipn_obj.request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % filename
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


valid_ipn_received.connect(payment_notification)
