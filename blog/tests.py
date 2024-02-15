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
    # function to create our test and run them
    def test_blog_content(self):
        post= Post.postobjects.get(id=1)
        cat= Category.objects.get(id=1) 
        author =f'{post.author}'  
        excerpt =f'{post.excerpt}'  
        title =f'{post.title}'  
        content =f'{post.content}'  
        status =f'{post.status}'  
        self.assertEqual(author,'test_user1') # this command allow autor to be equal to test_user1
