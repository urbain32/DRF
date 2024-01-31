# serializer helps to conveeert data from our data into json  or xml data so that it can be easy to read
from rest_framework import serializers 
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        # from our model which field we want to work with
        field=("id","title","author","excerpt","content","status")
