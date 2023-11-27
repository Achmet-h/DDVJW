document.addEventListener('DOMContentLoaded', function () {
    // Find all input elements
    var inputs = document.getElementsByTagName('input');

    function setCustomMessages(input) {
        input.oninvalid = function (e) {
            e.target.setCustomValidity('');
            if (!e.target.validity.valid) {
                if (e.target.type === 'email') {
                    if (e.target.validity.valueMissing) {
                        e.target.setCustomValidity('Dit veld is verplicht.');
                    } else if (e.target.validity.typeMismatch) {
                        e.target.setCustomValidity('Voer een geldig emailadres in. Bijvoorbeeld: naam@voorbeeld.com');
                    }
                } else if (e.target.type === 'password') {
                    e.target.setCustomValidity('Een wachtwoord is vereist.');
                } else if (e.target.type === 'tel') {
                    e.target.setCustomValidity('Een telefoonnummer is vereist.');
                } else if (e.target.type === 'text') {
                    e.target.setCustomValidity('Dit veld mag niet leeg zijn.');
                }
            }
        };
        input.oninput = function (e) {
            e.target.setCustomValidity('');
        };
        input.onchange = function (e) {
            e.target.setCustomValidity('');
        };
    }

    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].hasAttribute('required')) {
            setCustomMessages(inputs[i]);
        }
    }

    const burgerIcon = document.querySelector('#burger');
    const navbarMenu = document.querySelector('#nav-links');
    burgerIcon.addEventListener('click', () => {
        navbarMenu.classList.toggle('is-active');
    });

    document.querySelectorAll('.faq-card .card-header').forEach((item) => {
        item.addEventListener('click', () => {
            const content = item.nextElementSibling;
            content.classList.toggle('is-hidden');
        });
    });


});

