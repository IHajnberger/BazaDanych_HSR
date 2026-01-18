console.log("characters.js loaded");

// =====================
// ELEMENTY DOM
// =====================
const container = document.getElementById("charactersContainer");
const userId = localStorage.getItem("user_id");

const searchInput = document.getElementById("searchInput");
const filtersPanel = document.getElementById("filtersPanel");

// PRZYCISKI FILTRÓW
const filterGroups = document.querySelectorAll(".filter-group");

if (!userId) {
    window.location.replace("/");
}

// =====================
// STAN
// =====================
let allCharacters = [];
let ownedCharacters = new Set();

let activeFilters = {
    path: null,
    role: null,
    element: null
};

// =====================
// NAV
// =====================
function goBack() {
    window.location.href = "/main";
}

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

    if (search) {
        result = result.filter(c =>
            c.Name.toLowerCase().includes(search)
        );
    }

    if (activeFilters.path) {
        result = result.filter(c => c.Path === activeFilters.path);
    }

    if (activeFilters.role) {
        result = result.filter(c => c.Role === activeFilters.role);
    }

    if (activeFilters.element) {
        result = result.filter(c => c.Element === activeFilters.element);
    }

    renderCharacters(result);
}

// =====================
// Image helpers
// =====================
function characterImage(name) {
    return `/static/img/characters_large/${name.toLowerCase()}.png`;
}

function elementImage(element) {
    return `/static/img/element/${element.toLowerCase()}.webp`;
}

function pathImage(path) {
    return `/static/img/path/${path.toLowerCase()}.webp`;
}

function displayName(name) {
    return name
        .replace(/_/g, " ")
        .replace(/\b\w/g, c => c.toUpperCase());
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
        tile.style.position = "relative";

        tile.innerHTML = `
            <input type="checkbox" ${isOwned ? "checked" : ""}>

            <div class="image">
                <img src="${characterImage(char.Name)}"
                     alt="${displayName(char.Name)}"
                     onerror="this.src='/static/img/characters_large/placeholder.png'">

                <!-- Nazwa postaci na dole grafiki -->
                <div class="image-title">${displayName(char.Name)}</div>

                <!-- Atrybuty w lewym górnym rogu -->
                <div class="attribute-icons">
                    <img src="${elementImage(char.Element)}" alt="${char.Element}">
                    <img src="${pathImage(char.Path)}" alt="${char.Path}">
                </div>

                <!-- Tooltip z tekstowymi informacjami -->
                <div class="info-tooltip">
                    <p><strong>Role:</strong> ${char.Role}</p>
                    <p><strong>Element:</strong> ${char.Element}</p>
                    <p><strong>Path:</strong> ${char.Path}</p>
                    <strong>Skills:</strong>
                    <ul class="skills-names">
                        ${char.Skills.map(skill => `<li>${skill.Name}: ${skill.Description}</li>`).join("")}
                    </ul>
                </div>
            </div>
        `;

        const checkbox = tile.querySelector("input");

        checkbox.addEventListener("change", () => {
            toggleCharacter(char.Name, checkbox.checked);
        });

        tile.addEventListener("click", e => {
            if (e.target.tagName !== "INPUT") {
                checkbox.checked = !checkbox.checked;
                toggleCharacter(char.Name, checkbox.checked);
            }
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

// FILTRY PRZYCISKOWE
filterGroups.forEach(group => {
    const filterType = group.dataset.filter;

    group.querySelectorAll("button").forEach(btn => {
        btn.addEventListener("click", () => {

            group.querySelectorAll("button")
                .forEach(b => b.classList.remove("active"));

            if (activeFilters[filterType] === btn.dataset.value) {
                activeFilters[filterType] = null;
            } else {
                btn.classList.add("active");
                activeFilters[filterType] = btn.dataset.value;
            }

            applyFilters();
        });
    });
});

// =====================
// INIT
// =====================
async function init() {
    await loadAllCharacters();
    await loadOwnedCharacters();
    renderCharacters(allCharacters);
}
init();

window.addEventListener("pageshow", () => {
    const userId = localStorage.getItem("user_id");
    if (!userId) {
        window.location.replace("/");
    }
});

