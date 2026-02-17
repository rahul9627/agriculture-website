"""
Weather Service Module
Integrates with OpenWeatherMap API to provide weather data and forecasts
"""

import requests
from datetime import datetime

# OpenWeatherMap API Configuration
API_KEY = "57c86e3f6a6c18f288591911080466f6"  # Get your free API key from https://openweathermap.org/api
BASE_URL = "http://api.openweathermap.org/data/2.5"

def get_current_weather(city=None, lat=None, lon=None):
    """
    Get current weather for a city or coordinates
    
    Args:
        city (str): City name (optional)
        lat (float): Latitude (optional)
        lon (float): Longitude (optional)
    
    Returns:
        dict: Weather data or error message
    """
    try:
        url = f"{BASE_URL}/weather"
        params = {
            'appid': API_KEY,
            'units': 'metric'
        }
        
        if lat and lon:
            params['lat'] = lat
            params['lon'] = lon
        elif city:
            params['q'] = city
        else:
            return {'success': False, 'error': 'No location provided'}
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            return {
                'success': True,
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': round(data['main']['temp'], 1),
                'feels_like': round(data['main']['feels_like'], 1),
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'wind_speed': round(data['wind']['speed'] * 3.6, 1),  # Convert m/s to km/h
                'description': data['weather'][0]['description'].title(),
                'icon': data['weather'][0]['icon'],
                'clouds': data['clouds']['all'],
                'visibility': data.get('visibility', 0) / 1000,  # Convert to km
                'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%I:%M %p'),
                'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%I:%M %p'),
            }
        else:
            return {
                'success': False,
                'error': 'Location not found. Please try again.'
            }
    except Exception as e:
        return {
            'success': False,
            'error': f'Error fetching weather data: {str(e)}'
        }


def get_forecast(city=None, lat=None, lon=None, days=7):
    """
    Get weather forecast for a city or coordinates
    
    Args:
        city (str): City name (optional)
        lat (float): Latitude (optional)
        lon (float): Longitude (optional)
        days (int): Number of days
    
    Returns:
        dict: Forecast data or error message
    """
    try:
        url = f"{BASE_URL}/forecast"
        params = {
            'appid': API_KEY,
            'units': 'metric',
            'cnt': days * 8
        }
        
        if lat and lon:
            params['lat'] = lat
            params['lon'] = lon
        elif city:
            params['q'] = city
        else:
            return {'success': False, 'error': 'No location provided'}
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            
            # Process forecast data - group by day
            daily_forecasts = {}
            
            for item in data['list']:
                date = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
                day_name = datetime.fromtimestamp(item['dt']).strftime('%A')
                
                if date not in daily_forecasts:
                    daily_forecasts[date] = {
                        'date': date,
                        'day': day_name,
                        'temps': [],
                        'humidity': [],
                        'descriptions': [],
                        'icons': [],
                        'rain_prob': 0
                    }
                
                daily_forecasts[date]['temps'].append(item['main']['temp'])
                daily_forecasts[date]['humidity'].append(item['main']['humidity'])
                daily_forecasts[date]['descriptions'].append(item['weather'][0]['description'])
                daily_forecasts[date]['icons'].append(item['weather'][0]['icon'])
                
                # Check for rain
                if 'rain' in item:
                    daily_forecasts[date]['rain_prob'] = max(
                        daily_forecasts[date]['rain_prob'],
                        item.get('pop', 0) * 100
                    )
            
            # Calculate daily averages
            forecast_list = []
            for date, data in list(daily_forecasts.items())[:days]:
                forecast_list.append({
                    'date': date,
                    'day': data['day'],
                    'temp_max': round(max(data['temps']), 1),
                    'temp_min': round(min(data['temps']), 1),
                    'temp_avg': round(sum(data['temps']) / len(data['temps']), 1),
                    'humidity': round(sum(data['humidity']) / len(data['humidity']), 1),
                    'description': max(set(data['descriptions']), key=data['descriptions'].count).title(),
                    'icon': max(set(data['icons']), key=data['icons'].count),
                    'rain_probability': round(data['rain_prob'], 1)
                })
            
            return {
                'success': True,
                'city': data['city']['name'],
                'country': data['city']['country'],
                'forecasts': forecast_list
            }
        else:
            return {
                'success': False,
                'error': 'City not found. Please check the spelling and try again.'
            }
    except Exception as e:
        return {
            'success': False,
            'error': f'Error fetching forecast data: {str(e)}'
        }


