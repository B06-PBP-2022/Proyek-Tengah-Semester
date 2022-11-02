// type="text/javascript"

function postNom() {
    fetch("add/",{
        method:"POST",
        body: new FormData(document.querySelector('#forms'))
    }).then(showNominal)
    document.getElementById("forms").reset();
    return false
}

// $(document).ready(function(){
//     fetch("pembayaran/",{
//         method:"POST",
//         body: new FormData(document.querySelector('#forms'))
//     }).then(showNominal)
//     document.getElementById("forms").reset();
//     return false
    
// });



function showNominal(){
    let str="";
    $.ajax({
        url: "json",
        type: "GET",
        dataType: "json",
        success: function(data) {
            document.getElementById("forms").style.display = "none";
            data.forEach(e => {
                str= `
                <div class="accordion-item">
                    <h2 class="accordion-header">
                        Total pembayaran <br>
                        <br>
                        Rp ${e.fields.nominal}
                    </h2>
                </div>`
                ;
            });
            $('#accordionPanelsStayOpenExample').html(str);
            
            
        }

    })
};
document.getElementById("submitbayar").onclick = postNom
