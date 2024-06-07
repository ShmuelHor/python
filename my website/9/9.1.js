const myBox1 = document.getElementById("yellow");
const myBox2 = document.getElementById("green");
const myBox3 = document.getElementById("blue");

function windowAlert(event1){
    // event.target.style.backgroundColor = "tomato"
    window.alert(`What's up man`);
}
myBox1.addEventListener("click",windowAlert)

function changeText(event2){
    event2.target.textContent = "What's up man"
}
myBox2.addEventListener("mouseover",changeText)

function changeTextGreen(event3){
    document.getElementById("green").textContent = `עבור מעליי`;

}
myBox3.addEventListener("mouseout",changeTextGreen)