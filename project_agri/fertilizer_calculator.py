# Fertilizer Calculator Module

"""
Calculate fertilizer requirements based on soil NPK levels and target crop.
Provides recommendations for Urea, DAP, and MOP fertilizers.
"""

# Fertilizer NPK content (percentage)
FERTILIZERS = {
    "Urea": {"N": 46, "P": 0, "K": 0, "price_per_kg": 6},
    "DAP": {"N": 18, "P": 46, "K": 0, "price_per_kg": 27},
    "MOP": {"N": 0, "P": 0, "K": 60, "price_per_kg": 17},
    "SSP": {"N": 0, "P": 16, "K": 0, "price_per_kg": 8}
}

# Crop NPK requirements (kg/hectare) - Optimal levels
CROP_REQUIREMENTS = {
    "Rice": {"N": 120, "P": 60, "K": 40},
    "Wheat": {"N": 120, "P": 60, "K": 40},
    "Cotton": {"N": 120, "P": 60, "K": 60},
    "Maize": {"N": 120, "P": 60, "K": 40},
    "Sorghum": {"N": 80, "P": 40, "K": 40},
    "Pearl Millet": {"N": 60, "P": 30, "K": 30},
    "Soybean": {"N": 30, "P": 60, "K": 40},  # Legume, fixes nitrogen
    "Groundnut": {"N": 25, "P": 50, "K": 75},
    "Sugarcane": {"N": 150, "P": 60, "K": 60},
    "Barley": {"N": 100, "P": 50, "K": 30},
    "Mustard": {"N": 80, "P": 40, "K": 40},
    "Peas": {"N": 20, "P": 60, "K": 40},  # Legume
    "Gram": {"N": 20, "P": 40, "K": 20},  # Legume
    "Lentils": {"N": 20, "P": 40, "K": 20},  # Legume
    "Potato": {"N": 120, "P": 60, "K": 120},
    "Onion": {"N": 100, "P": 50, "K": 100},
    "Tomato": {"N": 150, "P": 75, "K": 150},
    "Watermelon": {"N": 100, "P": 50, "K": 100},
    "Cucumber": {"N": 120, "P": 60, "K": 80},
    # New crops added - Phase 3 Enhancement
    "Chilli": {"N": 100, "P": 50, "K": 75},
    "Cabbage": {"N": 120, "P": 60, "K": 100},
    "Cauliflower": {"N": 120, "P": 60, "K": 100},
    "Carrot": {"N": 80, "P": 50, "K": 100},
    "Brinjal": {"N": 100, "P": 50, "K": 75},
    "Okra": {"N": 80, "P": 40, "K": 60},
    "Spinach": {"N": 100, "P": 50, "K": 80},
    "Radish": {"N": 60, "P": 40, "K": 60},
    "Garlic": {"N": 100, "P": 50, "K": 75},
    "Ginger": {"N": 100, "P": 50, "K": 100},
}

# Application schedule recommendations
APPLICATION_SCHEDULE = {
    "Rice": {
        "Basal": {"N": 50, "P": 100, "K": 100},  # At planting
        "Tillering": {"N": 25, "P": 0, "K": 0},  # 3-4 weeks
        "Panicle": {"N": 25, "P": 0, "K": 0}     # 6-7 weeks
    },
    "Wheat": {
        "Basal": {"N": 50, "P": 100, "K": 100},
        "Crown Root": {"N": 25, "P": 0, "K": 0},
        "Tillering": {"N": 25, "P": 0, "K": 0}
    },
    "Cotton": {
        "Basal": {"N": 33, "P": 100, "K": 50},
        "Squaring": {"N": 33, "P": 0, "K": 25},
        "Flowering": {"N": 34, "P": 0, "K": 25}
    },
    "Potato": {
        "Basal": {"N": 50, "P": 100, "K": 50},
        "Earthing Up": {"N": 50, "P": 0, "K": 50}
    },
    "Tomato": {
        "Basal": {"N": 40, "P": 100, "K": 50},
        "Flowering": {"N": 30, "P": 0, "K": 25},
        "Fruiting": {"N": 30, "P": 0, "K": 25}
    }
}


