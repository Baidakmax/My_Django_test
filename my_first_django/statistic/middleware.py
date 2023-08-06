from .models import UserStat


class SaveHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Save the request headers to the database, a file, or any other storage of your choice.
        request_headers = request.headers
        # Now, you can save the headers as you see fit, for example, using a model or writing to a file.
        UserStat.objects.create(headers= request_headers)
        # Call the next middleware or the view.
        response = self.get_response(request)
        return response