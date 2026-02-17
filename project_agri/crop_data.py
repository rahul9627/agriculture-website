# Crop Data - Seasonal Calendar and Weather-Based Care Guide

"""
This module contains crop calendar data and weather-based care recommendations
for the Agriculture Website.
"""

# Seasonal Crop Calendar Data
CROP_CALENDAR = {
    "Kharif": {
        "season_name": "Kharif (Monsoon Season)",
        "months": ["June", "July", "August", "September", "October"],
        "description": "Crops sown at the beginning of monsoon and harvested in autumn",
        "crops": [
            {
                "name": "Rice",
                "emoji": "🌾",
                "sowing": "June-July",
                "harvest": "October-November",
                "duration": "120-150 days",
                "description": "Major Kharif crop requiring flooded conditions and warm weather"
            },
            {
                "name": "Cotton",
                "emoji": "🌸",
                "sowing": "May-June",
                "harvest": "October-December",
                "duration": "150-180 days",
                "description": "Requires warm weather and moderate rainfall"
            },
            {
                "name": "Maize",
                "emoji": "🌽",
                "sowing": "June-July",
                "harvest": "September-October",
                "duration": "80-110 days",
                "description": "Versatile crop, grows well in warm and humid conditions"
            },
            {
                "name": "Sorghum",
                "emoji": "🌾",
                "sowing": "June-July",
                "harvest": "October-November",
                "duration": "100-140 days",
                "description": "Drought-resistant crop suitable for rain-fed areas"
            },
            {
                "name": "Pearl Millet",
                "emoji": "🌾",
                "sowing": "June-July",
                "harvest": "September-October",
                "duration": "70-90 days",
                "description": "Highly drought-tolerant, suitable for arid regions"
            },
            {
                "name": "Soybean",
                "emoji": "🫘",
                "sowing": "June-July",
                "harvest": "October-November",
                "duration": "90-120 days",
                "description": "Important oilseed crop, requires well-drained soil"
            },
            {
                "name": "Groundnut",
                "emoji": "🥜",
                "sowing": "June-July",
                "harvest": "October-November",
                "duration": "100-150 days",
                "description": "Oilseed crop requiring sandy loam soil"
            },
            {
                "name": "Sugarcane",
                "emoji": "🎋",
                "sowing": "February-March (Spring), September-October (Autumn)",
                "harvest": "12-18 months after planting",
                "duration": "12-18 months",
                "description": "Long-duration crop requiring abundant water"
            }
        ]
    },
    "Rabi": {
        "season_name": "Rabi (Winter Season)",
        "months": ["October", "November", "December", "January", "February", "March"],
        "description": "Crops sown in winter and harvested in spring",
        "crops": [
            {
                "name": "Wheat",
                "emoji": "🌾",
                "sowing": "October-November",
                "harvest": "March-April",
                "duration": "120-150 days",
                "description": "Major Rabi crop requiring cool weather for growth"
            },
            {
                "name": "Barley",
                "emoji": "🌾",
                "sowing": "October-November",
                "harvest": "March-April",
                "duration": "120-140 days",
                "description": "Hardy cereal crop tolerant to saline and alkaline soils"
            },
            {
                "name": "Mustard",
                "emoji": "🌻",
                "sowing": "October-November",
                "harvest": "February-March",
                "duration": "90-120 days",
                "description": "Important oilseed crop of Rabi season"
            },
            {
                "name": "Peas",
                "emoji": "🫛",
                "sowing": "October-November",
                "harvest": "January-February",
                "duration": "60-90 days",
                "description": "Legume crop requiring cool weather"
            },
            {
                "name": "Gram (Chickpea)",
                "emoji": "🫘",
                "sowing": "October-November",
                "harvest": "February-March",
                "duration": "100-120 days",
                "description": "Important pulse crop, drought-resistant"
            },
            {
                "name": "Lentils",
                "emoji": "🫘",
                "sowing": "October-November",
                "harvest": "February-March",
                "duration": "100-110 days",
                "description": "Pulse crop requiring cool, dry weather"
            },
            {
                "name": "Potato",
                "emoji": "🥔",
                "sowing": "October-November",
                "harvest": "January-March",
                "duration": "90-120 days",
                "description": "Tuber crop requiring cool weather and well-drained soil"
            },
            {
                "name": "Onion",
                "emoji": "🧅",
                "sowing": "October-November",
                "harvest": "February-April",
                "duration": "120-150 days",
                "description": "Bulb crop requiring cool weather initially"
            }
        ]
    },
    "Zaid": {
        "season_name": "Zaid (Summer Season)",
        "months": ["March", "April", "May", "June"],
        "description": "Short season crops grown between Rabi and Kharif",
        "crops": [
            {
                "name": "Watermelon",
                "emoji": "🍉",
                "sowing": "February-March",
                "harvest": "May-June",
                "duration": "80-100 days",
                "description": "Summer fruit requiring warm weather and irrigation"
            },
            {
                "name": "Muskmelon",
                "emoji": "🍈",
                "sowing": "February-March",
                "harvest": "May-June",
                "duration": "70-90 days",
                "description": "Summer fruit crop requiring sandy loam soil"
            },
            {
                "name": "Cucumber",
                "emoji": "🥒",
                "sowing": "February-March",
                "harvest": "April-June",
                "duration": "50-70 days",
                "description": "Quick-growing vegetable requiring warm weather"
            },
            {
                "name": "Bitter Gourd",
                "emoji": "🥒",
                "sowing": "February-March",
                "harvest": "April-June",
                "duration": "55-70 days",
                "description": "Vegetable crop requiring warm, humid conditions"
            },
            {
                "name": "Pumpkin",
                "emoji": "🎃",
                "sowing": "February-March",
                "harvest": "May-July",
                "duration": "90-120 days",
                "description": "Vine crop requiring warm weather and space"
            },
            {
                "name": "Tomato",
                "emoji": "🍅",
                "sowing": "February-March",
                "harvest": "May-June",
                "duration": "70-90 days",
                "description": "Versatile vegetable crop, can be grown year-round with care"
            },
            {
                "name": "Moong (Green Gram)",
                "emoji": "🫘",
                "sowing": "March-April",
                "harvest": "May-June",
                "duration": "60-75 days",
                "description": "Short-duration pulse crop"
            }
        ]
    }
}

