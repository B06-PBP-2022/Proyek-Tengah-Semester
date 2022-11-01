// Fungsi ini digunakan untuk memeriksa apakah localStorage didukung oleh browser atau tidak 
const STORAGE_KEY = 'DATA_DONASI';

function isStorageExist() /* boolean */ {
  if (typeof (Storage) === undefined) {
    alert('Browser kamu tidak mendukung local storage');
    return false;
  }
  return true;
  }
  
  /**
   * Fungsi ini digunakan untuk menyimpan data ke localStorage
   * berdasarkan KEY yang sudah ditetapkan sebelumnya.
   */
function saveData(data,pk) {
  if (isStorageExist()) {
    const parsed /* string */ = JSON.stringify(data);
    localStorage.setItem(STORAGE_KEY, parsed);
      
  }
}

function getItemById(data, id) {
  var i, len;
  for (i = 0, len = data.length; i < len; i += 1) {
      console.log(data[i])
      if(id === data[i].pk) {
          return data[i];
      }
  }

  return undefined;
}

function popUp(id){
  const serializedData /* string */ = localStorage.getItem(STORAGE_KEY); // mengambil data dari localStorage
  let data = JSON.parse(serializedData);
  // console.log(id)
  let spesifikData = getItemById(data, id);
  // console.log(data)

  // console.log(spesifikData)

  const tema_kegiatan = document.getElementById('title')
  const tanggal_pembuatan = document.getElementById('tanggal_pembuatan')
  const deskripsi = document.getElementById('deskripsi')
  const total_donasi_terkumpul = document.getElementById('total-donasi-terkumpul')
  


  tema_kegiatan.innerText = spesifikData.fields.tema_kegiatan
  tanggal_pembuatan.innerText = "Dibuat pada "+ spesifikData.fields.tanggal_pembuatan
  deskripsi.innerText = spesifikData.fields.deskripsi
  total_donasi_terkumpul.innerText = "Total donasi: " + spesifikData.fields.total_donasi_terkumpul + "/" + spesifikData.fields.target_donasi


}


$(document).ready(() => {
    $.get('/form-pembuatan-donasi/json', (daftar_donasi) => {
      // console.log(daftar_donasi)
      saveData(daftar_donasi)
    
      daftar_donasi.forEach((daftar) => {  
            
              $('#content-list').append(`

              <li class="ml-1">
              <div data-toggle="modal" data-target="#exampleModalLong">
                <span id="info-${daftar.pk}">${daftar.fields.tema_kegiatan}</span>
              </div>
              </li>
                      `)

              $('.non-organisasi').append(`
              <div class="card m-4" style="background-color:#EBFBEA;">
                  <h5 class="card-header h-6" style="background-color:#75C270;color:#fff">Oleh: ${daftar.fields.pencetus_donasi}</h5>
                  <div class="card-body">
                    <h5 class="card-title h-6">${daftar.fields.tema_kegiatan}</h5>
                    <h6 class="card-subtitle mb-2 text-muted">Dibuat pada ${daftar.fields.tanggal_pembuatan}</h6>
                    <p class="card-text">${daftar.fields.deskripsi}</p>
    
                    <p class="card-text">Total donasi terkumpul: ${daftar.fields.total_donasi_terkumpul} / ${daftar.fields.target_donasi}</p>
                    <a href="donasi/" class="btn-green sbmit">Donasi</a>
                  </div>
                </div>
                  
                      `)

              $(`#info-${daftar.pk}`).click(function(){
                popUp(daftar.pk)
                $('#myModal').modal('toggle')

              })
         
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
              // console.log(resp)      
              $('#content-list').append(`
              <li class="ml-1">
              <div data-toggle="modal" data-target="#exampleModalLong">
                <span id="info-${resp.pk}">${resp.tema_kegiatan}</span>
              </div>
              </li>
              `)

              $(`#info-${resp.pk}`).click(function(){
                const tema_kegiatan = document.getElementById('title')
                const tanggal_pembuatan = document.getElementById('tanggal_pembuatan')
                const deskripsi = document.getElementById('deskripsi')
                const total_donasi_terkumpul = document.getElementById('total-donasi-terkumpul')
                

                tema_kegiatan.innerText = resp.tema_kegiatan
                tanggal_pembuatan.innerText = "Dibuat pada "+ resp.tanggal_pembuatan
                deskripsi.innerText = resp.deskripsi
                total_donasi_terkumpul.innerText = "Total donasi: " + resp.total_donasi_terkumpul + "/" + resp.target_donasi       
                $('#myModal').modal('toggle')

              })
          },
      })
    })


  })

