   $(function() {
       $('#health').bind('click', function() {
          
           var currency1 = $("#currency1 option:selected").val();
           var currency2 = $("#currency2 option:selected").val();
           var amount = parseFloat($('#amount').val()).toFixed(2);
           if (currency1 == currency2) {
               var rate = 1;
               var converted_amount = amount;
                   $('#converted_amt').text(converted_amount);
           $('#rate').text(rate);
           } else {

               $.getJSON($SCRIPT_ROOT + '/convert/' + currency1 + '/' + amount + '/' + currency2, function(data) {
                   console.log(data);
                   console.log(data.converted_amount);
                   var converted_amount = data.converted_amount + ' ' + data.to;
                    console.log(data.converted_amount);
                   var rate = data.converted_amount / data.from_amount;
    $('#converted_amt').text(converted_amount);
           $('#rate').text(rate);

               });
           }

       
       });
       return false;
   });