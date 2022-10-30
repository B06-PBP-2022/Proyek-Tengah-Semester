$(document).ready(function(data){
    // ('#kendaraan-form').hide()
    $("#usage").change(function(){
        usage_type = $('#usage option:selected').val()
        alert(usage_type)
        if (usage_type != 'listrik'){
            $('#listrik-form').hide()
            $('#kendaraan-form').show()
        } else {
            $('#listrik-form').show()
            $('#kendaraan-form').hide()
        }
    })
    $("#calculate-btn").click(function(){
      usage_type = $('#usage option:selected').val()
        if (usage_type != 'listrik'){
            $.post(
              '/kalkulator-karbon/calculate-kendaraan/',
              {
                usage: $('#usage option:selected').val(),
                fuel_type: $('.fuel-type-class:checked').val(),
                kilometer_jarak: $('#kilometer_jarak').val(),
                litre_per_km: $('#litre_per_km').val()
              },
              function(data){
                alert(usage)
                // alert($('.fuel-type-class:checked').val())
              }
              )
              $("#kendaraan-form")[0].reset()
        } else {
          $.post(
              '/kalkulator-karbon/calculate-listrik/',
              {
                usage: $('#usage option:selected').val(),
                kilowatt_hour: $('#kilowatt_hour').val()
              },
              function(data){
                alert($('.fuel-type-class:checked').val())
              }
              )
              $("#listrik-form")[0].reset()
        }
    })

})