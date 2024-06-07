function Watch(){
    let time = new Date();
    let Hours = time.getHours();
    const meridiem = Hours >= 12 ? "PM" : "AM";
    Hours = Hours >= 12 ? Hours - 12 : Hours;
    Hours = Hours.toString().padStart(2,0)
    let Minutes = time.getMinutes().toString().padStart(2,0);
    let Seconds = time.getSeconds().toString().padStart(2,0);
    console.log(Minutes);
    document.getElementById("myWath").textContent = `${Hours} : ${Minutes} : ${Seconds} ${meridiem}`;
}
Watch()
setInterval(Watch,1000)