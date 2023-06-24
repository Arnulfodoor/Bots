import nltk
import re
from nltk.chat.util import Chat, reflections

pares = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, ¿cómo puedo ayudarte?",]
    ],
    [
        r"c[oó]mo (est[áa]s|andas|vas) ?",
        ["Estoy bien, gracias. ¿Y tú?",]
    ],
    [
        r"qu[eé] (.*) quieres ?",
        ["Estoy aquí para responder tus preguntas sobre programación.",]
    ],
    [
        r"c[oó]mo te llamas ?",
        ["Puedes llamarme Chatbot y estoy aquí para ayudarte.",]
    ],
    [
        r"adi[oó]s",
        ["Hasta luego. ¡Que tengas un buen día!",]
    ],
]

def preprocesar_entrada(entrada):
    entrada = entrada.lower()
    entrada = re.sub(r'[^\w\s]', '', entrada)
    entrada = re.sub(r'^\d+', '', entrada)
    entrada = entrada.strip()
    return entrada

def crear_chatbot():
    print("¡Hola! Soy un chatbot programado para responder preguntas sobre programación. Puedes preguntarme cualquier cosa. Escribe 'adiós' para salir.")
    chatbot = Chat(pares, reflections)
    
    while True:
        entrada = input("Tú: ")
        if entrada.lower() == "adiós":
            print("Chatbot: ¡Hasta luego! Que tengas un buen día.")
            break
        entrada = preprocesar_entrada(entrada)
        respuesta = chatbot.respond(entrada)
        print("Chatbot:", respuesta)

crear_chatbot()
