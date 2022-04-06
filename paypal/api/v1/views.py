import json

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.response import Response

from paypal.api.v1.utils.paypal_sdk import PaypalAPI
from paypal.models import BeforePaymentToken, AfterPaymentToken


PLANS = {
    settings.PAYPAL_3_MONTH_PLAN_ID: '3M',
    settings.PAYPAL_6_MONTH_PLAN_ID: '6M',
    settings.PAYPAL_12_MONTH_PLAN_ID: '12M',
}


@login_required
@api_view(['GET'])
def generate_payment_window(request, plan):
    data = PaypalAPI.create_subscription_billing(plan)
    for link in data['links']:
        if link['rel'] == 'approve':
            BeforePaymentToken.objects.create(paypal_subscription_id=data['id'], user=request.user)
            return Response(data={'redirect_url': link['href']}, status=200)


@require_http_methods(['POST'])
@csrf_exempt
def webhooks(request):
    data = json.loads(request.body)
    response = PaypalAPI.verify_webhook(request.headers, request.body)
    if response['verification_status'] == 'SUCCESS' and data['event_type'] == 'BILLING.SUBSCRIPTION.ACTIVATED':
        before_payment_token = BeforePaymentToken.objects.get(paypal_subscription_id=data['resource']['id'])
        AfterPaymentToken.objects.create(
            status='ACTIVE',
            user=before_payment_token.user,
            given_name=data['resource']['subscriber']['name']['given_name'],
            surname=data['resource']['subscriber']['name']['surname'],
            email_address=data['resource']['subscriber']['email_address'],
            payer_id=data['resource']['subscriber']['payer_id'],
            plan=PLANS[data['resource']['plan_id']],
            plan_id=data['resource']['plan_id'],
            expiration_date=data['resource']['billing_info']['next_billing_time'],
            before_payment_token=before_payment_token)

        before_payment_token.user.profile.is_premium = True
        before_payment_token.user.profile.save()

    return HttpResponse(status=200)
