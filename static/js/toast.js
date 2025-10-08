function showToast(title, message, type = 'info', duration = 5000) {
    const toastComponent = document.getElementById('toast-component');
    if (!toastComponent) return;

    const toastIcon = document.getElementById('toast-icon');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');

    // Definisikan ikon SVG
    const icons = {
        success: `<svg class="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>`,
        error: `<svg class="w-6 h-6 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>`,
        info: `<svg class="w-6 h-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>`,
    };

    // Reset classes
    toastComponent.classList.remove('bg-green-100', 'bg-red-100', 'bg-blue-100');
    
    // Set styles based on type
    if (type === 'success') {
        toastComponent.classList.add('bg-green-100');
    } else if (type === 'error') {
        toastComponent.classList.add('bg-red-100');
    } else { // info
        toastComponent.classList.add('bg-blue-100');
    }

    // Set ikon, judul, dan pesan
    toastIcon.innerHTML = icons[type] || icons['info'];
    toastTitle.textContent = title;
    toastMessage.textContent = message;

    // Show toast with animation
    toastComponent.classList.remove('opacity-0', 'translate-x-full');
    
    // Hide toast after duration
    setTimeout(() => {
        toastComponent.classList.add('opacity-0', 'translate-x-full');
    }, duration);
}