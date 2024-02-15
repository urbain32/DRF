from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post,Category

# Create your tests here.
class Test_Create_Post(TestCase):
    @classmethod
    # function to create data  to test
    def setUpTestData(cls):
        test_category= Category.objects.create(name="django")
        tetsuser1 = User.objects.create_user(username="test_user1",password="123456")
        test_post = Post.objects.create(category_id=1,title="Post title",excerpt="Post excerpt",content="Post content",slug="post-title",author_id=1,status="published",)
            
