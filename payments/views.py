from importlib import metadata
from locale import currency
import stripe
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from django.conf import settings
from .models import Payment
from .serializers import PaymentSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request,*args, **kwargs):
        data = request.data
        course_id = data.get('course_id')
        amount = data.get('amount')

        payment_intent = stripe.PaymentIntent.create(
            amount=int(amount * 100),
            currency='usd',
            metadata={'course_id': course_id, 'user_id': request.user.id}
        )

        payment = Payment.objects.create(
            user=request.user,
            course_id=course_id,
            amount=amount,
            stripe_payment_intent = payment_intent['id'],
            paid=False
        )

        return Response({
            'client_secret': payment_intent['client_secret']
        })
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        stripe.PaymentIntent.confirm(instance.strip_payment_intent)
        instance.paid = True
        instance.save()
        return Response({'status': 'Payment Confirm'})