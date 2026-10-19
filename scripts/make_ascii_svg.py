import cv2
import numpy as np

RAMP = " .:-=+*cs#%@"  # Do mais claro (espaço) ao mais escuro (@)

def image_to_ascii(img_path, width=100):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Imagem {img_path} não encontrada.")
        
    h, w = img.shape
    aspect_ratio = h / w
    height = int(width * aspect_ratio * 0.55)  # Ajuste para a proporção dos caracteres
    resized = cv2.resize(img, (width, height))
    
    ascii_grid = []
    for row in resized:
        line = ""
        for pixel in row:
            index = int((pixel / 255) * (len(RAMP) - 1))
            line += RAMP[index]
        ascii_grid.append(line)
    return ascii_grid

def create_svg(ascii_grid, output_svg="avi-ascii.svg"):
    font_size = 10
    char_width = 6
    line_height = 12
    
    width = len(ascii_grid[0]) * char_width + 20
    height = len(ascii_grid) * line_height + 20
    
    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '  <style>',
        '    .ascii-text { font-family: monospace; font-size: 10px; fill: #8b949e; white-space: pre; }',
        '    @keyframes wipe { 0% { width: 0%; } 100% { width: 100%; } }',
        '    .line { overflow: hidden; display: inline-block; animation: wipe 0.8s ease-out forwards; }',
        '  </style>',
        '  <rect width="100%" height="100%" fill="#0d1117" rx="6"/>',
        f'  <text x="10" y="20" class="ascii-text">'
    ]
    
    delay = 0.0
    for i, line in enumerate(ascii_grid):
        # Escapar caracteres especiais para XML/SVG
        escaped_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        y = 20 + i * line_height
        svg_lines.append(f'    <tspan x="10" y="{y}">{escaped_line}</tspan>')
        
    svg_lines.extend([
        '  </text>',
        '</svg>'
    ])
    
    with open(output_svg, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))
    print(f"SVG ASCII gerado com sucesso em: {output_svg}")

if __name__ == "__main__":
    grid = image_to_ascii("source-prepped.png", width=90)
    create_svg(grid)
