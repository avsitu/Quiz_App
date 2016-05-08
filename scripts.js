
var i = 0, init = true;
var obj;
var math = [{question:"What is 1+1?", answer:"2"},
            {question:"What is 2*2?", answer:"4"}];
var science = [{question:"What is Newton's second law?", answer:"f=ma"},
                {question:"What is life?", answer:"ball is life"}];
document.getElementById("question").innerHTML = "What subject?";
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
    document.getElementById("output").innerHTML = "";
    document.getElementById("input").value = "";
    document.getElementById("question").innerHTML = obj[i].question;
    document.getElementById("next").style.display = "none";
}