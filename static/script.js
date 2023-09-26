document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('upload-form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        try {
            const response = await fetch('/classify', {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                const data = await response.json();
                resultDiv.textContent = `Classified as : ${data.result}`;
            } else {
                resultDiv.textContent = 'Error occurred while classifying the image.';
            }
        } catch (error) {
            resultDiv.textContent = 'An error occurred. Please try again.';
            console.error('Error:', error);
        }
    });
});
