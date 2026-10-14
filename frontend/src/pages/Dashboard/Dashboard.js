const API_URL = "http://127.0.0.1:8000";


// =========================================
// FORMATADORES
// =========================================

const formatarMoeda = (valor) => {
    return new Intl.NumberFormat("pt-BR", {
        style: "currency",
        currency: "BRL"
    }).format(Number(valor) || 0);
};


const formatarNumero = (valor) => {
    return new Intl.NumberFormat("pt-BR").format(
        Number(valor) || 0
    );
};


const formatarPercentual = (valor) => {
    return `${Number(valor) || 0}%`;
};


// =========================================
// ELEMENTOS
// =========================================

const usuarioNome = document.getElementById("usuarioNome");
const logoutButton = document.getElementById("logoutButton");

// =========================================
// LOADING
// =========================================

function mostrarLoading() {

    const elementosMoeda = [
        "shalonDiaPedidosFeitos",
        "shalonDiaOrcamentosPendentes",
        "shalonDiaPedidosPendentes",
        "shalonDiaMeta",

        "shalonMesPedidosFeitos",
        "shalonMesOrcamentosPendentes",
        "shalonMesPedidosPendentes",
        "shalonMesMeta",

        "veracciDiaPedidosFeitos",
        "veracciDiaOrcamentosPendentes",
        "veracciDiaPedidosPendentes",
        "veracciDiaMeta",

        "veracciMesPedidosFeitos",
        "veracciMesOrcamentosPendentes",
        "veracciMesPedidosPendentes",
        "veracciMesMeta"
    ];

    const elementosNumero = [
        "shalonDiaClientesAtendidos",
        "shalonMesClientesAtendidos",
        "veracciDiaClientesAtendidos",
        "veracciMesClientesAtendidos"
    ];

    const elementosPercentual = [
        "shalonDiaPercentualMeta",
        "shalonMesPercentualMeta",
        "veracciDiaPercentualMeta",
        "veracciMesPercentualMeta"
    ];


    elementosMoeda.forEach((id) => {

        const elemento = document.getElementById(id);

        if (elemento) {
            elemento.textContent = "Carregando...";
        }
    });


    elementosNumero.forEach((id) => {

        const elemento = document.getElementById(id);

        if (elemento) {
            elemento.textContent = "Carregando...";
        }
    });


    elementosPercentual.forEach((id) => {

        const elemento = document.getElementById(id);

        if (elemento) {
            elemento.textContent = "Carregando...";
        }
    });
}


// =========================================
// SESSÃO
// =========================================

const usuario = JSON.parse(
    sessionStorage.getItem("dashboardUsuario")
);


if (!usuario) {
    window.location.href = "/";
}


// =========================================
// MOSTRAR USUÁRIO
// =========================================

if (usuario) {
    usuarioNome.textContent = `Usuário: ${usuario.usuario}`;
}


// =========================================
// PREENCHER DASHBOARD
// =========================================

function preencherEmpresa(prefixo, dados) {

    // -------------------------
    // DIA
    // -------------------------

    document.getElementById(
        `${prefixo}DiaPedidosFeitos`
    ).textContent = formatarMoeda(
        dados.dia.pedidosFeitos
    );


    document.getElementById(
        `${prefixo}DiaOrcamentosPendentes`
    ).textContent = formatarMoeda(
        dados.dia.orcamentosPendentes
    );


    document.getElementById(
        `${prefixo}DiaPedidosPendentes`
    ).textContent = formatarMoeda(
        dados.dia.pedidosPendentes
    );


    document.getElementById(
        `${prefixo}DiaClientesAtendidos`
    ).textContent = formatarNumero(
        dados.dia.clientesAtendidos
    );


    document.getElementById(
        `${prefixo}DiaMeta`
    ).textContent = formatarMoeda(
        dados.dia.meta
    );


    document.getElementById(
        `${prefixo}DiaPercentualMeta`
    ).textContent = formatarPercentual(
        dados.dia.percentualMeta
    );


    // -------------------------
    // MÊS
    // -------------------------

    document.getElementById(
        `${prefixo}MesPedidosFeitos`
    ).textContent = formatarMoeda(
        dados.mes.pedidosFeitos
    );


    document.getElementById(
        `${prefixo}MesOrcamentosPendentes`
    ).textContent = formatarMoeda(
        dados.mes.orcamentosPendentes
    );


    document.getElementById(
        `${prefixo}MesPedidosPendentes`
    ).textContent = formatarMoeda(
        dados.mes.pedidosPendentes
    );


    document.getElementById(
        `${prefixo}MesClientesAtendidos`
    ).textContent = formatarNumero(
        dados.mes.clientesAtendidos
    );


    document.getElementById(
        `${prefixo}MesMeta`
    ).textContent = formatarMoeda(
        dados.mes.meta
    );


    document.getElementById(
        `${prefixo}MesPercentualMeta`
    ).textContent = formatarPercentual(
        dados.mes.percentualMeta
    );
}


// =========================================
// BUSCAR DADOS
// =========================================

async function carregarDashboard() {

    if (!usuario) {
        return;
    }


    const codigoFuncionarioShalon =
        usuario.shalon?.codigoFuncionario;


    const codigoFuncionarioVeracci =
        usuario.veracci?.codigoFuncionario;


    if (!codigoFuncionarioShalon) {
        console.error(
            "Código do funcionário da Shalon não encontrado."
        );
    }


    if (!codigoFuncionarioVeracci) {
        console.error(
            "Código do funcionário da Veracci não encontrado."
        );
    }


    const parametros = new URLSearchParams({
        codigo_funcionario_shalon:
            codigoFuncionarioShalon || "",

        codigo_funcionario_veracci:
            codigoFuncionarioVeracci || ""
    });


    try {

        const resposta = await fetch(
            `${API_URL}/api/dashboard?${parametros.toString()}`
        );


        if (!resposta.ok) {

            const erro = await resposta.json();

            throw new Error(
                erro.detail ||
                "Erro ao carregar o dashboard."
            );
        }


        const dados = await resposta.json();


        console.log(
            "Dados do dashboard:",
            dados
        );


        // -------------------------
        // SHALON
        // -------------------------

        preencherEmpresa(
            "shalon",
            dados.shalon
        );


        // -------------------------
        // VERACCI
        // -------------------------

        preencherEmpresa(
            "veracci",
            dados.veracci
        );


    } catch (erro) {

        console.error(
            "Erro ao carregar dashboard:",
            erro
        );

        alert(
            "Não foi possível carregar os dados do dashboard."
        );
    }
}


// =========================================
// LOGOUT
// =========================================

logoutButton.addEventListener(
    "click",
    () => {

        sessionStorage.removeItem(
            "dashboardUsuario"
        );

        window.location.href = "/dashboard";
    }
);


// =========================================
// INICIALIZAÇÃO
// =========================================

mostrarLoading();
carregarDashboard();

// =========================================
// ATUALIZAÇÃO AUTOMÁTICA
// =========================================

setInterval(() => {
    carregarDashboard();
}, 2 * 60 * 1000);

