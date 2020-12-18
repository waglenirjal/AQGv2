$(document).ready(function(){
            $('#exampleModal').modal('show');
        });
var saveAnsButton;

function ruun(){
    start();
    saveAnsButton = document.getElementById('submit');
    saveAnsButton.onclick = getanswers
}

var ID = 0;
var seconds = 0;
var minute = 44;
var hour = 1;
function printMsg(){
    document.getElementById('op').innerHTML = hour+' : '+minute+' : ' + seconds;
    if(seconds == 59){
        seconds = 0;
        minute++;
    }
    if(minute == 59){
        seconds = 0;
        minute = 0;
        hour++;
    }
    if(hour == 1 && minute == 45){
        document.getElementById("op").style.color = "red";
        seconds = 0;
        minute++;
    }
    if(hour==2){
        window.location.replace('/home/dashboard/result');
    }
    else{
        seconds++;
    }

}
function start(){
    ID = window.setInterval(printMsg, 1000);
}
function stop(){
    window.clearInterval(ID);
}
answerList = []
function getanswers(){
    alert('I am in');
    var e = document.getElementsByTagName('input');
    for(i=0; i<e.length; i++){
        if(e[i].type == 'radio'){
            if(e[i].checked){
                answerList.push(e[i].value);
            }
        }
    }
    alert(answerList);
//            let csr = $('input[name=csrfmiddletoken').val();
//            mydata = {ans: answerList, csrfmiddlewaretoken: csr};

    alert('going inside');
    var urlData = "http://127.0.0.1:8000/home/dashboard/dataz";
    var req = new XMLHttpRequest();
    alert(urlData);
    $.ajax({
        url: urlData,
        type: 'POST',
        data: {'ans': answerList},
        traditional: true,
        dataType: 'html',
        success:function(result){
            console.log('You are shit');
        }
    });
    alert('Answer is Submitted');
}
