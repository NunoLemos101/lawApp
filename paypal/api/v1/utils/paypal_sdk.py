import json
import requests

from django.conf import settings

PLANS = {
    '3-month-plan': settings.PAYPAL_3_MONTH_PLAN_ID,
    '6-month-plan': settings.PAYPAL_6_MONTH_PLAN_ID,
    '12-month-plan': settings.PAYPAL_12_MONTH_PLAN_ID,
}


class PaypalSDK:
    def __init__(self, client_id, client_secret, mode):
        self.auth = (client_id, client_secret)
        self.base_url = "https://api.paypal.com" if mode == "live" else "https://api-m.sandbox.paypal.com"

    def verify_webhook(self, headers, body):
        webhook_event = body.decode('utf-8')
        webhook_event = json.loads(webhook_event)

        data = {
            "transmission_id": headers['Paypal-Transmission-Id'],
            "transmission_time": headers['Paypal-Transmission-Time'],
            "cert_url": headers['Paypal-Cert-Url'],
            "auth_algo": headers['Paypal-Auth-Algo'],
            "transmission_sig": headers['Paypal-Transmission-Sig'],
            "webhook_id": settings.PAYPAL_WEBHOOK_ID,
            "webhook_event": webhook_event
        }

        response = requests.post(
            self.base_url + "/v1/notifications/verify-webhook-signature",
            auth=self.auth,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data)
        )
        return response.json()

    def create_subscription_billing(self, plan):
        response = requests.post(
            self.base_url + "/v1/billing/subscriptions",
            auth=self.auth,
            headers={"Content-Type": "application/json"},
            data=json.dumps({"plan_id": PLANS[plan]})
        )
        return response.json()


PaypalAPI = PaypalSDK(settings.PAYPAL_CLIENT_ID, settings.PAYPAL_CLIENT_SECRET, settings.PAYPAL_MODE)
