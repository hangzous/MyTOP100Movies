const mobile_menu = document.getElementById('mobile_menu')
const nav_menu = document.getElementById('menu')
const ul_element = document.querySelector('#menu nav ul')

mobile_menu.addEventListener('click', () => {

    if (nav_menu.className) {
        nav_menu.removeAttribute('class')
    }

    document.body.style.overflowX = 'hidden'
    document.body.style.overflowY = 'hidden'


    span = document.createElement('span')
    span.id = 'dark_background'

    span.addEventListener('click', () => {

        nav_menu.style.display = 'none'

        document.body.removeChild(span)

        document.body.style.overflowY = 'visible'
        document.body.style.overflowX = 'visible'

        nav_menu.className = 'closed'
        span.className = 'invisible'

    })

    document.body.append(span)

    nav_menu.style.display = 'flex'

    
    for (const li of ul_element.children) {

        let hr = document.createElement('hr')

        if (li.children[1]) {
            li.removeChild(li.children[1])
        } 

        li.appendChild(hr)
   
    }

})
