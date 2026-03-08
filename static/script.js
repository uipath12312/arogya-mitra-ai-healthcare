document.getElementById('document').addEventListener('change', function(e) {
    const fileName = e.target.files[0]?.name || 'No file chosen';
    document.getElementById('fileName').textContent = fileName;
});

document.getElementById('uploadForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = new FormData(this);
    
    document.getElementById('loading').style.display = 'block';
    document.getElementById('results').style.display = 'none';
    
    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (response.ok) {
            displayResults(data);
        } else {
            alert('Error: ' + data.error);
        }
    } catch (error) {
        alert('Error analyzing document: ' + error.message);
    } finally {
        document.getElementById('loading').style.display = 'none';
    }
});

function displayResults(data) {
    // Display diagnosis
    document.getElementById('diagnosisContent').innerHTML = `
        <p><strong>Diagnosis:</strong> ${data.diagnosis.diagnosis}</p>
        <p><strong>Treatment:</strong> ${data.diagnosis.treatment}</p>
        <p><strong>Severity:</strong> ${data.diagnosis.severity}</p>
        <p><strong>Duration:</strong> ${data.diagnosis.duration}</p>
    `;
    
    // Display schemes
    const schemesHTML = data.eligible_schemes.map(scheme => `
        <div class="scheme-card">
            <h4>${scheme.name}</h4>
            <p><strong>Coverage:</strong> ₹${scheme.coverage.toLocaleString()}</p>
            <p>${scheme.benefits}</p>
        </div>
    `).join('');
    document.getElementById('schemesContent').innerHTML = schemesHTML || '<p>No schemes found</p>';
    
    // Display hospitals
    const hospitalsHTML = data.hospitals.map(hospital => `
        <div class="hospital-card">
            <h4>${hospital.name}</h4>
            <div class="hospital-info">
                <span><strong>Cost:</strong> ₹${hospital.estimated_cost.toLocaleString()}</span>
                <span><strong>Success Rate:</strong> ${hospital.success_rate}%</span>
                <span><strong>Rating:</strong> ${hospital.patient_reviews}/5</span>
                <span><strong>Type:</strong> ${hospital.type}</span>
            </div>
        </div>
    `).join('');
    document.getElementById('hospitalsContent').innerHTML = hospitalsHTML;
    
    // Display recommendations
    const recsHTML = data.recommendations.map(rec => `
        <p>✓ ${rec.message}</p>
    `).join('');
    document.getElementById('recommendationsContent').innerHTML = recsHTML;
    
    document.getElementById('results').style.display = 'block';
}
