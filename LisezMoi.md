# 📌 Détection Améliorée des Numéros de Dossards avec OCR et OpenCV

## 🔍 Présentation

Ce projet améliore la détection et l'extraction des numéros de dossards à partir d'images de courses en utilisant OpenCV pour le prétraitement avancé des images et Tesseract OCR pour la reconnaissance de texte. Les numéros de dossards extraits sont enregistrés dans un fichier JSON pour une analyse ultérieure.

## 🚀 Fonctionnalités

- 🎨 Prétraitement avancé des images avec conversion en niveaux de gris, flou gaussien, égalisation d'histogramme et opérations morphologiques.
- 🔍 Sélection dynamique de la région d'intérêt (ROI) pour une meilleure précision.
- 🔠 Amélioration du traitement OCR grâce à des configurations optimisées de Tesseract.
- 📂 Enregistrement des numéros de dossards extraits dans un fichier JSON structuré.

## 🛠 Installation

### 📌 Prérequis

Assurez-vous d'avoir les éléments suivants installés :

- 🐍 Python 3.x
- 🌿 Git
- 🖼 OpenCV (`cv2`)
- 🔠 Tesseract OCR

### ⚙️ Configuration

1. 🖥 Cloner le repo :
   ```sh
   git clone https://github.com/votreutilisateur/votre-repo.git
   cd votre-repo
   ```
2. 📦 Installer les dépendances :
   ```sh
   pip install -r requirements.txt
   ```
3. 🔠 Configurer Tesseract OCR :
   - 🪟 Windows : Télécharger et installer depuis [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
   - 🐧 Linux/macOS : Installer via le gestionnaire de paquets (`sudo apt install tesseract-ocr`)
4. 🛠 Mettre à jour le chemin `pytesseract` dans le script si nécessaire :
   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
   ```

## ▶️ Utilisation

1. 📂 Placer les images dans le dossier `images/`.
2. ▶️ Exécuter le script :
   ```sh
   python script.py
   ```
3. 💾 Les numéros de dossards extraits seront enregistrés dans `bib_numbers.json`.

## 📊 Résultat

Le script génère un fichier JSON avec les résultats :

```json
{
  "image1.jpg": "1234",
  "image2.jpg": "5678",
  "image3.jpg": "Non détecté"
}
```

## 🤝 Contribution

N'hésitez pas à fork ce repo et à soumettre des pull requests pour toute amélioration.

## 📜 Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.

