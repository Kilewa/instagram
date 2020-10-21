from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from users.models import Profile
# Create your tests here.
class PostTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Creating a new post and saving it
        self.new_user=User(username='Kilewa',email='kilewageorge230@gmail.com',password='kayolee1')
        self.new_user.save()
        self.new_profile=Profile.get_profile_by_user_id(self.new_user.id)


    # Tear Down method
    def tearDown(self):
        Post.objects.all().delete()
        Profile.objects.all().delete()
        Post.objects.all().delete()      

    # Testing Save Method
    def test_save_method(self):
        posts= Post.objects.all()
        self.assertTrue(len(post) < 0)  

    # Testing get all images Method
    def test_get_all_images_method(self):
        posts = Post.get_all_images()
        self.assertTrue(len(posts) < 0) 


    # Testing delete method
    def test_delete_post(self):
        Post.delete_post(self.new_post.id)
        posts = Post.get_all_images()
        self.assertTrue(len(posts) == 0)