def get_weather_recommendations(weather_data, crop=None):
    """
    Generate farming recommendations based on weather conditions
    
    Args:
        weather_data (dict): Current weather data
        crop (str): Optional crop name for specific recommendations
    
    Returns:
        dict: Recommendations for farming activities
    """
    if not weather_data.get('success'):
        return {'recommendations': []}
    
    temp = weather_data['temperature']
    humidity = weather_data['humidity']
    description = weather_data['description'].lower()
    
    recommendations = []
    alerts = []
    
    # Temperature-based recommendations
    if temp > 35:
        recommendations.append("🌡️ High temperature alert: Increase irrigation frequency")
        recommendations.append("☀️ Avoid spraying pesticides during peak heat (11 AM - 3 PM)")
        alerts.append("Extreme heat - protect crops with shade nets if possible")
    elif temp > 30:
        recommendations.append("🌡️ Warm weather: Ensure adequate water supply for crops")
        recommendations.append("💧 Consider drip irrigation to conserve water")
    elif temp < 10:
        recommendations.append("❄️ Cold weather: Protect sensitive crops from frost")
        recommendations.append("🌾 Good time for winter crops like wheat, mustard, peas")
        alerts.append("Frost risk - cover young plants overnight")
    
    # Humidity-based recommendations
    if humidity > 80:
        recommendations.append("💧 High humidity: Monitor for fungal diseases")
        recommendations.append("🍃 Ensure good air circulation in crops")
        recommendations.append("⚠️ Avoid overhead irrigation to prevent disease spread")
    elif humidity < 30:
        recommendations.append("🏜️ Low humidity: Increase irrigation to prevent wilting")
        recommendations.append("💨 Protect crops from drying winds")
    
    # Weather condition-based recommendations
    if 'rain' in description or 'drizzle' in description:
        recommendations.append("🌧️ Rainy conditions: Postpone fertilizer and pesticide application")
        recommendations.append("🚜 Avoid heavy field work to prevent soil compaction")
        recommendations.append("✅ Good time for transplanting seedlings")
    elif 'clear' in description or 'sunny' in description:
        recommendations.append("☀️ Clear weather: Ideal for harvesting and drying crops")
        recommendations.append("🌱 Good time for land preparation and sowing")
        recommendations.append("💊 Suitable for pesticide/fungicide application")
    elif 'cloud' in description:
        recommendations.append("☁️ Cloudy weather: Good for transplanting to reduce stress")
        recommendations.append("🌾 Suitable for most farming activities")
    
    # Crop-specific recommendations
    if crop:
        crop = crop.lower()
        if crop == 'rice':
            if temp > 25 and humidity > 60:
                recommendations.append("🌾 Rice: Ideal conditions for growth")
            if 'rain' in description:
                recommendations.append("🌾 Rice: Maintain 5-10 cm water level in fields")
        elif crop == 'wheat':
            if 15 <= temp <= 25:
                recommendations.append("🌾 Wheat: Optimal temperature for growth")
            if temp < 10:
                recommendations.append("🌾 Wheat: Good for grain filling stage")
        elif crop == 'cotton':
            if temp > 25:
                recommendations.append("🌱 Cotton: Favorable temperature for boll development")
            if humidity > 70:
                recommendations.append("🌱 Cotton: Watch for bollworm and fungal diseases")
    
    # General recommendations
    recommendations.append("📱 Check weather forecast before planning major farm activities")
    recommendations.append("💧 Adjust irrigation based on rainfall predictions")
    
    return {
        'recommendations': recommendations,
        'alerts': alerts,
        'best_activities': get_best_activities(weather_data)
    }


def get_best_activities(weather_data):
    """
    Suggest best farming activities based on current weather
    
    Args:
        weather_data (dict): Current weather data
    
    Returns:
        list: List of recommended activities
    """
    temp = weather_data['temperature']
    description = weather_data['description'].lower()
    
    activities = []
    
    if 'rain' in description:
        activities = [
            "Transplanting seedlings",
            "Checking drainage systems",
            "Indoor farm planning"
        ]
    elif 'clear' in description or 'sunny' in description:
        if 20 <= temp <= 30:
            activities = [
                "Harvesting crops",
                "Pesticide application",
                "Land preparation",
                "Sowing seeds",
                "Fertilizer application"
            ]
        elif temp > 30:
            activities = [
                "Early morning irrigation",
                "Evening pesticide application",
                "Mulching to retain moisture"
            ]
    else:  # Cloudy
        activities = [
            "Transplanting",
            "Weeding",
            "General farm maintenance",
            "Fertilizer application"
        ]
    
    return activities


# Indian cities for quick selection
INDIAN_CITIES = [
    "Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata",
    "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Lucknow",
    "Chandigarh", "Bhopal", "Indore", "Nagpur", "Patna",
    "Ludhiana", "Amritsar", "Dehradun", "Shimla", "Srinagar"
]
