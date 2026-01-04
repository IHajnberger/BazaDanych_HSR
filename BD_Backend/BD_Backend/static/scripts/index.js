const loginModal = document.getElementById("loginModal");
const registerModal = document.getElementById("registerModal");
// pop upy
function openLogin() {
    loginModal.style.display = "flex";
}

function closeAll() {
    loginModal.style.display = "none";
    registerModal.style.display = "none";
}

function switchToRegister() {
    loginModal.style.display = "none";
    registerModal.style.display = "flex";
}

function switchToLogin() {
    registerModal.style.display = "none";
    loginModal.style.display = "flex";
}

// close when clicking outside
window.onclick = function (e) {
    if (e.target === loginModal || e.target === registerModal) {
        closeAll();
    }
}

function showError(message) {
    const toast = document.getElementById("toast");
    toast.textContent = message;
    toast.style.display = "block";

    setTimeout(() => {
        toast.style.display = "none";
    }, 3000);
}

//Login function
async function login() {
    const username = document.getElementById("loginUsername").value;
    const password = document.getElementById("loginPassword").value;

    if (!username || !password) {
        showError("Please enter username and password");
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:5000/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (!response.ok) {
            showError(data.message || "Login failed");
            return;
        }

        localStorage.setItem("user_id", data.user_id);

        // przejœcie dalej
        window.location.href = "/main";

    } catch (err) {
        showError("Cannot connect to server");
    }
}

//Register function
async function register() {
    const username = document.getElementById("registerUsername").value;
    const password = document.getElementById("registerPassword").value;

    if (!username || !password) {
        showError("Please fill all fields");
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:5000/api/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (!response.ok) {
            showError(data.message || "Registration failed");
            return;
        }

        // po rejestracji wracamy do loginu
        switchToLogin();
        showError("Account created! You can log in now.");

    } catch (err) {
        showError("Cannot connect to server");
    }
}