const state = {
  currentUser: {
    name: 'Himanshu Shekhar',
    email: 'himanshushekhar@.com',
    initials: 'HS',
    course: 'Computer Science & Engineering'
  },
  // ... rest of the JavaScript logic for renderHome(), renderChat(), etc.
};
form.addEventListener('submit', e => {
    e.preventDefault();
    const title = form.title.value.trim();
    const course = form.course.value;
    const category = form.category.value;
    const priority = form.priority.value;
    const text = form.text.value.trim();

    if (title && course && category && priority && text) {
        fetch('/api/posts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title,
                course,
                category,
                priority,
                text
            })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            form.reset();
            setActiveNav('home');
            renderSection('home');
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Failed to submit the post.');
        });
    } else {
        alert('Please fill in all fields.');
    }
});

// Add all event handlers and renderSection() logic here

