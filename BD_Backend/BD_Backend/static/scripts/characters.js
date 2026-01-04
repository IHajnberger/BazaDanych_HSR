const API_BASE = "http://127.0.0.1:5000/api";

// ❗ na sztywno user_id (na razie)
const USER_ID = 1;

async function loadCharacters() {
    try {
        // wszystkie postacie
        const allRes = await fetch(`${API_BASE}/characters`);
        const allCharacters = await allRes.json();

        // postacie użytkownika
        const userRes = await fetch(`${API_BASE}/users/${USER_ID}/characters`);
        const userCharacters = await userRes.json();

        const ownedNames = new Set(
            userCharacters.map(c => c.Name)
        );

        const container = document.getElementById("characters");
        container.innerHTML = "";

        allCharacters.forEach(char => {
            const div = document.createElement("div");
            div.classList.add("character");

            if (ownedNames.has(char.Name)) {
                div.classList.add("owned");
            }

            div.innerHTML = `
                <strong>${char.Name}</strong>
                <span>${char.Role}</span>
                <span>${char.Element}</span>
                <span>${char.Path}</span>
            `;

            container.appendChild(div);
        });

    } catch (err) {
        console.error("Blad API:", err);
        alert("Nie udalo się zaladowac postaci");
    }
}

// start
loadCharacters();
