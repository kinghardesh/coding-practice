let player1="none"; //rock,paper,scissors
let player2="none"; //rock,paper,scissors
let player1btns=document.querySelectorAll(".player1-choice .box");
let player2btns=document.querySelectorAll(".player2-choice .box");
let resultmsg=document.querySelector("#result-msg");
let newgamebtn=document.querySelector("#new-btn");
let resetbtn=document.querySelector("#reset-btn");

player1btns.forEach((button)=>{
    button.addEventListener("click",()=>{
        if(player1 === "none"){
            player1=button.dataset.choice;
            button.classList.add("selected");
            player1btns.forEach(btn => btn.disabled = true);
            console.log(`player 1 selected ${player1}`);
        }
    });
});

player2btns.forEach((button)=>{
    button.addEventListener("click",()=>{
        if(player2 === "none"){
            player2=button.dataset.choice;
            button.classList.add("selected");
            console.log(`player 2 selected ${player2}`);
            player2btns.forEach(btn => btn.disabled = true);
            decideWinner();
        }
    });
});
function decideWinner() {
  if (player1 === "none" || player2 === "none") return;

  if (player1 === player2) {
    resultmsg.innerText = "It's a DRAW 🤝";
  } else if (
    (player1 === "rock" && player2 === "scissors") ||
    (player1 === "paper" && player2 === "rock") ||
    (player1 === "scissors" && player2 === "paper")
  ) {
    resultmsg.innerText = "Player 1 WINS 🎉";
  } else {
    resultmsg.innerText = "Player 2 WINS 🎉";
  }
}
setTimeout(decideWinner, 600);
function resetGame() {
  player1 = "none";
  player2 = "none";
  resultmsg.innerText = "";

  document.querySelectorAll(".box").forEach(box => {
    box.classList.remove("selected");
    btn.disabled = false;
  });
}
newgamebtn.addEventListener("click", resetGame);
resetbtn.addEventListener("click", resetGame);

