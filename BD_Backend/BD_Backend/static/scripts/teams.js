console.log("teams.js loaded");

const userId = localStorage.getItem("user_id");
const container = document.getElementById("teamsContainer");
let characterRoles = {};

if (!userId) {
    window.location.href = "/";
}

function goBack() {
    window.location.href = "/main";
}

async function loadCharacterRoles() {
    const res = await fetch("/api/characters");
    const characters = await res.json();

    characters.forEach(c => {
        characterRoles[c.Name] = c.Role;
    });
}

async function loadTeamScore(teamId, dpsName) {
    const res = await fetch(
        `/api/users/${userId}/teams/${teamId}/dps_score?dps_name=${encodeURIComponent(dpsName)}`
    );

    if (!res.ok) return null;
    return await res.json();
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

async function renderTeams(teams) {
    container.innerHTML = "";

    if (!teams || teams.length === 0) {
        container.innerHTML = "<p>No teams created yet.</p>";
        return;
    }

    for (const team of teams) {
        const tile = document.createElement("div");
        tile.className = "team-tile";

        const characterNames = Object.values(team.Characters);

        // znajdz DPS
        const dpsName = characterNames.find(
            name => characterRoles[name] === "DPS"
        );

        let scoreHtml = "<em>No DPS</em>";

        if (dpsName) {
            const scoreData = await loadTeamScore(team.id, dpsName);

            if (scoreData) {
                scoreHtml = `
                    ${scoreData.score}
                    (${scoreData.matched_needs}/${scoreData.total_needs})
                `;
            }
        }

        tile.innerHTML = `
            <h3>${team.Name}</h3>

            <p>
                <strong>Team:</strong>
                ${characterNames.join(", ")}
            </p>

            <p>
                <strong>Score:</strong> ${scoreHtml}
            </p>

            <button onclick="deleteTeam(${team.id})">Delete</button>
        `;

        container.appendChild(tile);
    }
}

async function deleteTeam(teamId) {
    if (!confirm("Delete this team?")) return;

    await fetch(`/api/users/${userId}/teams/${teamId}`, {
        method: "DELETE"
    });

    loadTeams();
}

async function initTeamsPage() {
    await loadCharacterRoles(); // najpierw role
    await loadTeams();          // dopiero potem teamy
}

initTeamsPage();
