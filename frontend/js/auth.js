const loginForm = document.getElementById("loginForm");
const message = document.getElementById("message");

loginForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/auth/login",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    email: email,
                    password: password
                })
            }
        );

        const data = await response.json();

        if (!response.ok) {
            message.textContent = data.detail;
            return;
        }

        localStorage.setItem(
            "access_token",
            data.access_token
        );

        message.textContent = "Login successful!";

        window.location.href = "dashboard.html";

    } catch (error) {

        message.textContent =
            "Unable to connect to the server.";

        console.error(error);
    }
});