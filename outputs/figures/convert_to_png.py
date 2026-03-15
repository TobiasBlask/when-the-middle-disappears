#!/usr/bin/env python3
"""Convert HTML figure files to high-resolution PNG images using Playwright."""

from playwright.sync_api import sync_playwright
from pathlib import Path

FIGURES_DIR = Path("/Users/tobias-benediktblask/2026_Order_Effects_Paper/outputs/figures")

figures = [
    ("fig1_methodology.html", "fig1_methodology.png", 1400, 540),
    ("fig2_consensus_heatmap.html", "fig2_consensus_heatmap.png", 1100, 700),
    ("fig3_geopolitical_divergence.html", "fig3_geopolitical_divergence.png", 1100, 850),
    ("fig4_three_order_cascade.html", "fig4_three_order_cascade.png", 1200, 880),
]

with sync_playwright() as p:
    browser = p.chromium.launch()

    for html_file, png_file, width, height in figures:
        html_path = FIGURES_DIR / html_file
        png_path = FIGURES_DIR / png_file

        page = browser.new_page(
            viewport={"width": width + 60, "height": height + 60},
            device_scale_factor=3,  # 3x for ~300 DPI
        )
        page.goto(f"file://{html_path}")
        page.wait_for_timeout(500)

        # Screenshot the figure container
        container = page.locator(".figure-container")
        container.screenshot(path=str(png_path), type="png")
        page.close()
        print(f"Saved: {png_path.name} ({png_path.stat().st_size // 1024} KB)")

    browser.close()
    print("\nAll figures converted successfully.")
