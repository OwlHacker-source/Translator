# Translator
Fonctionnement de l'application "Convertisseur Parole-Texte & Texte-Parole"

Cette application permet de convertir la parole en texte et inversement (texte en parole) avec une interface graphique en Tkinter.

### Fonctionnalités principales :

1. **Texte vers parole (Text-to-Speech)** :
   - Le bouton "🔊 Écouter" permet de lire à voix haute le texte saisi dans la zone de texte.
   - Utilise le module pyttsx3 pour la synthèse vocale.

2. **Parole vers texte (Speech-to-Text)** :
   - Le bouton "🎤 Parler" permet de lancer la reconnaissance vocale pour convertir la parole en texte et l'afficher dans la zone de texte.
   - La reconnaissance vocale est effectuée par le module speech_recognition et utilise Google Web Speech API.

3. **Gestion des erreurs et de la barre de progression** :
   - Si un problème survient pendant la reconnaissance vocale ou la synthèse vocale, un message d'erreur est affiché.
   - Une barre de progression est visible pendant la reconnaissance vocale.

4. **Réinitialisation du texte** :
   - Le bouton "Réinitialiser" permet de vider la zone de texte.
   - Ce bouton s'affiche uniquement si du texte est présent dans la zone.

5. **Changement de langue** :
   - L'application prend en charge deux langues : français et anglais. L'utilisateur peut choisir la langue de l'interface à l'aide du menu en haut.
   - L'interface se met à jour dynamiquement en fonction de la langue choisie (affichage des titres, boutons, et messages).

### Interface Utilisateur :

- **Fenêtre principale** (`root`) :
  Contient tous les éléments graphiques de l'application, y compris la zone de texte, les boutons, et la barre de progression.

- **Zone de texte** :
  L'utilisateur peut y saisir du texte ou y voir le texte transcrit par la reconnaissance vocale.

- **Cadre pour les boutons** :
  Contient les boutons "🎤 Parler" et "🔊 Écouter". Le bouton "Réinitialiser" est visible uniquement si du texte est présent.

- **Barre de menu** :
  Permet de changer la langue de l'interface (Français/Anglais).

### Modules utilisés :
- `tkinter` : pour créer l'interface graphique.
- `pyttsx3` : pour la synthèse vocale (texte vers parole).
- `speech_recognition` : pour la reconnaissance vocale (parole vers texte).
- `threading` : pour exécuter la reconnaissance vocale dans un thread séparé afin de ne pas bloquer l'interface.

### Instructions d'utilisation :
1. **Changement de langue** :
   - Utilisez le menu "Langue" pour passer entre le Français et l'Anglais.

2. **Parole vers texte** :
   - Cliquez sur "🎤 Parler" et parlez dans le microphone pour convertir la parole en texte.

3. **Texte vers parole** :
   - Entrez du texte dans la zone de texte et cliquez sur "🔊 Écouter" pour le lire à voix haute.

4. **Réinitialisation du texte** :
   - Cliquez sur le bouton "Réinitialiser" pour vider la zone de texte.

5. **Quitter l'application** :
   - Cliquez sur "Quitter" pour fermer l'application.

Assurez-vous que les modules requis sont installés : `pyttsx3`, `speech_recognition`, `tkinter`.

