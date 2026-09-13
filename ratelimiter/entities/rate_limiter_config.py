class RateLimiterConfig:
    def __init__(self, max_requests: int, window_in_seconds: int):
        self._max_requests = max_requests
        self._window_in_seconds = window_in_seconds
    
    @property
    def max_requests(self):
        return self._max_requests
    
    @property
    def window_in_seconds(self):
        return self._window_in_seconds