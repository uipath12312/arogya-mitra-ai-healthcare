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
        <p><strong>Severity:</strong> <span class="severity-${data.diagnosis.severity.toLowerCase()}">${data.diagnosis.severity}</span></p>
        <p><strong>Duration:</strong> ${data.diagnosis.duration}</p>
        ${data.diagnosis.estimated_base_cost ? `<p><strong>Estimated Base Cost:</strong> ₹${data.diagnosis.estimated_base_cost.toLocaleString()}</p>` : ''}
    `;
    
    // Display schemes
    const schemesHTML = data.eligible_schemes.map(scheme => `
        <div class="scheme-card">
            <h4>${scheme.name}</h4>
            <p><strong>Coverage:</strong> ₹${scheme.coverage.toLocaleString()}</p>
            <p><strong>Benefits:</strong> ${scheme.benefits}</p>
            ${scheme.eligibility ? `<p><strong>Eligibility:</strong> ${scheme.eligibility}</p>` : ''}
            ${scheme.how_to_apply ? `<p class="apply-info"><strong>How to Apply:</strong> ${scheme.how_to_apply}</p>` : ''}
        </div>
    `).join('');
    document.getElementById('schemesContent').innerHTML = schemesHTML || '<p>No schemes found based on your profile. Consider checking eligibility criteria.</p>';
    
    // Display hospitals
    const hospitalsHTML = data.hospitals.map((hospital, index) => `
        <div class="hospital-card ${index === 0 ? 'recommended' : ''}">
            <h4>${hospital.name} ${index === 0 ? '⭐ Recommended' : ''}</h4>
            <div class="hospital-info">
                <span><strong>Cost:</strong> ₹${hospital.estimated_cost.toLocaleString()}</span>
                <span><strong>Success Rate:</strong> ${hospital.success_rate}%</span>
                <span><strong>Rating:</strong> ${hospital.patient_reviews}/5 ⭐</span>
                <span><strong>Type:</strong> ${hospital.type}</span>
            </div>
            ${hospital.waiting_time ? `<p><strong>Waiting Time:</strong> ${hospital.waiting_time}</p>` : ''}
            ${hospital.facilities ? `<p><strong>Facilities:</strong> ${hospital.facilities}</p>` : ''}
        </div>
    `).join('');
    document.getElementById('hospitalsContent').innerHTML = hospitalsHTML;
    
    // Display recommendations with priority styling
    const recsHTML = data.recommendations.map(rec => {
        const icon = rec.type === 'scheme' ? '🎯' : 
                     rec.type === 'hospital' ? '🏥' : 
                     rec.type === 'savings' ? '💰' :
                     rec.type === 'alert' ? '⚠️' : '💡';
        const priorityClass = rec.priority || 'medium';
        return `<p class="recommendation-${priorityClass}">${icon} ${rec.message}</p>`;
    }).join('');
    document.getElementById('recommendationsContent').innerHTML = recsHTML;
    
    document.getElementById('results').style.display = 'block';
    document.getElementById('results').scrollIntoView({ behavior: 'smooth' });
}
