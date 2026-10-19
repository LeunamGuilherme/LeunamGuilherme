import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

def render_heatmap(json_path="data/contributions.json", output_svg="contrib-heatmap.svg"):
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return

    box_size = 11
    box_gap = 3
    start_x = 20
    start_y = 30

    weeks = [data[i:i+7] for i in range(0, len(data), 7)]
    width = len(weeks) * (box_size + box_gap) + 40
    height = 7 * (box_size + box_gap) + 60

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '  <style>',
        '    .bg { fill: #0d1117; rx: 6px; }',
        '    .border { stroke: #30363d; stroke-width: 1px; fill: none; }',
        '    .text { font-family: monospace; font-size: 12px; fill: #8b949e; }',
        '    @keyframes slideIn { from { opacity: 0; transform: scale(0.5); } to { opacity: 1; transform: scale(1); } }',
        '    .day { animation: slideIn 0.3s ease-out forwards; transform-origin: center; opacity: 0; }',
        '  </style>',
        '  <rect width="100%" height="100%" class="bg"/>',
        '  <rect width="100%" height="100%" class="border" rx="6"/>',
        f'  <text x="{start_x}" y="20" class="text">Gráfico de Contribuições do GitHub</text>'
    ]

    for w_idx, week in enumerate(weeks):
        for d_idx, day in enumerate(week):
            x = start_x + w_idx * (box_size + box_gap)
            y = start_y + d_idx * (box_size + box_gap)
            level = min(day.get("level", 0), len(PALETTE) - 1)
            color = PALETTE[level]
            delay = (w_idx * 0.02) + (d_idx * 0.01)

            rect = f'  <rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" rx="2" fill="{color}" class="day" style="animation-delay: {delay:.2f}s;"/>'
            svg_lines.append(rect)

    svg_lines.append('</svg>')

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))

    print(f"Gráfico de contribuições gerado com sucesso em: {output_svg}")

if __name__ == "__main__":
    render_heatmap()
