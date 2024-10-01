// Get the select element and button element
const selectElement = document.getElementById('card-type-select');
const submitButton = document.getElementById('submit-btn');

// Add an event listener to the button
submitButton.addEventListener('click', () => {
    // Get the selected value
    const selectedValue = selectElement.value;

    // Send an AJAX request to your Python script
    fetch('/generate_bin', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ selectedValue: selectedValue })
    })
    .then(response => response.json())
    .then(data => {
        // If the response is successful, redirect to a new HTML page
        if (data.success) {
            window.location.href = '/download_page';
        }
    })
    .catch(error => console.error(error));
});


