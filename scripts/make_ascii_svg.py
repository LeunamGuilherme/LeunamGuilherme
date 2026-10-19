import cv2

RAMP = "@%#*+=-:. "

def image_to_ascii(img_path, width=85):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Imagem {img_path} não encontrada.")
        
    h, w = img.shape
    height = int(width * (h / w) * 0.55)
    resized = cv2.resize(img, (width, height))
    
    ascii_grid = []
    for row in resized:
        line = "".join([RAMP[int((pixel / 255) * (len(RAMP) - 1))] for pixel in row])
        ascii_grid.append(line)
    return ascii_grid

def create_svg(ascii_grid, output_svg="avi-ascii.svg"):
    char_width = 6
    line_height = 11
    width = len(ascii_grid[0]) * char_width + 20
    height = len(ascii_grid) * line_height + 20
    
    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '  <rect width="100%" height="100%" fill="#0d1117" rx="6"/>',
        '  <text x="10" y="15" font-family="monospace" font-size="10" fill="#c9d1d9" xml:space="preserve">'
    ]
    
    for i, line in enumerate(ascii_grid):
        escaped_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        y = 15 + i * line_height
        svg_lines.append(f'    <tspan x="10" y="{y}">{escaped_line}</tspan>')
        
    svg_lines.extend(['  </text>', '</svg>'])
    
    with open(output_svg, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))
    print("avi-ascii.svg atualizado com sucesso!")

if __name__ == "__main__":
    grid = image_to_ascii("source-prepped.png", width=85)
    create_svg(grid)
