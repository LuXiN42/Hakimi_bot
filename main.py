import os
import random
import asyncio
from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters

load_dotenv()
0
token = "7114835642:AAF9XV6TRRW6Os465vxLPSo_wCF9rAIy-PU"

async def start(update, context):
    await update.message.reply_text("""Bienvenue sur le bot des Sunset.
Je suis Hakimi le bot préféré de ton bot préféré.
Tu peux faire : 
    - /dj
    - /rire
    - /liens
    - /chant
    - /fb
    - /president
    - /prochainpres
    - /capartencouilles
    - /canard
    - /meow
    - /snuss
    - /cachuetes
    - /dance
                                    """)


async def liens(update, context):
    keyboard = [
        [InlineKeyboardButton('Instagram', 'https://www.instagram.com/bde.sunset/')],
        [InlineKeyboardButton('Site', 'https://liste-sunset.fr/')],
        [InlineKeyboardButton('Youtube', 'https://youtube.com/@liste-sunset?si=FvB00brajx9j47bR')],
        [InlineKeyboardButton('TikTok', 'https://www.tiktok.com/@liste_sunset')],
        [InlineKeyboardButton('Canal', 'https://t.me/+uItkhH-TFwpmMGE0')]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text("Voici nos différents réseaux sociaux :",
                                    reply_markup = reply_markup)
    


######################################################################################################################
###################################################   VIDEO   ########################################################
######################################################################################################################


async def cacahuetes(update, context):
    video_path = "media/cacahuètes.mp4"  
    if os.path.exists(video_path):
        await update.message.reply_video(video=open(video_path, 'rb'))
    else:
        await update.message.reply_text("Désolé, la vidéo n'a pas pu être trouvée.")


async def dance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Dossier contenant les vidéos
    video_dir = "media/dance"
    videos = [f for f in os.listdir(video_dir) if f.endswith(".mp4")]
    
    if videos:
        # Choisir une vidéo aléatoirement
        video_choisi = random.choice(videos)
        video_path = os.path.join(video_dir, video_choisi)
        
        # Envoyer la vidéo
        await update.message.reply_video(video=open(video_path, "rb"))
    else:
        await update.message.reply_text("Désolé, il n'y a pas de vidéos disponibles.")


async def dj(update, context):
    video_path = "media/dj.MOV"  
    if os.path.exists(video_path):
        await update.message.reply_video(video=open(video_path, 'rb'))
    else:
        await update.message.reply_text("Désolé, la vidéo n'a pas pu être trouvée.")
        

async def sagmmescouilles(update, context):
    video_path = "media/sagmmescouilles.MP4"  
    if os.path.exists(video_path):
        await update.message.reply_video(video=open(video_path, 'rb'))
    else:
        await update.message.reply_text("Désolé, la vidéo n'a pas pu être trouvée.")


######################################################################################################################
#################################################   VOCAUX   #########################################################
######################################################################################################################


async def canard(update, context):
    # Liste des fichiers vocaux dans le dossier media/vocaux
    vocaux_path = "media/vocaux/"
    vocaux = [f for f in os.listdir(vocaux_path) if f.endswith(('.m4a', '.ogg'))]
    
    if vocaux:
        # Choisir un fichier aléatoire
        vocal_choisi = random.choice(vocaux)
        vocal_path = os.path.join(vocaux_path, vocal_choisi)
        
        # Envoyer le fichier vocal choisi
        await update.message.reply_voice(voice=open(vocal_path, 'rb'))
    else:
        await update.message.reply_text("Désolé, il n'y a pas de fichiers vocaux disponibles.")


async def chant(update, context):
    # Liste des fichiers vocaux dans le dossier media/vocaux
    vocaux_path = "media/vocaux/chants"
    vocaux = [f for f in os.listdir(vocaux_path) if f.endswith(('.ogg', '.mp3'))]
    
    if vocaux:
        # Choisir un fichier aléatoire
        vocal_choisi = random.choice(vocaux)
        vocal_path = os.path.join(vocaux_path, vocal_choisi)
        
        # Envoyer le fichier vocal choisi
        await update.message.reply_voice(voice=open(vocal_path, 'rb'))
    else:
        await update.message.reply_text("Désolé, il n'y a pas de fichiers vocaux disponibles.")


async def meow(update, context):
    # Liste des fichiers vocaux dans le dossier media/vocaux
    vocaux_path = "media/vocaux/meow"
    vocaux = [f for f in os.listdir(vocaux_path) if f.endswith(('.m4a', '.ogg'))]
    
    if vocaux:
        # Choisir un fichier aléatoire
        vocal_choisi = random.choice(vocaux)
        vocal_path = os.path.join(vocaux_path, vocal_choisi)
        
        # Envoyer le fichier vocal choisi
        await update.message.reply_voice(voice=open(vocal_path, 'rb'))
    else:
        await update.message.reply_text("Désolé, il n'y a pas de fichiers vocaux disponibles.")


async def rire(update, context):
    # Liste des fichiers vocaux dans le dossier media/vocaux
    vocaux_path = "media/vocaux/rires"
    vocaux = [f for f in os.listdir(vocaux_path) if f.endswith(('.ogg', '.mp3'))]
    
    if vocaux:
        # Choisir un fichier aléatoire
        vocal_choisi = random.choice(vocaux)
        vocal_path = os.path.join(vocaux_path, vocal_choisi)
        
        # Envoyer le fichier vocal choisi
        await update.message.reply_voice(voice=open(vocal_path, 'rb'))
    else:
        await update.message.reply_text("Désolé, il n'y a pas de fichiers vocaux disponibles.")


######################################################################################################################
###############################################   MESSAGES   #########################################################
######################################################################################################################


async def fb(update, context):
    # Liste des phrases à envoyer de façon aléatoire
    phrases = [
        "Ici breakfun, merci pour les cautions, on s'est régalé",
        "Il est 21h passé tout le monde se tait",
        "Fuckbreak",
        "Alors elles sont passés où les bannières ?",
        "Au revoir baptiste"
    ]
    
    # Choisir une phrase aléatoire
    phrase_choisie = random.choice(phrases)
    
    # Envoyer la phrase choisie
    await update.message.reply_text(phrase_choisie)


async def president(update, context):
    # Liste des phrases à envoyer de façon aléatoire
    phrases = [
        "On en est au combien déjà ?",
        "Qui veut devenir président ?",
        "Ca fait long Antonin tu veux pas on change ?"
    ]
    
    # Choisir une phrase aléatoire
    phrase_choisie = random.choice(phrases)
    
    # Envoyer la phrase choisie
    await update.message.reply_text(phrase_choisie)


async def nextPres(update, context):
    # Liste des phrases à envoyer de façon aléatoire
    phrase = "Le prochain président est"
    
    # Liste des noms des 28 personnes
    personnes = [
        "Andréa", "Lucas", "Kevin", "Clémence", "Eloise", "Jonathan", "Sofiane", 
        "Antonin", "Romain", "Lou", "Lilou", "Wail", "Enora", "Killian", "Loïc", 
        "Matthias", "Sophie", "Anfel", "Clément", "Tom", "Jonastan", "Daphné", 
        "Maël", "Charly", "Circé", "Sirine", "Vincent", "Emilline"
    ]

    random_person = random.choice(personnes)
    phrase += f" {random_person} SET"
    
    # Envoyer la phrase choisie
    await update.message.reply_text(phrase)


async def nimp(update, context):
    # Liste des phrases à envoyer de façon aléatoire
    phrase = "c’est des poulets mafieux au cinéma après avoir durement travaillé au téléphone rose et vendu des 10 balles pour repayer le téléphone de sofiane, il y a une bagarre au sunset à cergy pref entre des moutons pré aid et des poules pré chicken street qui se battent le rainté en match à mort par équipe, y’a aussi un lion sous dégradé à blanc qui s’est battu après les poules vont en soirée et elles twerkent ou dansent sur de la tectonic et y a le loup qui les surveillent et si elles dansent pas il les mange avec de la sauce salsa qui pique vraiment vraiment beaucoup parce que c'est de la sauce mexicaine qui vient de Pablo Escobar"

    
    # Envoyer la phrase choisie
    await update.message.reply_text(phrase)

        
async def snuss(update, context):
    # Liste des phrases à envoyer de façon aléatoire
    phrases = [
        "J'ai du HARDCORE",
        "C'est du 12 mg de nicotine",
        "La dernière fois que j'en ai pris j'étais en bad trip"
    ]
    
    # Choisir une phrase aléatoire
    phrase_choisie = random.choice(phrases)
    
    # Envoyer la phrase choisie
    await update.message.reply_text(phrase_choisie)
    
    



if __name__ == '__main__':
    app = Application.builder().token(token).build()
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('liens', liens))
    app.add_handler(CommandHandler('dj', dj))
    app.add_handler(CommandHandler('rire', rire))
    app.add_handler(CommandHandler('chant', chant))
    app.add_handler(CommandHandler('fb', fb))
    app.add_handler(CommandHandler('president', president))
    app.add_handler(CommandHandler('prochainpres', nextPres))
    app.add_handler(CommandHandler('capartencouilles', nimp))
    app.add_handler(CommandHandler('canard', canard))
    app.add_handler(CommandHandler('meow', meow))
    app.add_handler(CommandHandler('snuss', snuss))
    app.add_handler(CommandHandler('cacahuetes', cacahuetes))
    app.add_handler(CommandHandler('sagmmescouilles', sagmmescouilles))
    app.add_handler(CommandHandler('dance', dance))
    
    
    
    
    
    
    app.run_polling(poll_interval=5)