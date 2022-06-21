from rest_framework.views import APIView
from rest_framework.response import Response


class FirstView(APIView):
    def get(self, request):
        return Response('Method GET')

    def post(self, request):
        return Response('Method POST')

    def put(self, request):
        return Response('Method PUT')

    def patch(self, request):
        return Response('Method PATCH')

    def delete(self, request):
        return Response('Method DELETE')


class SecondView(APIView):
    def get(self, *args, **kwargs):
        print(args)
        query_params = self.request.query_params.dict()
        print(query_params)
        return Response(query_params)

    def post(self, *args, **kwargs):
        data = self.request.data
        print(data)
        return Response(data)


class ThirdView(APIView):
    def get(self, *args, **kwargs):
        print(kwargs)
        return Response(kwargs)


users = [
    {'id': 1, 'name': 'max', 'age': 15},
    {'id': 2, 'name': 'kira', 'age': 20},
    {'id': 3, 'name': 'anton', 'age': 35},
    {'id': 4, 'name': 'oleh', 'age': 21},
]


class UsersView(APIView):
    def get(self, *args, **kwargs):
        return Response(users)


class UserRetrieveView(APIView):
    def get(self, *args, **kwargs):
        id_user = kwargs.get('id')
        return Response(users[id_user - 1])
