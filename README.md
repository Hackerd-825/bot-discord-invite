
# 🤖 Bot Discord - Invitation Automatique

Ce projet est un **bot Discord** qui envoie automatiquement une **invitation prédéfinie** à des utilisateurs, puis suit leur réponse.  
Il est conçu pour être **hébergé facilement** sur **Windows ou Raspberry Pi (Linux)**.

---

## 🚀 Fonctionnalités

- 📤 Envoie une **invitation Discord fixe** en message privé à un utilisateur mentionné.
- 📝 Journalise :
  - Qui a reçu l'invitation (`sent.txt`)
  - Qui a rejoint le serveur (`accepted.txt`)
  - Qui n'a pas rejoint après un délai (`not_accepted.txt`)
- 📡 Affiche toutes les informations **en temps réel** dans la console.
- ⚙️ Fonctionne sur **Windows** (`start.bat`) ou **Raspberry Pi** (`start.sh`).

---

## 📁 Arborescence du projet

```

/bot-discord-invite
├── bot.py
├── config.json
├── requirements.txt
├── start.bat
├── start.sh
├── setup.sh
├── README.md
└── log/
├── sent.txt
├── accepted.txt
├── not\_accepted.txt

````

---

## ⚙️ Pré-requis

- **Python 3.8 ou supérieur** installé.
- Un **bot Discord** configuré (avec le **token**) et ajouté sur ton serveur.

---

## 🔑 Configuration

Crée un fichier `config.json` à la racine :

```json
{
  "token": "TON_TOKEN_ICI",
  "invite_url": "https://discord.gg/TON_INVITE"
}
````

* Remplace `"TON_TOKEN_ICI"` par le **token de ton bot Discord**.
* Remplace `"TON_INVITE"` par ton **lien d'invitation fixe**.

---

## 📦 Installation des dépendances

1️⃣ Ouvre un terminal dans le dossier du projet.

2️⃣ Installe les dépendances :

```bash
pip install -r requirements.txt
```

ou sur Raspberry Pi :

```bash
pip3 install -r requirements.txt
```

---

## ▶️ Lancement

**Sur Windows :**

```bash
start.bat
```

**Sur Raspberry Pi (Linux) :**

```bash
chmod +x start.sh
./start.sh
```

---

## 🗂️ Fonctionnement des journaux

Les logs sont sauvegardés dans le dossier **`log/`** :

| Fichier            | Contenu                                                     |
| ------------------ | ----------------------------------------------------------- |
| `sent.txt`         | Liste des utilisateurs à qui une invitation a été envoyée   |
| `accepted.txt`     | Liste des utilisateurs qui ont rejoint le serveur           |
| `not_accepted.txt` | Liste des utilisateurs qui n'ont pas rejoint après un délai |

---

## ⚠️ Utilisation Légale et Responsabilité

> ⚠️ **ATTENTION :** L’envoi automatisé d’invitations à des utilisateurs Discord **sans leur consentement** peut enfreindre les **règles de Discord** et **peut être illégal** selon votre pays.
>
> ✅ Ce projet est fourni **uniquement à titre éducatif**.
> 👉 **Utilisez-le uniquement dans un cadre légal**, par exemple pour faire des tests sur **vos propres comptes** ou des serveurs de test **avec l’autorisation de tous les participants**.
>
> ❌ **Je décline toute responsabilité en cas d’usage abusif ou illégal.**

---

## ✅ Hébergement

Hébergez le bot **en continu** sur une **Raspberry Pi** pour qu’il fonctionne 24h/24, ou **lancez-le manuellement** sur Windows.

---

### 📌 Bon usage et apprenez en toute sécurité ! 🚀

---

## requirements.txt

```
discord.py
```

```

---

Voilà, tu as là un `README.md` 100% markdown, avec toutes les parties : texte, arborescence, code, tableaux, citations… rien n’est “sorti” du markdown.

Tu peux copier-coller ça directement dans un fichier `README.md` sans soucis.  
Si tu veux, je peux aussi te faire pareil pour les autres fichiers (`start.bat`, `start.sh`, `setup.sh`, `bot.py`...) dans ce même style, dis-le moi.
```
