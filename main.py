import requests
import re

# URL del archivo README.md en el repositorio de GitHub
readme_url = "https://raw.githubusercontent.com/fralfaro/awesome-readme/master/readme.md"

# Obtener el contenido del archivo README.md
response = requests.get(readme_url)
readme_content = response.text

# Expresión regular para encontrar los bloques de información en el README.md
pattern = r"- \[([^\]]+)\]\(([^)]+)\) - (.+)"
matches = re.findall(pattern, readme_content)


# Imprimir los resultados
for match in matches:
    title, url, content = match
    print("- title:", title)
    print("  content: \"" + (content[:81] + '... \"') if len(content) > 82 else content + "\"")
    print("  image:", f"images/{title.replace('/', '-')}.png")
    print("  url:", url)
    print()
