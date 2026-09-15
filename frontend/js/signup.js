const signupForm = document.getElementById("signupForm");

signupForm.addEventListener("submit", async function(event) {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const message = document.getElementById("signupMessage");

    message.textContent = "";
    message.style.color = "";

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/auth/signup",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    name: name,
                    email: email,
                    password: password
                })
            }
        );

        const data = await response.json();

        if (!response.ok) {

            message.style.color = "#dc2626";

            message.textContent =
                data.detail || "Signup failed";

            return;
        }

        message.style.color = "#16a34a";

        message.textContent =
            "Account created successfully! Redirecting...";

        setTimeout(function() {

            window.location.href = "index.html";

        }, 1200);

    } catch (error) {

        console.error(error);

        message.style.color = "#dc2626";

        message.textContent =
            "Unable to connect to server. Make sure FastAPI is running.";

    }
});