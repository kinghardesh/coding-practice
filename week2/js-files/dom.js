document.getElementById("changeHeading").innerText="we are changing heading using js file";
function changeHeading(){
    document.getElementById("changeHeading").innerText="Heading changed";
}
document.getElementsByTagName("pre")[0].innerText="This is changed using DOM";
document.getElementsByClassName("text")[0].style.color="red";
document.getElementsByClassName("text")[1].style.fontSize="30px";
const ul = document.getElementsByTagName("ul")[0];
const li = document.createElement("li");
li.textContent = "banana";
ul.appendChild(li);
const li2 = document.createElement("li");
li2.textContent = "grapes";
ul.appendChild(li2);
function change() {
  document.getElementById("msg").innerText = "Changed!";
}
function check() {
    let n=document.getElementById("num").value;
    console.log(n);
}
document.getElementById("btn").addEventListener("click",dowork);
function dowork(){
    console.log("button clicked");
}


