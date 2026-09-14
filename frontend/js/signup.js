const signupForm = document.getElementById("signupForm");
const signupMessage = document.getElementById("signupMessage");


signupForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;


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

            signupMessage.textContent = data.detail;

            return;
        }


        signupMessage.textContent =
            "Account created successfully!";


        setTimeout(function() {

            window.location.href = "index.html";

        }, 1000);


    } catch (error) {

        signupMessage.textContent =
            "Unable to connect to the server.";

        console.error(error);
    }

});