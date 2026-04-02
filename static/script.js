document.getElementById('predict-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const temperature = document.getElementById('temperature').value;
    const resultDiv = document.getElementById('result');
    const loadingDiv = document.getElementById('loading');
    const predictionSpan = document.getElementById('prediction');

    // Hide result, show loading
    resultDiv.style.display = 'none';
    loadingDiv.style.display = 'block';

    // Prepare form data
    const formData = new FormData();
    formData.append('temperature', temperature);

    // Fetch prediction
    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        loadingDiv.style.display = 'none';
        if (data.error) {
            alert(data.error);
        } else {
            predictionSpan.textContent = data.prediction;
            resultDiv.style.display = 'block';
        }
    })
    .catch(error => {
        loadingDiv.style.display = 'none';
        alert('An error occurred. Please try again.');
        console.error('Error:', error);
    });
});

// Sample data for chart
const temperatures = [50, 52, 55, 57, 59, 60];
const sales = [23, 31, 43, 51, 61, 73];

const ctx = document.getElementById('salesChart').getContext('2d');
const salesChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: temperatures,
        datasets: [{
            label: 'Ice Cream Sales',
            data: sales,
            borderColor: 'rgba(102, 126, 234, 1)',
            backgroundColor: 'rgba(102, 126, 234, 0.2)',
            borderWidth: 2,
            fill: true
        }]
    },
    options: {
        responsive: true,
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Temperature (°C)'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Sales'
                }
            }
        }
    }
});