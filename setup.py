#!/usr/bin/env python3
"""
AROGYA-MITRA Setup Script
Initializes the application with sample data
"""

import os
import json

def create_directories():
    """Create necessary directories"""
    directories = ['data', 'uploads', 'logs']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ Created directory: {directory}")

def initialize_hospital_data():
    """Initialize hospital database"""
    data_file = os.path.join('data', 'hospitals.json')
    
    if os.path.exists(data_file):
        print(f"✓ Hospital data already exists: {data_file}")
        return
    
    cities = [
        "Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata",
        "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Lucknow"
    ]
    
    hospitals = []
    hospital_id = 1
    
    for city in cities:
        # Government Hospital
        hospitals.append({
            'hospital_id': f'H{hospital_id:04d}',
            'name': f'{city} Government Hospital',
            'city': city,
            'type': 'government',
            'rating': 3.8,
            'success_rate': 85,
            'address': f'Government Complex, {city}',
            'phone': f'+91-{1234567890 + hospital_id}',
            'specialties': ['General Medicine', 'Emergency', 'Surgery'],
            'government_schemes': True,
            'procedures': {
                'Blood Test': 150,
                'X-Ray': 240,
                'ECG': 180,
                'MRI': 1500,
                'CT Scan': 1200,
                'Ultrasound': 360,
                'Consultation': 240
            }
        })
        hospital_id += 1
        
        # Private Hospitals
        for hospital_name, rating, success_rate, specialties, cost_multiplier in [
            ('Apollo Hospital', 4.5, 92, ['Cardiology', 'Neurology', 'Orthopedics'], 5.0),
            ('Fortis Healthcare', 4.3, 89, ['General Medicine', 'Surgery', 'Pediatrics'], 3.3),
            ('Max Hospital', 4.4, 90, ['Oncology', 'Cardiology', 'Gastroenterology'], 4.0)
        ]:
            hospitals.append({
                'hospital_id': f'H{hospital_id:04d}',
                'name': f'{hospital_name} {city}',
                'city': city,
                'type': 'private',
                'rating': rating,
                'success_rate': success_rate,
                'address': f'Main Road, {city}',
                'phone': f'+91-{1234567890 + hospital_id}',
                'specialties': specialties,
                'government_schemes': hospital_name != 'Max Hospital',
                'procedures': {
                    'Blood Test': int(150 * cost_multiplier),
                    'X-Ray': int(240 * cost_multiplier),
                    'ECG': int(180 * cost_multiplier),
                    'MRI': int(1500 * cost_multiplier),
                    'CT Scan': int(1200 * cost_multiplier),
                    'Ultrasound': int(360 * cost_multiplier),
                    'Consultation': int(240 * cost_multiplier)
                }
            })
            hospital_id += 1
    
    data = {
        'cities': cities,
        'hospitals': hospitals
    }
    
    with open(data_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✓ Created hospital database: {data_file}")
    print(f"  - {len(cities)} cities")
    print(f"  - {len(hospitals)} hospitals")

def create_env_file():
    """Create .env file if not exists"""
    if os.path.exists('.env'):
        print("✓ .env file already exists")
        return
    
    env_content = """# Free AI API Keys (Optional - works without them using mock data)
GROQ_API_KEY=
# Get free API key from: https://console.groq.com/

# Alternative Free AI APIs (Optional)
HUGGINGFACE_API_KEY=
# Get free API key from: https://huggingface.co/settings/tokens
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("✓ Created .env file")

def main():
    print("=" * 60)
    print("AROGYA-MITRA Setup")
    print("=" * 60)
    print()
    
    print("Setting up application...")
    print()
    
    create_directories()
    initialize_hospital_data()
    create_env_file()
    
    print()
    print("=" * 60)
    print("Setup Complete! ✓")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Run: python app.py")
    print("2. Visit: http://localhost:5000")
    print("3. (Optional) Add GROQ_API_KEY to .env for real AI")
    print()
    print("For deployment: See DEPLOYMENT.md")
    print("For GitHub setup: See GITHUB_SETUP.md")
    print()

if __name__ == '__main__':
    main()
