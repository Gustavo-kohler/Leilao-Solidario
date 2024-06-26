var countdownElement = document.getElementById("countdown");
var timeLeft = parseInt(countdownElement.getAttribute('data-time-left'));

function formatTime(seconds) {
    var hours = Math.floor(seconds / 3600);
    var minutes = Math.floor((seconds % 3600) / 60);
    var seconds = seconds % 60;
    return (hours < 10 ? "0" + hours : hours) + ":" +
           (minutes < 10 ? "0" + minutes : minutes) + ":" +
           (seconds < 10 ? "0" + seconds : seconds);
}

var countdownElement = document.getElementById("countdown");
var countdownInterval = setInterval(function() {
    timeLeft--;
    countdownElement.textContent = formatTime(timeLeft);
    if (timeLeft <= 0) {
        clearInterval(countdownInterval);
        countdownElement.textContent = "00:00:00";
    }
}, 1000);