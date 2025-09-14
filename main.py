import os
import random
from pathlib import Path
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Charger .env en local (sans effet sur Fly si tu utilises fly secrets)
load_dotenv()

# Récupérer le token depuis l'environnement
TOKEN = os.environ.get("TELEGRAM_TOKEN")
if not TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN manquant. Définis-le via fly secrets set TELEGRAM_TOKEN=...")

# Racine des médias (assure-toi que ces chemins existent dans l'image Docker)
MEDIA_DIR = Path("media")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bienvenue sur le bot des Sunset.\n"
        "Je suis Hakimi le bot préféré de ton bot préféré.\n"
        "Tu peux faire : \n"
        "    - /dj\n"
        "    - /rire\n"
        "    - /liens\n"
        "    - /chant\n"
        "    - /fb\n"
        "    - /president\n"
        "    - /prochainpres\n"
        "    - /capartencouilles\n"
        "    - /canard\n"
        "    - /meow\n"
        "    - /snuss\n"
        "    - /cacahuetes\n"
        "    - /sagmmescouilles\n"
        "    - /dance\n"
    )

async def liens(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton('Instagram', url='https://www.instagram.com/bde.sunset/')],
        [InlineKeyboardButton('Site', url='https://liste-sunset.fr/')],
        [InlineKeyboardButton('Youtube', url='https://youtube.com/@liste-sunset?si=FvB00brajx9j47bR')],
        [InlineKeyboardButton('TikTok', url='https://www.tiktok.com/@liste_sunset')],
        [InlineKeyboardButton('Canal', url='https://t.me/+uItkhH-TFwpmMGE0')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Voici nos différents réseaux sociaux :", reply_markup=reply_markup)

# --------------------------------- VIDEOS ---------------------------------


async def send_video_path(update: Update, path: Path):
    if path.exists():
        with path.open("rb") as f:
            await update.message.reply_video(video=f)
    else:
        await update.message.reply_text("Désolé, la vidéo n'a pas pu être trouvée.")


async def cacahuetes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_video_path(update, MEDIA_DIR / "cacahuètes.mp4")


async def dj(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_video_path(update, MEDIA_DIR / "dj.MOV")


async def sagmmescouilles(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_video_path(update, MEDIA_DIR / "sagmmescouilles.MP4")


async def dance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video_dir = MEDIA_DIR / "dance"
    if not video_dir.is_dir():
        await update.message.reply_text("Désolé, le dossier des vidéos n'existe pas.")
        return
    videos = [p for p in video_dir.iterdir() if p.suffix.lower() == ".mp4"]
    if not videos:
        await update.message.reply_text("Désolé, il n'y a pas de vidéos disponibles.")
        return
    await send_video_path(update, random.choice(videos))


# --------------------------------- VOIX ---------------------------------


async def send_voice_path(update: Update, path: Path):
    if path.exists():
        with path.open("rb") as f:
            await update.message.reply_voice(voice=f)
    else:
        await update.message.reply_text("Désolé, le fichier vocal est introuvable.")


async def canard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    vocaux_path = MEDIA_DIR / "vocaux"
    if not vocaux_path.is_dir():
        await update.message.reply_text("Désolé, aucun dossier de vocaux.")
        return
    vocaux = [p for p in vocaux_path.iterdir() if p.suffix.lower() in (".m4a", ".ogg")]
    if not vocaux:
        await update.message.reply_text("Désolé, il n'y a pas de fichiers vocaux disponibles.")
        return
    await send_voice_path(update, random.choice(vocaux))


async def chant(update: Update, context: ContextTypes.DEFAULT_TYPE):
    vocaux_path = MEDIA_DIR / "vocaux" / "chants"
    if not vocaux_path.is_dir():
        await update.message.reply_text("Désolé, aucun dossier de chants.")
        return
    vocaux = [p for p in vocaux_path.iterdir() if p.suffix.lower() in (".ogg", ".mp3")]
    if not vocaux:
        await update.message.reply_text("Désolé, il n'y a pas de fichiers vocaux disponibles.")
        return
    await send_voice_path(update, random.choice(vocaux))


async def meow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    vocaux_path = MEDIA_DIR / "vocaux" / "meow"
    if not vocaux_path.is_dir():
        await update.message.reply_text("Désolé, aucun dossier 'meow'.")
        return
    vocaux = [p for p in vocaux_path.iterdir() if p.suffix.lower() in (".m4a", ".ogg")]
    if not vocaux:
        await update.message.reply_text("Désolé, il n'y a pas de fichiers vocaux disponibles.")
        return
    await send_voice_path(update, random.choice(vocaux))


async def rire(update: Update, context: ContextTypes.DEFAULT_TYPE):
    vocaux_path = MEDIA_DIR / "vocaux" / "rires"
    if not vocaux_path.is_dir():
        await update.message.reply_text("Désolé, aucun dossier 'rires'.")
        return
    vocaux = [p for p in vocaux_path.iterdir() if p.suffix.lower() in (".ogg", ".mp3")]
    if not vocaux:
        await update.message.reply_text("Désolé, il n'y a pas de fichiers vocaux disponibles.")
        return
    await send_voice_path(update, random.choice(vocaux))


# ------------------------------- TEXTES ---------------------------------


async def fb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phrases = [
        "Ici breakfun, merci pour les cautions, on s'est régalé",
        "Il est 21h passé tout le monde se tait",
        "Fuckbreak",
        "Alors elles sont passés où les bannières ?",
        "Au revoir baptiste",
    ]
    await update.message.reply_text(random.choice(phrases))


async def president(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phrases = [
        "On en est au combien déjà ?",
        "Qui veut devenir président ?",
        "Ca fait long Antonin tu veux pas on change ?",
    ]
    await update.message.reply_text(random.choice(phrases))


async def nextPres(update: Update, context: ContextTypes.DEFAULT_TYPE):
    personnes = [
        "Andréa","Lucas","Kevin","Clémence","Eloise","Jonathan","Sofiane",
        "Antonin","Romain","Lou","Lilou","Wail","Enora","Killian","Loïc",
        "Matthias","Sophie","Anfel","Clément","Tom","Jonastan","Daphné",
        "Maël","Charly","Circé","Sirine","Vincent","Emilline",
    ]
    await update.message.reply_text(f"Le prochain président est {random.choice(personnes)} SET")


async def nimp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phrase = ("c’est des poulets mafieux au cinéma après avoir durement travaillé au téléphone rose "
              "et vendu des 10 balles pour repayer le téléphone de sofiane, il y a une bagarre au sunset à cergy "
              "pref entre des moutons pré aid et des poules pré chicken street qui se battent le rainté en match à "
              "mort par équipe, y’a aussi un lion sous dégradé à blanc qui s’est battu après les poules vont en soirée "
              "et elles twerkent ou dansent sur de la tectonic et y a le loup qui les surveillent et si elles dansent pas "
              "il les mange avec de la sauce salsa qui pique vraiment vraiment beaucoup parce que c'est de la sauce mexicaine "
              "qui vient de Pablo Escobar")
    await update.message.reply_text(phrase)


async def snuss(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phrases = [
        "J'ai du HARDCORE",
        "C'est du 12 mg de nicotine",
        "La dernière fois que j'en ai pris j'étais en bad trip",
    ]
    await update.message.reply_text(random.choice(phrases))




def build_app() -> Application:
    app = Application.builder().token(TOKEN).build()

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
    return app

if __name__ == '__main__':
    application = build_app()
    application.run_polling(poll_interval=5)
