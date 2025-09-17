import path from 'path';
import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig(({ mode }) => {
    const env = loadEnv(mode, '.', '');
    return {
      plugins: [react({
        include: "**/*.{jsx,tsx}",
      })],
      define: {
        'process.env.API_KEY': JSON.stringify(env.GEMINI_API_KEY),
        'process.env.GEMINI_API_KEY': JSON.stringify(env.GEMINI_API_KEY)
      },
      resolve: {
        alias: {
          '@': path.resolve(__dirname, '.'),
        }
      },
      assetsInclude: [],
      css: {
        postcss: {
          plugins: []
        }
      },
      esbuild: {
        logOverride: { 'this-is-undefined-in-esm': 'silent' }
      },
      optimizeDeps: {
        include: ['react', 'react-dom'],
        exclude: ['tailwindcss', 'postcss', 'autoprefixer']
      },
      build: {
        cssCodeSplit: false,
        rollupOptions: {
          external: [],
          output: {
            manualChunks: {
              react: ['react', 'react-dom']
            }
          }
        }
      }
    };
});
