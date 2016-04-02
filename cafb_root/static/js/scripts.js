

  // A $( document ).ready() block.
$( document ).ready(function() {
      $(".button-collapse").sideNav();



        $('form#ajax_form').submit(function (e) { 
            event.preventDefault();
            console.log("form submitted!"); 

            var upc_code = $('input[name="upc_code"]').val();
            var csrf_token = $("input[name='csrfmiddlewaretoken']").val()


            var post_data = {             'upc_code': upc_code, 
                            'csrfmiddlewaretoken': csrf_token,
                           };

            console.log( post_data );
            
            create_post(post_data);
            return false;

        });

            function create_post( post_data ) {
            console.log("create post is working!") // sanity check
            $.ajax({
                url : "upc/", // the endpoint
                type : "POST", // http method
                traditional: true,
                data : post_data , // data sent with the post request

                // handle a successful response
                success : function(data) { 
                    console.log("success"); // another sanity check
                    console.log(data);
                    $('div[name="request_status"]').remove();
                // if ok == true
                    if (data['status'] == true){
                        $('form#ajax_form').parent().parent().append('   \
                                <div name="request_status" class="divider"></div>     \
                                  <div class="section">         \
                                    <h4> UPC Requested </h4> \
                                    <p class="flow-text"> \
                                    Item Name: ' + data['gtin_name'] + '<br>' +
                                    'UPC Code: '  + data['gtin_code'] +
                                     '</p> </div> ');
                    
                        
                    }
                    else {
                        $('form#ajax_form').parent().parent().append('\
                                <div name="request_status" class="divider"></div>     \
                                  <div class="section">         \
                                    <h4> UPC Not Found (maybe too many requests) </h4> \
                                    <p class="flow-text"> \
                                    UPC Code: '  + data['gtin_code'] + "</p> </div>");
                    }

                },
                error : function (request, status, error) {
                    console.log(request.responseText);
                }
            });
        }

});