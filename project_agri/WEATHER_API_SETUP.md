# Weather Integration - API Key Setup

## Important: OpenWeatherMap API Key Required

The Weather Forecast feature requires a **free** OpenWeatherMap API key to function.

### How to Get Your Free API Key:

1. **Sign up** at [OpenWeatherMap](https://openweathermap.org/api)
2. **Create a free account** (no credit card required)
3. **Navigate to** "API keys" in your account dashboard
4. **Copy** your API key

### How to Add Your API Key:

1. Open the file: `weather_service.py`
2. Find line 9: `API_KEY = "your_api_key_here"`
3. Replace `"your_api_key_here"` with your actual API key
4. Save the file

### Example:
```python
# Before:
API_KEY = "your_api_key_here"

# After (with your key):
API_KEY = "abc123def456ghi789jkl012mno345pqr"
```

### Free Tier Limits:
- **1,000 API calls per day** (more than enough for testing)
- **Current weather** + **7-day forecast**
- No credit card required

### Testing Without API Key:
The weather page will load but show an error message until you add a valid API key.

---

**Note:** Keep your API key private and don't share it publicly!
