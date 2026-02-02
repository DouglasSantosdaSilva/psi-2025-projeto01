// Função para carregar dados do jogador via AJAX
function carregarDetalhesJogador(id, urlBase) {
    const url = `${urlBase}${id}/`;

    fetch(url)
        .then(response => {
            if (!response.ok) throw new Error('Erro ao buscar dados');
            return response.json();
        })
        .then(data => {
            // Manipulando o DOM para exibir os dados (Aula 13)
            const modalConteudo = document.querySelector('#detalhe-ajax');
            if (modalConteudo) {
                modalConteudo.innerHTML = `
                    <div class="card-detalhe">
                        <img src="${data.foto_url || '/static/img/default.png'}" width="150">
                        <h2>${data.nome}</h2>
                        <p><strong>Posição:</strong> ${data.posicao}</p>
                        <p><strong>Idade:</strong> ${data.idade} anos</p>
                        <p><strong>Cidade:</strong> ${data.cidade}</p>
                    </div>
                `;
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            toastr.error("Não foi possível carregar os detalhes.");
        });
}