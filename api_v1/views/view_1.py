# for using rest_framework_api
from rest_framework.views import APIView
from api_v1.models import TestDataset
from django.http import JsonResponse

# Create your views here.
class viewV1(APIView):

    # def get request
    def get(self, requests):
        testInfo = TestDataset.objects.all()
        response = {"results": list(testInfo.values("id", "name"))}
        return JsonResponse(response)

    # define post request
    def post(self, requests):
        print requests.data
        for element in requests.data:
            print element
            TestDataset.objects.create(**element)
        return JsonResponse({"results": "Json Object Saved"})



