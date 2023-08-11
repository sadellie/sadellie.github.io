/** @type {import('tailwindcss').Config}*/
const config = {
  content: ["./src/**/*.{html,js,svelte,ts}"],

  theme: {
    extend: {
      colors: {
        'unitto': {
          "primary": "#006d34",
          "onPrimary": "#ffffff",
          "primaryContainer": "#7efba0",
          "onPrimaryContainer": "#00210b",
          "primaryFixed": "#7efba0",
          "onPrimaryFixed": "#00210b",
          "primaryFixedDim": "#61de87",
          "onPrimaryFixedVariant": "#005226",
          "secondary": "#506352",
          "onSecondary": "#ffffff",
          "secondaryContainer": "#d3e8d2",
          "onSecondaryContainer": "#0e1f12",
          "secondaryFixed": "#d3e8d2",
          "onSecondaryFixed": "#0e1f12",
          "secondaryFixedDim": "#b7ccb7",
          "onSecondaryFixedVariant": "#394b3b",
          "tertiary": "#3a656e",
          "onTertiary": "#ffffff",
          "tertiaryContainer": "#bdeaf5",
          "onTertiaryContainer": "#001f25",
          "tertiaryFixed": "#bdeaf5",
          "onTertiaryFixed": "#001f25",
          "tertiaryFixedDim": "#a2ced8",
          "onTertiaryFixedVariant": "#204d55",
          "error": "#ba1a1a",
          "errorContainer": "#ffdad6",
          "onError": "#ffffff",
          "onErrorContainer": "#410002",
          "background": "#fcfdf7",
          "onBackground": "#191c19",
          "outline": "#717970",
          "inverseOnSurface": "#f0f1ec",
          "inverseSurface": "#2e312e",
          "inversePrimary": "#61de87",
          "shadow": "#000000",
          "surfaceTint": "#006d34",
          "outlineVariant": "#c1c9be",
          "scrim": "#000000",
          "surface": "#f9faf4",
          "onSurface": "#191c19",
          "surfaceVariant": "#dde5da",
          "onSurfaceVariant": "#414941",
          "surfaceContainerHighest": "#e2e3de",
          "surfaceContainerHigh": "#e7e9e3",
          "surfaceContainer": "#edeee9",
          "surfaceContainerLow": "#f3f4ef",
          "surfaceContainerLowest": "#ffffff",
          "surfaceDim": "#d9dbd5",
          "surfaceBright": "#f9faf4",
          "surfaceContainer-active-hover": "#C4D8C4",
          "surfaceContainer-inactive-hover": "#EAECE6"
        }
      }
    },
  },

  plugins: [],
};

module.exports = config;
