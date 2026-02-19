import random
from datetime import datetime, timedelta

# Mock Data Generator for Market Prices
# In a real scenario, this would connect to the Agmarknet API

STATES = [
    "Maharashtra", "Punjab", "Haryana", "Uttar Pradesh", "Madhya Pradesh", 
    "Guitar", "Karnataka", "Tamil Nadu", "Rajasthan", "West Bengal"
]

DISTRICTS = {
    "Maharashtra": ["Pune", "Nashik", "Nagpur", "Ahmednagar", "Solapur"],
    "Punjab": ["Ludhiana", "Amritsar", "Jalandhar", "Patiala", "Bathinda"],
    "Haryana": ["Karnal", "Hisar", "Ambala", "Rohtak", "Gurugram"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi", "Agra", "Meerut"],
    "Madhya Pradesh": ["Indore", "Bhopal", "Jabalpur", "Gwalior", "Ujjain"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar"],
    "Karnataka": ["Bangalore", "Mysore", "Hubli", "Belgaum", "Mangalore"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Salem", "Tiruchirappalli"],
    "Rajasthan": ["Jaipur", "Jodhpur", "Kota", "Bikaner", "Ajmer"],
    "West Bengal": ["Kolkata", "Howrah", "Darjeeling", "Siliguri", "Asansol"]
}

COMMODITIES = [
    "Rice", "Wheat", "Maize", "Bajra", "Jowar", 
    "Cotton", "Sugarcane", "Potato", "Onion", "Tomato",
    "Soybean", "Groundnut", "Mustard", "Tur", "Gram"
]

VARIETIES = {
    "Rice": ["Basmati", "Sona Masuri", "Common", "IR-64"],
    "Wheat": ["Lokwan", "Sharbati", "Dara", "Common"],
    "Maize": ["Hybrid", "Local", "Yellow"],
    "Potato": ["Jyoti", "Chandramukhi", "Desi"],
    "Onion": ["Red", "White", "Nashik"],
    "Tomato": ["Hybrid", "Desi", "Local"],
    "Cotton": ["H-4", "LRA", "Bunny"],
    "Sugarcane": ["Co-86032", "Common"],
    "Soybean": ["Yellow", "Black"],
    "Groundnut": ["Bold", "Java"],
    "Mustard": ["Black", "Yellow"],
    "Tur": ["Red", "White"],
    "Gram": ["Desi", "Kabuli"],
    "Bajra": ["Hybrid", "Desi"],
    "Jowar": ["Hybrid", "Maldandi"]
}

def get_market_prices(state=None, commodity=None):
    """
    Generate realistic mock market price data.
    """
    results = []
    
    # Filter states
    target_states = [state] if state and state in STATES else STATES
    
    # Filter commodities
    target_commodities = [commodity] if commodity and commodity in COMMODITIES else COMMODITIES
    
    for s in target_states:
        districts = DISTRICTS.get(s, [])
        # Pick 3-5 random districts per state for variety
        selected_districts = random.sample(districts, min(len(districts), random.randint(3, 5)))
        
        for d in selected_districts:
            # Pick 2-4 random commodities per district
            selected_crops = random.sample(target_commodities, min(len(target_commodities), random.randint(2, 4)))
            
            for c in selected_crops:
                varieties = VARIETIES.get(c, ["Common"])
                variety = random.choice(varieties)
                
                # Generate realistic price logic
                base_price = random.randint(1500, 8000) # Base price per quintal
                min_price = base_price - random.randint(100, 500)
                max_price = base_price + random.randint(100, 500)
                modal_price = (min_price + max_price) // 2
                
                # Trend
                trend = random.choice(['up', 'down', 'stable'])
                
                results.append({
                    "state": s,
                    "district": d,
                    "market": f"{d} APMC",
                    "commodity": c,
                    "variety": variety,
                    "min_price": min_price,
                    "max_price": max_price,
                    "modal_price": modal_price,
                    "unit": "Rs/Quintal",
                    "arrival_date": datetime.now().strftime("%d-%m-%Y"),
                    "trend": trend
                })
                
    return results

def get_states():
    return sorted(STATES)

def get_commodities():
    return sorted(COMMODITIES)
