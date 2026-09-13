from abc import ABC, abstractmethod


class RateLimiter(ABC):
    def __init__(self, config: RateLimiterConfig, type: RateLimiterType):
        super().__init__()
        self.config = config
        self.type = type
    
    @abstractmethod
    def allow_request(self, user_id: str):
        pass
        