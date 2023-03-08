// register.javascripe

const form = document.querySelector('.register-form');
form.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const username = formData.get('username');
    const email = formData.get('email');
    const password1 = formData.get('password1');
    const password2 = formData.get('password2');
    fetch('/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            email: email,
            password1: password1,
            password2: password2
        })
    })
    .then(response => {
        if (response.ok) {
            window.location.href = '/';
        } else {
            throw new Error('Registration failed');
        }
    })
    .catch(error => {
        alert(error.message);
    });
});