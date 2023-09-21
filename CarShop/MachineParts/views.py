import json
from functools import reduce
import json
from django.db.models import Q
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import MachinePartsSerializer
from .serializers import MachineParts

# Create your views here.
and_and = lambda a, b: a & b


class MachinePartListView(ListAPIView):
    serializer_class = MachinePartsSerializer

    def get_queryset(self):
        if self.request.query_params.get('exact'):
            query_params_contains = self.request.query_params.get('filter')
            query_params_exact = json.loads(self.request.query_params.get('exact'))
            exact_filter = [Q(the_key=the_value) for the_key, the_value in query_params_exact.items()]
            queryset = MachineParts.objects.all(reduce(and_and, exact_filter))
            return queryset
        return MachineParts.objects.all()
