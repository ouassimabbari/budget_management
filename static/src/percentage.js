window.onpopstate = function(event) {
    $( document ).ready(function() {
        $("div.o_form_buttons_view :button.btn.btn-primary.o_form_button_edit").click(function () {
            console.log("hi");
            setTimeout(function(){
                if($("input[type='range']").val() == null){
                    if(document.location.toString().includes("model=budget_management.sub_configuration&view_type=form")){
                        $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "width", "20%" );
                        $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "margin-left", "15px" );
                        $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "margin-right", "8px" );
                        $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').append('%');
                        $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').prepend( "<input type='range' min='0' max='100' step='0.1' value='50' data-orientation='horizontal'/>");
                        $("div.o_group :input[type='range']").rangeslider().on('input', function() {
                            $("div.o_group :input[name='configuration_percentage_sub_budget']").val(this.value);
                          });
                        $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').css("text-align", "center");
                        $("div.o_group :input[name='configuration_percentage_sub_budget']").val($("div.o_group :input[type='range']").val());
                        $("div.o_group :input[name='configuration_percentage_sub_budget']").bind("change paste keyup", function() {
                            $("input[type='range']").val(parseFloat($(this).val())).change();
                         });
                    }else if(document.location.toString().includes("model=budget_management.configuration&view_type=form")){
                        $("div.table-responsive a[role='button']").click(function () {
                            setTimeout(function(){
                                $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "width", "20%" );
                                $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "margin-left", "15px" );
                                $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "margin-right", "8px" );
                                $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').append('%');
                                $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').prepend( "<input type='range' min='0' max='100' step='0.1' value='50' data-orientation='horizontal'/>");
                                $("div.o_group :input[type='range']").rangeslider().on('input', function() {
                                    $("div.o_group :input[name='configuration_percentage_sub_budget']").val(this.value);
                                  });
                                $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').css("text-align", "center");
                                $("div.o_group :input[name='configuration_percentage_sub_budget']").val($("div.o_group :input[type='range']").val());
                                $("div.o_group :input[name='configuration_percentage_sub_budget']").bind("change paste keyup", function() {
                                    $("input[type='range']").val(parseFloat($(this).val())).change();
                                 });
                            }, 600);
                        })
                    }else if(document.location.toString().includes("model=budget_management.budget&view_type=form")){
                        $("div[name='configuration']").click(function (e) {
                            setTimeout(function(){
                                $("ul.ui-menu.ui-widget.ui-widget-content.ui-autocomplete.ui-front a.ui-menu-item-wrapper").click(function (e) {
                                    setTimeout(function(){
                                    if ($("div.table-responsive a[role='button']").html() == "Add a line") {
                                        $("div.table-responsive a[role='button']").click(function (e) {
                                            setTimeout(function(){
                                                $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "width", "20%" );
                                                $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "margin-left", "15px" );
                                                $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "margin-right", "8px" );
                                                $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').append('%');
                                                $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').prepend( "<input type='range' min='0' max='100' step='0.1' value='50' data-orientation='horizontal'/>");
                                                $("div.o_group :input[type='range']").rangeslider().on('input', function() {
                                                    $("div.o_group :input[name='configuration_percentage_sub_budget']").val(this.value);
                                                  });
                                                $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').css("text-align", "center");
                                                $("div.o_group :input[name='configuration_percentage_sub_budget']").val($("div.o_group :input[type='range']").val());
                                                $("div.o_group :input[name='configuration_percentage_sub_budget']").bind("change paste keyup", function() {
                                                    $("input[type='range']").val(parseFloat($(this).val())).change();
                                                 });
                                            }, 600);
                                        });
                                    }else{
                                        console.log($("div.table-responsive a[role='button']").html())
                                    }}, 600);
                                });
                            }, 600);
                        });
                    }
                }
            }, 200);
        })
    });
        $( document ).ready(function() {
            if(document.location.toString().includes("model=budget_management.sub_configuration&view_type=form")){
                $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "width", "20%" );
                $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "margin-left", "15px" );
                $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "margin-right", "8px" );
                $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').append('%');
                $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').prepend( "<input type='range' min='0' max='100' step='0.1' value='50' data-orientation='horizontal'/>");
                $("div.o_group :input[type='range']").rangeslider().on('input', function() {
                    console.log(jQuery.type(this.value))
                    $("div.o_group :input[name='configuration_percentage_sub_budget']").val(this.value);
                  });
                $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').css("text-align", "center");
                $("div.o_group :input[name='configuration_percentage_sub_budget']").val($("div.o_group :input[type='range']").val());
                $("div.o_group :input[name='configuration_percentage_sub_budget']").bind("change paste keyup", function() {
                    console.log(jQuery.type($(this).val()))
                    $("input[type='range']").val(parseFloat($(this).val())).change();
                 });
            }else if(document.location.toString().includes("model=budget_management.configuration&view_type=form")){
                $("div.table-responsive a[role='button']").click(function () {
                    setTimeout(function(){
                        $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "width", "20%" );
                        $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "margin-left", "15px" );
                        $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "margin-right", "8px" );
                        $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').append('%');
                        $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').prepend( "<input type='range' min='0' max='100' step='0.1' value='50' data-orientation='horizontal'/>");
                        $("div.o_group :input[type='range']").rangeslider().on('input', function() {
                            $("div.o_group :input[name='configuration_percentage_sub_budget']").val(this.value);
                          });
                        $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').css("text-align", "center");
                        $("div.o_group :input[name='configuration_percentage_sub_budget']").val($("div.o_group :input[type='range']").val());
                        $("div.o_group :input[name='configuration_percentage_sub_budget']").bind("change paste keyup", function() {
                            $("input[type='range']").val(parseFloat($(this).val())).change();
                         });
                    }, 600);
                })
            }else if(document.location.toString().includes("model=budget_management.budget&view_type=form")){
                $("div[name='configuration']").click(function (e) {
                    setTimeout(function(){
                        $("ul.ui-menu.ui-widget.ui-widget-content.ui-autocomplete.ui-front a.ui-menu-item-wrapper").click(function (e) {
                            setTimeout(function(){
                            if ($("div.table-responsive a[role='button']").html() == "Add a line") {
                                $("div.table-responsive a[role='button']").click(function (e) {
                                    setTimeout(function(){
                                        $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "width", "20%" );
                                        $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "margin-left", "15px" );
                                        $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "margin-right", "8px" );
                                        $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').append('%');
                                        $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').prepend( "<input type='range' min='0' max='100' step='0.1' value='50' data-orientation='horizontal'/>");
                                        $("div.o_group :input[type='range']").rangeslider().on('input', function() {
                                            $("div.o_group :input[name='configuration_percentage_sub_budget']").val(this.value);
                                          });
                                        $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').css("text-align", "center");
                                        $("div.o_group :input[name='configuration_percentage_sub_budget']").val($("div.o_group :input[type='range']").val());
                                        $("div.o_group :input[name='configuration_percentage_sub_budget']").bind("change paste keyup", function() {
                                            $("input[type='range']").val(parseFloat($(this).val())).change();
                                         });
                                    }, 600);
                                });
                            }else{
                                console.log($("div.table-responsive a[role='button']").html())
                            }}, 600);
                        });
                    }, 600);
                });
            }
        });
  };

  window.onload = function(event) {
    $( document ).ready(function() {
        if(document.location.toString().includes("model=budget_management.sub_configuration&view_type=form")){
            $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "width", "20%" );
            $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "margin-left", "15px" );
            $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "margin-right", "8px" );
            $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').append('%');
            $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').prepend( "<input type='range' min='0' max='100' step='0.1' value='50' data-orientation='horizontal'/>");
            $("div.o_group :input[type='range']").rangeslider().on('input', function() {
                $("div.o_group :input[name='configuration_percentage_sub_budget']").val(this.value);
            });
            $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').css("text-align", "center");
            $("div.o_group :input[name='configuration_percentage_sub_budget']").val($("div.o_group :input[type='range']").val());
            $("div.o_group :input[name='configuration_percentage_sub_budget']").bind("change paste keyup", function() {
                $("input[type='range']").val(parseFloat($(this).val())).change();
            });
        }else if(document.location.toString().includes("model=budget_management.configuration&view_type=form")){
            $("div.table-responsive a[role='button']").click(function () {
                setTimeout(function(){
                    $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "width", "20%" );
                    $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "margin-left", "15px" );
                    $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "margin-right", "8px" );
                    $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').append('%');
                    $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').prepend( "<input type='range' min='0' max='100' step='0.1' value='50' data-orientation='horizontal'/>");
                    $("div.o_group :input[type='range']").rangeslider().on('input', function() {
                        $("div.o_group :input[name='configuration_percentage_sub_budget']").val(this.value);
                    });
                    $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').css("text-align", "center");
                    $("div.o_group :input[name='configuration_percentage_sub_budget']").val($("div.o_group :input[type='range']").val());
                    $("div.o_group :input[name='configuration_percentage_sub_budget']").bind("change paste keyup", function() {
                        $("input[type='range']").val(parseFloat($(this).val())).change();
                    });
                }, 600);
            })
        }else if(document.location.toString().includes("model=budget_management.budget&view_type=form")){
            $("div[name='configuration']").click(function (e) {
                setTimeout(function(){
                    $("ul.ui-menu.ui-widget.ui-widget-content.ui-autocomplete.ui-front a.ui-menu-item-wrapper").click(function (e) {
                        setTimeout(function(){
                        if ($("div.table-responsive a[role='button']").html() == "Add a line") {
                            $("div.table-responsive a[role='button']").click(function (e) {
                                setTimeout(function(){
                                    $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "width", "20%" );
                                    $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "margin-left", "15px" );
                                    $("div.o_group :input[name='configuration_percentage_sub_budget']").css( "margin-right", "8px" );
                                    $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').append('%');
                                    $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').prepend( "<input type='range' min='0' max='100' step='0.1' value='50' data-orientation='horizontal'/>");
                                    $("div.o_group :input[type='range']").rangeslider().on('input', function() {
                                        $("div.o_group :input[name='configuration_percentage_sub_budget']").val(this.value);
                                    });
                                    $("div.o_group :input[name='configuration_percentage_sub_budget']").closest('td').css("text-align", "center");
                                    $("div.o_group :input[name='configuration_percentage_sub_budget']").val($("div.o_group :input[type='range']").val());
                                    $("div.o_group :input[name='configuration_percentage_sub_budget']").bind("change paste keyup", function() {
                                        $("input[type='range']").val(parseFloat($(this).val())).change();
                                    });
                                }, 600);
                            });
                        }else{
                            console.log($("div.table-responsive a[role='button']").html())
                        }}, 600);
                    });
                }, 600);
            });
        }
    });
};


