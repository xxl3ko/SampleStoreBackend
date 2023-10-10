from store.models import Sample
from rest_framework.response import Response

from store.serializers import BuyingSampleSerializer


def dec_scrore(request):
    user = request.user
    sample = Sample.objects.get(pk=request.data['sample_id'])

    if user.score < sample.price:
        return Response({'mes': 'not money'})

    user.score = user.score - sample.price
    user.save()
    return Response({'mes': 'all OK'})


def is_purchased(request):
    serializer = BuyingSampleSerializer(data=)
    pass