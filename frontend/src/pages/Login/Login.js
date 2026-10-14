const API_URL = "http://127.0.0.1:8000";

const loginForm = document.getElementById("loginForm");
const loginButton = document.getElementById("loginButton");
const loginError = document.getElementById("loginError");

loginForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const login = document.getElementById("login").value.trim();
    const senha = document.getElementById("senha").value;

    loginError.textContent = "";

    if (!login || !senha) {
        loginError.textContent = "Informe o usuário e a senha.";
        return;
    }

    loginButton.disabled = true;
    loginButton.textContent = "Entrando...";

    try {
        const resposta = await fetch(`${API_URL}/api/auth/login`, {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                login,
                senha
            })
        });

        const dados = await resposta.json();

        if (!resposta.ok) {
            throw new Error(
                dados.detail || "Usuário ou senha inválidos."
            );
        }

        sessionStorage.setItem(
            "dashboardUsuario",
            JSON.stringify(dados)
        );

        window.location.href = "/frontend/src/pages/Dashboard/Dashboard.html";

    } catch (erro) {

        console.error("Erro ao realizar login:", erro);

        loginError.textContent = erro.message;

    } finally {

        loginButton.disabled = false;
        loginButton.textContent = "Entrar";
    }
});
