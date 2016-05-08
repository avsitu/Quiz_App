
var i = 0, init = false, correct = false;
var obj;
var math = [{question:"What is 1+1?", answer:"2"},
            {question:"What is 2*2?", answer:"4"}];
var science = [{question:"What is Newton's second law?", answer:"f=ma"},
                {question:"What is life?", answer:"ball is life"}];
                
document.getElementById("question").innerHTML = "What subject?";

//enter instead of click for input
$(document).ready(function(){
    $("#input").keypress(function(e){
        if(e.keyCode==13){
            if(correct)
                $("#next").click();
            else
                $("#submit").click();
        }
    });
});

function processInput() {
        var text = document.getElementById("input").value;
        if(init == false){
            init = true; 
            
            if("math" == text.toLowerCase())
                pickmath();
            else
                pickscience();
        }
        
        else if(obj[i].answer == text.toLowerCase()) {
            document.getElementById("wrong").style.display = "none";
            document.getElementById("correct").style.display = "block"; 
            document.getElementById("next").style.display = "inline";
            i++;
            i %= 2;
            correct = true;
        }
        else
            document.getElementById("wrong").style.display = "block";
}
function pickmath() {
    document.getElementById("dd").innerHTML = "Math ";
    obj = math;
    next();
}
function pickscience() {
    document.getElementById("dd").innerHTML = "Science ";
    obj = science;
    next();
}
function next() {
    //i++;
    correct = false;
    document.getElementById("input").value = "";
    document.getElementById("question").innerHTML = obj[i].question;
    document.getElementById("next").style.display = "none";
    document.getElementById("correct").style.display = "none"; 
}
