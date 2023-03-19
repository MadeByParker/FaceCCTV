const textSizeInput = document.getElementById('text-size');

textSizeInput.addEventListener('change', () => {
  const textSize = textSizeInput.value;
  localStorage.setItem('text-size', textSize);
  setTextSize();
});


function setTextSize() {
    const textSize = localStorage.getItem('text-size') || 'base';
    const root = document.documentElement;
    root.style.setProperty('--text-xs', `theme('fontSize.${textSize}.xs')`);
    root.style.setProperty('--text-sm', `theme('fontSize.${textSize}.sm')`);
    root.style.setProperty('--text-base', `theme('fontSize.${textSize}.base')`);
    root.style.setProperty('--text-lg', `theme('fontSize.${textSize}.lg')`);
    root.style.setProperty('--text-xl', `theme('fontSize.${textSize}.xl')`);
    root.style.setProperty('--text-2xl', `theme('fontSize.${textSize}.2xl')`);
    root.style.setProperty('--text-3xl', `theme('fontSize.${textSize}.3xl')`);
    root.style.setProperty('--text-4xl', `theme('fontSize.${textSize}.4xl')`);
    root.style.setProperty('--text-5xl', `theme('fontSize.${textSize}.5xl')`);
    root.style.setProperty('--text-6xl', `theme('fontSize.${textSize}.6xl')`);
  }