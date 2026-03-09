import os
import json
from typing import List, Dict

class HospitalService:
    def __init__(self):
        # Use JSON file storage instead of DynamoDB
        self.data_file = os.path.join(os.getcwd(), 'data', 'hospitals.json')
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        self._initialize_data()
    
    def _initialize_data(self):
        """Initialize hospital data if not exists"""
        if not os.path.exists(self.data_file):
            initial_data = {
                "cities": [
                    "Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata",
                    "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Lucknow"
                ],
                "hospitals": self._generate_hospital_data()
            }
            with open(self.data_file, 'w') as f:
                json.dump(initial_data, f, indent=2)
    
    def _generate_hospital_data(self) -> List[Dict]:
        """Generate initial hospital data"""
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
            
            # Apollo Hospital
            hospitals.append({
                'hospital_id': f'H{hospital_id:04d}',
                'name': f'Apollo Hospital {city}',
                'city': city,
                'type': 'private',
                'rating': 4.5,
                'success_rate': 92,
                'address': f'Main Road, {city}',
                'phone': f'+91-{1234567890 + hospital_id}',
                'specialties': ['Cardiology', 'Neurology', 'Orthopedics'],
                'government_schemes': True,
                'procedures': {
                    'Blood Test': 750,
                    'X-Ray': 1200,
                    'ECG': 900,
                    'MRI': 7500,
                    'CT Scan': 6000,
                    'Ultrasound': 1800,
                    'Consultation': 1200
                }
            })
            hospital_id += 1
            
            # Fortis Healthcare
            hospitals.append({
                'hospital_id': f'H{hospital_id:04d}',
                'name': f'Fortis Healthcare {city}',
                'city': city,
                'type': 'private',
                'rating': 4.3,
                'success_rate': 89,
                'address': f'Central Avenue, {city}',
                'phone': f'+91-{1234567890 + hospital_id}',
                'specialties': ['General Medicine', 'Surgery', 'Pediatrics'],
                'government_schemes': True,
                'procedures': {
                    'Blood Test': 500,
                    'X-Ray': 800,
                    'ECG': 600,
                    'MRI': 5000,
                    'CT Scan': 4000,
                    'Ultrasound': 1200,
                    'Consultation': 800
                }
            })
            hospital_id += 1
            
            # Max Hospital
            hospitals.append({
                'hospital_id': f'H{hospital_id:04d}',
                'name': f'Max Hospital {city}',
                'city': city,
                'type': 'private',
                'rating': 4.4,
                'success_rate': 90,
                'address': f'Park Street, {city}',
                'phone': f'+91-{1234567890 + hospital_id}',
                'specialties': ['Oncology', 'Cardiology', 'Gastroenterology'],
                'government_schemes': False,
                'procedures': {
                    'Blood Test': 600,
                    'X-Ray': 1000,
                    'ECG': 700,
                    'MRI': 6000,
                    'CT Scan': 5000,
                    'Ultrasound': 1500,
                    'Consultation': 1000
                }
            })
            hospital_id += 1
        
        return hospitals
    
    def get_cities(self) -> List[str]:
        """Get list of available cities"""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                return data.get('cities', [])
        except:
            return [
                "Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata",
                "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Lucknow"
            ]
    
    def get_recommendations(self, diagnosis: str, procedures: List[str], city: str) -> List[Dict]:
        """Get hospital recommendations based on diagnosis and city"""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                hospitals = data.get('hospitals', [])
            
            # Filter by city
            city_hospitals = [h for h in hospitals if h['city'] == city]
            
            # Add procedure costs
            for hospital in city_hospitals:
                hospital['procedures_list'] = []
                for proc in procedures:
                    cost = hospital['procedures'].get(proc, 1000)
                    hospital['procedures_list'].append({
                        "name": proc,
                        "cost": cost,
                        "estimated_duration": "1-2 days"
                    })
                
                # Calculate total cost
                hospital['total_cost'] = sum(p['cost'] for p in hospital['procedures_list'])
            
            # Sort by cost (cheapest first)
            city_hospitals.sort(key=lambda x: x['total_cost'])
            
            return city_hospitals
        
        except Exception as e:
            print(f"Error getting recommendations: {e}")
            return []
