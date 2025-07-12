import logging
from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property


logger = logging.getLogger(__name__)


def get_all_properties():
    properties = cache.get('all_properties')
    if properties is None:
        properties = list(Property.objects.all().values(
            'id', 'title', 'description', 'price', 'location', 'created_at'
        ))
        cache.set('all_properties', properties, timeout=3600)  # 1 hour
    return properties


def get_redis_cache_metrics():
    conn = get_redis_connection("default")
    info = conn.info()

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total = hits + misses
    hit_ratio = (hits / total) if total > 0 else 0

    metrics = {
        "keyspace_hits": hits,
        "keyspace_misses": misses,
        "hit_ratio": round(hit_ratio, 4)
    }

    logger.info(f"Redis Cache Metrics: {metrics}")
    return metrics
