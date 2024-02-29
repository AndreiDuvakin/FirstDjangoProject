var currentYearClient = new Date().getFullYear();
var currentYearServer = document.getElementById('current_year').innerText;

var diffHours = Math.abs(currentYearClient - currentYearServer);
if (diffHours > 24) {
    document.getElementById('current_year').innerText = currentYearClient;
}