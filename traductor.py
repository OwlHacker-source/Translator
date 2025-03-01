try:
    import tkinter as tk
    from tkinter import ttk, messagebox
    import speech_recognition as sr
    import pyttsx3
    import threading
except ModuleNotFoundError as e:
    print(f"Erreur d'importation: {e}. Assurez-vous que les modules requis sont installés.")
    exit()

# Langues disponibles et leurs codes pour la reconnaissance et la synthèse vocale
LANGUAGES = {
    "Français": "fr-FR",
    "Anglais": "en-US",
}

# Traductions des éléments de l'interface pour chaque langue
translations = {
    "fr-FR": {
        "title": "Convertisseur Parole-Texte & Texte-Parole",
        "label": "Entrez du texte ou utilisez la reconnaissance vocale",
        "speak_button": "🎤 Parler",
        "listen_button": "🔊 Écouter",
        "reset_button": "Réinitialiser",
        "quit_button": "Quitter",
        "language_menu": "Langue",
        "info_message": "Parlez maintenant...",
        "warning_message": "Veuillez entrer du texte à lire.",
        "error_message": "Une erreur est survenue.",
        "language_changed": "Langue changée en Français"
    },
    "en-US": {
        "title": "Speech-to-Text & Text-to-Speech Converter",
        "label": "Enter text or use speech recognition",
        "speak_button": "🎤 Speak",
        "listen_button": "🔊 Listen",
        "reset_button": "Reset",
        "quit_button": "Quit",
        "language_menu": "Language",
        "info_message": "Speak now...",
        "warning_message": "Please enter text to read.",
        "error_message": "An error occurred.",
        "language_changed": "Language changed to English"
    },
    # Ajoutez d'autres traductions pour les autres langues...
}

selected_language = "fr-FR"  # Langue par défaut

# Fonctions de mise à jour de la barre de progression
def update_progress_bar():
    progress_bar.start(10)

def stop_progress_bar():
    progress_bar.stop()

def text_to_speech():
    try:
        text = text_entry.get("1.0", tk.END).strip()
        if text:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)  # Vous pouvez ajuster la voix si nécessaire
            engine.setProperty('rate', 150)  # Vitesse de la voix
            engine.say(text)
            engine.runAndWait()
        else:
            messagebox.showwarning(translations[selected_language]["title"], translations[selected_language]["warning_message"])
    except Exception as e:
        messagebox.showerror(translations[selected_language]["title"], f"{translations[selected_language]['error_message']}: {e}")

def speech_to_text():
    def recognize_speech():
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                messagebox.showinfo(translations[selected_language]["title"], translations[selected_language]["info_message"])
                
                # Mise à jour de la barre de progression dans le thread principal
                root.after(0, update_progress_bar)
                
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language=selected_language)
                
                # Mise à jour de la zone de texte avec le texte reconnu
                root.after(0, lambda: text_entry.insert(tk.END, text))
                
        except OSError:
            root.after(0, lambda: messagebox.showerror(translations[selected_language]["title"], "Microphone non détecté."))
        except sr.UnknownValueError:
            root.after(0, lambda: messagebox.showerror(translations[selected_language]["title"], "Impossible de reconnaître la parole."))
        except sr.RequestError:
            root.after(0, lambda: messagebox.showerror(translations[selected_language]["title"], "Erreur de connexion avec le service de reconnaissance vocale."))
        except Exception as e:
            root.after(0, lambda: messagebox.showerror(translations[selected_language]["title"], f"{translations[selected_language]['error_message']}: {e}"))
        finally:
            # Arrêt de la barre de progression
            root.after(0, stop_progress_bar)

    # Lancer la fonction de reconnaissance vocale dans un thread séparé
    threading.Thread(target=recognize_speech, daemon=True).start()

def reset_text():
    text_entry.delete("1.0", tk.END)
    reset_button.pack_forget()  # Cache le bouton "Réinitialiser" après réinitialisation

def quit_application():
    root.quit()

def on_text_change(event):
    if text_entry.get("1.0", tk.END).strip():  # Vérifie s'il y a du texte
        if not reset_button.winfo_ismapped():  # Vérifie si le bouton "Réinitialiser" est déjà affiché
            reset_button.pack(pady=5)
    else:
        reset_button.pack_forget()  # Cache le bouton si la zone est vide

def change_language(language):
    global selected_language
    selected_language = LANGUAGES.get(language, "fr-FR")
    
    # Mettre à jour l'interface en fonction de la langue choisie
    title_label.config(text=translations[selected_language]["title"])
    label.config(text=translations[selected_language]["label"])
    btn_speak.config(text=translations[selected_language]["speak_button"])
    btn_listen.config(text=translations[selected_language]["listen_button"])
    reset_button.config(text=translations[selected_language]["reset_button"])
    quit_button.config(text=translations[selected_language]["quit_button"])
    messagebox.showinfo(translations[selected_language]["title"], translations[selected_language]["language_changed"])

# Création de la fenêtre principale
root = tk.Tk()
root.title("Convertisseur Parole-Texte & Texte-Parole")
root.geometry("500x450")
root.configure(bg="#87CEEB")  # Changer l'arrière-plan en bleu ciel

# Menu de sélection de langue
menu_bar = tk.Menu(root)
language_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label=translations[selected_language]["language_menu"], menu=language_menu)

# Ajouter les options de langue au menu
for lang in LANGUAGES.keys():
    language_menu.add_command(label=lang, command=lambda lang=lang: change_language(lang))

root.config(menu=menu_bar)

# Label principal
title_label = ttk.Label(root, text=translations[selected_language]["title"], font=("Arial", 14))
title_label.pack(pady=10)

label = ttk.Label(root, text=translations[selected_language]["label"], font=("Arial", 12))
label.pack(pady=10)

# Zone de texte
text_entry = tk.Text(root, height=5, width=50, font=("Arial", 10))
text_entry.pack(pady=10, padx=20)
text_entry.bind("<KeyRelease>", on_text_change)  # Détecte les changements de texte

# Cadre pour les boutons
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

# Boutons stylisés
btn_speak = ttk.Button(button_frame, text=translations[selected_language]["speak_button"], command=speech_to_text)
btn_speak.grid(row=0, column=0, padx=10, pady=5)

btn_listen = ttk.Button(button_frame, text=translations[selected_language]["listen_button"], command=text_to_speech)
btn_listen.grid(row=0, column=1, padx=10, pady=5)

# Bouton "Réinitialiser"
reset_button = ttk.Button(root, text=translations[selected_language]["reset_button"], command=reset_text)

# Bouton "Quitter"
quit_button = ttk.Button(root, text=translations[selected_language]["quit_button"], command=quit_application)
quit_button.pack(pady=10)

# Barre de progression
progress_bar = ttk.Progressbar(root, mode='indeterminate', length=200)

# Lancement de l'interface
try:
    root.mainloop()
except Exception as e:
    print(f"Erreur lors de l'exécution de l'interface: {e}")
