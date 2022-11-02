$(document).ready( function(){
    $('#submit-username-button').click( function(){
        alert("TERTEKAN");
        let username= $('#id-username').val();
        let CSRFtoken = $('input[name="csrfmiddlewaretoken"]').val();
        // alert("TERTEKAN");
        $.ajax({
            url:'username-available/',
            type:'GET',
            data:{username:username}
        }).done(function(response){
            if(response=="True"){
                $.post('change-username/', {
                    username: username,
                    csrfmiddlewaretoken: CSRFtoken
                });
                $('#id-username').val("");
                $('#id-username-content').text(username);
                $('#edit-username-div').hide;
            } else {
                alert('Username is not available');
            }
        });
    })

    $('#submit-contact-button').click( function(){
        let contact= $('#id-contact').val();
        let CSRFtoken = $('input[name="csrfmiddlewaretoken"]').val();
        alert("TERTEKAN");
        $.ajax({
            url:'change-contact/',
            type:'POST',
            data:{contact:contact, csrfmiddlewaretoken:CSRFtoken}
        }).done(function(response){
            $('#id-contact').val("");
            $('#id-contact-content').text(contact);
            $('#edit-contact-div').hide;
        });
    })

    $('#submit-email-button').click( function(){
        let email= $('#id-email').val();
        let CSRFtoken = $('input[name="csrfmiddlewaretoken"]').val();
        alert("TERTEKAN");
        
        // Validasi email
        if (ValidateEmail(email)){
            $.ajax({
                url:'change-email/',
                type:'POST',
                data:{email:email, csrfmiddlewaretoken:CSRFtoken}
            }).done(function(response){
                $('#id-email').val("");
                $('#id-email-content').text(email);
                $('#edit-email-div').hide;
            });
        } else {
            alert('Email is not valid');
        }
    })
})

function edit_username_button() {
    $("#edit-username-div").show();
    $("#edit-username-button").hide();
}

function close_edit_username() {
    $("#edit-username-div").hide();
    $("#edit-username-button").show();
}

function edit_contact_button() {
    $("#edit-contact-div").show();
    $("#edit-contact-button").hide();
}

function close_edit_contact() {
    $("#edit-contact-div").hide();
    $("#edit-contact-button").show();
}


function edit_email_button() {
    $("#edit-email-div").show();
    $("#edit-email-button").hide();
}

function close_edit_email() {
    $("#edit-email-div").hide();
    $("#edit-email-button").show();
}

function ValidateEmail(input) {

    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  
    if (input.value.match(validRegex)) {
        return true;
    } else {
        return false;
    } 
}