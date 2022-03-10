let list = document.getElementById('list')
let options = document.getElementById('options')

if (list.children[1]) {
    options.removeChild(options.children[0])
}