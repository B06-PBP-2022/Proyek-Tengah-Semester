$(document).ready(function () {
    showFaq();
  }); 

// fungsi POST
function addFaq() {
    fetch("add/", {
      method: "POST",
      body: new FormData(document.querySelector('#form'))
    }).then(showFaq)
    document.getElementById("form").reset();
    return false
  }

// fungsi get data todolist
function showFaq() {
    let htmlString = "";
    let count = 0;
    $.ajax({
      url: "json",
      type: "GET",
      dataType: "json",
      success: function(data) {
        data.forEach(faq => {
          htmlString += `
          <div class="accordion-item">
                <h2 class="accordion-header" id="panelsStayOpen-heading${count}">
                    <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse${count}" aria-expanded="true" aria-controls="panelsStayOpen-collapse${count}">
                        ${faq.fields.question}
                    </button>
                </h2>
                <div id="panelsStayOpen-collapse${count}" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-headingO${count}">
                    <div class="accordion-body">
                      <span style="background-color: #75C270; margin-bottom: 8px;" class="badge">asked by ${faq.fields.username}</span>
                      <br>
                        <strong style="color: #75C270;">jawaban: ${faq.fields.answer}</strong>
                    </div>
                </div>
            </div>`
          ;
          count++;
          $('#accordionPanelsStayOpenExample').html(htmlString);
      })
    }, error: function(data) {
      console.log("error");
    }
  })
  };

  

document.getElementById("button").onclick = addFaq