document.addEventListener("DOMContentLoaded", function () {
    const swiper = new Swiper(".swiper-container", {
        direction: "horizontal",
        loop: true,
        slidesPerView: 3,
        autoplay: {
            delay: 3000,
            disableOnInteraction: true,
        },
        spaceBetween: 20,
        grabCursor: true,
        freeMode: true,
        mousewheel: true,
        speed: 300,
    });
});




const swiperHero = new Swiper(".mySwiper", {
    spaceBetween: 30,
    effect: "fade",
    loop: true,
    hashNavigation: {
        watchState: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
    keyboard: {
        enabled: true,
    },
    autoplay: {
        delay: 6000,
        disableOnInteraction: true,
    },
    on: {

        slideChangeTransitionStart: function () {
            this.slides[this.previousIndex].classList.add("fadeOut");
            
        },
        slideChangeTransitionEnd: function () {
            this.slides.forEach((slide) => {
                slide.classList.remove("fadeOut");
            });
        },
    },
});

