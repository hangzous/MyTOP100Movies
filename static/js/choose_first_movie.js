const add_movie_buttons = document.querySelectorAll('.add_movie')

add_movie_buttons.forEach(movie => {

    movie.addEventListener('click', (event) => {
        
        if (event) {

            let clicked_button = event.target

            clicked_button.id = 'chosen_movie'
            clicked_button.textContent ='✔️'
            clicked_button.setAttribute('disabled', 'disabled')


            for (const button of add_movie_buttons) {
                
                if (button.id == 'chosen_movie') {

                    var list_name = document.createElement('input')
                    list_name.required = true
                    list_name.type = 'text'
                    list_name.id = 'list_name'
                    list_name.name = 'list_name'
                    list_name.placeholder = 'Nome da Lista'

                    
                    // Atribui o elemento list_name para possibilitar a escolha do nome da lista
                    var form = document.getElementById('form')
                    form.insertBefore(list_name, form.children[1])

                    
                    if (form.children[2].id == 'list_name') {
                        form.removeChild(form.children[2])
                    }


                    var disable_search = document.getElementById('search')
                    disable_search.setAttribute('disabled', 'disabled')
                    disable_search.style.backgroundColor = 'rgba(81, 131, 131, 0.8)'


                    var enable_confirm = document.getElementById('confirm')
                    enable_confirm.removeAttribute('disabled')
                    enable_confirm.style.backgroundColor = 'rgba(119, 230, 230, .8)'


                    var selected_movie = document.getElementById('movie')
                    selected_movie.setAttribute('readonly', true)

                    let movie_name = undefined

                    movie_name = button['parentElement']['parentElement']['innerText']

                    selected_movie.value = movie_name.slice(17)


                    var remove_selected_movie = document.createElement('span')
                    remove_selected_movie.title = 'Remover Filme Selecionado'
                    remove_selected_movie.id = 'remove_selected_movie'
                    remove_selected_movie.textContent = 'X'
                    form.insertBefore(remove_selected_movie, form.children[3])

                    if (form.children[4].id == 'remove_selected_movie') {
                        form.removeChild(form.children[4])
                    }

                    remove_selected_movie.addEventListener('click', clear_input)
                    

                } else if (!button.id) {

                    button.className = 'add_movie blocked'
                    button.textContent = '❌'
                    button.setAttribute('disabled', 'disabled')

                }

                function clear_input() {

                    form.removeChild(form.children[3])
                    form.removeChild(form.children[1])


                    for (const buttons of add_movie_buttons) {

                        list_name.setAttribute('disabled', 'disabled')

                        selected_movie.removeAttribute('readonly')
                        selected_movie.value = ''

                        buttons.removeAttribute('id')
                        buttons.textContent = '➕'
                        buttons.className = 'add_movie'
                        buttons.removeAttribute('disabled')

                        disable_search.removeAttribute('disabled')
                        disable_search.style.backgroundColor = 'rgba(119, 230, 230, .8)'

                        enable_confirm.setAttribute('disabled', 'disabled')
                        enable_confirm.style.backgroundColor = 'rgba(81, 131, 131, 0.8)'
                        
                    }
                    
                }

            }   

        }

    })
    
})


