// const myModal = document.getElementById('myModal')
// const myInput = document.getElementById('myInput')

// myModal.addEventListener('shown.bs.modal', () => {
//     myInput.focus()
// })

$(document).ready( function(){
    $('#submit-username-button').click( function(){
        let username= $('#id-username').val();
        let CSRFtoken = $('input[name="csrfmiddlewaretoken"]').val();
        // alert("TERTEKAN")
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
                    $('#id-name-header').text(username);
                    $('#id-username').val("");
                    $('#id-username-content').text(username);
                    $('#edit-username-div').hide;
            } else {
                alert('Username is not available');
            }
        });
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

// function submit_username() {
//     console.log("TERTEKAN")
// }

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