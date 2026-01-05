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

    if (teams.length === 0) {
        container.innerHTML = "<p>No teams created yet.</p>";
        return;
    }

    teams.forEach(team => {
        const tile = document.createElement("div");
        tile.className = "team-tile";

        const charactersHtml = team.Characters.map(char => `
            <img 
                src="/static/images/characters/${char.Name}.png"
                alt="${char.Name}"
            >
        `).join("");

        tile.innerHTML = `
            <div class="team-characters">
                ${charactersHtml}
            </div>

            <div class="team-info">
                <h3>${team.Name}</h3>
                <p>Score: <strong>${team.Score}</strong></p>
            </div>

            <div class="team-actions">
                <button onclick="deleteTeam(${team.id})">Delete</button>
            </div>
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
