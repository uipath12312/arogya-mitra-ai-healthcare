// Load cities on page load
document.addEventListener('DOMContentLoaded', () => {
    loadCities();
});

async function loadCities() {
    try {
        const response = await fetch('/api/cities');
        const data = await response.json();
        
        const citySelect = document.getElementById('city');
        data.cities.forEach(city => {
            const option = document.createElement('option');
            option.value = city;
            option.textContent = city;
            citySelect.appendChild(option);
        });
    } catch (error) {
        console.error('Error loading cities:', error);
    }
}

// Handle form submission
document.getElementById('analysisForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    const btnText = document.getElementById('btnText');
    const btnLoader = document.getElementById('btnLoader');
    const submitBtn = e.target.querySelector('button[type="submit"]');
    const errorDiv = document.getElementById('error');
    const resultsDiv = document.getElementById('results');
    
    // Show loading state
    btnText.style.display = 'none';
    btnLoader.style.display = 'inline-block';
    submitBtn.disabled = true;
    errorDiv.style.display = 'none';
    resultsDiv.style.display = 'none';
    
    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Analysis failed');
        }
        
        displayResults(data);
        resultsDiv.style.display = 'block';
        
        // Scroll to results
        resultsDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        
    } catch (error) {
        errorDiv.textContent = error.message;
        errorDiv.style.display = 'block';
    } finally {
        btnText.style.display = 'inline';
        btnLoader.style.display = 'none';
        submitBtn.disabled = false;
    }
});

function displayResults(data) {
    displayMedicalInfo(data.medical_info);
    displaySchemeInfo(data.scheme_eligibility);
    displayHospitals(data.recommendations);
}

function displayMedicalInfo(info) {
    const content = document.getElementById('medicalInfoContent');
    content.innerHTML = `
        <div class="info-item">
            <strong>Diagnosis:</strong> ${info.diagnosis}
        </div>
        <div class="info-item">
            <strong>Recommended Procedures:</strong> ${info.procedures.join(', ')}
        </div>
        <div class="info-item">
            <strong>Severity:</strong> <span style="color: ${getSeverityColor(info.severity)}">${info.severity}</span>
        </div>
        <div class="info-item">
            <strong>Urgency:</strong> ${info.urgency}
        </div>
        <div class="info-item">
            <strong>Summary:</strong> ${info.summary}
        </div>
    `;
}

function displaySchemeInfo(scheme) {
    const content = document.getElementById('schemeInfoContent');
    
    let html = '';
    
    if (scheme.ayushman_bharat.eligible) {
        html += `
            <div class="info-item">
                <strong>✅ Ayushman Bharat (PM-JAY):</strong> Eligible<br>
                <small>${scheme.ayushman_bharat.coverage}</small>
            </div>
        `;
    } else {
        html += `
            <div class="info-item">
                <strong>❌ Ayushman Bharat (PM-JAY):</strong> Not Eligible
            </div>
        `;
    }
    
    if (scheme.state_schemes && scheme.state_schemes.length > 0) {
        scheme.state_schemes.forEach(s => {
            html += `
                <div class="info-item">
                    <strong>${s.eligible ? '✅' : '❌'} ${s.name}:</strong> 
                    ${s.eligible ? 'Eligible' : 'Not Eligible'}
                </div>
            `;
        });
    }
    
    html += `
        <div class="info-item">
            <strong>Recommendations:</strong> ${scheme.recommendations}
        </div>
    `;
    
    content.innerHTML = html;
}

function displayHospitals(hospitals) {
    const list = document.getElementById('hospitalList');
    
    list.innerHTML = hospitals.map((hospital, index) => `
        <div class="hospital-card ${index === 0 ? 'recommended' : ''}">
            ${index === 0 ? '<div style="color: #4caf50; font-weight: 600; margin-bottom: 10px;">⭐ BEST VALUE</div>' : ''}
            
            <div class="hospital-header">
                <div class="hospital-name">${hospital.name}</div>
                <div class="cost-badge">₹${hospital.total_cost.toLocaleString()}</div>
            </div>
            
            <div class="hospital-info">
                <div class="info-badge">
                    ⭐ Rating: ${hospital.rating}/5
                </div>
                <div class="info-badge">
                    ✅ Success Rate: ${hospital.success_rate}%
                </div>
                <div class="info-badge">
                    📍 ${hospital.city}
                </div>
                <div class="info-badge">
                    📞 ${hospital.phone}
                </div>
            </div>
            
            <div style="margin-top: 10px; color: #666;">
                <strong>Address:</strong> ${hospital.address}
            </div>
            
            <div style="margin-top: 10px;">
                <strong>Specialties:</strong> ${hospital.specialties.join(', ')}
            </div>
            
            ${hospital.government_schemes ? '<span class="scheme-badge">Accepts Government Schemes</span>' : ''}
            
            <div class="procedures-list">
                <h4>Procedure Costs:</h4>
                ${hospital.procedures_list.map(proc => `
                    <div class="procedure-item">
                        <span>${proc.name}</span>
                        <span style="font-weight: 600;">₹${proc.cost.toLocaleString()}</span>
                    </div>
                `).join('')}
            </div>
        </div>
    `).join('');
}

function getSeverityColor(severity) {
    const colors = {
        'mild': '#4caf50',
        'moderate': '#ff9800',
        'severe': '#f44336'
    };
    return colors[severity.toLowerCase()] || '#666';
}
