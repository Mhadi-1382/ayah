/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: [
    "./templates/**/*.html",
    "./**/templates/**/*.html"
  ],
  theme: {
    extend: {
      screens: {
        '2md': '868px',
        'xs': '400px',
      }
    },
  },
  plugins: [],
}
