from rest_framework.pagination import PageNumberPagination


class ModulePaginator(PageNumberPagination):
    """
    Paginator for Module objects.

    Attributes:
        page_size (int): The default page size for paginated results.
        page_size_query_param (str): The query parameter to control the page size.
        max_page_size (int): The maximum page size allowed.
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20


class LessonPaginator(PageNumberPagination):
    """
    Paginator for Lesson objects.

    Attributes:
        page_size (int): The default page size for paginated results.
        page_size_query_param (str): The query parameter to control the page size.
        max_page_size (int): The maximum page size allowed.
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20
