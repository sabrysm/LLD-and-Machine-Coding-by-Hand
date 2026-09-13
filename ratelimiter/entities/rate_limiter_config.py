class RateLimiterConfig:
    def __init__(self, max_requests: int, window_in_seconds: int):
        self.max_requests = max_requests
        self.window_in_seconds = window_in_seconds