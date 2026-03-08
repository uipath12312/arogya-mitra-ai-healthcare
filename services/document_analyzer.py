import boto3
import json
import os
from PyPDF2 import PdfReader
from io import BytesIO

class DocumentAnalyzer:
    def __init__(self):
        self.bedrock = boto3.client('bedrock-runtime', region_name=os.getenv('AWS_REGION', 'ap-south-1'))
        self.s3 = boto3.client('s3')
        
    def extract_diagnosis(self, file):
        """Extract diagnosis and treatment info from medical document"""
        # Read document content
        content = self._read_document(file)
        
        # Use Amazon Bedrock for AI analysis
        diagnosis_info = self._analyze_with_bedrock(content)
        
        return diagnosis_info
    
    def _read_document(self, file):
        """Read PDF or image document"""
        if file.filename.endswith('.pdf'):
            pdf_reader = PdfReader(BytesIO(file.read()))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        else:
            # For images, would use OCR (Textract)
            return "Image processing not implemented in prototype"
    
    def _analyze_with_bedrock(self, content):
        """Use Amazon Bedrock to extract medical information"""
        prompt = f"""Analyze this medical document and extract:
1. Primary diagnosis
2. Recommended treatment
3. Severity level
4. Estimated treatment duration

Document content:
{content[:2000]}

Respond in JSON format."""
        
        try:
            response = self.bedrock.invoke_model(
                modelId='anthropic.claude-v2',
                body=json.dumps({
                    'prompt': f'\n\nHuman: {prompt}\n\nAssistant:',
                    'max_tokens_to_sample': 500
                })
            )
            
            result = json.loads(response['body'].read())
            return json.loads(result.get('completion', '{}'))
        except:
            # Fallback for prototype/testing
            return {
                'diagnosis': 'Sample Diagnosis',
                'treatment': 'Sample Treatment',
                'severity': 'moderate',
                'duration': '2-3 weeks'
            }
