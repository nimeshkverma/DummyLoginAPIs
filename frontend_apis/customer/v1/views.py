from rest_framework.views import APIView
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from customer import models
import serializers


class MetaDataResponse(Response):
    meta_data_dict = {
        "meta": "",
        "data": {}
    }

    def __init__(self, *args, **kwargs):
        if args:
            MetaDataResponse.meta_data_dict["data"] = args[0]
            if len(args) >= 2:
                MetaDataResponse.meta_data_dict["meta"] = args[1]
            modified_args = tuple([MetaDataResponse.meta_data_dict])
        super(MetaDataResponse, self).__init__(*modified_args, **kwargs)


class Config(APIView):

    @csrf_exempt
    def post(self, request):
        data = {
            'username': 'NimeshVerma',
            'bio': 'The Startup Guy',
            'email': 'nimesh.aug11@gmail.com',
            'pic': '',
        }
        return MetaDataResponse(data, status=status.HTTP_200_OK)


class DataLogList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = models.DataLog.objects.all()
    serializer_class = serializers.DataLogSerializer

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DataLogDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = models.DataLog.objects.all()
    serializer_class = serializers.DataLogSerializer

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @csrf_exempt
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
