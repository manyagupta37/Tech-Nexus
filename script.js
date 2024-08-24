
function navigateTo(page) {
    window.location.href = page;
}

document.addEventListener('DOMContentLoaded', function() {
    const appointmentButton = document.querySelector('.btn-appointment');
    const backButtons = document.querySelectorAll('.btn-secondary');

    if (appointmentButton) {
        appointmentButton.addEventListener('click', function() {
            window.location.href = 'departments.html';
        });
    }

    backButtons.forEach(function(backButton) {
        backButton.addEventListener('click', function() {
            if (document.URL.includes('departments.html')) {
                window.location.href = 'index.html';
            } else if (document.URL.includes('appointment.html')) {
                window.location.href = 'departments.html';
            }
        });
    });
});
