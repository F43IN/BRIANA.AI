import speech_recognition as sr
import openai
from playsound import playsound
from requests import get
from bs4 import BeautifulSoup
from gtts import gTTS
import webbrowser as browser

openai.api_key = "enterYourAPIKey"

hotword = "briana"

def mic_detect():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        #while True:
        print("Como posso ajudar?")
        audio = mic.listen(source)
        try:
            trigger = (mic.recognize_whisper_api(audio, api_key=openai.api_key))
            trigger = trigger.lower()
                
            if hotword in trigger:
                print("COMANDO: ", trigger)
                if "obrigado" in trigger:
                    denada()
                else:
                    exe_com(trigger)
                   # break
                
        except sr.RequestError as e:
            print("Could not request results from Whisper API")

    
def resp(arq):
    playsound("enter/file/path" + arq + ".mp3")
    feedback = open("enter/file/path" + arq + ".mp3", "rb")
    transcricao = openai.Audio.transcribe("whisper-1", feedback)
    print(f"\n  {transcricao}  \n")

def cria_audio(mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save("C:/Users/yourUserName/BRIANA/resp_din.mp3")
    playsound("C:/Users/yourUserName/BRIANA/resp_din.mp3")

def exe_com(trigger):
    if "notícias" in trigger:
        resp("resposta_1")
        noticias_do_dia()
    elif "música" in trigger:
        musica()        
    else:
        mensagem = trigger.strip(hotword)
        cria_audio(mensagem)
        print("COMANDO INVALIDO: ", mensagem)
        resp("resposta_4")


#####__COMANDOS__#####

        
def noticias_do_dia():
    playsound("C:/Users/yourUserName/BRIANA/falas/resposta_2.mp3")
    site = get("https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419")
    noticias = BeautifulSoup(site.text, "html.parser")
    for item in noticias.findAll("item")[:3]:
        mensagem = item.title.text
        print("\n", mensagem)
        cria_audio(mensagem)
        
def denada():
    print("\nDe nada! :)")
    playsound("C:/Users/yourUserName/BRIANA/falas/resposta_3.mp3")

def musica():
    resp("resposta_5")
    browser.open("https://open.spotify.com/intl-pt/track/2iNQ124Rh953SjXTSZhuLd?si=1fc2f475198e4b19")
    

#####__FUNÇÃO_PRINCIPAL__#####

def main():    
    while True:
        mic_detect()

main()
