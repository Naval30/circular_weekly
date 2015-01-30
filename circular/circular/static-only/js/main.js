//Main javascript file
//JQUERY

$(function(){
//---------------deals.html--------------------------------------
        $('.btn').click(function(){
                var id = $(this).attr('id');
                $('.main-content >#'+id+'> p').slideToggle().siblings().hide();
                $('.main-content >#'+id+'> li').slideToggle().siblings().hide();
        });
        
        $('.location').click(function(){
                var id = $(this).attr('id');
                $('.main-content >#'+id+'> li').slideToggle("fast");
        });



//------------------recipe_form.html-------------------------------        
       /*
        //Slider for miin and max values of flavor
        var min;
       var max;
       $( "#slider-range" ).slider({
        range: true,
        min: 0,
        max: 1,
        step:0.1,
        values: [ 0, 1 ],
        slide: function( event, ui ) {
                $( "#fval" ).val(  ui.values[ 0 ] + " - " + ui.values[ 1 ] );
                min = ui.values[0];
                max = ui.values[1];
                }
                });*/
       
       
       $('#userChoice').on('submit',function(e){
        if ($('#id_q').val().length == 0 ) {
                alert("Please enter Recipe name")
        }
        else if ($('#id_AllowedIngredients').val().length ==0 ) {
                alert("Please enter Allowed Ingredients ")
        }
        else if ($('#id_ExcludedIngredients').val().length ==0 ) {
                alert("Please enter the Excluded Ingredients ")
        }
        else if ($('#id_cuisine').val().length ==0 ) {
                alert("Please enter the cuisine ")
        }
        else if ($('#id_course').val().length ==0 ) {
                alert("Please enter the course ")
        }
        else{
                $('#result_1').html('<img src="http://preloaders.net/preloaders/287/Filling%20broken%20ring.gif"> loading...');
                
                e.preventDefault();
                var myData = {
                        csrfmiddlewaretoken : $('input[name="csrfmiddlewaretoken"]').val(),
                        q: $('#id_q').val(),
                        AllowedIngredients: $('#id_AllowedIngredients').val(),
                        ExcludedIngredients : $('#id_ExcludedIngredients').val(),
                        allowedCuisine: $('#id_cuisine').val(),
                        allowedCourse: $('#id_course').val(),
                        //Minimum : min_flavor,
                        //Maximum : max_flavor,
                        }
                $.ajax({
                        type: "POST",
                        url: "/recipe/",
                        dataType: "json",
                        data: myData,
                        success: function(json) {
                                $('.result').text("");
                                $('.result').css('border','solid');
                                $('#result_1').append("<br>");
                                $('#result_1').append("&emsp;"+'<b>Recipe Name: </b>' + json.name+"<br>");
                                $('#result_1').append("&emsp;"+'<b>Total Time: </b>' + json.totalTime+"<br>");
                                $('#result_1').append("&emsp;"+'<b>Link: </b>' +"<a href=\'"+json.url+"\'>"+ json.url+"<br>");
                                $('#result_1').append("&emsp;"+'<b>Rating: </b>' + json.Rating+"<br>");
                                $('#result_1').append("&emsp;"+"<b>Ingrideints required  </b><br>")
                                for (var i=0; i<json.Ingredients.length; i++) {
                                        $('#result_1').append("&emsp;&emsp;"+json.Ingredients[i]+"<br>");
                                }
                                $('#result_1').append("<br>");
                                
                                $('#result_2').append("<br>");
                                $('#result_2').append("&emsp;"+'<b>Recipe Name: </b>' + json.name1+"<br>");
                                $('#result_2').append("&emsp;"+'<b>Total Time: </b>' + json.totalTime1+"<br>");
                                $('#result_2').append("&emsp;"+'<b>Link: </b>' +"<a href=\'"+json.url1+"\'>"+ json.url1+"<br>");
                                $('#result_2').append("&emsp;"+'<b>Rating: </b>' + json.Rating1+"<br>");
                                $('#result_2').append("&emsp;"+"<b>Ingrideints required  </b><br>")
                                for (var i=0; i<json.Ingredients1.length; i++) {
                                        $('#result_2').append("&emsp;&emsp;"+json.Ingredients[i]+"<br>");
                                }
                                $('#result_2').append("<br>");
                        },
                        error:function(){
                               alert("Sorry, No Recipe found. Please try again with different options");
                        }
                        });
                }
                return false;
        });
       
       $('#clear').click(function() {
                $(this).closest('form').find("input[type=text], textarea").val("");
                $('.result').html("");
                $('.result').css('display','none');
        });
       
        
    });
