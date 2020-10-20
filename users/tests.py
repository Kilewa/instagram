from django.test import TestCase
from .models import Profile
import datetime as dt
from django.contrib.auth.models import User
# Create your tests here.


class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Creating a new profile and saving it
        self.new_user = User(
            username='Kilewa', email='kilewageorge230@gmail.com', password='kayolee1')
        self.new_user.save()

        self.new_profile = Profile.get_profile_by_user_id(self.new_user.id)
    # Tear Down method

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    # Testing Save Method
    def test_save_method(self):
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    # Testing get_profile_by_user_id Method

    def test_get_profile_by_user_id(self):
        profile = Profile.get_profile_by_user_id(self.new_user.id)
        self.assertEqual(profile.id, self.new_profile.id)
