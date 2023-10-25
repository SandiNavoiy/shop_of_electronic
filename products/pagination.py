from rest_framework.pagination import PageNumberPagination


class ProductPaginator(PageNumberPagination):
    """Класс описания пагинации , разбивает данные
     на страницы на основе номера страницы.
    Клиент может указать номер страницы в запросе
    для получения нужной страницы данных"""

    page_size = 20  # количество элементов на с