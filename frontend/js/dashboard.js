const token = localStorage.getItem("access_token");

if (!token) {
    window.location.href = "index.html";
}


async function loadDashboard() {

    try {

        const statsResponse = await fetch(
            "http://127.0.0.1:8000/stats/",
            {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            }
        );

        if (!statsResponse.ok) {
            throw new Error("Unable to load statistics");
        }

        const stats = await statsResponse.json();

        document.getElementById("totalApplications").textContent =
            stats.total_applications;

        document.getElementById("appliedApplications").textContent =
            stats.by_status.applied || 0;

        document.getElementById("interviewApplications").textContent =
            stats.by_status.interview || 0;

        document.getElementById("rejectedApplications").textContent =
            stats.by_status.rejected || 0;

        document.getElementById("offerApplications").textContent =
            stats.by_status.offer || 0;


        const applicationsResponse = await fetch(
            "http://127.0.0.1:8000/applications/",
            {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            }
        );

        if (!applicationsResponse.ok) {
            throw new Error("Unable to load applications");
        }

        const applications =
            await applicationsResponse.json();

        displayApplications(applications);

    } catch (error) {

        console.error(error);

    }
}


function displayApplications(applications) {

    const container =
        document.getElementById("recentApplications");

    if (applications.length === 0) {

        container.innerHTML =
            '<p class="empty-message">No applications yet.</p>';

        return;
    }

    const recentApplications =
        applications.slice(-5).reverse();

    container.innerHTML = "";

    recentApplications.forEach(application => {

        const item = document.createElement("div");

        item.innerHTML = `
            <p>
                <strong>${application.company_name}</strong>
                -
                ${application.job_title}
            </p>
            <p>${application.status}</p>
        `;

        container.appendChild(item);

    });
}


loadDashboard();