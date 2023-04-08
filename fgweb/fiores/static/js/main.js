$(document).ready(function () {
    const $hamburgerButton = $("#toggle-button");
    const $closeButton = $(".toggled-navbar button");
    const $toggledNavbar = $(".toggled-navbar");
  
    $hamburgerButton.on("click", function () {
      $toggledNavbar.addClass("show");
    });
  
    $closeButton.on("click", function () {
      $toggledNavbar.removeClass("show");
    });
  });
  


function navbarScript() {
    $(window).scroll(function () {
      const scrollTop = $(window).scrollTop();
      if (scrollTop > 400) {
        $(".main-navbar").fadeOut();
      } else {
        $(".main-navbar").fadeIn();
      }
    });
    let navbarDown = false;
  
    $(document).on("mousemove", function (e) {
      const scrollTop = $(window).scrollTop();
      if (scrollTop > 400 && e.clientY <= 80 && !navbarDown) {
        $(".main-navbar").stop(true, true).fadeIn();
        navbarDown = true;
      } else if (scrollTop <= 400 && navbarDown) {
        $(".main-navbar").stop(true, true).fadeOut();
        navbarDown = false;
      }
    });
  
    $(".main-navbar").on("mouseleave", function () {
      const scrollTop = $(window).scrollTop();
      if (scrollTop > 400 && navbarDown) {
        $(".main-navbar").stop(true, true).fadeOut();
        navbarDown = false;
      }
    });
  }
  
  const mediaQuery = window.matchMedia("(min-width: 768px)");
  
  if (mediaQuery.matches) {
    navbarScript();
  }
  
  mediaQuery.addEventListener("change", (event) => {
    if (event.matches) {
      navbarScript();
    }
  });
  

 