const buttons = document.querySelectorAll('.select_movie')
const form = document.querySelector('form')

buttons.forEach(btn => {
    btn.addEventListener('click', (event) => {

        if (event) {
        
            var container_movie = document.createElement('div')
            var movie_name = document.createElement('input')
            var remove_movie = document.createElement('span')

            movie_name.id = 'movie_name'
            movie_name.name = 'movie_name'
            movie_name.setAttribute('readonly', true)

            movie_name.value = btn.previousElementSibling.textContent

            remove_movie.textContent = 'X'

            if (form.children[4].tagName == 'DIV') {
                form.removeChild(form.children[4])
            }

            form.insertBefore(container_movie, form.children[4])
            
            container_movie.appendChild(movie_name)
            container_movie.appendChild(remove_movie)

            form.children[1].removeAttribute('disabled')
            form.children[3].setAttribute('disabled', true)
            form.children[5].setAttribute('disabled', true)
            form.children[7].removeAttribute('disabled')

            // Quando o evento acontece, o método HTTP muda de GET para POST
            form.method = 'post'

        }

        remove_movie.addEventListener('click', () => {
            form.removeChild(form.children[4])
            form.children[1].setAttribute('disabled', true)
            form.children[3].removeAttribute('disabled')
            form.children[4].removeAttribute('disabled')
            form.children[6].setAttribute('disabled', true)

            form.method = 'get'
        })

    })  
})
