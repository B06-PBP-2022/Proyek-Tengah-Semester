
$(document).ready(() => {
    $.get('/form-pembuatan-donasi/json', (daftar_donasi) => {
      console.log(daftar_donasi)
    
      daftar_donasi.forEach((daftar) => {  
        
            $('#content-list').append(`
            <li class="ml-1"><a href="#" target="_blank">${daftar.fields.tema_kegiatan}</a></li>
                
                    `)
        })
  })


  $.get('/form-pembuatan-donasi/json', (daftar_donasi) => {
    console.log(daftar_donasi)
  
    daftar_donasi.forEach((daftar) => {  
      
          $('.non-organisasi').append(`
          <div class="card m-4" style="background-color:#EBFBEA;">
              <h5 class="card-header h-6" style="background-color:#75C270;color:#fff">Oleh: ${daftar.fields.user}</h5>
              <div class="card-body">
                <h5 class="card-title h-6">${daftar.fields.tema_kegiatan}</h5>
                <h6 class="card-subtitle mb-2 text-muted">Dibuat pada ${daftar.fields.tanggal_pembuatan}</h6>
                <p class="card-text">${daftar.fields.deskripsi}</p>

                <p class="card-text">Total donasi terkumpul: ${daftar.fields.total_donasi_terkumpul} /  ${daftar.fields.target_donasi}</p>
                <a href="#" class="btn btn-success" style="background-color:#4A9745">Donasi</a>
              </div>
            </div>
              
                  `)
      })
})


  
    $('#form').submit((e) => {
      e.preventDefault();
      $.ajax({
          url: '/form-pembuatan-donasi/open-donasi/',
          type: 'POST',
          dataType: 'json',
          data: $('#form').serialize(),
          success: (resp) => {
              
              console.log(resp)
              $('#content-list').append(`
              <li class="m-1"><a href="#" target="_blank">${resp.tema_kegiatan}</a></li>
              `)
          },
      })
    })


  })

