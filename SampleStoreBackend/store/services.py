from store.models import Sample, Relation, BuyingSample
from rest_framework.response import Response

from store.serializers import BuyingSampleSerializer


def dec_scrore(request):
    user = request.user
    sample = Sample.objects.get(pk=request.data['sample_id'])

    if user.score < sample.price:
        return Response({'mes': 'not money'})

    user.score = user.score - sample.price
    print(user)
    user.save()
    return Response({'mes': 'all OK'})


def is_purchased(request):
    obj, _ = BuyingSample.objects.get_or_create(
            user=request.user,
            sample_id=request.data['sample_id'],
        )

    return obj
