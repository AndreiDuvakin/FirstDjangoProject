var currentYearClient = new Date().getFullYear();
var currentYearServer = document.getElementById('current_year').innerText;

if (currentYearClient != currentYearServer) {
    document.getElementById('current_year').innerText = currentYearClient;
}