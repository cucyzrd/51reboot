/**
 * Created by zhourudong on 2016/12/14.
 */
jQuery(document).ready(function () {


    jQuery(".users").dataTable({
        responsive: true,
        "dom": 'T<"clear">lfrtip',
        "tableTools": { "sSwfPath": "/static/sfv/js/plugins/dataTables/swf/copy_csv_xls_pdf.swf" }
    });


    jQuery('.btn-save').on('click',function() {
        jQuery.post("/user/save/",
            jQuery('.form-create').serializeArray(),
            function(response) {
                if(response["code"] == 200){
                     window.location.reload();
                } else if(response["code"] == 400){
                    alert(response['error']);
                }
            }, "json");
    });


    jQuery('.btn-edit').on('click', function() {
        jQuery.get("/user/view/",
            {"id" : jQuery(this).data("id")},
            function(response) {
            for(var key in response){
                console.log(key)
                jQuery("[name=" + key + "]").val(response[key]);
            }
            },"json");
    });


    jQuery(".btn-modify").on("click", function(){
        jQuery.post("/user/modify/",
            jQuery(.form-edit"").serializeArray(),
            function(response){
                if(response["code"] == 200) {
                    window.location.reload();
                } else if(response["code"] = 400) {
                    alert(response["error"]);
                }
            },'json');
    });


    jQuery(".btn-delete").on('click',function(){
        var url = "/usr/delete/?id=" + jQuery(this).data('id');
        if(confirm("确定删除吗?")){
            window.location.replace(url);
        }
    });


    jQuery(".users").on("click", ".btn-password-edit", function () {
       jQuery("input[name=id]").val(jQuery(this).data("id"));
       jQuery("#dialog-password-edit").modal("show");
    });


    jQuery(".btn-password-modify").on("click", function(){
       jQuery.post('/user/password/modify/',
           jQuery(".form-password-edit").serializeArray(),
           function (response){
            if(response["code"] == 200){
                window.location.reload();
            } else if(response["code"] == 400){
                alert(response["error"]);
            }
           },'json');
    });


});