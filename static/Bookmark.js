function bookQues(){
    var ques_tag = $("input[name$='intqno_tag']").val();

    var postUrl = "http://127.0.0.1:8000/home/dashboard/book";
    var req = new XMLHttpRequest();
    $.ajax({
        url: postUrl,
        type: 'POST',
        data: {'ques_tag':ques_tag},
        traditional: true,
        dataType: 'html',
        success: function(result){
            console.log('You are shit')
            }

    });

}

function delbook(quesID){
    var postUrl = "http://127.0.0.1:8000/home/dashboard/delbook";
    var req = new XMLHttpRequest();
    $.ajax({
        url: postUrl,
        type: 'POST',
        data: {'quesID':quesID},
        traditional: true,
        dataType: 'html',
        success: function(result){
            console.log('You are shit');
            window.location.reload(true);
            }
    });



}