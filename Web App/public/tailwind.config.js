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
            screens: {
                  xs: "350px",
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