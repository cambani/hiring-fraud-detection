document.getElementById("fraudForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent page reload

    const formData = new FormData(this);
    const jsonData = {};
    formData.forEach((value, key) => jsonData[key] = value);

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(jsonData)
    })
    .then(response => response.json())
    .then(data => {
        const resultElement = document.getElementById("prediction_result");
        resultElement.innerText = data.prediction;

        // Apply appropriate color styling
        if (data.prediction === "Legitimate Hiring") {
            resultElement.className = "result-container result legitimate";
        } else {
            resultElement.className = "result-container result fraud";
        }
    })
    .catch(error => console.error("Error:", error));
});
