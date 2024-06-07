const startBtn = document.getElementById("start");
const stopBtn = document.getElementById("stop");

let Minutes = 0;
let Seconds = 0;
let hundredthsSecond = 0;
function MyTimer() {
    hundredthsSecond = hundredthsSecond + 1;
    if (hundredthsSecond >= 100) {
        Seconds = Seconds + 1;
        hundredthsSecond = 0;
    }
    if (Seconds >= 60) {
        Seconds = 0
        Minutes = Minutes + 1
    }
    document.getElementById("myTimer").textContent = `${Minutes} : ${Seconds} : ${hundredthsSecond}`;

}

startBtn.addEventListener("click", start);

let myInterval;

function start() {
    myInterval = setInterval(MyTimer, 1000);
    startBtn.disabled = true;
    stopBtn.disabled = false;
}

function stop(event2) {
    clearInterval(myInterval);
    startBtn.disabled = false;
    stopBtn.disabled = true;
}


stopBtn.addEventListener("click", stop);

