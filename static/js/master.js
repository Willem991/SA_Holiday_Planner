let navbar = $(".navbar-custom")

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.addClass('hide-nav')
    }else{
        navbar.removeClass('hide-nav')
    }
})

//Bar Expansion

const bars = document.querySelectorAll('.bar');
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        console.log(bars)
        if (entry.isIntersecting) {
        // Add animation classes based on which bar it is
            if (entry.target.classList.contains('bar1')) {
                entry.target.classList.add('animate-left');
            } else if (entry.target.classList.contains('bar2')) {
                entry.target.classList.add('animate-right');
            } else if (entry.target.classList.contains('bar3')) {
                entry.target.classList.add('animate-left');
            }
            observer.unobserve(entry.target); // animate only once
        }
    });
}, { threshold: 0.6 });

bars.forEach(bar => observer.observe(bar));