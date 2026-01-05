console.log("teams.js loaded");

const userId = localStorage.getItem("user_id");
const container = document.getElementById("teamsContainer");

if (!userId) {
    window.location.href = "/";
}

function goBack() {
    window.location.href = "/main";
}

async function loadTeams() {
    try {
        const res = await fetch(`/api/users/${userId}/teams`);
        const teams = await res.json();

        renderTeams(teams);
    } catch (err) {
        console.error("Failed to load teams", err);
    }
}

function renderTeams(teams) {
    container.innerHTML = "";

    if (!teams || teams.length === 0) {
        container.innerHTML = "<p>No teams created yet.</p>";
        return;
    }

    teams.forEach(team => {
        const tile = document.createElement("div");
        tile.className = "team-tile";

        let charactersHtml = "";

        if (team.Characters && typeof team.Characters === "object") {
            charactersHtml = Object.values(team.Characters)
                .map(name => `<span class="char-name">${name}</span>`)
                .join(", ");
        } else {
            charactersHtml = "<em>No characters</em>";
        }

        tile.innerHTML = `
            <div class="team-info">
                <h3>${team.Name}</h3>
                <p><strong>Characters:</strong> ${charactersHtml}</p>
                <p><strong>Score:</strong> ${team.Score}</p>
            </div>

            <button onclick="deleteTeam(${team.id})">Delete</button>
        `;

        container.appendChild(tile);
    });
}



async function deleteTeam(teamId) {
    if (!confirm("Delete this team?")) return;

    await fetch(`/api/users/${userId}/teams/${teamId}`, {
        method: "DELETE"
    });

    loadTeams();
}

loadTeams();
