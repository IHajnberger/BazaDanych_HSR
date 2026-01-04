console.log("characters.js loaded");

const container = document.getElementById("charactersContainer");

const dummyCharacters = [
    {
        Name: "Kafka",
        Role: "DPS",
        Element: "Lightning",
        Path: "Nihility"
    },
    {
        Name: "Bronya",
        Role: "Support",
        Element: "Wind",
        Path: "Harmony"
    },
    {
        Name: "Seele",
        Role: "DPS",
        Element: "Quantum",
        Path: "Hunt"
    }
];

function goBack() {
    window.location.href = "/api/main"; 
}

function renderCharacters() {
    container.innerHTML = "";

    dummyCharacters.forEach(char => {
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

renderCharacters();
