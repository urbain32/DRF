from rest_framework import generics
from blog.models import Post
from .seriliazers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all() # e return all post data that are published only.
    serializer_class = PostSerializer
    pass

class PostDetail(generics.RetrieveDestroyAPIView):
    pass