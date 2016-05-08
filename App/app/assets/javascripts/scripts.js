var i = 0, init = false, correct = false;
var mobj;
var sobj;
var obj;
var math = [{question:"What is 1+1?", answer:"2"},
            {question:"What is 2*2?", answer:"4"}];
var science = [{question:"What is Newton's second law?", answer:"f=ma"},
                {question:"What is life?", answer:"ball is life"}];
                
//document.getElementById("question").innerHTML = "What subject?";
function initialize(marr, sarr) {
    mobj = marr;
    sobj = sarr;
    document.getElementById("question").innerHTML = "Choose subject.";

}
//enter instead of click for input
function skip() {
    i++;
    i %= 100;
    document.getElementById("question").innerHTML = obj[i].ask;
    document.getElementById("cheat").style.display="none";
}
function cheat() {
    document.getElementById("cheat").innerHTML = obj[i].correct_answer;
    document.getElementById("cheat").style.display="inline";
}
function processInput() {
        var text = document.getElementById("input").value;
        /*if(init == false){
            //init = true; 
            //window.alert("WTF?")
            if("math" == text.toLowerCase())
                pickmath();
            else if("science" == text.toLowerCase())
                pickscience();
        }
        
        else {*/
            if(obj[i].correct_answer.toLowerCase() == text.toLowerCase()) {
                //window.alert("???");
                document.getElementById("wrong").style.display = "none";
                document.getElementById("correct").style.display = "block"; 
                document.getElementById("next").style.display = "inline";
                document.getElementById("skip").style.display = "none";
                correct = true;

            }
            else
                document.getElementById("wrong").style.display = "block";
        //}
}
function pickmath() {
    init = true;
    document.getElementById("dd").innerHTML = "Math ";
    obj = mobj;
    //document.myform.subject.value = "Math";
    next();
}
function pickscience() {
    init = true;
    document.getElementById("dd").innerHTML = "Science ";
    obj = sobj;
    //document.myform.subject.value = "Science";
    next();
}
function next() {
    i++;
    i %= 100;
    correct = false;
    document.getElementById("input").value = "";
    document.getElementById("skip").style.display = "inline";
    document.getElementById("cheat").style.display="none";
    document.getElementById("question").innerHTML = obj[i].ask;
    document.getElementById("wrong").style.display = "none";
    document.getElementById("next").style.display = "none";
    document.getElementById("correct").style.display = "none"; 
}
