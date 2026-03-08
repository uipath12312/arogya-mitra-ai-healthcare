import boto3
import os
from decimal import Decimal

class HospitalComparator:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb', region_name=os.getenv('AWS_REGION', 'ap-south-1'))
        self.table_name = os.getenv('DYNAMODB_TABLE_NAME', 'arogya-mitra-hospitals')
        
    def compare_hospitals(self, diagnosis_info):
        """Compare hospitals based on treatment cost and success rate"""
        diagnosis = diagnosis_info.get('diagnosis', '')
        
        # Query DynamoDB for hospitals
        hospitals = self._get_hospitals_for_treatment(diagnosis)
        
        # Sort by cost and success rate
        ranked_hospitals = self._rank_hospitals(hospitals)
        
        return ranked_hospitals
    
    def _get_hospitals_for_treatment(self, diagnosis):
        """Fetch hospitals from DynamoDB"""
        # Prototype data
        return [
            {
                'name': 'AIIMS Delhi',
                'estimated_cost': 15000,
                'success_rate': 92,
                'patient_reviews': 4.5,
                'location': 'Delhi',
                'type': 'Government'
            },
            {
                'name': 'Apollo Hospital',
                'estimated_cost': 45000,
                'success_rate': 95,
                'patient_reviews': 4.7,
                'location': 'Delhi',
                'type': 'Private'
            },
            {
                'name': 'Safdarjung Hospital',
                'estimated_cost': 8000,
                'success_rate': 88,
                'patient_reviews': 4.2,
                'location': 'Delhi',
                'type': 'Government'
            }
        ]
    
    def _rank_hospitals(self, hospitals):
        """Rank hospitals by affordability and quality"""
        for hospital in hospitals:
            # Calculate score (lower cost + higher success rate = better)
            cost_score = 100 - (hospital['estimated_cost'] / 1000)
            quality_score = hospital['success_rate']
            hospital['overall_score'] = (cost_score + quality_score) / 2
        
        return sorted(hospitals, key=lambda h: h['overall_score'], reverse=True)
