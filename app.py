from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from dotenv import load_dotenv
import google.generativeai as genai
import random
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
CORS(app)

# Chargement des variables d'environnement
load_dotenv()

# Configuration de l'API Gemini
genai.configure(api_key=os.getenv("AIzaSyBNAXF0JBzQ_uctOMaJcQUP9XkM2wuUl4Q"))

# Initialisation du modèle
model = genai.GenerativeModel('gemini-pro')

# Base de données des psychologues par gouvernorat
psychologists = {
    "Tunis": [
        {"name": "Dr. Amira Ben Salem", "specialty": "thérapie cognitivo-comportementale", "quote": "Chaque jour est une nouvelle opportunité de guérison et de croissance."},
        {"name": "Dr. Mehdi Trabelsi", "specialty": "psycho-oncologie", "quote": "Ensemble, nous pouvons transformer les défis en force intérieure."}
    ],
    "Sfax": [
        {"name": "Dr. Leila Bouazizi", "specialty": "thérapie de groupe", "quote": "La force ne vient pas du corps, mais d'une volonté indomptable."},
        {"name": "Dr. Karim Gharsallah", "specialty": "gestion du stress", "quote": "Chaque pas compte dans votre voyage vers le bien-être."}
    ],
    "Sousse": [
        {"name": "Dr. Fatma Zouari", "specialty": "thérapie familiale", "quote": "Dans l'unité familiale, nous trouvons notre plus grande force."},
        {"name": "Dr. Nabil Hadj Ali", "specialty": "mindfulness", "quote": "La paix intérieure est votre allié le plus puissant dans cette bataille."}
    ],
}

def get_ai_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Désolé, une erreur s'est produite : {str(e)}"

@app.route('/')
def serve_index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    action = data.get('action', '')
    message = data.get('message', '')
    stage = data.get('stage', '')
    governorate = data.get('governorate', '')
    emotion = data.get('emotion', '')

    if action == 'motivation':
        prompt = "Donnez une citation motivante et encourageante pour une patiente atteinte d'un cancer du sein, en mettant l'accent sur la force intérieure et l'espoir."
    elif action == 'recommendation':
        prompt = f"Donnez une recommandation spécifique pour une patiente atteinte d'un cancer du sein au stade {stage}, en incluant des conseils pour le bien-être émotionnel et la gestion du stress."
    elif action == 'psychologist':
        if governorate in psychologists:
            psychologist = random.choice(psychologists[governorate])
            return jsonify({"response": f"J'aimerais vous présenter {psychologist['name']}, spécialisé(e) en {psychologist['specialty']}. {psychologist['name']} a un message pour vous : '{psychologist['quote']}' N'hésitez pas à prendre contact avec {psychologist['name']}, qui saura vous accompagner avec empathie et professionnalisme dans votre parcours."})
        else:
            return jsonify({"response": "Je comprends que vous cherchiez un soutien psychologique dans votre région. Malheureusement, je n'ai pas de psychologue spécifique à recommander dans votre gouvernorat pour le moment. Cependant, je vous encourage vivement à contacter la Ligue nationale contre le cancer. Ils pourront vous orienter vers des professionnels qualifiés et bienveillants, prêts à vous accompagner dans votre parcours. N'oubliez pas, vous n'êtes pas seule dans cette épreuve."})
    elif action == 'coping-strategy':
        prompt = "Suggérez une stratégie d'adaptation efficace pour les patients atteints de cancer du sein, en mettant l'accent sur la gestion des émotions et le maintien d'une attitude positive."
    elif action == 'relaxation-exercise':
        prompt = "Décrivez un exercice de relaxation simple et efficace pour aider les patients atteints de cancer du sein à réduire leur stress et leur anxiété."
    elif action == 'emotional-response':
        prompt = f"En tant qu'assistant psychologique empathique, donnez une réponse réconfortante et encourageante à une patiente atteinte d'un cancer du sein qui se sent {emotion}. Utilisez un langage chaleureux et rassurant."
    else:
        prompt = f"En tant qu'assistant psychologique empathique spécialisé dans le soutien aux patientes atteintes d'un cancer du sein au stade {stage}, répondez avec beaucoup d'empathie, de compréhension et d'encouragement à ce message : {message}. Offrez un soutien émotionnel chaleureux et des conseils pratiques bienveillants."

    response = get_ai_response(prompt)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)