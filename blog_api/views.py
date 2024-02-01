from rest_framework import generics
from blog.models import Post
from .seriliazers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all() # e return all post data that are published only.
    serializer_class = PostSerializer

# generics to retrieve and delete api view
class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all() # e return all post data.
    serializer_class = PostSerializer