import joblib
import os
from flask import Flask, render_template, request, flash, redirect, url_for, session
from models import User, bcrypt

from flask_login import LoginManager, login_required

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'  # Change this in production!

# Initialize Bcrypt
bcrypt.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# Register Auth Blueprint
from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# For debugging production crashes - remove before final delivery
@app.errorhandler(500)
@app.errorhandler(Exception)
def handle_exception(e):
    import traceback
    return f"<h1>Runtime Error</h1><pre>{traceback.format_exc()}</pre>", 500

@app.before_request
def track_user_session():
    """Track unique visits using session"""
    if 'visited' not in session:
        from analytics import track_visit
        track_visit()
        session['visited'] = True


@app.route('/')
def index():
    from analytics import track_page_view
    track_page_view('Home')
    return render_template('index.html')


@app.route('/news')
def news():
    from analytics import track_page_view
    track_page_view('News')
    return render_template('news.html')


@app.route('/crop_prediction')
def crop_prediction():
    from analytics import track_page_view
    track_page_view('Crop Prediction')
    return render_template('form.html')


@app.route('/about')
def about():
    from analytics import track_page_view
    track_page_view('About Us')
    return render_template('about.html')


@app.route('/crop-calendar')
def crop_calendar():
    from crop_data import CROP_CALENDAR, get_current_season
    from analytics import track_page_view
    track_page_view('Crop Calendar')
    import datetime
    current_month = datetime.datetime.now().strftime("%B")
    current_season = get_current_season(current_month)
    return render_template('crop_calendar.html', 
                         calendar=CROP_CALENDAR, 
                         current_month=current_month,
                         current_season=current_season)


@app.route('/crop-care')
def crop_care():
    from crop_data import CROP_CARE
    from analytics import track_page_view
    track_page_view('Crop Care')
    crops = list(CROP_CARE.keys())
    return render_template('crop_care.html', crops=crops, care_data=CROP_CARE)


@app.route('/crop-care/<crop_name>')
def crop_care_detail(crop_name):
    from crop_data import CROP_CARE
    crop_data = CROP_CARE.get(crop_name.capitalize())
    if not crop_data:
        flash(f'Crop "{crop_name}" not found in our database.', 'error')
        return redirect(url_for('crop_care'))
    return render_template('crop_care_detail.html', 
                         crop=crop_name.capitalize(), 
                         care=crop_data)


@app.route('/form', methods=["POST"])
def brain():
    from analytics import track_feature, track_crop_search
    track_feature('Crop Prediction')
    try:
        # Get form data and convert to float
        nitrogen = float(request.form['Nitrogen'])
        phosphorus = float(request.form['Phosphorus'])
        potassium = float(request.form['Potassium'])
        temperature = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['PH'])
        rainfall = float(request.form['Rainfall'])

        # Validate input ranges
        if not (0 < ph <= 14):
            flash('PH value must be between 0 and 14', 'error')
            return redirect(url_for('crop_prediction'))
        
        if not (temperature < 100):
            flash('Temperature must be less than 100°C', 'error')
            return redirect(url_for('crop_prediction'))
        
        if not (humidity > 0):
            flash('Humidity must be greater than 0%', 'error')
            return redirect(url_for('crop_prediction'))

        # Prepare input for model
        value = [nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]

        # Load model and make prediction
        if not os.path.exists('crop_recommend'):
            flash('Model file not found. Please contact administrator.', 'error')
            return redirect(url_for('crop_prediction'))
        
        model = joblib.load('crop_recommend')
        arr = [value]
        prediction = model.predict(arr)
        
        # Clean up prediction output - remove brackets and quotes
        crop_name = str(prediction[0]) if len(prediction) > 0 else "Unknown"
        track_crop_search(crop_name)
        
        # Store input values to display on result page
        input_data = {
            'nitrogen': nitrogen,
            'phosphorus': phosphorus,
            'potassium': potassium,
            'temperature': temperature,
            'humidity': humidity,
            'ph': ph,
            'rainfall': rainfall
        }
        
        return render_template('predict.html', prediction=crop_name, input_data=input_data)
    
    except ValueError as e:
        flash('Invalid input values. Please enter valid numbers.', 'error')
        return redirect(url_for('crop_prediction'))
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('crop_prediction'))


@app.route('/contact', methods=["POST"])
def contact():
    """Handle contact/donation form submissions"""
    try:
        name = request.form.get('Name', '')
        email = request.form.get('e-mail', '')
        phone = request.form.get('telephone', '')
        message = request.form.get('textbox', '')
        amount = request.form.get('amount', '0')
        
        # In a real application, you would save this to a database or send an email
        # For now, just show a success message
        flash(f'Thank you {name}! Your message has been received.', 'success')
        return redirect(url_for('index'))
    except Exception as e:
        flash('Failed to submit form. Please try again.', 'error')
        return redirect(url_for('index'))




