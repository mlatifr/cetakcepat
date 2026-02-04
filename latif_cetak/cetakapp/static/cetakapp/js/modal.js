let currentProductId = null;

function showDeleteModal(productName, productId) {
        currentProductId = productId;
        const messageEl = document.getElementById('deleteModalMessage');
        const modalEl = document.getElementById('deleteModal');

        if (messageEl && modalEl) {
                messageEl.textContent = 'Apakah Anda yakin ingin menghapus produk "' + productName + '"?';
                modalEl.classList.add('active');
        } else {
                console.error('Modal elements not found');
        }
}

function hideDeleteModal() {
        const modalEl = document.getElementById('deleteModal');
        if (modalEl) {
                modalEl.classList.remove('active');
        }
        currentProductId = null;
}

// Get CSRF token from cookie
function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                        const cookie = cookies[i].trim();
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                break;
                        }
                }
        }
        return cookieValue;
}

document.addEventListener('DOMContentLoaded', function () {
        // Confirm delete button
        const confirmBtn = document.getElementById('confirmDeleteBtn');
        if (confirmBtn) {
                confirmBtn.addEventListener('click', function () {
                        if (currentProductId) {
                                const csrftoken = getCookie('csrftoken');

                                // Show loading state
                                const originalText = confirmBtn.textContent;
                                confirmBtn.textContent = 'Menghapus...';
                                confirmBtn.disabled = true;

                                fetch('/delete/' + currentProductId + '/', {
                                        method: 'POST',
                                        headers: {
                                                'Content-Type': 'application/json',
                                                'X-CSRFToken': csrftoken
                                        }
                                })
                                        .then(response => {
                                                if (!response.ok) {
                                                        throw new Error('Network response was not ok');
                                                }
                                                return response.json();
                                        })
                                        .then(data => {
                                                if (data.success) {
                                                        window.location.reload();
                                                } else {
                                                        alert('Error: ' + data.message);
                                                        confirmBtn.textContent = originalText;
                                                        confirmBtn.disabled = false;
                                                        hideDeleteModal();
                                                }
                                        })
                                        .catch(error => {
                                                console.error('Error:', error);
                                                alert('Terjadi kesalahan saat menghapus produk: ' + error.message);
                                                confirmBtn.textContent = originalText;
                                                confirmBtn.disabled = false;
                                                hideDeleteModal();
                                        });
                        }
                });
        }

        // Close modal when clicking outside
        const modalEl = document.getElementById('deleteModal');
        if (modalEl) {
                modalEl.addEventListener('click', function (e) {
                        if (e.target === this) {
                                hideDeleteModal();
                        }
                });
        }

        // Close modal with Escape key
        document.addEventListener('keydown', function (e) {
                if (e.key === 'Escape') {
                        hideDeleteModal();
                }
        });
});
