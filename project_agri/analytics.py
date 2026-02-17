# Analytics Module for Agriculture Website

"""
Track and analyze user interactions with the agriculture website.
Provides insights on feature usage, popular crops, and user behavior.
"""

import os
import json
from datetime import datetime
from collections import defaultdict, Counter
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "agriculture_website"
COLLECTION_NAME = "analytics"

# In-memory fallback if DB is not available
_memory_analytics = None

# Global variable for the MongoDB client
_mongo_client = None

def get_mongo_client():
    """Get or initialize the MongoDB client lazily"""
    global _mongo_client
    if _mongo_client is None and MONGO_URI:
        try:
            # Note: dnspython is required for srv URIs
            _mongo_client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        except Exception as e:
            print(f"MongoDB connection setup failed: {e}")
    return _mongo_client

def get_db_collection():
    """Get MongoDB collection or None if not configured/failed"""
    client = get_mongo_client()
    if not client:
        return None
    try:
        db = client[DB_NAME]
        return db[COLLECTION_NAME]
    except Exception as e:
        print(f"MongoDB selection error: {e}")
        return None

# Initialize analytics structure
def init_analytics():
    """Initialize analytics data structure"""
    return {
        "page_views": {},
        "feature_usage": {},
        "crop_searches": {},
        "scheme_views": {},
        "rotation_queries": {},
        "weather_queries": {},
        "fertilizer_calculations": {},
        "total_visits": 0,
        "last_updated": datetime.now().isoformat()
    }

# Load analytics data
def load_analytics():
    """Load analytics data from MongoDB or fallback"""
    global _memory_analytics
    
    collection = get_db_collection()
    
    if collection:
        try:
            data = collection.find_one({"_id": "main_analytics"})
            if data:
                # Convert regular dicts to Counter/defaultdict behavior where needed
                # For read operations, we just return the dict, logic handles the rest
                return data
        except Exception as e:
            print(f"Error loading from MongoDB: {e}")
    
    # Fallback to in-memory if DB fails or empty
    if _memory_analytics is None:
        _memory_analytics = init_analytics()
    return _memory_analytics

# Save analytics data
def save_analytics(analytics):
    """Save analytics data to MongoDB"""
    global _memory_analytics
    
    # Update timestamp
    analytics["last_updated"] = datetime.now().isoformat()
    
    collection = get_db_collection()
    
    if collection:
        try:
            # MongoDB doesn't like Counter/defaultdict types directly, ensure they are dicts
            data_to_save = {
                "page_views": dict(analytics.get("page_views", {})),
                "feature_usage": dict(analytics.get("feature_usage", {})),
                "crop_searches": dict(analytics.get("crop_searches", {})),
                "scheme_views": dict(analytics.get("scheme_views", {})),
                "rotation_queries": dict(analytics.get("rotation_queries", {})),
                "weather_queries": dict(analytics.get("weather_queries", {})),
                "fertilizer_calculations": dict(analytics.get("fertilizer_calculations", {})),
                "total_visits": analytics.get("total_visits", 0),
                "last_updated": analytics["last_updated"]
            }
            
            collection.update_one(
                {"_id": "main_analytics"},
                {"$set": data_to_save},
                upsert=True
            )
            return
        except Exception as e:
            print(f"Error saving to MongoDB: {e}")
    
    # Update in-memory fallback
    _memory_analytics = analytics

# Helper to safely increment a value in a nested dict structure
def _safe_increment(category, key):
    analytics = load_analytics()
    
    # Ensure category exists and is a dict
    if category not in analytics or not isinstance(analytics[category], dict):
        analytics[category] = {}
        
    # Increment
    current_val = analytics[category].get(key, 0)
    analytics[category][key] = current_val + 1
    
    save_analytics(analytics)

# Track page view
def track_page_view(page_name):
    """Track a page view"""
    _safe_increment("page_views", page_name)

# Track unique visit
def track_visit():
    """Track a unique website visit"""
    analytics = load_analytics()
    analytics["total_visits"] = analytics.get("total_visits", 0) + 1
    save_analytics(analytics)

# Track feature usage
def track_feature(feature_name):
    """Track feature usage"""
    _safe_increment("feature_usage", feature_name)

# Track crop search
def track_crop_search(crop_name):
    """Track crop prediction search"""
    _safe_increment("crop_searches", crop_name)

# Track scheme view
def track_scheme_view(scheme_name):
    """Track government scheme view"""
    _safe_increment("scheme_views", scheme_name)

# Track rotation query
def track_rotation_query(crop_name):
    """Track crop rotation query"""
    _safe_increment("rotation_queries", crop_name)

# Track weather query
def track_weather_query(city_name):
    """Track weather query"""
    _safe_increment("weather_queries", city_name)

# Track fertilizer calculation
def track_fertilizer_calc(crop_name):
    """Track fertilizer calculation"""
    _safe_increment("fertilizer_calculations", crop_name)

# Get analytics summary
def get_analytics_summary():
    """Get summary of analytics data"""
    analytics = load_analytics()
    
    # Helper to get Counter-like objects
    def get_counter(key):
        return Counter(analytics.get(key, {}))
    
    # Get top items
    top_crops = get_counter("crop_searches").most_common(5)
    top_schemes = get_counter("scheme_views").most_common(5)
    top_rotations = get_counter("rotation_queries").most_common(5)
    top_weather = get_counter("weather_queries").most_common(5)
    top_fertilizer = get_counter("fertilizer_calculations").most_common(5)
    
    page_views = analytics.get("page_views", {})
    feature_usage = analytics.get("feature_usage", {})
    
    top_pages = sorted(page_views.items(), key=lambda x: x[1], reverse=True)[:5]
    top_features = sorted(feature_usage.items(), key=lambda x: x[1], reverse=True)[:5]
    
    return {
        "total_visits": analytics.get("total_visits", 0),
        "total_page_views": sum(page_views.values()),
        "total_features_used": sum(feature_usage.values()),
        "top_pages": top_pages,
        "top_features": top_features,
        "top_crops": top_crops,
        "top_schemes": top_schemes,
        "top_rotations": top_rotations,
        "top_weather_cities": top_weather,
        "top_fertilizer_crops": top_fertilizer,
        "last_updated": analytics.get("last_updated", datetime.now().isoformat()),
        "db_status": "Connected" if get_db_collection() is not None else "Disconnected (Using Memory)",
        "mongo_uri_configured": bool(MONGO_URI)
    }

# Get detailed analytics
def get_detailed_analytics():
    """Get detailed analytics data"""
    return load_analytics()
