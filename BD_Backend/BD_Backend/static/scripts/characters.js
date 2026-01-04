console.log("characters.js loaded");

const container = document.getElementById("charactersContainer");

if (!container) {
    console.error("charactersContainer not found in HTML");
}

async function loadCharacters() {
    try {
        const res = await fetch("/api/characters");
        const characters = await res.json();

        console.log("Characters from API:", characters);

        renderCharacters(characters);
    } catch (err) {
        console.error("Failed to load characters:", err);
    }
}

function renderCharacters(characters) {
    container.innerHTML = "";

    characters.forEach(char => {
        const tile = document.createElement("div");
        tile.className = "character-tile";

        tile.innerHTML = `
            <input type="checkbox">

            <div class="info">
                <h3>${char.Name}</h3>
                <p>Role: ${char.Role}</p>
                <p>Element: ${char.Element}</p>
                <p>Path: ${char.Path}</p>
            </div>
        `;

        container.appendChild(tile);
    });
}

loadCharacters();
