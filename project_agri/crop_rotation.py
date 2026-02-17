# Crop Rotation Planner

"""
Provides crop rotation recommendations for sustainable farming.
Helps farmers plan crop sequences for soil health and pest management.
"""

# Crop rotation recommendations
ROTATION_PLANS = {
    "Rice": {
        "next_crops": [
            {
                "name": "Wheat",
                "season": "Rabi",
                "benefits": [
                    "Balances soil nutrients - different nutrient requirements",
                    "Different root depth prevents soil depletion",
                    "Breaks pest and disease cycle",
                    "Utilizes residual moisture"
                ],
                "rating": 5
            },
            {
                "name": "Mustard",
                "season": "Rabi",
                "benefits": [
                    "Breaks pest cycle effectively",
                    "Adds organic matter to soil",
                    "Deep roots improve soil structure",
                    "Good cash crop option"
                ],
                "rating": 4
            },
            {
                "name": "Peas",
                "season": "Rabi",
                "benefits": [
                    "Fixes atmospheric nitrogen (20-40 kg/ha)",
                    "Improves soil structure",
                    "Reduces nitrogen fertilizer need for next crop",
                    "Short duration crop"
                ],
                "rating": 5
            }
        ],
        "avoid": ["Rice"],
        "reason": "Continuous rice cultivation depletes specific nutrients, increases pest/disease pressure, and degrades soil structure"
    },
    
    "Wheat": {
        "next_crops": [
            {
                "name": "Rice",
                "season": "Kharif",
                "benefits": [
                    "Classic rice-wheat rotation",
                    "Complementary nutrient requirements",
                    "Assured income from both crops",
                    "Well-established practice"
                ],
                "rating": 5
            },
            {
                "name": "Cotton",
                "season": "Kharif",
                "benefits": [
                    "Different nutrient requirements",
                    "Breaks disease cycle",
                    "Good cash crop",
                    "Deep rooted crop improves soil"
                ],
                "rating": 4
            },
            {
                "name": "Maize",
                "season": "Kharif",
                "benefits": [
                    "Different root system",
                    "Breaks pest cycle",
                    "Quick growing crop",
                    "Multiple uses (grain, fodder)"
                ],
                "rating": 4
            }
        ],
        "avoid": ["Wheat", "Barley"],
        "reason": "Continuous cereal cultivation depletes soil nutrients and increases disease pressure"
    },
    
    "Cotton": {
        "next_crops": [
            {
                "name": "Wheat",
                "season": "Rabi",
                "benefits": [
                    "Cereal after cash crop balances economics",
                    "Different nutrient requirements",
                    "Breaks bollworm cycle",
                    "Utilizes residual fertilizer"
                ],
                "rating": 5
            },
            {
                "name": "Gram",
                "season": "Rabi",
                "benefits": [
                    "Fixes nitrogen for next crop",
                    "Breaks pest cycle",
                    "Improves soil structure",
                    "Low input requirement"
                ],
                "rating": 5
            },
            {
                "name": "Mustard",
                "season": "Rabi",
                "benefits": [
                    "Different crop family",
                    "Breaks pest cycle",
                    "Good cash crop",
                    "Short duration"
                ],
                "rating": 4
            }
        ],
        "avoid": ["Cotton"],
        "reason": "Continuous cotton increases bollworm, whitefly pressure and depletes soil"
    },
    
    "Maize": {
        "next_crops": [
            {
                "name": "Wheat",
                "season": "Rabi",
                "benefits": [
                    "Good cereal rotation",
                    "Complementary nutrient use",
                    "Breaks pest cycle",
                    "Maintains soil fertility"
                ],
                "rating": 5
            },
            {
                "name": "Potato",
                "season": "Rabi",
                "benefits": [
                    "High value crop after cereal",
                    "Different nutrient requirements",
                    "Good economic returns",
                    "Breaks pest cycle"
                ],
                "rating": 4
            },
            {
                "name": "Peas",
                "season": "Rabi",
                "benefits": [
                    "Nitrogen fixation",
                    "Improves soil health",
                    "Breaks pest cycle",
                    "Low fertilizer requirement"
                ],
                "rating": 5
            }
        ],
        "avoid": ["Maize", "Sorghum"],
        "reason": "Continuous coarse cereals deplete soil and increase stem borer pressure"
    },
    
    "Potato": {
        "next_crops": [
            {
                "name": "Rice",
                "season": "Kharif",
                "benefits": [
                    "Cereal after tuber crop",
                    "Utilizes residual fertilizer",
                    "Different pest spectrum",
                    "Balances crop economics"
                ],
                "rating": 4
            },
            {
                "name": "Maize",
                "season": "Kharif",
                "benefits": [
                    "Different root system",
                    "Breaks disease cycle",
                    "Good fodder option",
                    "Quick growing"
                ],
                "rating": 4
            },
            {
                "name": "Onion",
                "season": "Kharif",
                "benefits": [
                    "Both are high value crops",
                    "Different pest/disease spectrum",
                    "Good economic returns",
                    "Efficient land use"
                ],
                "rating": 3
            }
        ],
        "avoid": ["Potato", "Tomato"],
        "reason": "Solanaceous crops share diseases (late blight, early blight) and pests"
    },
    
    "Tomato": {
        "next_crops": [
            {
                "name": "Wheat",
                "season": "Rabi",
                "benefits": [
                    "Cereal after vegetable",
                    "Breaks disease cycle",
                    "Different nutrient requirements",
                    "Soil rest from intensive cultivation"
                ],
                "rating": 5
            },
            {
                "name": "Onion",
                "season": "Rabi",
                "benefits": [
                    "Different crop family",
                    "Breaks pest cycle",
                    "High value crop",
                    "Good market demand"
                ],
                "rating": 4
            },
            {
                "name": "Peas",
                "season": "Rabi",
                "benefits": [
                    "Nitrogen fixation",
                    "Breaks disease cycle",
                    "Improves soil health",
                    "Short duration"
                ],
                "rating": 5
            }
        ],
        "avoid": ["Tomato", "Potato", "Chili"],
        "reason": "Solanaceous crops share common diseases and pests"
    },
    
    # New crops added - Phase 3 Enhancement
    "Sugarcane": {
        "next_crops": [
            {
                "name": "Wheat",
                "season": "Rabi",
                "benefits": [
                    "Cereal after sugarcane restores soil balance",
                    "Breaks pest cycle effectively",
                    "Utilizes residual fertilizer",
                    "Different nutrient requirements"
                ],
                "rating": 5
            },
            {
                "name": "Peas",
                "season": "Rabi",
                "benefits": [
                    "Nitrogen fixation (20-40 kg/ha)",
                    "Restores soil nitrogen after heavy feeder",
                    "Breaks disease cycle",
                    "Improves soil structure"
                ],
                "rating": 5
            },
            {
                "name": "Potato",
                "season": "Rabi",
                "benefits": [
                    "High value crop after sugarcane",
                    "Different pest spectrum",
                    "Good economic returns",
                    "Efficient land use"
                ],
                "rating": 4
            }
        ],
        "avoid": ["Sugarcane"],
        "reason": "Continuous sugarcane depletes soil severely and increases red rot, wilt diseases"
    },
    
    "Soybean": {
        "next_crops": [
            {
                "name": "Wheat",
                "season": "Rabi",
                "benefits": [
                    "Cereal after legume is ideal rotation",
                    "Utilizes residual nitrogen from soybean",
                    "Reduces fertilizer requirement by 25-30%",
                    "Breaks pest cycle"
                ],
                "rating": 5
            },
            {
                "name": "Mustard",
                "season": "Rabi",
                "benefits": [
                    "Different crop family",
                    "Breaks pest cycle",
                    "Good cash crop option",
                    "Short duration crop"
                ],
                "rating": 4
            },
            {
                "name": "Gram",
                "season": "Rabi",
                "benefits": [
                    "Both are legumes but different families",
                    "Continues nitrogen fixation",
                    "Low input requirement",
                    "Good market demand"
                ],
                "rating": 3
            }
        ],
        "avoid": ["Soybean"],
        "reason": "Continuous soybean increases rust, pod borer pressure and depletes micronutrients"
    },
    
    "Groundnut": {
        "next_crops": [
            {
                "name": "Wheat",
                "season": "Rabi",
                "benefits": [
                    "Cereal after legume maximizes nitrogen use",
                    "Reduces nitrogen fertilizer by 30%",
                    "Different root depth",
                    "Breaks pest cycle"
                ],
                "rating": 5
            },
            {
                "name": "Rice",
                "season": "Kharif",
                "benefits": [
                    "Utilizes residual nitrogen",
                    "Different water requirement",
                    "Breaks pest cycle",
                    "Good crop sequence"
                ],
                "rating": 4
            },
            {
                "name": "Cotton",
                "season": "Kharif",
                "benefits": [
                    "Cash crop after legume",
                    "Utilizes fixed nitrogen",
                    "Different pest spectrum",
                    "Good economic returns"
                ],
                "rating": 4
            }
        ],
        "avoid": ["Groundnut", "Soybean"],
        "reason": "Continuous legumes increase soil-borne diseases and pest pressure"
    },
    
    "Sunflower": {
        "next_crops": [
            {
                "name": "Wheat",
                "season": "Rabi",
                "benefits": [
                    "Cereal after oilseed balances soil",
                    "Different nutrient requirements",
                    "Breaks pest cycle",
                    "Good crop rotation"
                ],
                "rating": 5
            },
            {
                "name": "Gram",
                "season": "Rabi",
                "benefits": [
                    "Legume after oilseed",
                    "Nitrogen fixation",
                    "Improves soil health",
                    "Low input cost"
                ],
                "rating": 5
            },
            {
                "name": "Mustard",
                "season": "Rabi",
                "benefits": [
                    "Different oilseed family",
                    "Breaks pest cycle",
                    "Good cash crop",
                    "Short duration"
                ],
                "rating": 3
            }
        ],
        "avoid": ["Sunflower"],
        "reason": "Continuous sunflower increases Alternaria blight and head rot diseases"
    }
}

