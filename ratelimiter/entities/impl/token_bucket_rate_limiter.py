from datetime import datetime

from ratelimiter.entities.rate_limiter import RateLimiter
from ratelimiter.entities.rate_limiter_config import RateLimiterConfig
from ratelimiter.entities.rate_limiter_type import RateLimiterType


class TokenBucketRateLimiter(RateLimiter):
    def __init__(self, config: RateLimiterConfig):
        super().__init__(config)
        self.config: RateLimiterConfig = config
        self.type = RateLimiterType.TOKEN_BUCKET
        self.tokens = {} # user_id, int
        self.last_refill_at = {} # user_id, datetime
    
    def allow_request(self, user_id):        
        current_tokens = self.refill_tokens(user_id)
        
        if current_tokens > 0:
            self.tokens[user_id] -= 1
            return True
        
        return False
    
    def refill_tokens(self, user_id: str):
        now = datetime.now()
        last_refill_at: datetime = self.last_refill_at[user_id]
        elapsed_time: float = (now - last_refill_at).total_seconds()
        refill_rate = self.config[user_id].window_in_seconds // self.config[user_id].max_requests
        
        tokens_refilled = elapsed_time // refill_rate
        current_tokens = min(self.config[user_id].max_requests, tokens_refilled)
        
        if current_tokens > 0:
            self.last_refill_at[user_id] = now
        return current_tokens