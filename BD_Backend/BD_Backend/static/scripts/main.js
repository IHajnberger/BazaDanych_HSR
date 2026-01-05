const userId = localStorage.getItem("user_id");

if (!userId) {
    // brak sesji -> cofamy do loginu
    window.location.href = "/";
}

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
