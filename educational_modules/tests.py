from unittest import TestCase

from rest_framework import status, serializers
from rest_framework.test import APITestCase, APIRequestFactory

from educational_modules.models import Lesson, Module
from educational_modules.serializers.lesson import LessonSerializer
from educational_modules.serializers.module import ModuleSerializer
from educational_modules.validiators import validate_module_owner
from users.models import User


# Tests for CRUD operations Module and Lesson models
class LessonTestCase(APITestCase):
    """
    Test case for Lesson API views.

    This test case provides methods to test the creation, retrieval, updating, and deletion of lessons through the API.

    Attributes:
        user: A superuser created for authentication.
    """

    def setUp(self):
        """
        Set up method to create a superuser and authenticate the client.
        """
        self.user = User.objects.create(
            email='test@gmail.com',
            password='test'
        )
        self.user.is_superuser = True
        self.user.save()

        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        """
        Test method to create a lesson through the API.

        This method sends a POST request to the lessons endpoint with valid data and checks if the response status
        code is 201 CREATED.
        """
        data = {
            'title': 'test for create',
            'description': 'test for create',
            'content': 'test for create',
            'video_url': 'https://www.youtube.com/'
        }

        response = self.client.post(
            '/lessons/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'pk': 1,
                'title': 'test for create',
                'description': 'test for create',
                'preview': None,
                'video_url': 'https://www.youtube.com/',
                'content': 'test for create',
                'module': None,
                "owner": 1
            }
        )

    def test_list_lesson(self):
        """
        Test method to retrieve a list of lessons through the API.

        This method sends a GET request to the lessons endpoint and checks if the response status code is 200 OK,
        and if the retrieved lesson matches the expected data.
        """
        lesson = Lesson.objects.create(
            title='list test',
            description='list test',
            content='list test',
            video_url='https://www.youtube.com/'
        )

        response = self.client.get(
            '/lessons/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {'pk': lesson.pk,
                     'title': 'list test',
                     'description': 'list test',
                     'preview': None,
                     'video_url': 'https://www.youtube.com/',
                     'content': 'list test',
                     'module': None,
                     'owner': None
                     }
                ]
            }
        )

    def test_detail_lesson(self):
        """
        Test method to retrieve details of a specific lesson through the API.

        This method sends a GET request to the specific lesson endpoint and checks if the response status code is
        200 OK, and if the retrieved lesson matches the expected data.
        """
        lesson = Lesson.objects.create(
            title='detail test',
            description='detail test',
            content='detail test',
            video_url='https://www.youtube.com/'
        )

        response = self.client.get(f'/lessons/{lesson.pk}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'pk': lesson.pk,
                'title': 'detail test',
                'description': 'detail test',
                'preview': None,
                'video_url': 'https://www.youtube.com/',
                'content': 'detail test',
                'module': None,
                'owner': None
            }
        )

    def test_update_lesson(self):
        """
        Test method to update a lesson through the API.

        This method sends a PUT request to the specific lesson endpoint with updated data and checks if the response
        status code is 200 OK, and if the updated lesson matches the expected data.
        """
        lesson = Lesson.objects.create(
            title='test for update',
            description='test for update',
            content='test for update',
            video_url='https://www.youtube.com/'
        )

        updated_data = {
            'title': 'updated title',
            'description': 'updated description',
            'content': 'updated content',
            'video_url': 'https://www.youtube.com/'
        }

        response = self.client.put(
            f'/lessons/{lesson.pk}/',
            data=updated_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'pk': lesson.pk,
                'title': 'updated title',
                'description': 'updated description',
                'preview': None,
                'video_url': 'https://www.youtube.com/',
                'content': 'updated content',
                'module': None,
                'owner': None
            }
        )

    def test_delete_lesson(self):
        """
        Test method to delete a lesson through the API.

        This method sends a DELETE request to the specific lesson endpoint and checks if the response status code is
        204 NO CONTENT, indicating successful deletion.
        """
        lesson = Lesson.objects.create(
            title='test for delete',
            description='test for delete',
            content='test for delete',
            video_url='https://www.youtube.com/'
        )

        response = self.client.delete(
            f'/lessons/{lesson.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class ModuleTestCase(APITestCase):
    """
    Test case for Module API views.

    This test case provides methods to test the creation, retrieval, updating, and deletion of modules through the API.

    Attributes:
        user: A superuser created for authentication.
    """

    def setUp(self):
        """
        Set up method to create a superuser and authenticate the client.
        """
        self.user = User.objects.create(
            email='test@gmail.com',
            password='test'
        )
        self.user.is_superuser = True
        self.user.save()

        self.client.force_authenticate(user=self.user)

    def test_create_module(self):
        """
        Test method to create a module through the API.

        This method sends a POST request to the module creation endpoint with valid data and checks if the response
        status code is 201 CREATED, and if the created module matches the expected data.
        """

        data = {
            'title': 'test for create module',
            'description': 'test for create module'
        }

        response = self.client.post(
            '/module/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'pk': 1,
                'title': 'test for create module',
                'description': 'test for create module',
                'preview': None,
                'lessons_count': 0,
                'lessons': [],
                "owner": 6
            }
        )

    def test_list_module(self):
        """
        Test method to retrieve a list of modules through the API.

        This method sends a GET request to the modules list endpoint and checks if the response status code is
        200 OK, and if the retrieved module matches the expected data.
        """

        module = Module.objects.create(
            title='list test module',
            description='list test module',
        )

        response = self.client.get(
            '/module/list/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {'pk': module.pk,
                     'title': 'list test module',
                     'description': 'list test module',
                     'preview': None,
                     'lessons_count': 0,
                     'lessons': [],
                     'owner': None
                     }
                ]
            }
        )

    def test_detail_module(self):
        """
        Test method to retrieve details of a specific module through the API.

        This method sends a GET request to the specific module detail endpoint and checks if the response status code
        is 200 OK, and if the retrieved module matches the expected data.
        """

        module = Module.objects.create(
            title='detail test',
            description='detail test'
        )

        response = self.client.get(f'/module/detail/{module.pk}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'pk': module.pk,
                'title': 'detail test',
                'description': 'detail test',
                'preview': None,
                'lessons_count': 0,
                'lessons': [],
                'owner': None
            }
        )

    def test_update_module(self):
        """
        Test method to update a module through the API.

        This method sends a PUT request to the specific module update endpoint with updated data and checks if the
        response status code is 200 OK, and if the updated module matches the expected data.
        """
        module = Module.objects.create(
            title='test for update',
            description='test for update'
        )

        updated_data = {
            'title': 'updated title module',
            'description': 'updated description module'
        }

        response = self.client.put(
            f'/module/update/{module.pk}/',
            data=updated_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'pk': module.pk,
                'title': 'updated title module',
                'description': 'updated description module',
                'preview': None,
                'lessons_count': 0,
                'lessons': [],
                'owner': None
            }
        )

    def test_delete_module(self):
        """
        Test method to delete a module through the API.

        This method sends a DELETE request to the specific module delete endpoint and checks if the response status
        code is 204 NO CONTENT, indicating successful deletion.
        """
        module = Module.objects.create(
            title='test for module delete',
            description='test for module delete'
        )

        response = self.client.delete(
            f'/module/delete/{module.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


# Tests for serializers Lesson and Module models
class LessonSerializerTest(TestCase):
    """
    Test case for LessonSerializer.

    This test case provides methods to test the LessonSerializer.

    Attributes:
        user: A user created for testing.
        module: A module created for testing.
    """

    def setUp(self):
        """
        Set up method to create a user and a module for testing.
        """
        self.user = User.objects.create(email='test1_for_serializator@gmail.com')
        self.module = Module.objects.create(title='Test Module', description='test description', owner=self.user)

    def test_lesson_serializer(self):
        """
        Test method for LessonSerializer.

        This method creates a fake request using APIRequestFactory, creates lesson data, and tests the LessonSerializer
        by checking if the serializer is valid and if the lesson is saved correctly with the associated module.
        """

        request_factory = APIRequestFactory()
        request = request_factory.get('/fake-path/')  # Creating a fake request
        request.user = self.user

        lesson_data = {
            'title': 'Test Lesson',
            'description': 'Test description',
            'preview': None,
            'video_url': 'https://www.youtube.com/',
            'content': 'Test content',
            'module': self.module.pk,
            'owner': self.user.pk
        }
        serializer = LessonSerializer(data=lesson_data, context={'request': request})
        self.assertTrue(serializer.is_valid())
        lesson = serializer.save()
        self.assertEqual(lesson.module, self.module)


class ModuleSerializerTest(TestCase):
    """
    Test case for ModuleSerializer.

    This test case provides methods to test the ModuleSerializer.

    Attributes:
        user: A user created for testing.
        module: A module created for testing.
        lesson: A lesson created for testing.
    """

    def setUp(self):
        """
        Set up method to create a user, a module, and a lesson for testing.
        """
        self.user = User.objects.create(email='test_user@example.com')
        self.module = Module.objects.create(title='Test Module', description='Test description', owner=self.user)
        self.lesson = Lesson.objects.create(title='Test Lesson', description='Lesson description', owner=self.user,
                                            module=self.module)

    def test_module_serializer(self):
        """
        Test method for ModuleSerializer.

        This method tests if the ModuleSerializer properly serializes a module with its associated lessons.
        """

        serializer = ModuleSerializer(instance=self.module)
        serialized_data = serializer.data

        self.assertEqual(serialized_data['pk'], self.module.pk)
        self.assertEqual(serialized_data['title'], self.module.title)
        self.assertEqual(serialized_data['description'], self.module.description)
        self.assertEqual(serialized_data['owner'], self.user.pk)

        # Check if lessons_count is correctly calculated
        self.assertEqual(serialized_data['lessons_count'], 1)

        # Check if lessons are correctly serialized
        self.assertTrue('lessons' in serialized_data)
        self.assertEqual(len(serialized_data['lessons']), 1)
        lesson_data = serialized_data['lessons'][0]
        self.assertEqual(lesson_data['title'], self.lesson.title)
        self.assertEqual(lesson_data['description'], self.lesson.description)
        self.assertEqual(lesson_data['owner'], self.user.pk)
        self.assertEqual(lesson_data['module'], self.module.pk)


# Tests for Validator
class ValidatorTestCase(APITestCase):
    """
    Test case for the validate_module_owner function.

    This test case checks the behavior of the validate_module_owner function.

    Attributes:
        user: A user created for testing.
    """

    def setUp(self):
        """
        Set up method to create a user and authenticate the client.
        """
        self.user = User.objects.create(
            email='testnewforvalidator@gmail.com',
            password='test'
        )
        self.user.is_superuser = True
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_validate_module_owner(self):
        """
        Test method for validate_module_owner.

        This method tests the validation of module ownership.
        """
        user = self.user

        # Test validating module ownership with the same user
        module = Module.objects.create(title='Test Module', owner=user)
        validated_module = validate_module_owner(module, user)
        self.assertEqual(validated_module, module)

        # Test validating module ownership with another user
        another_user = User.objects.create(email='another_user@example.com', password='123456')
        with self.assertRaises(serializers.ValidationError):
            validate_module_owner(module, another_user)

        # Test validating a non-existent module
        with self.assertRaises(serializers.ValidationError):
            validate_module_owner('not_a_module', user)

        # Test validating a module without an owner
        module_without_owner = Module.objects.create(title='Module without owner')
        with self.assertRaises(serializers.ValidationError):
            validate_module_owner(module_without_owner, user)