# Three-year rotation plans
THREE_YEAR_PLANS = [
    {
        "name": "Rice-Wheat-Legume Rotation",
        "sequence": [
            {"crop": "Rice", "season": "Kharif (Jun-Oct)"},
            {"crop": "Wheat", "season": "Rabi (Nov-Mar)"},
            {"crop": "Moong/Peas", "season": "Zaid (Mar-Jun)"}
        ],
        "benefits": [
            "Nitrogen fixation from legume reduces fertilizer cost",
            "Balanced nutrient use across crops",
            "Year-round income generation",
            "Breaks pest and disease cycles",
            "Improves soil organic matter"
        ],
        "suitable_for": "Irrigated areas with good water availability",
        "estimated_income": "High - Three crops per year"
    },
    {
        "name": "Cotton-Wheat-Moong Rotation",
        "sequence": [
            {"crop": "Cotton", "season": "Kharif (May-Nov)"},
            {"crop": "Wheat", "season": "Rabi (Nov-Mar)"},
            {"crop": "Moong", "season": "Zaid (Mar-May)"}
        ],
        "benefits": [
            "Cash crop (cotton) followed by food crops",
            "Legume fixes nitrogen for next cotton crop",
            "Breaks bollworm cycle",
            "Diversified income sources",
            "Efficient use of land throughout year"
        ],
        "suitable_for": "Semi-arid regions with moderate irrigation",
        "estimated_income": "Very High - Cotton provides major income"
    },
    {
        "name": "Maize-Potato-Onion Rotation",
        "sequence": [
            {"crop": "Maize", "season": "Kharif (Jun-Sep)"},
            {"crop": "Potato", "season": "Rabi (Oct-Jan)"},
            {"crop": "Onion", "season": "Rabi/Zaid (Jan-May)"}
        ],
        "benefits": [
            "High value vegetable crops",
            "Different crop families reduce pest pressure",
            "Intensive cultivation with high returns",
            "Good market demand for all crops",
            "Efficient nutrient utilization"
        ],
        "suitable_for": "Areas with good irrigation and market access",
        "estimated_income": "Very High - All high-value crops"
    },
    {
        "name": "Soybean-Wheat-Moong Rotation",
        "sequence": [
            {"crop": "Soybean", "season": "Kharif (Jun-Oct)"},
            {"crop": "Wheat", "season": "Rabi (Nov-Mar)"},
            {"crop": "Moong", "season": "Zaid (Mar-Jun)"}
        ],
        "benefits": [
            "Two legumes fix atmospheric nitrogen",
            "Reduces fertilizer cost significantly",
            "Improves soil health and structure",
            "Good protein source crops",
            "Sustainable and eco-friendly"
        ],
        "suitable_for": "Medium to heavy soils with moderate irrigation",
        "estimated_income": "Medium to High - Lower input costs"
    },
    {
        "name": "Rice-Mustard-Watermelon Rotation",
        "sequence": [
            {"crop": "Rice", "season": "Kharif (Jun-Oct)"},
            {"crop": "Mustard", "season": "Rabi (Oct-Feb)"},
            {"crop": "Watermelon", "season": "Zaid (Feb-May)"}
        ],
        "benefits": [
            "Diversified crop portfolio",
            "Cash crop (watermelon) in summer",
            "Different root systems improve soil",
            "Breaks pest cycles effectively",
            "Good income distribution across year"
        ],
        "suitable_for": "Alluvial soils with assured irrigation",
        "estimated_income": "High - Watermelon provides good returns"
    }
]

