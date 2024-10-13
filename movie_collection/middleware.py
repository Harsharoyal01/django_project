from django.utils.deprecation import MiddlewareMixin

class RequestCounterMiddleware(MiddlewareMixin):
    request_count = 0  # Class variable to keep track of request count

    def process_request(self, request):
        # Incrementing the request count
        RequestCounterMiddleware.request_count += 1  # Accessing the variable via the class name

    @classmethod
    def get_request_count(cls):
        return cls.request_count  # Accessing the class variable through the class
