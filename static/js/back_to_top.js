
const back_button = document.querySelector(".back_to_top")

document.addEventListener("scroll", () => {
    
    if (document.documentElement.scrollTop > 2400) {
        
        back_button.classList.remove("hidden")

    } else {
        
        back_button.classList.add("hidden")

    }

})


back_button.addEventListener('click', () => {
    document.documentElement.scrollIntoView({ behavior : "smooth" })
})