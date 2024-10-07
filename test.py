import os
from dotenv import load_dotenv
import google.generativeai as genai
import random
import tkinter as tk
from tkinter import ttk, scrolledtext
# Chargement des variables d'environnement
load_dotenv()

# Configuration de l'API Gemini
genai.configure(api_key=os.getenv("AIzaSyBNAXF0JBzQ_uctOMaJcQUP9XkM2wuUl4Q"))

# Initialisation du modèle
model = genai.GenerativeModel('gemini-pro')

# Base de données améliorée des psychologues par gouvernorat
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
    # Ajoutez d'autres gouvernorats selon vos besoins
}

def get_ai_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Désolé, une erreur s'est produite : {str(e)}"

def get_motivation():
    prompt = "Donnez une citation motivante et encourageante pour une patiente atteinte d'un cancer du sein, en mettant l'accent sur la force intérieure et l'espoir."
    return get_ai_response(prompt)

def get_recommendation(stage):
    prompt = f"Donnez une recommandation spécifique pour une patiente atteinte d'un cancer du sein au stade {stage}, en incluant des conseils pour le bien-être émotionnel et la gestion du stress."
    return get_ai_response(prompt)

def get_psychologist(governorate):
    if governorate in psychologists:
        psychologist = random.choice(psychologists[governorate])
        return f"J'aimerais vous présenter {psychologist['name']}, spécialisé(e) en {psychologist['specialty']}. {psychologist['name']} a un message pour vous : '{psychologist['quote']}' N'hésitez pas à prendre contact avec {psychologist['name']}, qui saura vous accompagner avec empathie et professionnalisme dans votre parcours."
    else:
        return "Je comprends que vous cherchiez un soutien psychologique dans votre région. Malheureusement, je n'ai pas de psychologue spécifique à recommander dans votre gouvernorat pour le moment. Cependant, je vous encourage vivement à contacter la Ligue nationale contre le cancer. Ils pourront vous orienter vers des professionnels qualifiés et bienveillants, prêts à vous accompagner dans votre parcours. N'oubliez pas, vous n'êtes pas seule dans cette épreuve."

def get_coping_strategy():
    prompt = "Suggérez une stratégie d'adaptation efficace pour les patients atteints de cancer du sein, en mettant l'accent sur la gestion des émotions et le maintien d'une attitude positive."
    return get_ai_response(prompt)

def get_relaxation_exercise():
    prompt = "Décrivez un exercice de relaxation simple et efficace pour aider les patients atteints de cancer du sein à réduire leur stress et leur anxiété."
    return get_ai_response(prompt)

def get_emotional_response(emotion):
    prompt = f"En tant qu'assistant psychologique empathique, donnez une réponse réconfortante et encourageante à une patiente atteinte d'un cancer du sein qui se sent {emotion}. Utilisez un langage chaleureux et rassurant."
    return get_ai_response(prompt)

def chatbot():
    print("Bonjour, je suis votre assistant virtuel de soutien pour le cancer du sein. Je suis là pour vous écouter, vous guider et vous soutenir à chaque étape de votre parcours.")
    patient_stage = input("Pouvez-vous me dire à quel stade de cancer du sein vous êtes (1-4) ? Cela m'aidera à mieux comprendre votre situation. ")
    patient_governorate = input("Dans quel gouvernorat résidez-vous ? Cela me permettra de vous orienter vers des ressources locales si besoin. ")
    patient_emotion = input("Comment vous sentez-vous aujourd'hui ? N'hésitez pas à partager vos émotions, qu'elles soient positives ou négatives. ")
    
    print(f"\nJe vous remercie de partager cela avec moi. Je comprends que vous vous sentez {patient_emotion}. C'est tout à fait normal et valide de ressentir cela. Voici quelques mots pour vous :")
    print(get_emotional_response(patient_emotion))

    while True:
        print("\nComment puis-je continuer à vous soutenir aujourd'hui ? Voici ce que je peux faire pour vous :")
        print("1. Vous offrir une pensée motivante pour illuminer votre journée")
        print("2. Vous donner des recommandations spécifiques adaptées à votre situation")
        print("3. Vous aider à trouver un psychologue bienveillant près de chez vous")
        print("4. Vous suggérer une stratégie d'adaptation pour mieux gérer vos émotions")
        print("5. Vous guider à travers un exercice de relaxation apaisant")
        print("6. Discuter de ce qui vous préoccupe, je suis là pour vous écouter")
        print("7. Terminer notre conversation")
        
        choice = input("Que souhaitez-vous faire ? N'hésitez pas à choisir ce dont vous avez le plus besoin en ce moment (1-7): ")

        if choice == "1":
            print("\nVoici une pensée motivante spécialement pour vous :")
            print(get_motivation())
        elif choice == "2":
            print(f"\nJe comprends que vous êtes au stade {patient_stage}. Voici quelques recommandations qui pourraient vous être utiles :")
            print(get_recommendation(patient_stage))
        elif choice == "3":
            print(f"\nJe sais combien il est important d'avoir un soutien psychologique adapté. Voici une recommandation pour vous :")
            print(get_psychologist(patient_governorate))
        elif choice == "4":
            print("\nGérer ses émotions peut être un défi. Voici une stratégie d'adaptation qui pourrait vous aider :")
            print(get_coping_strategy())
        elif choice == "5":
            print("\nPrenons un moment pour nous détendre. Voici un exercice de relaxation que vous pouvez essayer :")
            print(get_relaxation_exercise())
        elif choice == "6":
            user_input = input("\nJe suis là pour vous écouter. Que souhaitez-vous partager avec moi aujourd'hui ? ")
            prompt = f"En tant qu'assistant psychologique empathique spécialisé dans le soutien aux patientes atteintes d'un cancer du sein au stade {patient_stage}, répondez avec beaucoup d'empathie, de compréhension et d'encouragement à ce message : {user_input}. Offrez un soutien émotionnel chaleureux et des conseils pratiques bienveillants."
            print("\nMerci de partager cela avec moi. Voici ce que je peux vous dire :")
            print(get_ai_response(prompt))
        elif choice == "7":
            print("Je vous remercie pour cette conversation. N'oubliez jamais que vous êtes forte, courageuse, et que chaque jour est une victoire. Je suis là pour vous soutenir à chaque étape de votre parcours. Prenez soin de vous et n'hésitez pas à revenir me voir quand vous en ressentez le besoin. Vous n'êtes pas seule dans cette épreuve.")
            break
        else:
            print("Je n'ai pas bien compris votre choix. Pouvez-vous le répéter s'il vous plaît ?")
        
        input("\nQuand vous vous sentez prête à continuer, appuyez simplement sur Entrée...")

if __name__ == "__main__":
    chatbot()