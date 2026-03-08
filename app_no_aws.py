from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import hashlib

load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

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
        # Get patient info
        age = request.form.get('age', '35')
        income = request.form.get('income', '200000')
        state = request.form.get('state', 'delhi')
        
        # Mock analysis based on file type for realistic demo
        file_ext = file.filename.split('.')[-1].lower()
        
        # Simulate different diagnoses based on demo scenarios
        diagnoses_pool = [
            {
                'diagnosis': 'Type 2 Diabetes Mellitus',
                'treatment': 'Insulin therapy, dietary management, regular monitoring',
                'severity': 'Moderate',
                'duration': '3-6 months initial treatment',
                'estimated_base_cost': 12000
            },
            {
                'diagnosis': 'Coronary Artery Disease',
                'treatment': 'Angioplasty with stent placement',
                'severity': 'High',
                'duration': '1-2 weeks hospitalization',
                'estimated_base_cost': 150000
            },
            {
                'diagnosis': 'Hypertension (High Blood Pressure)',
                'treatment': 'Antihypertensive medication, lifestyle modification',
                'severity': 'Moderate',
                'duration': '2-3 months',
                'estimated_base_cost': 5000
            },
            {
                'diagnosis': 'Chronic Kidney Disease Stage 3',
                'treatment': 'Dialysis, medication, dietary restrictions',
                'severity': 'High',
                'duration': '6-12 months',
                'estimated_base_cost': 80000
            }
        ]
        
        # Select diagnosis (use hash of filename for consistency)
        diagnosis_idx = int(hashlib.md5(file.filename.encode()).hexdigest(), 16) % len(diagnoses_pool)
        diagnosis = diagnoses_pool[diagnosis_idx]
        base_cost = diagnosis['estimated_base_cost']
        
        # Mock hospital data with realistic pricing
        hospitals = [
            {
                'name': 'AIIMS Delhi',
                'estimated_cost': int(base_cost * 0.3),
                'success_rate': 92,
                'patient_reviews': 4.5,
                'location': 'Delhi',
                'type': 'Government',
                'overall_score': 90,
                'waiting_time': '2-3 weeks',
                'facilities': 'ICU, Emergency, 24x7'
            },
            {
                'name': 'Safdarjung Hospital',
                'estimated_cost': int(base_cost * 0.2),
                'success_rate': 88,
                'patient_reviews': 4.2,
                'location': 'Delhi',
                'type': 'Government',
                'overall_score': 92,
                'waiting_time': '1-2 weeks',
                'facilities': 'General Ward, OPD'
            },
            {
                'name': 'Apollo Hospital',
                'estimated_cost': int(base_cost * 1.2),
                'success_rate': 95,
                'patient_reviews': 4.7,
                'location': 'Delhi',
                'type': 'Private',
                'overall_score': 78,
                'waiting_time': 'Immediate',
                'facilities': 'Premium ICU, Private Rooms'
            },
            {
                'name': 'Fortis Hospital',
                'estimated_cost': int(base_cost * 1.0),
                'success_rate': 94,
                'patient_reviews': 4.6,
                'location': 'Delhi',
                'type': 'Private',
                'overall_score': 80,
                'waiting_time': 'Same day',
                'facilities': 'ICU, Emergency, Specialists'
            },
            {
                'name': 'Max Super Speciality Hospital',
                'estimated_cost': int(base_cost * 1.1),
                'success_rate': 93,
                'patient_reviews': 4.5,
                'location': 'Delhi',
                'type': 'Private',
                'overall_score': 79,
                'waiting_time': '1-2 days',
                'facilities': 'Advanced ICU, Robotic Surgery'
            },
            {
                'name': 'Ram Manohar Lohia Hospital',
                'estimated_cost': int(base_cost * 0.25),
                'success_rate': 89,
                'patient_reviews': 4.3,
                'location': 'Delhi',
                'type': 'Government',
                'overall_score': 91,
                'waiting_time': '1-2 weeks',
                'facilities': 'General Ward, Emergency'
            }
        ]
        
        # Sort hospitals by overall score
        hospitals.sort(key=lambda h: h['overall_score'], reverse=True)
        
        # Mock schemes based on income
        schemes = []
        income_val = int(income) if income.isdigit() else 200000
        
        if income_val < 500000:
            schemes.append({
                'name': 'Ayushman Bharat (PM-JAY)',
                'coverage': 500000,
                'benefits': 'Free treatment up to ₹5 lakh per family per year at empaneled hospitals',
                'eligibility': 'Income below ₹5 lakh annually',
                'how_to_apply': 'Visit nearest Ayushman Mitra or apply online at pmjay.gov.in'
            })
        
        if income_val < 300000:
            schemes.append({
                'name': 'State Health Insurance Scheme',
                'coverage': 200000,
                'benefits': 'Cashless treatment at government and empaneled private hospitals',
                'eligibility': 'Income below ₹3 lakh annually',
                'how_to_apply': 'Apply at district health office or online portal'
            })
        
        if int(age) >= 60:
            schemes.append({
                'name': 'Senior Citizen Health Scheme',
                'coverage': 100000,
                'benefits': 'Free OPD consultation and 50% discount on medicines',
                'eligibility': 'Age 60 years and above',
                'how_to_apply': 'Visit nearest government hospital with age proof'
            })
        
        # Calculate potential savings
        cheapest_hospital = min(hospitals, key=lambda h: h['estimated_cost'])
        total_scheme_coverage = sum(s['coverage'] for s in schemes)
        potential_savings = min(cheapest_hospital['estimated_cost'], total_scheme_coverage)
        
        recommendations = []
        
        if schemes:
            recommendations.append({
                'type': 'scheme',
                'priority': 'high',
                'message': f'You qualify for {len(schemes)} government schemes with total coverage up to ₹{total_scheme_coverage:,}'
            })
            recommendations.append({
                'type': 'savings',
                'priority': 'high',
                'message': f'Potential savings: ₹{potential_savings:,} through government schemes'
            })
        
        recommendations.append({
            'type': 'hospital',
            'priority': 'high',
            'message': f'Most affordable: {cheapest_hospital["name"]} - ₹{cheapest_hospital["estimated_cost"]:,}'
        })
        
        recommendations.append({
            'type': 'hospital',
            'priority': 'medium',
            'message': f'Best rated: {hospitals[0]["name"]} - Success rate {hospitals[0]["success_rate"]}%'
        })
        
        if diagnosis['severity'] == 'High':
            recommendations.append({
                'type': 'alert',
                'priority': 'high',
                'message': 'High severity condition detected. Immediate medical attention recommended.'
            })
        
        # Add alternative treatment suggestion
        recommendations.append({
            'type': 'alternative',
            'priority': 'low',
            'message': 'Consider preventive care and lifestyle modifications to reduce treatment costs'
        })
        
        return jsonify({
            'diagnosis': diagnosis,
            'hospitals': hospitals,
            'eligible_schemes': schemes,
            'recommendations': recommendations
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
