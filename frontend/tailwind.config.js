// tailwind.config.js
module.exports = {
  darkMode: 'class',
  content: [
    './src/**/*.{js,ts,jsx,tsx}',
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './app/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        background: 'hsl(210, 30%, 5%)', // near-black/navy
        accent: 'hsl(190, 80%, 50%)', // electric cyan
        success: 'hsl(120, 80%, 40%)', // green
        warning: 'hsl(45, 100%, 50%)', // amber
        danger: 'hsl(0, 80%, 50%)', // red
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
