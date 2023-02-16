/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.{html,js}"],
  theme: {
      extend: {
        colors: {
          primary: "#0B65C6",
          secondary: "#EEF1F6",
          tertiary: "#0e1133",
  
          lightBlue: "#E1F6FE",
          lightPink: "#FDEEDC",
          lightGreen: "#E1FDE2",

          "bookmark-purple": "#5267DF",
          "bookmark-red": "#FA5959",
          "bookmark-blue": "#242A45",
          "bookmark-grey": "#9194A2",
          "bookmark-white": "#f7f7f7",
        },
      },
      fontFamily: {
        IBMPlex: ["IBM Plex Sans", "sans-serif"],
      },
      containerShowcase: {
            center: true,
            padding: "1rem",
            screens: {
              lg: "1124px",
              xl: "1124px",
              "2xl": "1124px",
            },
          },
    },
  plugins: [
    require('flowbite/plugin'),
    require('@tailwindcss/line-clamp'),
]
}