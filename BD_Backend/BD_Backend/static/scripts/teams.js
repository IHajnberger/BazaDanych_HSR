document.addEventListener("DOMContentLoaded", () => {
    console.log("teams.js loaded");

    const userId = localStorage.getItem("user_id");

    if (!userId) {
        window.location.replace("/");
    }

    // =====================
    // ELEMENTY DOM
    // =====================
    const teamsContainer = document.getElementById("teamsContainer");
    const dpsSelect = document.getElementById("dpsSelect");
    const supportBox = document.getElementById("supportSuggestions");
    const sustainBox = document.getElementById("sustainSuggestions");
    const readyBtn = document.getElementById("readyBtn");

    const teamNameInput = document.getElementById("teamNameInput");
    const selectedDpsEl = document.getElementById("selectedDps");
    const selectedSupport1El = document.getElementById("selectedSupport1");
    const selectedSupport2El = document.getElementById("selectedSupport2");
    const selectedSustainEl = document.getElementById("selectedSustain");

    if (!teamsContainer || !dpsSelect || !readyBtn) {
        console.error("Teams page DOM not loaded correctly");
        return;
    }

    // =====================
    // STAN
    // =====================
    let characterRoles = {};
    let selectedDps = null;
    let selectedSupports = [];
    let selectedSustain = null;
    let editMode = false;
    let editedTeamId = null;

    // =====================
    // NAV
    // =====================
    window.goBack = function () {
        window.location.href = "/main";
    };

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

        dpsSelect.innerHTML = `<option value="">-- select DPS --</option>`;

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

        renderSupportSuggestions(candidates.filter(c => c.Role === "Support"));
        renderSustainSuggestions(candidates.filter(c => c.Role === "Sustain"));
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

            if (selectedSupports.includes(char.Name)) {
                el.classList.add("selected");
            }

            el.onclick = () => {
                if (selectedSupports.includes(char.Name)) {
                    selectedSupports = selectedSupports.filter(n => n !== char.Name);
                } else {
                    if (selectedSupports.length >= 2) return;
                    selectedSupports.push(char.Name);
                }

                updatePreview();
                renderSupportSuggestions(list);
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

            if (selectedSustain === char.Name) {
                el.classList.add("selected");
            }

            el.onclick = () => {
                selectedSustain =
                    selectedSustain === char.Name ? null : char.Name;

                updatePreview();
                renderSustainSuggestions(list);
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

    readyBtn.onclick = createOrUpdateTeam;

    // =====================
    // CREATE / UPDATE
    // =====================
    async function createOrUpdateTeam() {
        const payload = {
            Name: teamNameInput.value || "New Team",
            characters: [
                selectedDps,
                selectedSupports[0],
                selectedSupports[1],
                selectedSustain
            ]
        };

        const url = editMode
            ? `/api/users/${userId}/teams/${editedTeamId}`
            : `/api/users/${userId}/teams`;

        const method = editMode ? "PUT" : "POST";

        await fetch(url, {
            method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        resetBuilder();
        loadTeams();
    }

    // =====================
    // RESET
    // =====================
    function resetBuilder() {
        selectedDps = null;
        selectedSupports = [];
        selectedSustain = null;

        editMode = false;
        editedTeamId = null;

        dpsSelect.value = "";
        teamNameInput.value = "";

        supportBox.innerHTML = "";
        sustainBox.innerHTML = "";

        readyBtn.textContent = "Ready";
        readyBtn.disabled = true;

        updatePreview();
    }


    // =====================
    // TEAMS LIST
    // =====================
    async function loadTeams() {
        const res = await fetch(`/api/users/${userId}/teams`);
        const teams = await res.json();

        teamsContainer.innerHTML = "";

        if (!teams.length) {
            teamsContainer.innerHTML = "<p>No teams created yet.</p>";
            return;
        }

        for (const team of teams) {
            const names = Object.values(team.Characters);
            const dpsName = names.find(n => characterRoles[n] === "DPS");

            const tile = document.createElement("div");
            tile.className = "team-tile";
            tile.innerHTML = `
                <h3>${team.Name}</h3>
                <p>${names.join(", ")}</p>
                <button onclick="editTeam(${team.id})">Edit</button>
                <button onclick="deleteTeam(${team.id})">Delete</button>
            `;

            teamsContainer.appendChild(tile);
        }
    }

    window.deleteTeam = async function (teamId) {
        if (!confirm("Delete this team?")) return;

        await fetch(`/api/users/${userId}/teams/${teamId}`, { method: "DELETE" });
        loadTeams();
    };

    window.editTeam = async function (teamId) {
        const res = await fetch(`/api/users/${userId}/teams/${teamId}`);
        const team = await res.json();

        editMode = true;
        editedTeamId = teamId;

        teamNameInput.value = team.Name;

        const names = Object.values(team.Characters);
        selectedDps = names.find(n => characterRoles[n] === "DPS");
        selectedSupports = names.filter(n => characterRoles[n] === "Support");
        selectedSustain = names.find(n => characterRoles[n] === "Sustain");

        dpsSelect.value = selectedDps;

        updatePreview();
        loadCandidatesForDps(selectedDps);

        readyBtn.textContent = "Update Team";
    };

    // =====================
    // INIT
    // =====================
    async function init() {
        await loadCharacterRoles();
        await loadDpsOptions();
        await loadTeams();
    }

    init();
});
window.addEventListener("pageshow", () => {
    const userId = localStorage.getItem("user_id");
    if (!userId) {
        window.location.replace("/");
    }
});
