from enum import Enum


class RateLimiterType(Enum):
    FIXED_WINDOW = 1
    TOKEN_BUCKET = 2
    SLIDING_WINDOW_LOGS = 3
    SLIDING_WINDOW_COUNTER = 4