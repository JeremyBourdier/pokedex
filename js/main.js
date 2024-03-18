const listaPokemon = document.querySelector("#listaPokemon");
const botonesHeader = document.querySelectorAll(".btn-header");
let URL = "https://pokeapi.co/api/v2/pokemon/";

for (let i = 0; i <= 100; i++) {
    fetch(URL + i)
        .then((response) => response.json())
        .then(data => mostrarPokemon(data))
}

function mostrarPokemon(poke) {

    let tipos = poke.types.map((type) => `<p class="${type.type.name} tipo">${type.type.name}</p>`);
    tipos = tipos.join('');

    let pokeId = poke.id.toString();
    if (pokeId.length === 1) {
        pokeId = "00" + pokeId;
    } else if (pokeId.length === 2) {
        pokeId = "0" + pokeId;
    }


    const div = document.createElement("div");
    div.classList.add("pokemon");
    div.innerHTML = `
        <p class="pokemon-id-back">#${pokeId}</p>
        <div class="pokemon-imagen">
            <img src="${poke.sprites.other["official-artwork"].front_default}" alt="${poke.name}">
        </div>
        <div class="pokemon-info">
            <div class="nombre-contenedor">
                <p class="pokemon-id">#${pokeId}</p>
                <h2 class="pokemon-nombre">${poke.name}</h2>
            </div>
            <div class="pokemon-tipos">
                ${tipos}
            </div>
            <div class="pokemon-stats">
                <p class="stat">${poke.height}m</p>
                <p class="stat">${poke.weight}kg</p>
            </div>
        </div>
    `;
    div.addEventListener('click', () => mostrarDetallesPokemon(poke));
    listaPokemon.append(div);
}

function cargarListaInicial() {
    listaPokemon.innerHTML = ''; // Limpiar lista antes de cargar nuevos Pokémon

    for (let i = 1; i <= 100; i++) {
        fetch(URL + i)
            .then(response => response.json())
            .then(data => mostrarPokemon(data));
    }
}

document.querySelector('.nav').addEventListener('click', () => {
    cargarListaInicial();
});

cargarListaInicial();

function mostrarDetallesPokemon(poke) {
    listaPokemon.innerHTML = ''; // Limpia la vista actual

    // Construcción de una vista detallada
    const detallesHTML = `
        <div class="pokemon-detalle">
            <img src="${poke.sprites.other["official-artwork"].front_default}" alt="${poke.name}" class="imagen-detalle">
            <h2>${poke.name.toUpperCase()}</h2>
            <p>Id: #${poke.id}</p>
            <p>Altura: ${poke.height / 10}m</p>
            <p>Peso: ${poke.weight / 10}kg</p>
            <p>Tipo(s): ${poke.types.map(type => type.type.name).join(', ')}</p>
            <p>Estadísticas:</p>
            <ul>
                ${poke.stats.map(stat => `<li>${stat.stat.name}: ${stat.base_stat}</li>`).join('')}
            </ul>
        </div>
    `;

    listaPokemon.innerHTML = detallesHTML;
}




botonesHeader.forEach(boton => boton.addEventListener("click", (event) => {
    const botonId = event.currentTarget.id;

    listaPokemon.innerHTML = "";

    for (let i = 1; i <= 100; i++) {
        fetch(URL + i)
            .then((response) => response.json())
            .then(data => {

                if (botonId === "ver-todos") {
                    mostrarPokemon(data);
                } else {
                    const tipos = data.types.map(type => type.type.name);
                    if (tipos.some(tipo => tipo.includes(botonId))) {
                        mostrarPokemon(data);
                    }
                }

            })
    }

    
}))