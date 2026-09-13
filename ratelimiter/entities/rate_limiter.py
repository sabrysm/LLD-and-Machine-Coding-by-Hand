from abc import ABC, abstractmethod

from ratelimiter.entities.rate_limiter_config import RateLimiterConfig
from ratelimiter.entities.rate_limiter_type import RateLimiterType


class RateLimiter(ABC):
    def __init__(self, config: RateLimiterConfig, type: RateLimiterType):
        super().__init__()
        self.config = config
        self.type = type
    
    @abstractmethod
    def allow_request(self, user_id: str):
        pass
        