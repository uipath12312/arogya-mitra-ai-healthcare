import json
import boto3
import base64
from services.document_analyzer import DocumentAnalyzer
from services.hospital_comparator import HospitalComparator
from services.scheme_detector import SchemeDetector

# Initialize services
doc_analyzer = DocumentAnalyzer()
hospital_comparator = HospitalComparator()
scheme_detector = SchemeDetector()

def lambda_handler(event, context):
    """AWS Lambda handler for document analysis"""
    
    try:
        # Parse request
        body = json.loads(event.get('body', '{}'))
        
        # Get document from S3 or base64
        if 'document_s3_key' in body:
            document = get_document_from_s3(body['document_s3_key'])
        elif 'document_base64' in body:
            document = base64.b64decode(body['document_base64'])
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No document provided'})
            }
        
        # Analyze document
        diagnosis = doc_analyzer.extract_diagnosis(document)
        
        # Get hospital comparisons
        hospitals = hospital_comparator.compare_hospitals(diagnosis)
        
        # Check scheme eligibility
        patient_info = body.get('patient_info', {})
        schemes = scheme_detector.check_eligibility(diagnosis, patient_info)
        
        # Generate recommendations
        recommendations = generate_recommendations(diagnosis, hospitals, schemes)
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'diagnosis': diagnosis,
                'hospitals': hospitals,
                'eligible_schemes': schemes,
                'recommendations': recommendations
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def get_document_from_s3(s3_key):
    """Retrieve document from S3"""
    s3 = boto3.client('s3')
    bucket = os.getenv('S3_BUCKET_NAME')
    response = s3.get_object(Bucket=bucket, Key=s3_key)
    return response['Body'].read()

def generate_recommendations(diagnosis, hospitals, schemes):
    """Generate treatment recommendations"""
    recommendations = []
    
    if schemes:
        recommendations.append({
            'type': 'scheme',
            'priority': 'high',
            'message': f'You qualify for {len(schemes)} government healthcare schemes'
        })
    
    if hospitals:
        best_hospital = min(hospitals, key=lambda h: h['estimated_cost'])
        recommendations.append({
            'type': 'hospital',
            'priority': 'high',
            'message': f'Most affordable option: {best_hospital["name"]} at ₹{best_hospital["estimated_cost"]}'
        })
    
    return recommendations
