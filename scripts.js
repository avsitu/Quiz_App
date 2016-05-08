
var i = 0, init = true, correct = false;
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
    if(init == true) {
        pick();
        
    }
    else {
        var text = document.getElementById("input").value;
        if(obj[i].answer == text.toLowerCase()) {
            document.getElementById("output").innerHTML = "Correct! ";
            document.getElementById("next").style.display = "inline";
            i++;
            i %= 2;
            correct = true;
        }
        else
            document.getElementById("output").innerHTML = "Try Again...";
    }
}
function pick() {
    var text = document.getElementById("input").value;
    if(text.toLowerCase() == "math") {
        init = false;
        obj = math;	
        next();	
    }
    else if(text.toLowerCase() == "science") {
        init = false;
        obj = science;
        next();
    }
    else {
        document.getElementById("output").innerHTML = "Invalid Subject."
    }
}
function next() {
    //i++;
    correct = false;
    document.getElementById("output").innerHTML = "";
    document.getElementById("input").value = "";
    document.getElementById("question").innerHTML = obj[i].question;
    document.getElementById("next").style.display = "none";
}
