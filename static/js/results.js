document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const sintomas = urlParams.get('sintomas');

    document.getElementById('sintomas').textContent = sintomas;
});