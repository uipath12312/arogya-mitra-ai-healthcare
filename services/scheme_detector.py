import json
import os

class SchemeDetector:
    def __init__(self):
        self.schemes_data = self._load_schemes()
    
    def check_eligibility(self, diagnosis_info, patient_info):
        """Check eligibility for government healthcare schemes"""
        eligible_schemes = []
        
        for scheme in self.schemes_data:
            if self._is_eligible(scheme, diagnosis_info, patient_info):
                eligible_schemes.append(scheme)
        
        return eligible_schemes
    
    def _load_schemes(self):
        """Load government schemes data"""
        schemes = [
            {
                'name': 'Ayushman Bharat (PM-JAY)',
                'coverage': 500000,
                'eligibility': {
                    'income_limit': 'BPL or lower middle class',
                    'age_limit': None
                },
                'benefits': 'Free treatment up to ₹5 lakh per family per year'
            },
            {
                'name': 'State Health Insurance',
                'coverage': 200000,
                'eligibility': {
                    'income_limit': 'Below ₹3 lakh annual income',
                    'age_limit': None
                },
                'benefits': 'Cashless treatment at empaneled hospitals'
            },
            {
                'name': 'PM Jan Arogya Yojana',
                'coverage': 500000,
                'eligibility': {
                    'income_limit': 'SECC database beneficiaries',
                    'age_limit': None
                },
                'benefits': 'Secondary and tertiary care hospitalization'
            }
        ]
        return schemes
    
    def _is_eligible(self, scheme, diagnosis_info, patient_info):
        """Check if patient is eligible for a scheme"""
        # Simplified eligibility check for prototype
        # In production, would check against actual criteria
        return True  # For demo purposes
