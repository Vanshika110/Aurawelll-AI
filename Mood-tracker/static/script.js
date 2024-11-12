document.addEventListener("DOMContentLoaded", function () {
    const moodForm = document.getElementById("moodForm");
    const moodChart = document.getElementById("moodChart");

    // Function to update the mood chart
    function updateMoodChart() {
        fetch('/fetch_mood') // Adjust the URL as needed
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Clear existing chart data
                moodChart.innerHTML = '';

                // Populate the chart with new data
                for (const [day, mood] of Object.entries(data)) {
                    const moodItem = document.createElement("div");
                    moodItem.textContent = `Day ${day}: Mood ${mood}`;
                    moodChart.appendChild(moodItem);
                }
            })
            .catch(error => {
                console.error('Error fetching mood data:', error);
            });
    }

    // Event listener for form submission
    moodForm.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission

        const formData = new FormData(moodForm);
        fetch('/submit', { // Adjust the URL as needed
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Mood data submitted successfully!");
                updateMoodChart(); // Refresh the chart after submission
            } else {
                alert("Error: " + (data.error || "Unknown error"));
            }
        })
        .catch(error => {
            console.error('Error submitting mood data:', error);
        });
    });

    // Initial chart update when the page loads
    updateMoodChart();
});