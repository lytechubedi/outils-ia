import os

# 1. On imagine qu'on récupère de nouvelles questions fraîches (via une API ou une liste rotative)
nouvelles_faq = """
        <section>
            <h2 class="ia-title">Astuce du jour : Optimiser ses Prompts</h2>
            <p class="question">💡 Comment obtenir de meilleures réponses avec Gemini ?</p>
            <p class="reponse">Attribuez toujours un rôle à l'IA avant de poser votre question (Ex: 'Agis en tant qu'expert en développement...'). Cela affine la précision des réponses.</p>
        </section>
"""

# 2. Ouvrir et modifier le fichier index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# On localise la zone à mettre à jour
start_tag = ""
end_tag = ""

if start_tag in html_content and end_tag in html_content:
    parts = html_content.split(start_tag)
    before = parts[0]
    after = parts[1].split(end_tag)[1]
    
    # On reconstruit le fichier avec les nouveautés
    nouveau_html = f"{before}{start_tag}{nouvelles_faq}{end_tag}{after}"
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(nouveau_html)
    print("Le site a été mis à jour avec succès !")