def calculate_fertilizer(crop, soil_n, soil_p, soil_k, area_hectares):
    """
    Calculate fertilizer requirements based on soil test and crop needs.
    
    Args:
        crop: Name of the crop
        soil_n: Current soil nitrogen (kg/hectare)
        soil_p: Current soil phosphorus (kg/hectare)
        soil_k: Current soil potassium (kg/hectare)
        area_hectares: Farm area in hectares
    
    Returns:
        Dictionary with fertilizer quantities and cost
    """
    if crop not in CROP_REQUIREMENTS:
        return {"error": f"Crop '{crop}' not found in database"}
    
    required = CROP_REQUIREMENTS[crop]
    
    # Calculate nutrient deficit
    deficit_n = max(0, required["N"] - soil_n)
    deficit_p = max(0, required["P"] - soil_p)
    deficit_k = max(0, required["K"] - soil_k)
    
    # Calculate fertilizer quantities (kg)
    # Urea for Nitrogen
    urea_kg = (deficit_n / FERTILIZERS["Urea"]["N"]) * 100 * area_hectares
    
    # DAP for Phosphorus (also provides some Nitrogen)
    dap_kg = (deficit_p / FERTILIZERS["DAP"]["P"]) * 100 * area_hectares
    n_from_dap = (dap_kg * FERTILIZERS["DAP"]["N"]) / 100
    
    # Adjust Urea for Nitrogen already provided by DAP
    urea_kg = max(0, urea_kg - (n_from_dap / FERTILIZERS["Urea"]["N"]) * 100)
    
    # MOP for Potassium
    mop_kg = (deficit_k / FERTILIZERS["MOP"]["K"]) * 100 * area_hectares
    
    # Calculate costs
    urea_cost = urea_kg * FERTILIZERS["Urea"]["price_per_kg"]
    dap_cost = dap_kg * FERTILIZERS["DAP"]["price_per_kg"]
    mop_cost = mop_kg * FERTILIZERS["MOP"]["price_per_kg"]
    total_cost = urea_cost + dap_cost + mop_cost
    
    # Get application schedule
    schedule = APPLICATION_SCHEDULE.get(crop, {
        "Basal": {"N": 50, "P": 100, "K": 100},
        "Top Dressing": {"N": 50, "P": 0, "K": 0}
    })
    
    return {
        "fertilizers": {
            "Urea": {
                "quantity_kg": round(urea_kg, 2),
                "bags_50kg": round(urea_kg / 50, 1),
                "cost": round(urea_cost, 2),
                "nutrient": "Nitrogen (N)"
            },
            "DAP": {
                "quantity_kg": round(dap_kg, 2),
                "bags_50kg": round(dap_kg / 50, 1),
                "cost": round(dap_cost, 2),
                "nutrient": "Phosphorus (P) + Nitrogen (N)"
            },
            "MOP": {
                "quantity_kg": round(mop_kg, 2),
                "bags_50kg": round(mop_kg / 50, 1),
                "cost": round(mop_cost, 2),
                "nutrient": "Potassium (K)"
            }
        },
        "total_cost": round(total_cost, 2),
        "nutrient_deficit": {
            "N": round(deficit_n, 2),
            "P": round(deficit_p, 2),
            "K": round(deficit_k, 2)
        },
        "crop_requirements": required,
        "application_schedule": schedule,
        "area": area_hectares
    }


def get_fertilizer_tips(crop):
    """Get general fertilizer application tips for a crop"""
    tips = {
        "Rice": [
            "Apply nitrogen in 3 splits for better efficiency",
            "Apply all phosphorus and potassium as basal dose",
            "Use green manure or FYM for organic matter",
            "Avoid nitrogen application during flowering"
        ],
        "Wheat": [
            "Apply phosphorus and potassium at sowing",
            "Split nitrogen application for better uptake",
            "First irrigation at crown root initiation stage",
            "Avoid excess nitrogen which causes lodging"
        ],
        "Cotton": [
            "Apply potassium in splits for better boll development",
            "Avoid excess nitrogen which promotes vegetative growth",
            "Apply boron and zinc if deficient",
            "Use FYM or compost for soil health"
        ],
        "Potato": [
            "Apply all phosphorus at planting",
            "Split nitrogen and potassium applications",
            "Ensure adequate potassium for tuber quality",
            "Avoid fresh manure which promotes scab disease"
        ],
        "Tomato": [
            "Apply calcium to prevent blossom end rot",
            "Split nitrogen application throughout season",
            "Increase potassium during fruiting",
            "Use balanced fertilization for quality fruits"
        ]
    }
    
    return tips.get(crop, [
        "Apply fertilizers based on soil test results",
        "Split nitrogen applications for efficiency",
        "Apply phosphorus and potassium as basal dose",
        "Use organic manure for soil health"
    ])
