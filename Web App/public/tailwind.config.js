/** @type {import('tailwindcss').Config} */
module.exports = {
      content: [
            "./index.html",
            "./showcase/index.html",
            "./face-detection/index.html",
            "./image-enhancement/index.html",
            "./settings/index.html",
            "./download/index.html",
      ],
      theme: {
        extend: {
            fontSize: {
                'xs': '1rem',
                'sm': '1.25rem',
                'base': '1.5em',
                'lg': '1.75rem',
                'xl': '2rem',
                '2xl': '2.25rem',
                '3xl': '2.5rem',
                '4xl': '2.75rem',
                '5xl': '3rem',
                '6xl': '4rem',
            },
            screens: {
                  xs: "350px",
                  mobile: "860px",
                  md: "1100px",
            },
            colors: {
            primary: { "50": "#eff6ff", "100": "#dbeafe", "200": "#bfdbfe", "300": "#93c5fd", "400": "#60a5fa", "500": "#3b82f6", "600": "#2563eb", "700": "#1d4ed8", "800": "#1e40af", "900": "#1e3a8a" },
        },
      },
      plugins: [
        require('flowbite/plugin'),
        require("daisyui"),
    ]
}
}