// console.log('ok')
// jQuery(function($){
//     $(document).ready(function(){
//         $("#id_project_select").change(function(){
//             // console.log(obj.currentTarget.value);
//             $.ajax({
//                 url:"/get_phases/",
//                 type:"POST",
//                 data:{project: $(this).val(),},
//                 success: function(result) {
//                     console.log(result);
//                     cols = document.getElementById("id_phase_select");
//                     cols.options.length = 0;
//                     for(var k in result){
//                         cols.options.add(new Option(k, result[k]));
//                     }
//                 },
//                 error: function(e){
//                     console.error(JSON.stringify(e));
//                 },
//             });
//         });
//     });
// });


function getKabupaten(prov_id) {
    let $ = django.jQuery;
    $.get('/kabupaten/' + prov_id, function (resp){
        console.log(resp)
        let kabupaten_list = '<option value="" selected="">---------</option>'
        $.each(resp.data, function(i, item){
           kabupaten_list += '<option value="'+ item.id +'">'+ item.name +'</option>'
        });
        $('#id_kabupaten').html(kabupaten_list);
    });
}

function getKecamatan(kabupaten_id) {
    let $ = django.jQuery;
    $.get('/kecamatan/' + kabupaten_id, function (resp){
        let kecamatan_list = '<option value="" selected="">---------</option>'
        $.each(resp.data, function(i, item){
           kecamatan_list += '<option value="'+ item.id +'">'+ item.name +'</option>'
        });
        $('#id_kecamatan').html(kecamatan_list);
    });
}

function getKelurahan(kecamatan_id) {
    let $ = django.jQuery;
    $.get('/kelurahan/' + kecamatan_id, function (resp){
        console.log(resp)
        let kelurahan_list = '<option value="" selected="">---------</option>'
        $.each(resp.data, function(i, item){
           kelurahan_list += '<option value="'+ item.id +'">'+ item.name +'</option>'
        });
        $('#id_kelurahan').html(kelurahan_list);
    });
}