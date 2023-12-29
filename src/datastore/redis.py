import redis.asyncio as redis

from src.core.config import settings


class RedisConnector:
    """Load Redis settings and build valid URI"""

    async def initialize_cache(self) -> None:
        """start redis client with Beanie and load models"""

        redis_dsn = settings.redis_dsn.unicode_string()
        redis_socket_timeout = settings.redis_socket_timeout

        try:
            client = redis.Redis.from_url(redis_dsn, decode_responses=True, socket_timeout=redis_socket_timeout)
            print(f"Connected to redis")
            return client
        except Exception:
            raise ConnectionError


cache = RedisConnector()