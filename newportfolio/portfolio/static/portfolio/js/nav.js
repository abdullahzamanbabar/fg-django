
let expand = document.getElementById("expand");
let collapse = document.getElementById("collapse");
let navlist = document.getElementById("navlist");
expand.style.display = 'none';
collapse.style.display = 'block';
navlist.style.display = 'flex';

function expand_collapse(){

    if (expand.style.display == "block"){
        expand.style.opacity = "0";
        expand.style.transition = "opacity 2s ease-out";
        setTimeout(function() {
            expand.style.display = "none";
            navlist.style.display = "flex"; 
            collapse.style.display = "block";
            collapse.style.opacity = "1";
            collapse.style.transition = "";     // see comment below
            collapse.onmouseover = () => collapse.style.opacity = '0.5';
            collapse.onmouseout = () => collapse.style.opacity = '1';
        }, 400);
    }
    else if (collapse.style.display == "block") {
        collapse.style.opacity = "0";
        collapse.style.transition = "opacity 2s ease-out";
        setTimeout(function() {
            collapse.style.display = "none";
            navlist.style.display = "none";
            expand.style.display = "block";
            expand.style.opacity = "1";
            expand.style.transition = "";
            expand.onmouseover = () => expand.style.opacity = '0.5';
            expand.onmouseout = () => expand.style.opacity = '1';
        }, 400);
    }
}

// If I want navlist to appear as drop down for small screen then try 

// navlist.style.display = 'block'; => instead of all flex here

/*
The reason why the opacity transition still applies even after the first time the function is called is because the opacity property is still being animated by the transition property. To make the opacity change instantly on hover after the function is called, you can remove the transition property from the elements' styles once they have been hidden
*/

// The following code is not used because I found an easy solution by cahnging background of body in css

let stikImgOrignal = document.getElementById('stik').style.backgroundImage;
let stikImgChange = document.getElementById('stik');

window.addEventListener('scroll', function() {
    var stickyDiv = document.querySelector('.sticky-top');
    var rect = stickyDiv.getBoundingClientRect();
    if (rect.top <= 0) {
      stikImgChange.style.backgroundImage = 'none';
      stikImgChange.style.backgroundColor = 'transparent';
    } else {
        stikImgChange.style.backgroundImage = stikImgOrignal;
    }
  });