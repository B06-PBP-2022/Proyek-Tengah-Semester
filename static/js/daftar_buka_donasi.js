
$(document).ready(() => {
    $.get('/form-pembuatan-donasi/json', (daftar_donasi) => {
      console.log(daftar_donasi)
    
      daftar_donasi.forEach((daftar) => {  
        
            $('#content-list').append(`
            <li class="ml-1"><a href="#" target="_blank">${daftar.fields.tema_kegiatan}</a></li>
                
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