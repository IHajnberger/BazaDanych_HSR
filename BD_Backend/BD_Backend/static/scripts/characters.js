console.log("characters.js loaded");

// =====================
// ELEMENTY DOM
// =====================
const container = document.getElementById("charactersContainer");
const userId = localStorage.getItem("user_id");

if (!userId) {
    window.location.href = "/";
}

let ownedCharacters = new Set();

function goBack() {
    window.location.href = "/main";
}

// =====================
//  CHARACTERS LOAD
// =====================

async function loadCharacters() {
    try {
        // 1. wszystkie postacie
        const allRes = await fetch("/api/characters");
        const allCharacters = await allRes.json();

        // 2. postacie usera
        const ownedRes = await fetch(`/api/users/${userId}/characters`);
        const owned = await ownedRes.json();

        ownedCharacters = new Set(owned.map(c => c.Name));

        renderCharacters(allCharacters);

    } catch (err) {
        console.error("Failed to load characters:", err);
    }
}

// =====================
// RENDER CHARACTERS
// =====================

function renderCharacters(characters) {
    container.innerHTML = "";

    characters.forEach(char => {
        const isOwned = ownedCharacters.has(char.Name);

        const tile = document.createElement("div");
        tile.className = `character-tile ${isOwned ? "owned" : "not-owned"}`;

        // kafelek
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
// API INTERACTIONS
// =====================

async function toggleCharacter(name, checked) {
    try {
        if (checked) {
            await fetch(`/api/users/${userId}/characters`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ Name: name })
            });

            ownedCharacters.add(name);

        } else {
            await fetch(`/api/users/${userId}/characters/${name}`, {
                method: "DELETE"
            });

            ownedCharacters.delete(name);
        }

        // reload
        loadCharacters();

    } catch (err) {
        console.error("Failed to update character:", err);
    }
}

// =====================
// INNIT
// =====================

loadCharacters();