# Fertilizer Calculator Routes
@app.route('/fertilizer-calculator')
def fertilizer_calculator():
    from fertilizer_calculator import CROP_REQUIREMENTS
    from analytics import track_page_view
    track_page_view('Fertilizer Calculator')
    crops = list(CROP_REQUIREMENTS.keys())
    return render_template('fertilizer_calculator.html', crops=crops)


@app.route('/calculate-fertilizer', methods=['POST'])
def calculate_fertilizer_route():
    from fertilizer_calculator import calculate_fertilizer, get_fertilizer_tips
    from analytics import track_feature, track_fertilizer_calc
    
    track_feature('Fertilizer Calculator')
    
    crop = request.form.get('crop')
    soil_n = float(request.form.get('soil_n', 0))
    soil_p = float(request.form.get('soil_p', 0))
    soil_k = float(request.form.get('soil_k', 0))
    area = float(request.form.get('area', 1))
    
    result = calculate_fertilizer(crop, soil_n, soil_p, soil_k, area)
    tips = get_fertilizer_tips(crop)
    track_fertilizer_calc(crop)
    
    return render_template('fertilizer_result.html', 
                         result=result, 
                         tips=tips,
                         crop=crop)


# Government Schemes Routes
@app.route('/government-schemes')
def government_schemes():
    from government_schemes import get_all_schemes, get_categories
    from analytics import track_page_view
    track_page_view('Government Schemes')
    schemes = get_all_schemes()
    categories = get_categories()
    return render_template('government_schemes.html', 
                         schemes=schemes,
                         categories=categories)


@app.route('/scheme/<int:scheme_id>')
def scheme_detail(scheme_id):
    from government_schemes import get_scheme_by_id
    from analytics import track_scheme_view
    scheme = get_scheme_by_id(scheme_id)
    if scheme:
        track_scheme_view(scheme['name'])
    if not scheme:
        flash('Scheme not found', 'error')
        return redirect(url_for('government_schemes'))
    return render_template('scheme_detail.html', scheme=scheme)


@app.route('/analytics')
@login_required
def analytics_dashboard():
    """Analytics dashboard showing usage statistics"""
    from analytics import get_analytics_summary
    summary = get_analytics_summary()
    return render_template('analytics.html', summary=summary)


# Weather Forecast Routes
@app.route('/weather')
def weather():
    from weather_service import get_current_weather, get_forecast, get_weather_recommendations, INDIAN_CITIES
    from analytics import track_page_view
    track_page_view('Weather')
    
    city = request.args.get('city', '')
    custom_city = request.args.get('custom_city', '')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    # Use custom city if provided, otherwise use selected city
    selected_city = custom_city if custom_city else city
    
    current = None
    forecast = None
    recommendations = None
    
    if lat and lon:
        # Get weather by coordinates
        try:
            current = get_current_weather(lat=float(lat), lon=float(lon))
            if current.get('success'):
                selected_city = current.get('city')
                # Track weather query by coordinates
                from analytics import track_weather_query
                track_weather_query(f"{selected_city} (GPS)")
        except ValueError:
            current = {'success': False, 'error': 'Invalid coordinates'}
            
    elif selected_city:
        # Get weather by city name
        current = get_current_weather(selected_city)
        if current.get('success'):
            # Track weather query by city
            from analytics import track_weather_query
            track_weather_query(selected_city)

    if current and current.get('success'):
        # Get forecast (using lat/lon if available, otherwise city)
        if lat and lon:
            forecast = get_forecast(lat=float(lat), lon=float(lon), days=7)
        else:
            forecast = get_forecast(selected_city, days=7)
            
        # Get recommendations
        recommendations = get_weather_recommendations(current)
        
        return render_template('weather.html',
                             cities=INDIAN_CITIES,
                             city=selected_city,
                             custom_city=custom_city,
                             current=current,
                             forecast=forecast if forecast.get('success') else None,
                             recommendations=recommendations)
    else:
        # Error or no location selected
        return render_template('weather.html',
                             cities=INDIAN_CITIES,
                             city=selected_city,
                             custom_city=custom_city,
                             error=current.get('error') if current else None)


# Crop Rotation Planner Routes
@app.route('/crop-rotation')
def crop_rotation():
    from crop_rotation import ROTATION_PLANS
    from analytics import track_page_view
    track_page_view('Crop Rotation')
    crops = list(ROTATION_PLANS.keys())
    return render_template('crop_rotation.html', crops=crops)


@app.route('/rotation-suggestions', methods=['POST'])
def rotation_suggestions():
    from crop_rotation import get_rotation_suggestions, get_three_year_plans, get_rotation_principles
    from analytics import track_feature, track_rotation_query
    
    track_feature('Crop Rotation')
    
    current_crop = request.form.get('crop')
    track_rotation_query(current_crop)
    suggestions = get_rotation_suggestions(current_crop)
    three_year_plans = get_three_year_plans()
    principles = get_rotation_principles()
    
    return render_template('rotation_result.html',
                         current_crop=current_crop,
                         suggestions=suggestions,
                         three_year_plans=three_year_plans,
                         principles=principles)


# Error handlers

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)

