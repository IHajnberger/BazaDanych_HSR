const userId = localStorage.getItem("user_id");

if (!userId) {
    // brak sesji -> cofamy do loginu
    window.location.href = "/api/";
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
    window.location.href = "/api/";
}

loadUser();
