(async () => {
    // Import Mermaid 11 (latest stable with better ELK support)
    const mermaid = (await import("https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs")).default;
    
    // Import ELK layout engine
    const elkLayouts = (await import("https://cdn.jsdelivr.net/npm/@mermaid-js/layout-elk@0.1.4/dist/mermaid-layout-elk.esm.min.mjs")).default;

    // Register ELK
    mermaid.registerLayoutLoaders([elkLayouts]);

    // Initialize with ELK as default renderer for flowcharts
    mermaid.initialize({
        startOnLoad: true,
        flowchart: {
            defaultRenderer: "elk"
        },
        theme: "dark" // Default to dark, material theme will override via CSS if needed
    });
})();
