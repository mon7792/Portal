$('.navbar-brand').on('click',function(e){
        e.preventDefault();
        $('.sidebar').toggleClass('nav-open');
        $('.main').toggleClass('nav-open');
    });