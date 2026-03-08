from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from services.document_analyzer import DocumentAnalyzer
from services.hospital_comparator import HospitalComparator
from services.scheme_detector import SchemeDetector

load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Initialize services
doc_analyzer = DocumentAnalyzer()
hospital_comparator = HospitalComparator()
scheme_detector = SchemeDetector()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze_document():
    if 'document' not in request.files:
        return jsonify({'error': 'No document uploaded'}), 400
    
    file = request.files['document']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    try:
        # Extract diagnosis from document
        diagnosis = doc_analyzer.extract_diagnosis(file)
        
        # Get hospital comparisons
        hospitals = hospital_comparator.compare_hospitals(diagnosis)
        
        # Check scheme eligibility
        schemes = scheme_detector.check_eligibility(diagnosis, request.form)
        
        return jsonify({
            'diagnosis': diagnosis,
            'hospitals': hospitals,
            'eligible_schemes': schemes,
            'recommendations': generate_recommendations(diagnosis, hospitals, schemes)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def generate_recommendations(diagnosis, hospitals, schemes):
    recommendations = []
    
    if schemes:
        recommendations.append({
            'type': 'scheme',
            'message': f'You are eligible for {len(schemes)} government schemes'
        })
    
    if hospitals:
        best_hospital = min(hospitals, key=lambda h: h['estimated_cost'])
        recommendations.append({
            'type': 'hospital',
            'message': f'Most affordable: {best_hospital["name"]} - ₹{best_hospital["estimated_cost"]}'
        })
    
    return recommendations

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
