console.log("main.js loaded");

// =====================
// ELEMENTY DOM
// =====================
const userId = localStorage.getItem("user_id");
const menuBtn = document.getElementById("menuBtn");
const menuPopup = document.getElementById("menuPopup");

menuBtn.addEventListener("click", () => {
    menuPopup.classList.toggle("hidden");
});

if (!userId) {
    window.location.replace("/");
}

document.addEventListener("click", e => {
    if (!menuPopup.contains(e.target) && !menuBtn.contains(e.target)) {
        menuPopup.classList.add("hidden");
    }
});

// =====================
// MENU
// =====================
function goTo(path) {
    if (path === "/") {
        localStorage.removeItem("user_id");
        window.location.replace("/");
    } else {
        window.location.href = path;
    }
}

// =====================
// USERNAME LOAD
// =====================
async function loadUser() {
    try {
        const response = await fetch(`/api/users/${userId}`);
        if (!response.ok) throw new Error();

        const data = await response.json();
        document.getElementById("username").textContent = data.username;
    } catch {
        logout();
    }
}
function logout() {
    localStorage.removeItem("user_id");

    window.location.replace("/");
}

// =====================
// LOAD OVERVIEW
// =====================
async function loadOverview() {
    const userId = localStorage.getItem("user_id");
    if (!userId) return;

    try {
        const [charsRes, teamsRes] = await Promise.all([
            fetch(`/api/users/${userId}/characters`),
            fetch(`/api/users/${userId}/teams`)
        ]);

        const characters = await charsRes.json();
        const teams = await teamsRes.json();

        document.getElementById("charactersCount").textContent = characters.length;
        document.getElementById("teamsCount").textContent = teams.length;

    } catch (err) {
        console.error("Failed to load overview");
    }
}

// =====================
// LOAD OWNED CHARACTERS
// =====================

function characterImage(name) {
    return `/static/img/characters_small/${name.toLowerCase()}.webp`;
}

function characterImageLarge(name) {
    return `/static/img/characters_large/${name.toLowerCase()}.png`;
}

async function loadMyCharacters() {
    const userId = localStorage.getItem("user_id");
    if (!userId) return;

    try {
        const res = await fetch(`/api/users/${userId}/characters`);
        const characters = await res.json();

        const container = document.getElementById("myCharacters");
        container.innerHTML = "";

        characters.forEach(char => {
            const tile = document.createElement("div");
            tile.className = "character owned";

            tile.innerHTML = `
                <div class="avatar"> <img src="${characterImage(char.Name)}"
                     alt="${char.Name}"></div>
            `;

            container.appendChild(tile);
        });

    } catch (err) {
        console.error("Failed to load owned characters");
    }
}

// =====================
// LOAD TEAMS
// =====================
async function loadMyTeams() {
    const userId = localStorage.getItem("user_id");
    if (!userId) return;

    try {
        const res = await fetch(`/api/users/${userId}/teams`);
        const teams = await res.json();

        const container = document.getElementById("myTeams");
        if (!container) return;

        if (teams.length === 0) {
            container.innerHTML = "<p>No teams yet</p>";
            return;
        }

        teams.forEach(async (team) => {
            const tile = document.createElement("div");
            tile.className = "team preview";

            const names = Object.values(team.Characters);
            const score = await getTeamScore(team);

            tile.innerHTML = `
                <div class="singular-team">
                    <h4 class="team-name">
                        ${team.Name}
                        <span class="team-score">Score: ${score}</span>
                    </h4>

                    <div class="team-characters">
                        ${names.map(name => `
                            <div class="team-avatar">
                                <img src="${characterImageLarge(name)}" alt="${name}">
                            </div>
                        `).join("")}
                    </div>
                </div>
            `;

            container.appendChild(tile);
        });


    } catch {
        console.error("Failed to load teams");
    }
}

// =====================
// LOAD BEST TEAM SCORE
// =====================
async function loadBestTeamScore() {
    const userId = localStorage.getItem("user_id");
    if (!userId) return;

    try {
        
        const charsRes = await fetch("/api/characters");
        const allCharacters = await charsRes.json();

        const roles = {};
        allCharacters.forEach(c => {
            roles[c.Name] = c.Role;
        });

        const teamsRes = await fetch(`/api/users/${userId}/teams`);
        const teams = await teamsRes.json();

        let bestScore = 0;

        for (const team of teams) {
            const characterNames = Object.values(team.Characters);

            const dpsName = characterNames.find(
                name => roles[name] === "DPS"
            );

            if (!dpsName) continue;

            const scoreRes = await fetch(
                `/api/users/${userId}/teams/${team.id}/dps_score?dps_name=${encodeURIComponent(dpsName)}`
            );

            if (!scoreRes.ok) continue;

            const scoreData = await scoreRes.json();
            bestScore = Math.max(bestScore, scoreData.score);
        }

        const scoreEl = document.getElementById("bestTeamScore");
        if (!scoreEl) return;
        scoreEl.textContent = bestScore > 0 ? bestScore : "-";


    } catch (err) {
        console.error("Failed to load best team score");
    }
}

// =====================
// INNIT
// =====================
document.addEventListener("DOMContentLoaded", () => {
    loadUser();
    loadOverview();
    loadMyCharacters();
    loadMyTeams();
    loadBestTeamScore();
});

window.addEventListener("pageshow", () => {
    const userId = localStorage.getItem("user_id");
    if (!userId) {
        window.location.replace("/");
    }
});

// =====================
// HELPERS - score
// =====================
async function getTeamScore(team) {
    if (!window.rolesCache) {
        const res = await fetch("/api/characters");
        const chars = await res.json();
        window.rolesCache = {};

        chars.forEach(function (c) {
            window.rolesCache[c.Name] = c.Role;
        });
    }

    const names = Object.values(team.Characters);
    const dpsName = names.find(function (name) {
        return window.rolesCache[name] === "DPS";
    });

    if (!dpsName) return "-";

    const res = await fetch(
        `/api/users/${userId}/teams/${team.id}/dps_score?dps_name=${encodeURIComponent(dpsName)}`
    );

    if (!res.ok) return "-";

    const data = await res.json();
    return data.score;
}
