$(document).ready(function(data){
    // ('#kendaraan-form').hide()
    $("#usage").change(function(){
        usage_type = $('#usage option:selected').val()
        if (usage_type != 'listrik'){
            $('#listrik-form').hide()
            $('#kendaraan-form').show()
        } else {
            $('#listrik-form').show()
            $('#kendaraan-form').hide()
        }
        $("#hasil_kalkulasi").html("0")
    })
    $("#calculate-btn").click(function(){
      usage_type = $('#usage option:selected').val()
        if (usage_type != 'listrik'){
            $.post(
              'calculate-kendaraan/',
              {
                usage: $('#usage option:selected').val(),
                fuel_type: $('.fuel-type-class:checked').val(),
                kilometer_jarak: $('#kilometer_jarak').val(),
                litre_per_km: $('#litre_per_km').val()
              },
              function(data){
                $.get(
                  'get_total_carbon/',
                  function(data){
                    $("#total").html(data['carbon_print_total'].toFixed(2))
                    $("#hasil_kalkulasi").html(data['hasil_kalkulasi'].toFixed(2))
                  }
                )
              }
              )
              $("#kendaraan-form")[0].reset()
        } else {
          $.post(
              'calculate-listrik/',
              {
                usage: $('#usage option:selected').val(),
                kilowatt_hour: $('#kilowatt_hour').val()
              },
              function(data){
                $.get(
                  'get_total_carbon/',
                  function(data){
                    $("#total").html(data['carbon_print_total'].toFixed(2));
                    $("#hasil_kalkulasi").html(data['hasil_kalkulasi'].toFixed(2))
                  }
                )
              }
              )
              $("#listrik-form")[0].reset()
        }
    })

})