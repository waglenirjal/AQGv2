//       $(document).ready(function(){
//            $('#exampleModal').modal('show');
//        });

window.onload = initall;
var saveAnsButton;

function initall(){
    start();
    saveAnsButton = document.getElementById('submit');
    saveAnsButton.onclick = getanswers
}

var ID = 0;
var seconds = 45;
var minute = 58;
var hour = 1;
function printMsg(){

    if(seconds == 59){
        seconds = -1;
        minute++;
    }
    if(minute == 59){
        seconds = -1;
        minute = 0;
        hour++;
    }
    if(hour == 1 && minute == 45){
        document.getElementById("op").style.color = "red";
        seconds = -1;
        minute++;
    }
    if(hour==2){
        stop();
        alert('Time is Up. <br> Go Below at End and Click on Done');
        getanswers();
    }
    else{
        seconds++;
    }
    document.getElementById('op').innerHTML = hour+' : '+minute+' : ' + seconds;
}
function start(){
    ID = window.setInterval(printMsg, 1000);
    console.log(ID);
}
function stop(){
    window.clearInterval(ID);
}

answerList = []
function getanswers(){

    var e = document.getElementsByTagName('input');
    console.log(e.length);
    for(i=0; i<e.length; i++){
        if(e[i].type == 'radio'){
            if(e[i].checked){
                answerList.push(e[i].value);
            }
        }
    }

//            let csr = $('input[name=csrfmiddletoken').val();
//            mydata = {ans: answerList, csrfmiddlewaretoken: csr};


    var urlData = "http://127.0.0.1:8000/home/dashboard/dataz";
    var req = new XMLHttpRequest();

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
    saveAnsButton = document.getElementById('submit');
    var x = document.getElementById('done');
    saveAnsButton.style.display = 'none';
    x.style.display = 'block';
}
