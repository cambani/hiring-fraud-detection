function predictFraud() {
    let data = {
        "qualification_match": parseInt(document.getElementById("qualification_match").value),
        "experience_years": parseInt(document.getElementById("experience_years").value),
        "interview_rounds": parseInt(document.getElementById("interview_rounds").value),
        "time_to_hire_days": parseInt(document.getElementById("time_to_hire_days").value),
        "referral_connection": parseInt(document.getElementById("referral_connection").value),
        "salary_increase_percent": parseFloat(document.getElementById("salary_increase_percent").value)
    };

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        let result = data.hiring_fraud_prediction === 1 ? "Fraud Detected" : "Legitimate";
        document.getElementById("result").innerText = result;
    })
    .catch(error => console.error("Error:", error));
}
