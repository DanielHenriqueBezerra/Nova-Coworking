import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  base: "/Nova-Coworking/",
  plugins: [react()],
  build: {
    outDir: "../../docs",
    emptyOutDir: true,
  },
});
