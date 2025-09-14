<p align="center">
  <img src="https://skillicons.dev/icons?i=python" alt="logo python" width="15%">
  <br><br>
  <i>First experiment with Machine Learning & AI applied to Sentiment Analysis in Italian,<br>
  using Hugging Face models and a simple Tkinter GUI.</i>
</p>

---

# 📖 Index
- 📌 [Overview](#-overview)  
- 📥 [Download & Installation](#-download--installation)  
- 🏗️ [Architecture & Workflow](#%EF%B8%8F-architecture--workflow)  
- 📷 [Usage Examples](#-usage-examples)  
- 📄 [License](#-license)  

---

# 📌 Overview

**Sentiment Analyzer** is my **first personal project** exploring the world of **Machine Learning and Natural Language Processing (NLP)**.  

It is a simple **desktop application** (built with **Python + Tkinter**) that analyzes:  
- **Sentiment** → *positive / negative / neutral*  
- **Emotions** → *joy, sadness, anger, fear*  

All in **Italian language** 🇮🇹.  

The app integrates **Hugging Face Transformers pipelines**, allowing users to analyze text through an intuitive graphical interface.  

---

# 📥 Download & Installation

👉 **No Python required!**  

1. Download the latest `SentimentAnalyzer.exe`.
2. Double-click the `.exe` to start the application.  

⚠️ On first run the models will be downloaded from Hugging Face (Internet required).  
After that, the app works **offline**.  

---

# 🏗️ Architecture & Workflow

1. **User Input** → The user writes a short text in Italian.  
2. **Model Processing** → Hugging Face models classify both sentiment and emotions.  
3. **Results** → Shown as text in a popup and visualized as a bar chart.  

---

# 📷 Usage Examples

### App Interface  
The user writes an Italian text, then clicks **"Analizza Sentimento"**.  

### Example Output  

**Testo Analizzato:**  
`Oggi è una giornata fantastica!`  

**Sentimento principale:**  
`positivo (Confidenza: 0.92)`  

**Emozioni:**  
- Gioia → 0.88  
- Tristezza → 0.03  
- Rabbia → 0.04  
- Paura → 0.05  

---

# 📄 License

Released under the **MIT License**.  
Feel free to use, modify, and share 🚀
