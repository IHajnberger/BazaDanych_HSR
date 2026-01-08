console.log("characters.js loaded");

// =====================
// ELEMENTY DOM
// =====================
const container = document.getElementById("charactersContainer");
const userId = localStorage.getItem("user_id");

const searchInput = document.getElementById("searchInput");
const filterToggle = document.getElementById("filterToggle");
const filtersPanel = document.getElementById("filtersPanel");

const filterPath = document.getElementById("filterPath");
const filterRole = document.getElementById("filterRole");
const filterElement = document.getElementById("filterElement");

if (!userId) {
    window.location.replace("/");
}

// =====================
// STAN
// =====================
let allCharacters = [];
let ownedCharacters = new Set();

// =====================
// NAV
// =====================
function goBack() {
    window.location.href = "/main";
}

filterToggle.onclick = () => {
    const isHidden = filtersPanel.classList.contains("hidden");

    if (isHidden) {
        filtersPanel.classList.remove("hidden");
        filterToggle.textContent = "Clear";
    } else {
        clearFilters();
    }
};

// =====================
// LOAD DATA
// =====================
async function loadAllCharacters() {
    const res = await fetch("/api/characters");
    allCharacters = await res.json();
}

async function loadOwnedCharacters() {
    const res = await fetch(`/api/users/${userId}/characters`);
    const owned = await res.json();

    ownedCharacters = new Set(owned.map(c => c.Name));
}

// =====================
// FILTER + SEARCH
// =====================
function applyFilters() {
    let result = [...allCharacters];

    const search = searchInput.value.toLowerCase();
    const path = filterPath.value;
    const role = filterRole.value;
    const element = filterElement.value;

    if (search) {
        result = result.filter(c =>
            c.Name.toLowerCase().includes(search)
        );
    }

    if (path) {
        result = result.filter(c => c.Path === path);
    }

    if (role) {
        result = result.filter(c => c.Role === role);
    }

    if (element) {
        result = result.filter(c => c.Element === element);
    }

    renderCharacters(result);
}

function clearFilters() {
    searchInput.value = "";
    filterPath.value = "";
    filterRole.value = "";
    filterElement.value = "";

    filtersPanel.classList.add("hidden");
    filterToggle.textContent = "Filters";

    renderCharacters(allCharacters);
}


// =====================
// RENDER
// =====================
function renderCharacters(characters) {
    container.innerHTML = "";

    characters.forEach(char => {
        const isOwned = ownedCharacters.has(char.Name);

        const tile = document.createElement("div");
        tile.className = `character-tile ${isOwned ? "owned" : "not-owned"}`;

        tile.innerHTML = `
            <input type="checkbox" ${isOwned ? "checked" : ""}>

            <div class="info">
                <h3>${char.Name}</h3>
                <p>Role: ${char.Role}</p>
                <p>Element: ${char.Element}</p>
                <p>Path: ${char.Path}</p>
            </div>
        `;

        const checkbox = tile.querySelector("input");

        checkbox.addEventListener("change", () => {
            toggleCharacter(char.Name, checkbox.checked);
        });

        container.appendChild(tile);
    });
}

// =====================
// OWN / UNOWN
// =====================
async function toggleCharacter(name, checked) {
    if (checked) {
        await fetch(`/api/users/${userId}/characters`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ Name: name })
        });

        ownedCharacters.add(name);
    } else {
        await fetch(`/api/users/${userId}/characters/${name}`, {
            method: "DELETE"
        });

        ownedCharacters.delete(name);
    }

    applyFilters();
}

// =====================
// EVENTS
// =====================
searchInput.addEventListener("input", applyFilters);
filterPath.addEventListener("change", applyFilters);
filterRole.addEventListener("change", applyFilters);
filterElement.addEventListener("change", applyFilters);

// =====================
// INIT
// =====================
async function init() {
    await loadAllCharacters();
    await loadOwnedCharacters();
    renderCharacters(allCharacters); // ⬅️ WSZYSTKIE NA START
    filterToggle.textContent = "Filters";
    filtersPanel.classList.add("hidden");
}
window.addEventListener("pageshow", () => {
    const userId = localStorage.getItem("user_id");
    if (!userId) {
        window.location.replace("/");
    }
});
init();
