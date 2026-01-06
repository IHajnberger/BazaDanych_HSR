console.log("teams.js loaded");

const userId = localStorage.getItem("user_id");

if (!userId) {
    window.location.href = "/";
}

// =====================
// ELEMENTY DOM
// =====================
const teamsContainer = document.getElementById("teamsContainer");
const dpsSelect = document.getElementById("dpsSelect");
const supportBox = document.getElementById("supportSuggestions");
const sustainBox = document.getElementById("sustainSuggestions");
const readyBtn = document.getElementById("readyBtn");

const selectedDpsEl = document.getElementById("selectedDps");
const selectedSupport1El = document.getElementById("selectedSupport1");
const selectedSupport2El = document.getElementById("selectedSupport2");
const selectedSustainEl = document.getElementById("selectedSustain");

// =====================
// STAN
// =====================
let characterRoles = {};
let selectedDps = null;
let selectedSupports = [];
let selectedSustain = null;

// =====================
// NAV
// =====================
function goBack() {
    window.location.href = "/main";
}

// =====================
// LOAD ROLES
// =====================
async function loadCharacterRoles() {
    const res = await fetch("/api/characters");
    const characters = await res.json();

    characters.forEach(c => {
        characterRoles[c.Name] = c.Role;
    });
}

// =====================
// LOAD DPS LIST
// =====================
async function loadDpsOptions() {
    const res = await fetch(`/api/users/${userId}/characters`);
    const characters = await res.json();

    characters
        .filter(c => c.Role === "DPS")
        .forEach(dps => {
            const option = document.createElement("option");
            option.value = dps.Name;
            option.textContent = dps.Name;
            dpsSelect.appendChild(option);
        });
}

dpsSelect.addEventListener("change", () => {
    selectedDps = dpsSelect.value || null;
    selectedSupports = [];
    selectedSustain = null;

    updatePreview();
    readyBtn.disabled = true;

    if (selectedDps) {
        loadCandidatesForDps(selectedDps);
    } else {
        supportBox.innerHTML = "";
        sustainBox.innerHTML = "";
    }
});

// =====================
// LOAD CANDIDATES
// =====================
async function loadCandidatesForDps(dpsName) {
    const res = await fetch(
        `/api/users/${userId}/dps/${encodeURIComponent(dpsName)}/candidates`
    );

    const candidates = await res.json();

    renderSupportSuggestions(
        candidates.filter(c => c.Role === "Support")
    );

    renderSustainSuggestions(
        candidates.filter(c => c.Role === "Sustain")
    );
}

// =====================
// RENDER SUGGESTIONS
// =====================
function renderSupportSuggestions(list) {
    supportBox.innerHTML = "";

    list.forEach(char => {
        const el = document.createElement("div");
        el.className = "suggestion";
        el.textContent = `${char.Name} (${char.score})`;

        el.onclick = () => {
            if (selectedSupports.includes(char.Name)) return;
            if (selectedSupports.length >= 2) return;

            selectedSupports.push(char.Name);
            updatePreview();
        };

        supportBox.appendChild(el);
    });
}

function renderSustainSuggestions(list) {
    sustainBox.innerHTML = "";

    list.forEach(char => {
        const el = document.createElement("div");
        el.className = "suggestion";
        el.textContent = `${char.Name} (${char.score})`;

        el.onclick = () => {
            selectedSustain = char.Name;
            updatePreview();
        };

        sustainBox.appendChild(el);
    });
}

// =====================
// PREVIEW + READY
// =====================
function updatePreview() {
    selectedDpsEl.textContent = selectedDps || "-";
    selectedSupport1El.textContent = selectedSupports[0] || "-";
    selectedSupport2El.textContent = selectedSupports[1] || "-";
    selectedSustainEl.textContent = selectedSustain || "-";

    readyBtn.disabled = !(
        selectedDps &&
        selectedSupports.length === 2 &&
        selectedSustain
    );
}

readyBtn.onclick = createTeam;

// =====================
// CREATE TEAM
// =====================
async function createTeam() {
    const characters = [
        selectedDps,
        selectedSupports[0],
        selectedSupports[1],
        selectedSustain
    ];

    await fetch(`/api/users/${userId}/teams`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            Name: "New Team",
            characters
        })
    });

    loadTeams();
}

// =====================
// TEAMS LIST
// =====================
async function loadTeamScore(teamId, dpsName) {
    const res = await fetch(
        `/api/users/${userId}/teams/${teamId}/dps_score?dps_name=${encodeURIComponent(dpsName)}`
    );
    if (!res.ok) return null;
    return await res.json();
}

async function loadTeams() {
    const res = await fetch(`/api/users/${userId}/teams`);
    const teams = await res.json();

    teamsContainer.innerHTML = "";

    if (!teams.length) {
        teamsContainer.innerHTML = "<p>No teams created yet.</p>";
        return;
    }

    for (const team of teams) {
        const tile = document.createElement("div");
        tile.className = "team-tile";

        const names = Object.values(team.Characters);
        const dpsName = names.find(n => characterRoles[n] === "DPS");

        let scoreHtml = "-";

        if (dpsName) {
            const score = await loadTeamScore(team.id, dpsName);
            if (score) {
                scoreHtml = `${score.score} (${score.matched_needs}/${score.total_needs})`;
            }
        }

        tile.innerHTML = `
            <h3>${team.Name}</h3>
            <p>${names.join(", ")}</p>
            <p><strong>Score:</strong> ${scoreHtml}</p>
            <button onclick="deleteTeam(${team.id})">Delete</button>
        `;

        teamsContainer.appendChild(tile);
    }
}

async function deleteTeam(teamId) {
    if (!confirm("Delete this team?")) return;

    await fetch(`/api/users/${userId}/teams/${teamId}`, {
        method: "DELETE"
    });

    loadTeams();
}

// =====================
// INIT
// =====================
async function init() {
    await loadCharacterRoles();
    await loadDpsOptions();
    await loadTeams();
}

init();
