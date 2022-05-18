    $(document).ready(function() {
      $('#example').DataTable( {
          "language": {
              "lengthMenu": "Mostrar _MENU_ Registros por pagina",
              "zeroRecords": "No se encontraron registros",
              "info": "Mostrando pagina _PAGE_ de _PAGES_",
              "thousands":      ".",
              "infoFiltered": "(filtrado de _MAX_ registros totales)",
              "infoEmpty":      "Mostrando 0 a 0 de 0 entradas",
              "paginate": {
          "first":      "Primero",
          "last":       "Ultimo",
          "next":       "Siguiente",
          "previous":   "Anterior"
      },
              "search":         "Buscar:",
          }
      } );
      $('#example').show();
    
    } );

