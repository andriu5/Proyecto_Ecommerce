console.log("Nuevo!");

let productos = [];

function saveItem(params) {
    alert(params);
    console.log("Nuevo! desde saveItem!");
    productos.push(params)
    console.log(productos)
    localStorage.setItem("productos", JSON.stringify(productos))
    updateCount(productos.length);
}

function getItems() {
    productos = JSON.parse(localStorage.getItem("productos"))
    for (producto of productos) {
        console.log(producto);
    }
    updateCount(productos.length);
}

function updateCount(numItems) {
    let count = document.getElementById("productsCount")
    count.textContent = numItems
}

function eliminarDelCarrito(id) {

    let data = $('#formCart').serialize();
    $.ajax({
        type: "POST",
        url: '/tienda/delete_item_cart/'+id+'/',
        data: data
    })
    .done(function(respuesta) {
        alert(respuesta.message);
        $.ajax({
            type: "GET",
            url: '/tienda/carrito/'
        })
    })
    .fail(function() {
        console.log('Carrito: Error, revisar!');
    })
    .always(function() {
        console.log('Acción completada!');
    });
}

// $(document).ready(function() {
//     $("sup").click(function(){
//         $("#info").remove();
//     });
// });

// $(document).ready(function() {
//     $('#form1').submit(function(){
//         let first_name = $('#first_name-id').val();
//         if (first_name === "") {
//             return false;
//         }
//         if (first_name.length < 2 ) {
//             alert('First Name should be at least 2 characters!');
//         }
//         let last_name = $('#last_name-id').val();
//         if (last_name === "") {
//             return false;
//         }
//         if (last_name.length < 2 ) {
//             alert('Last Name should be at least 2 characters!');
//             return false;
//         }
//         let password = $('#password-id').val();
//         if (password.length < 8 ) {
//             alert('Password should be at least 8 character!');
//             // console.log("El Largo de la Password es: "+password.length)
//             return false;
//         }
//     });

//     $('#email-id').focusout(function(){
//         verificarEmail();
//     })

// });

// function verificarEmail() {

//     let data = $('#form1').serialize();
//     $.ajax({
//         type: "POST",
//         url: '/verificar_email/',
//         data: data
//     })
//     .done(function(respuesta) {
//         alert(respuesta.errors);
//     })
//     .fail(function() {
//         console.log('email: Error!');
//     })
//     .always(function() {
//         console.log('Verificartion Complete!');
//     });
// }