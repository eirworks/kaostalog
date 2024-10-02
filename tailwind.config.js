/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        "brand": "#e62129"
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography')
  ],
}

