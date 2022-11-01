$(document).ready(() => {
    $.get('daftar-donasi/json', (daftar_donasi) => {

    
      daftar_donasi.forEach((daftar) => {        
              $('#content').append(`
              <div class="col sec-card">
                <div class="card mb-3">
                    <img class="card-img" src="static/image/donating_card.png" class="img-fluid rounded-start">
                    <div class="card-body">
                    <h5 class="text card-title">${daftar.fields.tema_kegiatan}</h5>
                    <p class="text card-text">Dari: ${daftar.fields.pencetus_donasi}</p>
                    <span style="color: #75C270; background-color: white;" class="badge text-wrap text-truncate"> ${daftar.fields.total_donasi_terkumpul} / ${daftar.fields.target_donasi}</span>
                    <hr class="divider-card">
                    <p class="text card-text">${daftar.fields.deskripsi}</p>
                    <a href="donasi/">
                        <button type="button" class="btn-white card-button">Donate</button>
                    </a>
                    </div>
                </div>
            </div>
                  
            `)

        
         
        })
  })


  
 
})

