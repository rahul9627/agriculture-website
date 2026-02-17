# Analytics Module for Agriculture Website

"""
Track and analyze user interactions with the agriculture website.
Provides insights on feature usage, popular crops, and user behavior.
"""

import json
import os
from datetime import datetime
from collections import defaultdict, Counter

# Analytics data file
ANALYTICS_FILE = "analytics_data.json"

# Initialize analytics structure
def init_analytics():
    """Initialize analytics data structure"""
    return {
        "page_views": defaultdict(int),
        "feature_usage": defaultdict(int),
        "crop_searches": Counter(),
        "scheme_views": Counter(),
        "rotation_queries": Counter(),
        "weather_queries": Counter(),
        "fertilizer_calculations": Counter(),
        "total_visits": 0,
        "last_updated": datetime.now().isoformat()
    }

# Load analytics data
def load_analytics():
    """Load analytics data from file"""
    if os.path.exists(ANALYTICS_FILE):
        try:
            with open(ANALYTICS_FILE, 'r') as f:
                data = json.load(f)
                # Convert to defaultdict and Counter
                analytics = {
                    "page_views": defaultdict(int, data.get("page_views", {})),
                    "feature_usage": defaultdict(int, data.get("feature_usage", {})),
                    "crop_searches": Counter(data.get("crop_searches", {})),
                    "scheme_views": Counter(data.get("scheme_views", {})),
                    "rotation_queries": Counter(data.get("rotation_queries", {})),
                    "weather_queries": Counter(data.get("weather_queries", {})),
                    "fertilizer_calculations": Counter(data.get("fertilizer_calculations", {})),
                    "total_visits": data.get("total_visits", 0),
                    "last_updated": data.get("last_updated", datetime.now().isoformat())
                }
                return analytics
        except Exception as e:
            print(f"Error loading analytics: {e}")
            return init_analytics()
    return init_analytics()

# Save analytics data
def save_analytics(analytics):
    """Save analytics data to file"""
    try:
        # Convert defaultdict and Counter to regular dict for JSON serialization
        data = {
            "page_views": dict(analytics["page_views"]),
            "feature_usage": dict(analytics["feature_usage"]),
            "crop_searches": dict(analytics["crop_searches"]),
            "scheme_views": dict(analytics["scheme_views"]),
            "rotation_queries": dict(analytics["rotation_queries"]),
            "weather_queries": dict(analytics["weather_queries"]),
            "fertilizer_calculations": dict(analytics["fertilizer_calculations"]),
            "total_visits": analytics["total_visits"],
            "last_updated": datetime.now().isoformat()
        }
        with open(ANALYTICS_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error saving analytics: {e}")

# Track page view
def track_page_view(page_name):
    """Track a page view"""
    analytics = load_analytics()
    analytics["page_views"][page_name] += 1
    save_analytics(analytics)

# Track unique visit
def track_visit():
    """Track a unique website visit"""
    analytics = load_analytics()
    analytics["total_visits"] += 1
    save_analytics(analytics)

# Track feature usage
def track_feature(feature_name):
    """Track feature usage"""
    analytics = load_analytics()
    analytics["feature_usage"][feature_name] += 1
    save_analytics(analytics)

# Track crop search
def track_crop_search(crop_name):
    """Track crop prediction search"""
    analytics = load_analytics()
    analytics["crop_searches"][crop_name] += 1
    save_analytics(analytics)

# Track scheme view
def track_scheme_view(scheme_name):
    """Track government scheme view"""
    analytics = load_analytics()
    analytics["scheme_views"][scheme_name] += 1
    save_analytics(analytics)

# Track rotation query
def track_rotation_query(crop_name):
    """Track crop rotation query"""
    analytics = load_analytics()
    analytics["rotation_queries"][crop_name] += 1
    save_analytics(analytics)

# Track weather query
def track_weather_query(city_name):
    """Track weather query"""
    analytics = load_analytics()
    analytics["weather_queries"][city_name] += 1
    save_analytics(analytics)

# Track fertilizer calculation
def track_fertilizer_calc(crop_name):
    """Track fertilizer calculation"""
    analytics = load_analytics()
    analytics["fertilizer_calculations"][crop_name] += 1
    save_analytics(analytics)

# Get analytics summary
def get_analytics_summary():
    """Get summary of analytics data"""
    analytics = load_analytics()
    
    # Get top items
    top_crops = analytics["crop_searches"].most_common(5)
    top_schemes = analytics["scheme_views"].most_common(5)
    top_rotations = analytics["rotation_queries"].most_common(5)
    top_weather = analytics["weather_queries"].most_common(5)
    top_fertilizer = analytics["fertilizer_calculations"].most_common(5)
    top_pages = sorted(analytics["page_views"].items(), key=lambda x: x[1], reverse=True)[:5]
    top_features = sorted(analytics["feature_usage"].items(), key=lambda x: x[1], reverse=True)[:5]
    
    return {
        "total_visits": analytics["total_visits"],
        "total_page_views": sum(analytics["page_views"].values()),
        "total_features_used": sum(analytics["feature_usage"].values()),
        "top_pages": top_pages,
        "top_features": top_features,
        "top_crops": top_crops,
        "top_schemes": top_schemes,
        "top_rotations": top_rotations,
        "top_weather_cities": top_weather,
        "top_fertilizer_crops": top_fertilizer,
        "last_updated": analytics["last_updated"]
    }

# Get detailed analytics
def get_detailed_analytics():
    """Get detailed analytics data"""
    analytics = load_analytics()
    return {
        "page_views": dict(analytics["page_views"]),
        "feature_usage": dict(analytics["feature_usage"]),
        "crop_searches": dict(analytics["crop_searches"]),
        "scheme_views": dict(analytics["scheme_views"]),
        "rotation_queries": dict(analytics["rotation_queries"]),
        "weather_queries": dict(analytics["weather_queries"]),
        "fertilizer_calculations": dict(analytics["fertilizer_calculations"]),
        "total_visits": analytics["total_visits"],
        "last_updated": analytics["last_updated"]
    }
