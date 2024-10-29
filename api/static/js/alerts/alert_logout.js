document.getElementById('logout-button').addEventListener('click', function () {
    Swal.fire({
        title: 'Are You Sure?',
        text: 'You will lose your current session',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',  // Corregido
        cancelButtonColor: '#d33',      // Corregido
        confirmButtonText: 'Yes, Bye',
        cancelButtonText: 'No'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = '/logout/';  // Corregido el uso de url tag
        }
    });
});
