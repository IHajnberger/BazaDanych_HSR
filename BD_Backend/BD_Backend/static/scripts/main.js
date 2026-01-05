const userId = localStorage.getItem("user_id");

if (!userId) {
    // brak sesji -> cofamy do loginu
    window.location.href = "/";
}

// username load
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
    window.location.href = "/";
}

// overview load
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

// load owned characters
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
                <img src="/static/images/characters/${char.Name}.png" 
                     alt="${char.Name}">
            `;

            container.appendChild(tile);
        });

    } catch (err) {
        console.error("Failed to load owned characters");
    }
}

loadMyCharacters();
loadUser();
loadOverview();