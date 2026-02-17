# Government Schemes Database

"""
Comprehensive database of Indian government agricultural schemes and subsidies.
Includes central and state schemes with eligibility, benefits, and application details.
"""

GOVERNMENT_SCHEMES = [
    {
        "id": 1,
        "name": "PM-KISAN",
        "full_name": "Pradhan Mantri Kisan Samman Nidhi",
        "type": "Central",
        "category": "Income Support",
        "icon": "💰",
        "benefits": "₹6,000 per year in 3 equal installments of ₹2,000 each",
        "eligibility": [
            "All landholding farmer families",
            "Small and marginal farmers",
            "No income limit"
        ],
        "how_to_apply": "Online through PM-KISAN portal or visit nearest CSC (Common Service Centre)",
        "documents_required": [
            "Aadhaar card",
            "Bank account details",
            "Land ownership documents"
        ],
        "website": "https://pmkisan.gov.in",
        "helpline": "155261 / 011-24300606",
        "description": "Direct income support to all landholding farmers to supplement financial needs for agriculture and allied activities."
    },
    {
        "id": 2,
        "name": "Kisan Credit Card (KCC)",
        "full_name": "Kisan Credit Card Scheme",
        "type": "Central",
        "category": "Credit/Loan",
        "icon": "💳",
        "benefits": "Low-interest crop loans up to ₹3 lakh at 4% interest (with 3% subvention)",
        "eligibility": [
            "All farmers (owner cultivators)",
            "Tenant farmers, oral lessees, sharecroppers",
            "Self Help Groups (SHGs) or Joint Liability Groups (JLGs)"
        ],
        "how_to_apply": "Visit nearest bank branch (Nationalized/Cooperative/RRB) with required documents",
        "documents_required": [
            "Identity proof (Aadhaar/Voter ID)",
            "Address proof",
            "Land ownership documents",
            "Passport size photographs"
        ],
        "website": "https://www.nabard.org/content1.aspx?id=523&catid=8&mid=489",
        "helpline": "Contact nearest bank branch",
        "description": "Provides adequate and timely credit support to farmers for agriculture and allied activities."
    },
    {
        "id": 3,
        "name": "PMFBY",
        "full_name": "Pradhan Mantri Fasal Bima Yojana",
        "type": "Central",
        "category": "Insurance",
        "icon": "🛡️",
        "benefits": "Comprehensive crop insurance covering yield losses due to natural calamities, pests & diseases",
        "eligibility": [
            "All farmers growing notified crops",
            "Compulsory for loanee farmers",
            "Voluntary for non-loanee farmers"
        ],
        "how_to_apply": "Through banks, CSCs, or insurance company agents. Online portal available",
        "documents_required": [
            "Aadhaar card",
            "Bank account details",
            "Land records",
            "Sowing certificate (if applicable)"
        ],
        "website": "https://pmfby.gov.in",
        "helpline": "011-23382012",
        "description": "Provides insurance coverage and financial support to farmers in case of crop failure."
    },
    {
        "id": 4,
        "name": "PM-KUSUM",
        "full_name": "Pradhan Mantri Kisan Urja Suraksha evam Utthaan Mahabhiyan",
        "type": "Central",
        "category": "Energy/Solar",
        "icon": "☀️",
        "benefits": "Subsidy for solar pumps (60% central + 30% state = 90% subsidy)",
        "eligibility": [
            "Individual farmers",
            "Farmer Producer Organizations (FPOs)",
            "Cooperatives"
        ],
        "how_to_apply": "Apply through state nodal agency or DISCOM website",
        "documents_required": [
            "Land ownership documents",
            "Aadhaar card",
            "Bank account details",
            "Electricity connection details"
        ],
        "website": "https://pmkusum.mnre.gov.in",
        "helpline": "State-specific helplines",
        "description": "Provides financial support for installation of solar pumps and grid-connected solar power plants."
    },
    {
        "id": 5,
        "name": "Soil Health Card Scheme",
        "full_name": "Soil Health Card Scheme",
        "type": "Central",
        "category": "Soil Testing",
        "icon": "🧪",
        "benefits": "Free soil testing and health card with fertilizer recommendations",
        "eligibility": [
            "All farmers"
        ],
        "how_to_apply": "Contact nearest Soil Testing Laboratory or Agriculture Department",
        "documents_required": [
            "Land ownership documents",
            "Aadhaar card"
        ],
        "website": "https://soilhealth.dac.gov.in",
        "helpline": "State Agriculture Department",
        "description": "Provides soil health cards to farmers every 2 years with nutrient status and fertilizer recommendations."
    },
    {
        "id": 6,
        "name": "PKVY",
        "full_name": "Paramparagat Krishi Vikas Yojana",
        "type": "Central",
        "category": "Organic Farming",
        "icon": "🌱",
        "benefits": "₹50,000 per hectare over 3 years for organic farming",
        "eligibility": [
            "Farmers willing to adopt organic farming",
            "Cluster approach (minimum 50 farmers)"
        ],
        "how_to_apply": "Through District Agriculture Officer or State Agriculture Department",
        "documents_required": [
            "Land records",
            "Aadhaar card",
            "Bank account details"
        ],
        "website": "Contact State Agriculture Department",
        "helpline": "State Agriculture Department",
        "description": "Promotes organic farming through cluster-based approach and provides financial assistance."
    },
    {
        "id": 7,
        "name": "PMKSY",
        "full_name": "Pradhan Mantri Krishi Sinchayee Yojana",
        "type": "Central",
        "category": "Irrigation",
        "icon": "💧",
        "benefits": "Subsidy for micro-irrigation systems (drip/sprinkler) - up to 55% for small farmers",
        "eligibility": [
            "All categories of farmers",
            "Higher subsidy for small & marginal farmers"
        ],
        "how_to_apply": "Through District Agriculture Office or online state portal",
        "documents_required": [
            "Land ownership documents",
            "Aadhaar card",
            "Bank account details",
            "Water source proof"
        ],
        "website": "https://pmksy.gov.in",
        "helpline": "State-specific helplines",
        "description": "Aims to expand cultivated area with assured irrigation, improve water use efficiency."
    },
    {
        "id": 8,
        "name": "National Mission for Sustainable Agriculture",
        "full_name": "National Mission for Sustainable Agriculture (NMSA)",
        "type": "Central",
        "category": "Sustainable Farming",
        "icon": "♻️",
        "benefits": "Financial assistance for soil health management, water conservation, and climate adaptation",
        "eligibility": [
            "All farmers",
            "Farmer groups and organizations"
        ],
        "how_to_apply": "Through State Agriculture Department",
        "documents_required": [
            "Land records",
            "Aadhaar card",
            "Project proposal (for groups)"
        ],
        "website": "Contact State Agriculture Department",
        "helpline": "State Agriculture Department",
        "description": "Promotes sustainable agriculture practices through various interventions."
    },
    {
        "id": 9,
        "name": "Sub-Mission on Agricultural Mechanization",
        "full_name": "Sub-Mission on Agricultural Mechanization (SMAM)",
        "type": "Central",
        "category": "Mechanization",
        "icon": "🚜",
        "benefits": "40-50% subsidy on agricultural machinery and equipment",
        "eligibility": [
            "Individual farmers",
            "Custom Hiring Centers",
            "FPOs and cooperatives"
        ],
        "how_to_apply": "Through District Agriculture Office or online portal",
        "documents_required": [
            "Aadhaar card",
            "Land ownership documents",
            "Bank account details",
            "Quotations from dealers"
        ],
        "website": "https://agrimachinery.nic.in",
        "helpline": "State Agriculture Department",
        "description": "Promotes farm mechanization to increase productivity and reduce drudgery."
    },
    {
        "id": 10,
        "name": "National Horticulture Mission",
        "full_name": "National Horticulture Mission (NHM)",
        "type": "Central",
        "category": "Horticulture",
        "icon": "🍎",
        "benefits": "Subsidy for protected cultivation, nursery, post-harvest management (40-50%)",
        "eligibility": [
            "Farmers growing horticultural crops",
            "Entrepreneurs",
            "FPOs"
        ],
        "how_to_apply": "Through District Horticulture Officer",
        "documents_required": [
            "Land documents",
            "Aadhaar card",
            "Bank account details",
            "Project report"
        ],
        "website": "Contact State Horticulture Department",
        "helpline": "State Horticulture Department",
        "description": "Promotes holistic growth of horticulture sector through area-based regionally differentiated strategies."
    },
    {
        "id": 11,
        "name": "Rashtriya Krishi Vikas Yojana",
        "full_name": "Rashtriya Krishi Vikas Yojana (RKVY)",
        "type": "Central",
        "category": "Agriculture Development",
        "icon": "📈",
        "benefits": "State-specific schemes for agriculture infrastructure and development",
        "eligibility": [
            "Varies by state and specific scheme"
        ],
        "how_to_apply": "Through State Agriculture Department",
        "documents_required": [
            "Varies by specific scheme"
        ],
        "website": "Contact State Agriculture Department",
        "helpline": "State Agriculture Department",
        "description": "Provides states flexibility to plan and execute agriculture development programs."
    },
    {
        "id": 12,
        "name": "National Food Security Mission",
        "full_name": "National Food Security Mission (NFSM)",
        "type": "Central",
        "category": "Food Security",
        "icon": "🌾",
        "benefits": "Support for increasing production of rice, wheat, pulses, and coarse cereals",
        "eligibility": [
            "Farmers in identified districts",
            "Focus on rice, wheat, pulses, coarse cereals"
        ],
        "how_to_apply": "Through District Agriculture Office",
        "documents_required": [
            "Land documents",
            "Aadhaar card"
        ],
        "website": "Contact State Agriculture Department",
        "helpline": "State Agriculture Department",
        "description": "Aims to increase production and productivity of targeted crops through area expansion and productivity enhancement."
    },
    {
        "id": 13,
        "name": "Interest Subvention Scheme",
        "full_name": "Interest Subvention Scheme for Short-term Crop Loans",
        "type": "Central",
        "category": "Credit/Loan",
        "icon": "💵",
        "benefits": "2% interest subvention + 3% prompt repayment incentive = Effective 4% interest on crop loans",
        "eligibility": [
            "Farmers availing crop loans up to ₹3 lakh",
            "Prompt repayment required for additional 3% benefit"
        ],
        "how_to_apply": "Automatic benefit when taking crop loan from banks",
        "documents_required": [
            "Same as crop loan requirements"
        ],
        "website": "Contact lending bank",
        "helpline": "Bank helpline",
        "description": "Provides interest subvention on short-term crop loans to make credit affordable."
    },
    {
        "id": 14,
        "name": "Kisan Maan Dhan Yojana",
        "full_name": "Pradhan Mantri Kisan Maan Dhan Yojana (PM-KMY)",
        "type": "Central",
        "category": "Pension",
        "icon": "👴",
        "benefits": "₹3,000 per month pension after 60 years of age",
        "eligibility": [
            "Small and marginal farmers (18-40 years)",
            "Landholding up to 2 hectares"
        ],
        "how_to_apply": "Through CSCs or online portal",
        "documents_required": [
            "Aadhaar card",
            "Bank account (with Aadhaar seeding)",
            "Land records"
        ],
        "website": "https://maandhan.in",
        "helpline": "1800-3000-3468",
        "description": "Old age pension scheme for small and marginal farmers."
    },
    {
        "id": 15,
        "name": "Modified Interest Subvention Scheme",
        "full_name": "Modified Interest Subvention Scheme for Animal Husbandry & Fisheries",
        "type": "Central",
        "category": "Animal Husbandry",
        "icon": "🐄",
        "benefits": "2% interest subvention on loans for dairy, poultry, fisheries",
        "eligibility": [
            "Farmers engaged in animal husbandry and fisheries",
            "Loans up to ₹2 lakh"
        ],
        "how_to_apply": "Through banks providing animal husbandry loans",
        "documents_required": [
            "Aadhaar card",
            "Bank account details",
            "Project report"
        ],
        "website": "Contact lending bank",
        "helpline": "Bank helpline",
        "description": "Provides interest subvention on loans for animal husbandry and fisheries activities."
    }
]


def get_all_schemes():
    """Return all government schemes"""
    return GOVERNMENT_SCHEMES


def get_scheme_by_id(scheme_id):
    """Get specific scheme by ID"""
    for scheme in GOVERNMENT_SCHEMES:
        if scheme["id"] == scheme_id:
            return scheme
    return None


def get_schemes_by_category(category):
    """Filter schemes by category"""
    return [s for s in GOVERNMENT_SCHEMES if s["category"] == category]


def get_schemes_by_type(scheme_type):
    """Filter schemes by type (Central/State)"""
    return [s for s in GOVERNMENT_SCHEMES if s["type"] == scheme_type]


def search_schemes(query):
    """Search schemes by name or description"""
    query = query.lower()
    results = []
    for scheme in GOVERNMENT_SCHEMES:
        if (query in scheme["name"].lower() or 
            query in scheme["full_name"].lower() or 
            query in scheme["description"].lower()):
            results.append(scheme)
    return results


def get_categories():
    """Get all unique categories"""
    return list(set(s["category"] for s in GOVERNMENT_SCHEMES))
