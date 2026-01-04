let boxes= document.querySelectorAll(".box");
let RESETBTN=document.querySelector("#RBTN");
let turnO =true; //player X,player O
let newgamebtn=document.querySelector("#new-btn");
let msgcontainer=document.querySelectorAll(".msg-container");
let msg=document.querySelector("#msg");
let winningCombos=[
    [0,1,2],
    [0,3,6],
    [0,4,8],
    [1,4,7],
    [2,5,8],
    [2,4,6],
    [3,4,5],
    [6,7,8]
];
const resetGame = () => {
  turnO = true;

  boxes.forEach((box) => {
    box.innerText = "";
    box.disabled = false;
  });

  msg.innerText = "";
  msgcontainer.classList.add("hide");
};

boxes.forEach((box)=>{
    box.addEventListener("click",()=>{
        console.log("box clicked");
        if(turnO){
            box.innerText="O";
            turnO=false;
        }
        else{
            box.innerText="X";
            turnO=true;
        }
        box.disabled=true;
        checkwinner();
         
    })
});
    const disableBoxes = () => {
        for(box of boxes){
            box.disabled = true;
        }
    };
    const enableBoxes = () => {
        for(box of boxes){
            box.disabled = false;
            msgcontainer.classList.add("hide"); 
            box.innerText = "";
        }
    };
    const showWinnerMessage = (winner) => {
        msg.innerText=`congratualtions the winner is ${winner}`;
        disableBoxes();
    };

    const checkwinner = () => {
        for(pattern of winningCombos){
            let pos1=boxes[pattern[0]].innerText;
            let pos2=boxes[pattern[1]].innerText;
            let pos3=boxes[pattern[2]].innerText;
            if(pos1 !="" && pos2 !="" && pos3 !="" ){
                if(pos1===pos2 && pos2===pos3){
                    console.log("we have a winner",pos1);
                    showWinnerMessage(pos1);
                }
            }
        }    
    }
    newgamebtn.addEventListener("click",resetGame);
    RESETBTN.addEventListener("click",resetGame);






