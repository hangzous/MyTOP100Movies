const hamburger = document.querySelector('#mobile_menu img')
const menu = document.querySelector('header #menu')
const close_icon = document.querySelector('img#close')

hamburger.addEventListener('click', () => {
    menu.className = 'onscreen'
    close_icon.className = 'close'
    document.body.style.overflowY = 'hidden'
    document.body.style.overflowX = 'hidden'
    hamburger.style.display = 'hidden'
})

close_icon.addEventListener('click', () => {
    menu.className = ''
    close_icon.className = ''
    hamburger.style.display = 'block'
    document.body.style.overflowY = 'auto'
})