class RateLimiterConfig:
    def __init__(self, max_requests: int, window_in_seconds: int):
        self._max_requests = max_requests
        self._window_in_seconds = window_in_seconds
    
    @property
    def max_requests(self):
        return self._max_requests
    
    @property.setter
    def max_requests(self, value):
        if not isinstance(value, int):
            raise TypeError("max_requests must be Integer")
        self._max_requests = value
    
    @property
    def window_in_seconds(self):
        return self._window_in_seconds
    
    @property.setter
    def window_in_seconds(self, value):
        if not isinstance(value, int):
            raise TypeError("window_in_seconds must be Integer")
        self._window_in_seconds = value