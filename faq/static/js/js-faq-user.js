$(document).ready(function () {
    showFaq();
  }); 

// fungsi POST
function addFaq() {
    fetch("add/", {
      method: "POST",
      body: new FormData(document.querySelector('#form'))
    }).then(showFaq)
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
                        ${faq.fields.answer}
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