import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
import elkLayouts from "https://unpkg.com/@mermaid-js/layout-elk@0/dist/mermaid-layout-elk.esm.min.mjs";


window.mermaid = mermaid;

mermaid.registerLayoutLoaders(elkLayouts);

mermaid.initialize({
  startOnLoad: false,
  securityLevel: "loose",
  layout: "elk"
});


document$.subscribe(() => {
  mermaid.run();
});
