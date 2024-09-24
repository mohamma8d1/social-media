from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerializer , CommentSerializer ,LikeSerializer
from .models import Post ,Comment ,Like


class PostView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request , post_pk):
        try:
            post = Post.objects.get(pk=post_pk , user=request.user)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer_data = PostSerializer(post).data
        return Response(serializer_data)


    def post(self , request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostListView(APIView):
    def get(self,request):
        posts = Post.objects.filter(is_active=True)
        serializer_data = PostSerializer(posts,many=True).data
        return Response(serializer_data)

class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def _get_post(self,post_pk):
        try:
            return Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return False

    def get(self,request,post_pk):
        post = self._get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)

        comments = post.comments.filter(is_approved=True)
        serializer = CommentSerializer(comments).data
        return Response(serializer)

    def post(self, request , post_pk):
        post = self._get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)


        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post,user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def _get_post(self,post_pk):
        try:
            return Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return False

    def get(self,request,post_pk):
        post = self._get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)

        likes = post.likes.filter(is_liked=True).count()
        return Response({"likes" : likes})

    def post(self, request , post_pk):
        post = self._get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)


        serializer = LikeSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post,user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)