# Weather-Based Crop Care Recommendations
CROP_CARE = {
    "Rice": {
        "general": "Rice is a water-intensive crop requiring flooded conditions during most of its growth period.",
        "Hot": [
            "Maintain adequate water levels in fields (5-10 cm)",
            "Ensure continuous water supply to prevent stress",
            "Monitor for leaf folder and stem borer pests",
            "Apply mulch around field bunds to reduce evaporation",
            "Avoid draining fields during hot spells"
        ],
        "Cold": [
            "Protect seedlings from frost damage",
            "Reduce water depth in fields during cold nights",
            "Apply potassium fertilizers to improve cold tolerance",
            "Monitor for blast disease which thrives in cool conditions",
            "Delay transplanting if severe cold is expected"
        ],
        "Rainy": [
            "Ensure proper drainage to prevent waterlogging",
            "Watch for blast disease and brown spot",
            "Apply fungicide if disease symptoms appear",
            "Check for pest infestation (especially stem borers)",
            "Avoid fertilizer application during heavy rains",
            "Monitor for bacterial leaf blight"
        ],
        "Dry": [
            "Increase irrigation frequency",
            "Maintain consistent water levels",
            "Apply organic mulch to conserve moisture",
            "Monitor for drought stress symptoms (leaf rolling)",
            "Consider alternate wetting and drying if water is scarce"
        ],
        "Humid": [
            "Improve field ventilation by proper spacing",
            "Watch for fungal diseases (blast, sheath blight)",
            "Apply preventive fungicides",
            "Monitor for bacterial diseases",
            "Ensure good drainage to reduce humidity at soil level"
        ]
    },
    "Wheat": {
        "general": "Wheat is a Rabi crop requiring cool weather for growth and warm weather for ripening.",
        "Hot": [
            "Increase irrigation frequency during grain filling",
            "Apply light irrigation to prevent heat stress",
            "Monitor for aphids and termites",
            "Harvest promptly when mature to prevent grain shattering",
            "Avoid irrigation during flowering to prevent lodging"
        ],
        "Cold": [
            "Protect from severe frost during flowering",
            "Apply irrigation before expected frost to moderate temperature",
            "Monitor for rust diseases which thrive in cool, moist conditions",
            "Apply nitrogen fertilizer in split doses",
            "Ensure good drainage to prevent waterlogging"
        ],
        "Rainy": [
            "Ensure proper drainage to prevent waterlogging",
            "Watch for rust diseases (yellow, brown, black rust)",
            "Apply fungicides if rust symptoms appear",
            "Delay irrigation if rainfall is adequate",
            "Monitor for aphid infestation",
            "Avoid nitrogen application during heavy rains"
        ],
        "Dry": [
            "Provide irrigation at critical stages (crown root initiation, tillering, flowering, grain filling)",
            "Apply light, frequent irrigations",
            "Use mulch to conserve soil moisture",
            "Monitor for drought stress",
            "Consider drought-tolerant varieties for future seasons"
        ],
        "Humid": [
            "Improve air circulation by proper spacing",
            "Watch for rust and powdery mildew",
            "Apply preventive fungicides",
            "Avoid excessive nitrogen which promotes disease",
            "Monitor for aphids and other pests"
        ]
    },
    "Cotton": {
        "general": "Cotton requires warm weather, moderate rainfall, and plenty of sunshine.",
        "Hot": [
            "Maintain regular irrigation schedule",
            "Apply irrigation during boll formation stage",
            "Monitor for whitefly and jassid infestation",
            "Provide adequate potassium for heat tolerance",
            "Watch for boll shedding due to heat stress"
        ],
        "Cold": [
            "Protect young plants from cold stress",
            "Delay sowing if cold weather is expected",
            "Apply phosphorus fertilizers for root development",
            "Monitor for slow growth and yellowing",
            "Ensure good drainage"
        ],
        "Rainy": [
            "Ensure excellent drainage to prevent waterlogging",
            "Watch for boll rot and bacterial blight",
            "Monitor for increased pest activity",
            "Delay pesticide application during rains",
            "Check for pink bollworm and American bollworm",
            "Avoid picking cotton when wet"
        ],
        "Dry": [
            "Provide regular irrigation, especially during flowering and boll formation",
            "Apply mulch to conserve moisture",
            "Monitor for drought stress (wilting, leaf drop)",
            "Increase irrigation frequency during dry spells",
            "Watch for spider mites which thrive in dry conditions"
        ],
        "Humid": [
            "Improve field ventilation",
            "Watch for fungal diseases (Alternaria leaf spot, boll rot)",
            "Monitor for increased insect pest activity",
            "Apply preventive fungicides and insecticides",
            "Ensure proper plant spacing"
        ]
    },
    "Maize": {
        "general": "Maize requires warm weather, adequate moisture, and good drainage.",
        "Hot": [
            "Provide adequate irrigation during tasseling and silking",
            "Apply irrigation during grain filling",
            "Monitor for stem borer and fall armyworm",
            "Ensure adequate potassium for stress tolerance",
            "Watch for leaf scorching"
        ],
        "Cold": [
            "Protect seedlings from frost",
            "Delay sowing if severe cold is expected",
            "Apply phosphorus for better root development",
            "Monitor for slow growth",
            "Ensure good soil drainage"
        ],
        "Rainy": [
            "Ensure proper drainage to prevent waterlogging",
            "Watch for stalk rot and ear rot diseases",
            "Monitor for increased pest activity (stem borer, fall armyworm)",
            "Delay fertilizer application during heavy rains",
            "Check for fungal diseases"
        ],
        "Dry": [
            "Provide irrigation at critical stages (knee-high, tasseling, grain filling)",
            "Apply mulch to conserve moisture",
            "Monitor for drought stress (leaf rolling)",
            "Increase irrigation frequency",
            "Watch for spider mites"
        ],
        "Humid": [
            "Improve air circulation",
            "Watch for fungal diseases (blight, rust)",
            "Monitor for increased insect activity",
            "Apply preventive fungicides",
            "Ensure proper plant spacing"
        ]
    },
    "Potato": {
        "general": "Potato requires cool weather, well-drained soil, and consistent moisture.",
        "Hot": [
            "Increase irrigation frequency",
            "Apply mulch to keep soil cool",
            "Monitor for early blight and late blight",
            "Harvest early if excessive heat is expected",
            "Watch for aphids which transmit viruses"
        ],
        "Cold": [
            "Protect from frost damage (cover with straw if needed)",
            "Delay planting if severe frost is expected",
            "Monitor for slow growth",
            "Ensure good drainage to prevent rot",
            "Apply adequate potassium for cold tolerance"
        ],
        "Rainy": [
            "Ensure excellent drainage to prevent tuber rot",
            "Watch for late blight disease (most serious in wet conditions)",
            "Apply fungicides preventively",
            "Hill up plants to improve drainage",
            "Monitor for bacterial wilt",
            "Delay harvesting until soil dries"
        ],
        "Dry": [
            "Provide regular, consistent irrigation",
            "Avoid water stress during tuber formation",
            "Apply mulch to conserve moisture",
            "Monitor for drought stress",
            "Ensure even moisture to prevent hollow heart"
        ],
        "Humid": [
            "Improve air circulation",
            "Watch for late blight and early blight",
            "Apply preventive fungicides",
            "Monitor for aphids and other pests",
            "Ensure proper hilling for drainage"
        ]
    },
    "Tomato": {
        "general": "Tomato requires warm weather, consistent moisture, and good air circulation.",
        "Hot": [
            "Provide shade during extreme heat",
            "Increase irrigation frequency",
            "Apply mulch to keep roots cool",
            "Monitor for blossom end rot (calcium deficiency)",
            "Watch for fruit cracking and sunscald",
            "Ensure adequate calcium and potassium"
        ],
        "Cold": [
            "Protect from frost (use row covers)",
            "Delay transplanting if cold weather expected",
            "Monitor for slow growth and yellowing",
            "Ensure good drainage",
            "Apply phosphorus for root development"
        ],
        "Rainy": [
            "Ensure good drainage",
            "Watch for early blight, late blight, and septoria leaf spot",
            "Apply fungicides preventively",
            "Stake plants to improve air circulation",
            "Monitor for bacterial diseases",
            "Avoid overhead irrigation"
        ],
        "Dry": [
            "Provide consistent, regular irrigation",
            "Apply mulch to conserve moisture",
            "Monitor for blossom end rot",
            "Avoid water stress during fruit development",
            "Use drip irrigation for efficiency"
        ],
        "Humid": [
            "Improve air circulation by proper spacing and staking",
            "Watch for fungal diseases (early blight, late blight, powdery mildew)",
            "Apply preventive fungicides",
            "Monitor for whiteflies and aphids",
            "Prune lower leaves to improve airflow"
        ]
    },
    "Onion": {
        "general": "Onion requires cool weather initially, then warm weather for bulb development.",
        "Hot": [
            "Increase irrigation frequency",
            "Apply light, frequent irrigations",
            "Monitor for thrips infestation",
            "Watch for premature bolting in extreme heat",
            "Ensure adequate potassium for bulb development"
        ],
        "Cold": [
            "Protect seedlings from severe frost",
            "Monitor for slow growth",
            "Ensure good drainage",
            "Apply adequate nitrogen for leaf growth",
            "Watch for purple blotch disease"
        ],
        "Rainy": [
            "Ensure excellent drainage",
            "Watch for purple blotch and downy mildew",
            "Apply fungicides preventively",
            "Monitor for bacterial rot",
            "Delay harvesting until bulbs dry",
            "Avoid nitrogen application during heavy rains"
        ],
        "Dry": [
            "Provide regular irrigation during bulb formation",
            "Avoid water stress which causes small bulbs",
            "Apply mulch to conserve moisture",
            "Monitor for drought stress",
            "Reduce irrigation 2-3 weeks before harvest"
        ],
        "Humid": [
            "Improve air circulation",
            "Watch for fungal diseases (purple blotch, downy mildew)",
            "Apply preventive fungicides",
            "Monitor for thrips",
            "Ensure proper spacing"
        ]
    }
}

# Get current season based on month
def get_current_season(month_name):
    """Returns the current season based on month name"""
    for season, data in CROP_CALENDAR.items():
        if month_name in data["months"]:
            return season
    return "Kharif"  # Default

# Get crops for current month
def get_current_month_crops(month_name):
    """Returns crops suitable for sowing in the current month"""
    season = get_current_season(month_name)
    return CROP_CALENDAR[season]["crops"]
