document.addEventListener("DOMContentLoaded", function() {
    const fondo = document.querySelector("#contenedor-fondo");
    const loginLinks = document.querySelectorAll(".login-link");
    const forgotPasswordLink = document.querySelector(".forgot-password-link");
    const iconoCerrar = document.querySelector(".icono-cerrar");
    const btnIniciarSesion = document.querySelector("#btn-iniciar-sesion");

    loginLinks.forEach(link => {
        link.addEventListener("click", (event) => {
            event.preventDefault(); // Prevenir la acción por defecto del enlace
            fondo.classList.remove('active');
            fondo.querySelector('.contenedor-form.login').style.transform = 'translateX(0)';
            fondo.querySelector('.contenedor-form.forgot-password').style.transform = 'translateX(400px)';
        });
    });

    forgotPasswordLink.addEventListener("click", (event) => {
        event.preventDefault(); // Prevenir la acción por defecto del enlace
        fondo.classList.add('active');
        fondo.querySelector('.contenedor-form.forgot-password').style.transform = 'translateX(0)';
        fondo.querySelector('.contenedor-form.login').style.transform = 'translateX(-400px)';
    });

    iconoCerrar.addEventListener("click", () => {
        fondo.classList.remove('active');
        fondo.classList.remove('active-btn');
        fondo.querySelector('.contenedor-form.login').style.transform = 'translateX(0)';
        fondo.querySelector('.contenedor-form.forgot-password').style.transform = 'translateX(400px)';
    });

    btnIniciarSesion.addEventListener("click", () => {
        fondo.classList.remove('hidden');
    });
});
