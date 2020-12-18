window.onload = initall;
var saveAnsButton;
var starting;
var ending;
var keeper;

function initall(){
    starting = new Date().getTime();
    saveAnsButton = document.getElementById('save_ans');
    saveAnsButton.onclick = saveans;
}

function saveans(){
    ending = new Date().getTime();
    keeper = (ending - starting)/1000;

    var e = document.getElementsByTagName("input");
    var anslist = []
    console.log('I am IN');
    var ans = $("input:radio:checked").val();


//    for (i=0; i<e.length; i++){
//        if(e[i].type=="radio"){
//            if(e[i].checked){
//                anslist.push(e[i].value);
//            }
//        }
//    }
    var postUrl = "http://127.0.0.1:8000/home/dashboard/saveQans";
    var req = new XMLHttpRequest();
    $.ajax({
        url: postUrl,
        type: 'POST',
        data: {'ans': ans, 'time':keeper},
        traditional: true,
        dataType: 'html',
        success: function(result){
            console.log('You are shit')
            }

    });
    saveAnsButton = document.getElementById('save_ans');
    var x = document.getElementById('next');
    saveAnsButton.style.display = 'none';
    x.style.display = 'block';
}