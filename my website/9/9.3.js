const send1 = document.getElementById("1");
const send2 = document.getElementById("3");
const stop1 = document.getElementById("2");
const stop2 = document.getElementById("4");

let time ;
function sendMessagesAlert(event1){
    // event.target.style.backgroundColor = "tomato"
    time = setTimeout(() => window.alert(`What's up man`), 3000);
    console.log("aaaa")
}
send1.addEventListener("click",sendMessagesAlert);

function sendMessagesLog(event1){
    // event.target.style.backgroundColor = "tomato"
    time = setTimeout(() => console.log(`What's up man`), 3000);
    console.log("cccc")
}
send2.addEventListener("click",sendMessagesLog);

function stop(event2){
    clearTimeout(time);
    console.log("dddd")
}
stop2.addEventListener("click",stop);
stop1.addEventListener("click",stop);