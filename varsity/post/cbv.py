from rest_framework.views import APIView
from rest_framework.response import Response
from post.models import Company, Post
from post.serializers import CompanySerializer, PostSerializer


class ListCreateCompanyAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = CompanySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class CompanyAPIView(APIView):
    def get_company(self, pk):
        try:
            company = Company.objects.get(id=pk)
            return company
        except Company.DoesNotExist:
            return None

    def get(self, request, pk):
        company = self.get_company(pk)
        if company is not None:
            serializer = CompanySerializer(company)
            return Response(serializer.data, status=200)
        else:
            return Response({'message': 'Not found'}, status=404)

    def put(self, request, pk):
        company = self.get_company(pk)
        if company is not None:
            data = request.data
            serializer = CompanySerializer(data=data, instance=company)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response({'message': 'Not found'}, status=404)

    def delete(self, request, pk):
        company = self.get_company(pk)
        if company is not None:
            company.delete()
            return Response({'message': 'Success!'}, status=200)
        else:
            return Response({'message': 'Not found'}, status=404)
        

class ListCreatePostAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = PostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class PostAPIView(APIView):
    def get_post(self, pk):
        try:
            post =Post.objects.get(id=pk)
            return post
        except Post.DoesNotExist:
            return None

    def get(self, request, pk):
        post = self.get_post(pk)
        if post is not None:
            serializer = PostSerializer(post)
            return Response(serializer.data, status=200)
        else:
            return Response({'message': 'Not found'}, status=404)

    def put(self, request, pk):
        post = self.get_post(pk)
        if post is not None:
            data = request.data
            serializer = PostSerializer(data=data, instance=post)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response({'message': 'Not found'}, status=404)

    def delete(self, request, pk):
        post = self.get_post(pk)
        if post is not None:
            post.delete()
            return Response({'message': 'Success!'}, status=200)
        else:
            return Response({'message': 'Not found'}, status=404)