# General rotation principles
ROTATION_PRINCIPLES = [
    {
        "principle": "Alternate Deep and Shallow Rooted Crops",
        "explanation": "Deep-rooted crops (cotton, pigeon pea) followed by shallow-rooted crops (wheat, rice) ensures nutrients from different soil layers are utilized",
        "example": "Cotton → Wheat"
    },
    {
        "principle": "Include Legumes in Rotation",
        "explanation": "Legumes fix atmospheric nitrogen (20-40 kg/ha) reducing fertilizer costs and improving soil health",
        "example": "Rice → Peas → Maize"
    },
    {
        "principle": "Avoid Same Crop Family Continuously",
        "explanation": "Crops from same family share pests and diseases. Rotating families breaks pest cycles",
        "example": "Avoid: Tomato → Potato (both Solanaceae)"
    },
    {
        "principle": "Balance Heavy and Light Feeders",
        "explanation": "Heavy feeders (vegetables, cotton) should be followed by light feeders (legumes, millets)",
        "example": "Potato → Peas"
    },
    {
        "principle": "Consider Market Demand and Economics",
        "explanation": "Balance food crops with cash crops for stable income and risk management",
        "example": "Cotton (cash) → Wheat (food)"
    }
]


def get_rotation_suggestions(current_crop):
    """Get crop rotation suggestions for a given crop"""
    return ROTATION_PLANS.get(current_crop, {
        "next_crops": [],
        "avoid": [],
        "reason": "Crop not found in database"
    })


def get_three_year_plans():
    """Get all three-year rotation plans"""
    return THREE_YEAR_PLANS


def get_rotation_principles():
    """Get general crop rotation principles"""
    return ROTATION_PRINCIPLES
