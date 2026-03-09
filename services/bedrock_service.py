import json
import os
import requests
from typing import Dict, List

class BedrockService:
    def __init__(self):
        # Use free AI alternatives
        self.use_free_ai = True
        self.groq_api_key = os.getenv('GROQ_API_KEY', '')  # Free Groq API
        self.groq_url = 'https://api.groq.com/openai/v1/chat/completions'
        self.model = 'llama3-8b-8192'  # Free Llama 3 model
    
    def analyze_document(self, file, additional_text: str = '') -> Dict:
        """Analyze medical document using AI"""
        # Read file content
        file_content = file.read()
        file.seek(0)  # Reset file pointer
        
        prompt = f"""Analyze this medical document and extract:
1. Primary diagnosis or medical condition
2. Recommended medical procedures or tests
3. Severity level (mild/moderate/severe)
4. Urgency (routine/urgent/emergency)

Additional context: {additional_text}

Provide response in JSON format:
{{
    "diagnosis": "condition name",
    "procedures": ["procedure1", "procedure2"],
    "severity": "level",
    "urgency": "level",
    "summary": "brief summary"
}}"""
        
        return self._invoke_bedrock(prompt)
    
    def analyze_text(self, problem_text: str) -> Dict:
        """Analyze medical problem description"""
        prompt = f"""Based on this medical problem description, identify:
1. Likely medical condition or diagnosis
2. Recommended medical tests or procedures
3. Severity level
4. Urgency level

Problem: {problem_text}

Provide response in JSON format:
{{
    "diagnosis": "condition name",
    "procedures": ["procedure1", "procedure2"],
    "severity": "level",
    "urgency": "level",
    "summary": "brief summary"
}}"""
        
        return self._invoke_bedrock(prompt)
    
    def check_scheme_eligibility(self, medical_info: Dict) -> Dict:
        """Check eligibility for government healthcare schemes"""
        prompt = f"""Based on this medical condition, determine eligibility for Indian government healthcare schemes:

Diagnosis: {medical_info.get('diagnosis')}
Procedures: {', '.join(medical_info.get('procedures', []))}
Severity: {medical_info.get('severity')}

Check eligibility for:
1. Ayushman Bharat (PM-JAY)
2. State government schemes
3. Other applicable schemes

Provide response in JSON format:
{{
    "ayushman_bharat": {{"eligible": true/false, "coverage": "details"}},
    "state_schemes": [{{"name": "scheme", "eligible": true/false}}],
    "recommendations": "guidance text"
}}"""
        
        return self._invoke_bedrock(prompt)
    
    def _invoke_bedrock(self, prompt: str) -> Dict:
        """Invoke Free AI API (Groq)"""
        try:
            if self.groq_api_key:
                # Use Groq API (Free)
                headers = {
                    'Authorization': f'Bearer {self.groq_api_key}',
                    'Content-Type': 'application/json'
                }
                
                payload = {
                    'model': self.model,
                    'messages': [
                        {
                            'role': 'system',
                            'content': 'You are a medical AI assistant. Always respond with valid JSON.'
                        },
                        {
                            'role': 'user',
                            'content': prompt
                        }
                    ],
                    'temperature': 0.7,
                    'max_tokens': 2000
                }
                
                response = requests.post(self.groq_url, headers=headers, json=payload, timeout=30)
                
                if response.status_code == 200:
                    data = response.json()
                    content = data['choices'][0]['message']['content']
                    
                    # Extract JSON from response
                    start = content.find('{')
                    end = content.rfind('}') + 1
                    if start != -1 and end > start:
                        return json.loads(content[start:end])
                    
                    return json.loads(content)
            
            # Fallback to mock data
            return self._get_mock_response(prompt)
        
        except Exception as e:
            print(f"AI API error: {e}")
            # Return mock data for development
            return self._get_mock_response(prompt)
    
    def _get_mock_response(self, prompt: str) -> Dict:
        """Mock response for development without AWS credentials"""
        if "scheme" in prompt.lower():
            return {
                "ayushman_bharat": {
                    "eligible": True,
                    "coverage": "Up to ₹5 lakh per family per year"
                },
                "state_schemes": [
                    {"name": "State Health Insurance", "eligible": True}
                ],
                "recommendations": "Apply for Ayushman Bharat card at nearest health center"
            }
        else:
            return {
                "diagnosis": "General Health Checkup Required",
                "procedures": ["Blood Test", "X-Ray", "ECG"],
                "severity": "moderate",
                "urgency": "routine",
                "summary": "Routine medical examination recommended"
            }
