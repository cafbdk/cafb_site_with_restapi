$(function() {
    var App = {
        init: function() {
            App.attachListeners();
        },
        config: {
            reader: "ean", //"code_128",
            length: 10
        },
        attachListeners: function() {
            var self = this;

            $(".controls input[type=file]").on("change", function(e) {
                if (e.target.files && e.target.files.length) {
                    App.decode(URL.createObjectURL(e.target.files[0]));
                }
            });

            $(".controls button").on("click", function(e) {
                var input = document.querySelector(".controls input[type=file]");
                if (input.files && input.files.length) {
                    App.decode(URL.createObjectURL(input.files[0]));
                }
            });

            // $(".controls .reader-config-group").on("change", "input, select", function(e) {
            //     e.preventDefault();
            //     var $target = $(e.target),
            //         value = $target.attr("type") === "checkbox" ? $target.prop("checked") : $target.val(),
            //         name = $target.attr("name"),
            //         state = self._convertNameToState(name);
            //
            //     console.log("Value of "+ state + " changed to " + value);
            //     self.setState(state, value);
            // });

        },
        _accessByPath: function(obj, path, val) {
            var parts = path.split('.'),
                depth = parts.length,
                setter = (typeof val !== "undefined") ? true : false;

            return parts.reduce(function(o, key, i) {
                if (setter && (i + 1) === depth) {
                    o[key] = val;
                }
                return key in o ? o[key] : {};
            }, obj);
        },
        _convertNameToState: function(name) {
            return name.replace("_", ".").split("-").reduce(function(result, value) {
                return result + value.charAt(0).toUpperCase() + value.substring(1);
            });
        },
        detachListeners: function() {
            $(".controls input[type=file]").off("change");
            $(".controls .reader-config-group").off("change", "input, select");
            $(".controls button").off("click");

        },
        decode: function(src) {
            var self = this,
                config = $.extend({}, self.state, {src: src});

            Quagga.decodeSingle(config, function(result) {});
        },
        setState: function(path, value) {
            var self = this;

            if (typeof self._accessByPath(self.inputMapper, path) === "function") {
                value = self._accessByPath(self.inputMapper, path)(value);
            }

            self._accessByPath(self.state, path, value);

            console.log(JSON.stringify(self.state));
            App.detachListeners();
            App.init();
        },
        inputMapper: {
            inputStream: {
                size: function(value){
                    return parseInt(value);
                }
            },
            numOfWorkers: function(value) {
                return parseInt(value);
            },
            decoder: {
                readers: function(value) {
                    return [value + "_reader"];
                }
            }
        },
        state: {
            inputStream: {
                size: 800
            },
            locator: {
                patchSize: "large",
                halfSample: false
            },
            numOfWorkers: 1,
            decoder: {
                readers: ["ean_reader"]
            },
            locate: true,
            src: null
        }
    };
    
    App.init();

    Quagga.onProcessed(function(result) {
        // var drawingCtx = Quagga.canvas.ctx.overlay,
        //     drawingCanvas = Quagga.canvas.dom.overlay;

        // if (result) {
        //     if (result.boxes) {
        //         drawingCtx.clearRect(0, 0, parseInt(drawingCanvas.getAttribute("width")), parseInt(drawingCanvas.getAttribute("height")));
        //         result.boxes.filter(function (box) {
        //             return box !== result.box;
        //         }).forEach(function (box) {
        //             Quagga.ImageDebug.drawPath(box, {x: 0, y: 1}, drawingCtx, {color: "green", lineWidth: 2});
        //         });
        //     }
        //
        //     if (result.box) {
        //         Quagga.ImageDebug.drawPath(result.box, {x: 0, y: 1}, drawingCtx, {color: "#00F", lineWidth: 2});
        //     }
        //
        //     if (result.codeResult && result.codeResult.code) {
        //         Quagga.ImageDebug.drawPath(result.line, {x: 'x', y: 'y'}, drawingCtx, {color: 'red', lineWidth: 3});
        //     }
        // }
        if (result){
            if (result.codeResult && result.codeResult.code){}
            else{
                $('form#ajax_form').parent().parent().append('\
                                <div name="request_status" class="divider"></div>     \
                                  <div class="section">         \
                                    <h4> UPC Not Detected </h4> \
                                    ');
            };
        };
    });

    Quagga.onDetected(function(result) {
        var code = result.codeResult.code,
            $node,
            canvas = Quagga.canvas.dom.image;

        //$node = $('<li><div class="thumbnail"><div class="imgWrapper"><img /></div><div class="caption"><h4 class="code"></h4></div></div></li>');
        //$node.find("img").attr("src", canvas.toDataURL());
        //$node.find("h4.code").html(code);
        //$("#result_strip ul.thumbnails").prepend($node);

        //var upc_code = $('input[name="upc_code"]').val();
        var csrf_token = $("input[name='csrfmiddlewaretoken']").val()


        var post_data = {             'upc_code': code,
            'csrfmiddlewaretoken': csrf_token,
        };

        console.log( post_data );

        create_post(post_data);


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
                    if (data['wellness']) {
                        $('form#ajax_form').parent().parent().append('   \
                                <div name="wellness_status" class="divider"></div>     \
                                  <div class="section">         \
                                    <h4> Healthy </h4> \
                                    ');
                    }
                    else{
                        $('form#ajax_form').parent().parent().append('   \
                                <div name="wellness_status" class="divider"></div>     \
                                  <div class="section">         \
                                    <h4> Unhealthy </h4> \
                                    ');
                    };
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