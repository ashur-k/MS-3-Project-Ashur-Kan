$("form[name=signup_form").submit(function(e){

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize(); // to send our data to backend which incase user/signup form

    $.ajax({
        url: "/user/signup",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            //console.log(resp)
            window.location.href = "/dashboard/";
        },
        error: function(resp) {
            //console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    e.preventDefault(); //to stop default form behaviour to submit itself to another page or refreshing
})

$("form[name=login_form").submit(function(e){

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize(); // to send our data to backend which incase user/signup form

    $.ajax({
        url: "/user/login",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            console.log(resp)
            window.location.href = "/dashboard/";

        },
        error: function(resp) {
            //console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    e.preventDefault(); //to stop default form behaviour to submit itself to another page or refreshing
})