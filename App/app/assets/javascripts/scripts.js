var i = 0, init = false, correct = false;
var obj;
var math = [{question:"What is 1+1?", answer:"2"},
            {question:"What is 2*2?", answer:"4"}];
var science = [{question:"What is Newton's second law?", answer:"f=ma"},
                {question:"What is life?", answer:"ball is life"}];
                
//document.getElementById("question").innerHTML = "What subject?";

//enter instead of click for input
function processInput() {
        var text = document.getElementById("input").value;
        if(init == false){
            //init = true; 
            window.alert("WTF?")
            if("math" == text.toLowerCase())
                pickmath();
            else if("science" == text.toLowerCase())
                pickscience();
        }
        
        else {
            if(obj[i].answer == text.toLowerCase()) {
                //window.alert("???");
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
}
function pickmath() {
    init = true;
    document.getElementById("dd").innerHTML = "Math ";
    obj = math;
    next();
}
function pickscience() {
    init = true;
    document.getElementById("dd").innerHTML = "Science ";
    obj = science;
    next();
}
function next() {
    correct = false;
    document.getElementById("input").value = "";
    document.getElementById("question").innerHTML = obj[i].question;
    document.getElementById("wrong").style.display = "none";
    document.getElementById("next").style.display = "none";
    document.getElementById("correct").style.display = "none"; 
}
