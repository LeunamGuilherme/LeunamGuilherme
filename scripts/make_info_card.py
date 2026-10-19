def generate_info_card(output_svg="info-card.svg"):
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" width="490" height="350" viewBox="0 0 490 350">
  <style>
    .bg { fill: #0d1117; rx: 6px; }
    .title { font-family: monospace; font-size: 14px; font-weight: bold; fill: #58a6ff; }
    .key { font-family: monospace; font-size: 12px; font-weight: bold; fill: #79c0ff; }
    .value { font-family: monospace; font-size: 12px; fill: #c9d1d9; }
    .border { stroke: #30363d; stroke-width: 1px; fill: none; }
    
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(5px); }
      to { opacity: 1; transform: translateY(0); }
    }
    
    .line { animation: fadeIn 0.5s ease-out forwards; opacity: 0; }
    .l1 { animation-delay: 0.2s; }
    .l2 { animation-delay: 0.4s; }
    .l3 { animation-delay: 0.6s; }
    .l4 { animation-delay: 0.8s; }
    .l5 { animation-delay: 1.0s; }
  </style>
  
  <rect width="100%" height="100%" class="bg" />
  <rect width="100%" height="100%" class="border" rx="6" />
  
  <!-- Cabeçalho do Terminal -->
  <g transform="translate(20, 30)" class="line l1">
    <text class="title">guilherme@github ~ $ neofetch</text>
  </g>
  
  <!-- Linha divisória -->
  <path d="M 20 45 L 470 45" stroke="#30363d" stroke-width="1" class="line l1"/>
  
  <!-- Informações -->
  <g transform="translate(20, 80)" class="line l2">
    <text class="key">Role:</text>
    <text x="100" class="value">Full Stack Developer &amp; Student</text>
  </g>
  
  <g transform="translate(20, 120)" class="line l3">
    <text class="key">Course:</text>
    <text x="100" class="value">Mapa do Emprego Full Stack</text>
  </g>
  
  <g transform="translate(20, 160)" class="line l4">
    <text class="key">Stack:</text>
    <text x="100" class="value">Python, Git, HTML/CSS, SQL</text>
  </g>
  
  <g transform="translate(20, 200)" class="line l5">
    <text class="key">Focus:</text>
    <text x="100" class="value">Software Architecture, Automation &amp; Web</text>
  </g>
</svg>'''

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Cartão de informações gerado com sucesso em: {output_svg}")

if __name__ == "__main__":
    generate_info_card()
