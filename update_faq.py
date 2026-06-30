import os
import google.generativeai as genai

# 1. Récupération sécurisée de la clé API
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Erreur : La clé GEMINI_API_KEY est introuvable dans les Secrets GitHub.")
    exit(1)

genai.configure(api_key=api_key)

# 2. Configuration du modèle Gemini (génère du texte ultra-rapide et propre)
model = genai.GenerativeModel('gemini-2.5-flash')

prompt = """
Tu es un expert en SEO et en intelligence artificielle. Rédige une mise à jour quotidienne sous forme de FAQ pour un site web.
Génère exactement 5 blocs HTML (un pour ChatGPT, un pour Gemini, un pour Claude, un pour Canva AI et un pour Perplexity).
Pour chaque outil, trouve 1 question originale et pertinente (astuces de prompt, cas d'usage, nouveautés de productivité) et sa réponse.

Tu dois impérativement respecter EXACTEMENT cette structure HTML pour chaque bloc, sans ajouter de balises Markdown comme ```html autour, donne-moi le code brut directement :

<section>
    <h2 class="ia-title">Outil : [Nom de l'IA]</h2>
    <div class="faq-box">
        <p class="question">💡 [Ta question ici] ?</p>
        <p class="reponse">[Ta réponse optimisée pour le SEO, claire et rédigée en français parfait]</p>
    </div>
</section>

Sois créatif et change les questions par rapport à d'habitude pour apporter de la nouveauté.
"""

try:
    # 3. Demande à Gemini
    response = model.generate_content(prompt)
    nouvelles_faq = response.text.strip()

    # Nettoyage de sécurité si Gemini ajoute des résidus de balises Markdown
    nouvelles_faq = nouvelles_faq.replace("```html", "").replace("```", "").strip()

    # 4. Lecture et modification de index.html
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    start_tag = ""
    end_tag = ""

    if start_tag in html_content and end_tag in html_content:
        parts = html_content.split(start_tag)
        before = parts[0]
        after = parts[1].split(end_tag)[1]

        # Reconstruction propre du fichier index.html
        nouveau_html = f"{before}{start_tag}\n{nouvelles_faq}\n{end_tag}{after}"

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(nouveau_html)
        print("Fichier index.html mis à jour avec succès par Gemini !")
    else:
        print("Erreur : Les balises de repère HTML sont introuvables.")

except Exception as e:
    print(f"Une erreur est survenue lors de l'exécution : {e}")
