let navbar = $(".navbar-custom")
console.log(navbar)

window.addEventListener('scroll', () => {
    console.log(window.scrollY)
    if (window.scrollY > 50) {
        navbar.addClass('hide-nav')
        console.log(navbar)
    }else{
        navbar.removeClass('hide-nav')
    }
})