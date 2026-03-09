from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from services.bedrock_service import BedrockService
from services.hospital_service import HospitalService
from services.s3_service import S3Service

load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Initialize services
bedrock_service = BedrockService()
hospital_service = HospitalService()
s3_service = S3Service()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/cities', methods=['GET'])
def get_cities():
    """Get list of available cities"""
    cities = hospital_service.get_cities()
    return jsonify({'cities': cities})

@app.route('/api/analyze', methods=['POST'])
def analyze_document():
    """Analyze medical document and get recommendations"""
    try:
        # Get form data
        city = request.form.get('city')
        problem_text = request.form.get('problem_text', '')
        file = request.files.get('document')
        
        if not city:
            return jsonify({'error': 'City is required'}), 400
        
        # Extract medical information
        if file:
            # Upload to S3 and analyze
            file_url = s3_service.upload_file(file)
            medical_info = bedrock_service.analyze_document(file, problem_text)
        elif problem_text:
            medical_info = bedrock_service.analyze_text(problem_text)
        else:
            return jsonify({'error': 'Please provide medical document or problem description'}), 400
        
        # Get hospital recommendations
        recommendations = hospital_service.get_recommendations(
            diagnosis=medical_info['diagnosis'],
            procedures=medical_info['procedures'],
            city=city
        )
        
        # Check government scheme eligibility
        scheme_eligibility = bedrock_service.check_scheme_eligibility(medical_info)
        
        return jsonify({
            'medical_info': medical_info,
            'recommendations': recommendations,
            'scheme_eligibility': scheme_eligibility
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
