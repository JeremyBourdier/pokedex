(function () {
    const POKEMON_API_URL = 'https://pokeapi.co/api/v2/pokemon/';
    const searchInput = document.getElementById('search');
    const listaPokemon = document.getElementById('listaPokemon');

    function showError(message) {
        listaPokemon.innerHTML = `<p class="error">${message}</p>`;
    }

    async function searchPokemon() {
        const searchedPokemon = searchInput.value.toLowerCase();

 
        if (searchedPokemon.trim() === '') {
            listaPokemon.innerHTML = '';

            // Recarga la lista inicial de Pokémon
            for (let i = 1; i <= 100; i++) {
                fetch(URL + i)
                    .then((response) => response.json())
                    .then(data => mostrarPokemon(data));
            }
            return; 
        }

        try {
            const response = await fetch(`${POKEMON_API_URL}${searchedPokemon}`);
            if (!response.ok) {
                showError(`No se encontró ningún Pokémon llamado "${searchedPokemon}".`);
                return;
            }
            const data = await response.json();

            listaPokemon.innerHTML = ''; // Limpiar lista antes de mostrar resultado
            mostrarPokemon(data); // Muestra el Pokémon buscado
        } catch (error) {
            showError('Ha ocurrido un error al buscar el Pokémon');
            console.error(error);
        }
    }


    // Event listeners
    document.querySelector('#searchButton').addEventListener('click', searchPokemon);
    searchInput.addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
            searchPokemon();
        }
    });


})();
