import datetime
from unittest.mock import patch

from django.core import mail
from django.test import TestCase
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, APIRequestFactory

from users.models import User
from users.permissions import IsOwner
from users.serializers.user import UserSerializer
from users.services import sending_notice
from users.tasks import notice_for_users


# Tests for CRUD operations User model
class UserTestCase(APITestCase):
    """
    Test case for the User API endpoints.

    Attributes:
        user: A superuser created for testing.
    """

    def setUp(self):
        """
        Set up method to create a superuser and authenticate the client.
        """

        self.user = User.objects.create(
            email='pavelakulich1999@gmail.com',
            password='password123',
        )

        self.user.is_superuser = True
        self.user.save()

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        """
        Test method for creating a user.
        """
        data = {
            "email": "test_user@gmail.com",
            "password": "password123456789"
        }
        response = self.client.post(
            '/users/users/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_user_list(self):
        """
        Test method for listing users.
        """
        response = self.client.get(
            '/users/users/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [
                {
                    "pk": self.user.pk,
                    "email": self.user.email,
                    "first_name": self.user.first_name,
                    "last_name": self.user.last_name,
                    "phone": None,
                    "country": None,
                    "avatar": None
                }
            ]
        )

    def test_user_update(self):
        """
        Test method for updating user details.
        """
        updated_data = {
            "email": self.user.email,
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "phone": "+123456789",
            "country": "test_country"
        }

        response = self.client.put(
            f'/users/users/{self.user.pk}/',
            data=updated_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_delete(self):
        """
        Test method for deleting a user.
        """
        response = self.client.delete(
            f'/users/users/{self.user.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


# Tests for User Serializer
class UserSerializerTestCase(TestCase):
    """
    Test case for the UserSerializer class.
    """

    def setUp(self):
        """
        Set up method to define valid user data.
        """
        self.valid_data = {
            'email': 'testserializeruser1@example.com',
            'first_name': 'test_name',
            'last_name': 'test_last_name',
            'phone': '+123456789',
            'country': 'testCountry',
            'avatar': None,
        }

    def test_user_serializer_save(self):
        """
        Test method to ensure that UserSerializer properly saves a user with valid data.
        """
        serializer = UserSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.email, self.valid_data['email'])
        self.assertEqual(user.first_name, self.valid_data['first_name'])
        self.assertEqual(user.last_name, self.valid_data['last_name'])
        self.assertEqual(user.phone, self.valid_data['phone'])
        self.assertEqual(user.country, self.valid_data['country'])
        self.assertEqual(user.avatar, self.valid_data['avatar'])


# Tests for User Permissions
class IsOwnerTestCase(TestCase):
    """
    Test case for the IsOwner permission class.
    """

    def setUp(self):
        """
        Set up method to create a superuser and authenticate the client.
        """
        self.user = User.objects.create(
            email='pavelakulichtest@gmail.com',
            password='password123newtest',
        )

        self.user.is_superuser = True
        self.user.save()

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_has_object_permission(self):
        """
        Test method to check if the IsOwner permission allows access to the object owner.
        """
        user = self.user
        obj = user

        request = APIRequestFactory().get('/')
        request.user = user
        permission = IsOwner()

        self.assertTrue(permission.has_object_permission(request, None, obj))


# Tests for Sending Notice and Notice Task
class SendingNoticeTestCase(TestCase):
    """
    Test case for sending notice email.
    """

    def test_sending_notice(self):
        """
        Test sending notice email.
        """
        email = 'test_for_mail@example.com'
        username = 'test_user_mail'
        sending_notice(email, username)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Educational Modules')
        self.assertEqual(mail.outbox[0].to, [email])
        self.assertIn(username, mail.outbox[0].body)


class NoticeForUsersTestCase(TestCase):
    """
    Test case for the notice_for_users celery task.
    """

    def setUp(self):
        """
        Set up method to create users and set last login for one user.
        """
        self.user1 = User.objects.create(email='test1@example.com', first_name='User1')
        self.user2 = User.objects.create(email='test2@example.com', first_name='User2')
        self.user3 = User.objects.create(email='test3@example.com', first_name='User3')
        # Setting the last login to user1 20 days ago
        self.user1.last_login = timezone.now() - datetime.timedelta(days=20)
        self.user1.save()

    @patch('users.tasks.sending_notice')
    def test_notice_for_users(self, mock_sending_notice):
        """
        Test the celery task notice_for_users.
        """
        notice_for_users()
        self.assertEqual(mock_sending_notice.call_count, 1)
        mock_sending_notice.assert_called_once_with(self.user1.email, self.user1.first_name)
