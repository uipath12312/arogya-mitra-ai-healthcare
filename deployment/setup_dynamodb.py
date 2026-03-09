import boto3
import json
from decimal import Decimal

def setup_hospitals_data():
    """Populate DynamoDB with sample hospital data"""
    
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('hospitals')
    
    cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata"]
    
    hospitals_data = []
    hospital_id = 1
    
    for city in cities:
        # Government Hospital
        hospitals_data.append({
            'hospital_id': f'H{hospital_id:04d}',
            'name': f'{city} Government Hospital',
            'city': city,
            'type': 'government',
            'rating': Decimal('3.8'),
            'success_rate': Decimal('85'),
            'address': f'Government Complex, {city}',
            'phone': f'+91-{1234567890 + hospital_id}',
            'specialties': ['General Medicine', 'Emergency', 'Surgery'],
            'government_schemes': True,
            'procedures': {
                'Blood Test': Decimal('150'),
                'X-Ray': Decimal('240'),
                'ECG': Decimal('180'),
                'MRI': Decimal('1500'),
                'CT Scan': Decimal('1200'),
                'Ultrasound': Decimal('360'),
                'Consultation': Decimal('240')
            }
        })
        hospital_id += 1
        
        # Apollo Hospital
        hospitals_data.append({
            'hospital_id': f'H{hospital_id:04d}',
            'name': f'Apollo Hospital {city}',
            'city': city,
            'type': 'private',
            'rating': Decimal('4.5'),
            'success_rate': Decimal('92'),
            'address': f'Main Road, {city}',
            'phone': f'+91-{1234567890 + hospital_id}',
            'specialties': ['Cardiology', 'Neurology', 'Orthopedics'],
            'government_schemes': True,
            'procedures': {
                'Blood Test': Decimal('750'),
                'X-Ray': Decimal('1200'),
                'ECG': Decimal('900'),
                'MRI': Decimal('7500'),
                'CT Scan': Decimal('6000'),
                'Ultrasound': Decimal('1800'),
                'Consultation': Decimal('1200')
            }
        })
        hospital_id += 1
        
        # Fortis Healthcare
        hospitals_data.append({
            'hospital_id': f'H{hospital_id:04d}',
            'name': f'Fortis Healthcare {city}',
            'city': city,
            'type': 'private',
            'rating': Decimal('4.3'),
            'success_rate': Decimal('89'),
            'address': f'Central Avenue, {city}',
            'phone': f'+91-{1234567890 + hospital_id}',
            'specialties': ['General Medicine', 'Surgery', 'Pediatrics'],
            'government_schemes': True,
            'procedures': {
                'Blood Test': Decimal('500'),
                'X-Ray': Decimal('800'),
                'ECG': Decimal('600'),
                'MRI': Decimal('5000'),
                'CT Scan': Decimal('4000'),
                'Ultrasound': Decimal('1200'),
                'Consultation': Decimal('800')
            }
        })
        hospital_id += 1
    
    # Batch write to DynamoDB
    with table.batch_writer() as batch:
        for hospital in hospitals_data:
            batch.put_item(Item=hospital)
    
    print(f"Successfully added {len(hospitals_data)} hospitals to DynamoDB")

if __name__ == '__main__':
    setup_hospitals_data()
