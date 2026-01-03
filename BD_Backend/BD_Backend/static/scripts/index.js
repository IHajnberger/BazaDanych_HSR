document.addEventListener("DOMContentLoaded", async () => {
    const statusEl = document.getElementById("api-status");

    const apiOk = await checkApiStatus();
    if (apiOk) {
        statusEl.textContent = "API dzia³a";
        statusEl.style.color = "green";
    } else {
        statusEl.textContent = "Brak po³¹czenia z API";
        statusEl.style.color = "red";
    }
});

document.getElementById("load-characters-btn")
    .addEventListener("click", async () => {
        const list = document.getElementById("characters-list");
        list.innerHTML = "";

        try {
            const characters = await fetchCharacters();

            characters.forEach(c => {
                const li = document.createElement("li");
                li.textContent = `${c.Name} (${c.Role}, ${c.Element}, ${c.Path})`;
                list.appendChild(li);
            });

        } catch (e) {
            alert("B³¹d pobierania postaci");
        }
    });
