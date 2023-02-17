/** @type {import('tailwindcss').Config} */
module.exports = {
      content: ["./*.{html,js}"],
      theme: {
            screens: {
                  xs: "350px",
                  md: "1100px",
            },
            colors: {
            'seablue': '#79bde9',
            'blue': '#3d7bd5',
            'darkblue': '#1a40c1',
            'black': '#000000',
            'white': '#ffffff',
            'lightgray': '#393c41',
            'gray': '#181c22',
        extend: {},
      },
      plugins: [
        require('flowbite/plugin'),
        require('@tailwindcss/line-clamp'),
    ]
}
}