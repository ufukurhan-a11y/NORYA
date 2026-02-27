/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./static/**/*.html",
    "./static/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ["DM Sans", "system-ui", "sans-serif"],
        display: ["Outfit", "DM Sans", "system-ui", "sans-serif"],
      },
      colors: {
        norya: {
          brand: "#e07a5f",
          "brand-hover": "#c9684a",
          "brand-light": "#fdf4f2",
          "brand-muted": "#e8a898",
          trust: "#1e3a5f",
          "trust-light": "#2d4a6f",
          "trust-muted": "#4a6b8a",
          surface: "#f8f9fb",
          "surface-elevated": "#ffffff",
          ink: "#0f1729",
          "ink-muted": "#475569",
          "ink-subtle": "#94a3b8",
          success: "#0d9488",
          "success-light": "#ccfbf1",
          warning: "#d97706",
          "warning-light": "#fef3c7",
          danger: "#b91c1c",
          "danger-light": "#fee2e2",
        },
      },
      borderRadius: {
        norya: "1rem",
        "norya-lg": "1.25rem",
        "norya-xl": "1.5rem",
      },
      boxShadow: {
        norya: "0 2px 8px rgba(14, 23, 41, 0.06)",
        "norya-md": "0 4px 20px rgba(14, 23, 41, 0.08)",
        "norya-lg": "0 8px 32px rgba(14, 23, 41, 0.1)",
        "norya-brand": "0 4px 16px rgba(224, 122, 95, 0.2)",
      },
      spacing: {
        norya: "0.625rem",
        "norya-2": "1.25rem",
        "norya-3": "1.875rem",
        "norya-4": "2.5rem",
      },
    },
  },
  plugins: [],
};
