# ALX Backend Caching - Property Listings (Django + Redis)
This project demonstrates how to build a simple Django application that caches property listing data using Redis. It includes Redis-based view caching, queryset-level caching, automatic cache invalidation via signals, and cache hit/miss metrics.

### 🚀 Project Objectives
Initialize Django with PostgreSQL and Redis (via Docker)

Cache property listing view with @cache_page

Use Django's low-level cache API to cache queryset

Invalidate Redis cache via Django signals

Retrieve and log Redis cache hit/miss metrics

0.  1️⃣ Project Setup: PostgreSQL + Redis + Django
Django Project Name: alx-backend-caching_property_listings

App Name: properties

Tools Used:
PostgreSQL (via Docker)

Redis (via Docker or locally installed)

Django 5.x

django-redis for Redis cache backend
```bash
python -m venv venv
venv/Scripts/activate
# inside the virtual environment run
pip install -r requirements.txt
django-admin startproject alx_backend_caching_property_listings
python manage.py startapp properties
python manage.py makemigrations
python manage.py migrate
```
1. 2️⃣ Caching Property List View with @cache_page
- Task:
Cache the view response for 15 minutes using @cache_page
- Purpose:
Reduce repeated database hits for the property list endpoint by caching entire view output.
2. 3️⃣ Caching Queryset Using Django Low-Level Cache API
- Task:
Use Redis to cache the queryset for 1 hour.
- Purpose:
Reduce queryset processing and DB I/O by storing results in Redis under a specific cache key.
3. 4️⃣ Invalidate Cache on Property Create/Update/Delete
- Task:
Use Django signals to delete the Redis cache whenever the Property model is modified.
- Purpose:
Ensure the cache never returns outdated property data when changes occur.
4. 5️⃣ Redis Cache Metrics: Hits, Misses, Hit Ratio
- Task:
Retrieve Redis cache statistics using django_redis to monitor cache effectiveness.

- Details:

Fetch keyspace_hits and keyspace_misses from Redis INFO command.
Calculate the cache hit ratio: hits / (hits + misses)
Log these metrics for analysis.

- Why It Works:
✅ Uses if total_requests > 0 else 0 to prevent divide-by-zero errors.
✅ Uses logger.error to handle and report Redis connection issues.