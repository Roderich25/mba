from rest_framework.views import APIView
from rest_framework.response import Response
from core.serializers import PostSerializer
from core.models import Post


class TestView(APIView):

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *rgs, **kargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
