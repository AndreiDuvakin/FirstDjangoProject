var currentDate = new Date();
var currentYearDateStr = document.getElementById("current_year").innerText;
var currentYearDate = new Date(currentYearDateStr);
var hourDiff = Math.abs(currentDate - currentYearDate);
var hDiff = hourDiff / 3600 / 1000;

if (hDiff < 24) {
    document.getElementById('current_year').innerText = currentDate.getFullYear();
} else {
    document.getElementById('current_year').innerText = currentYearDate.getFullYear();
}