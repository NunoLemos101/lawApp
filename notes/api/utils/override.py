from rest_framework.response import Response


class ResponseThen(Response):
    """
    Overrides the Response class
    takes in two extra arguments (callback function & callback arguments)
    calls that function after the connection is closed
    therefore giving the User a faster response
    """

    def __init__(self, data, then_callback, then_callback_arguments={}, **kwargs):
        super().__init__(data, **kwargs)
        self.then_callback = then_callback
        self.then_callback_arguments = then_callback_arguments

    def close(self):
        super().close()
        self.then_callback(self.then_callback_arguments)
