<p align="center">
<img src="https://skillicons.dev/icons?i=python" alt="logo python" width=15%> <br>
<i width=80%>First experiment with Machine Learning & AI applied to Sentiment Analysis in Italian, using Hugging Face models and a simple Tkinter GUI.</i>
</p>
<br>

<br>
<br>

# 📖 INDEX  
 * 📥 [Installation Guide](#-installation-guide)  
 * 📌 [Overview](#-overview)  
 * 🏗️ [Architecture & Workflow](#%EF%B8%8F-architecture--workflow)  
 * 🛠️ [Technologies Used](#%EF%B8%8F-technologies-used)  
 * 📷 [Usage Examples](#-usage-examples)  
 * 📄 [License](#-license)  

<br>
<br>

# 📌 Overview  

**Sentiment Analyzer** is a personal project created as my **first step into Machine Learning and AI**.  
It is a simple GUI-based application written in **Python + Tkinter** that analyzes **sentiment** (positive / negative / neutral) and **emotions** (joy, sadness, anger, fear) in **Italian text**.  

Originally built as an experiment, the project helped me explore **NLP (Natural Language Processing)** and how to integrate Hugging Face models into a standalone desktop app.  

> [!TIP]  
> You can use the **.exe version** (Windows) without needing to install Python.  

<br>

---
<br>

# 🏗️ Architecture & Workflow  

*The app works entirely offline once the models are downloaded.*  
The user inputs Italian text → The Hugging Face pipelines classify sentiment and emotions → Results are shown in a Tkinter popup.  

<img src="https://github.com/michelecortiana/DigitML/blob/main/README%20-%20Stuff/data-flow.svg" width=70% alt="workflow example"/>  

<br>

---
<br>

# 📥 Installation Guide  

### Option 1: Run with Python  
```bash
git clone https://github.com/yourusername/sentiment-analyzer.git
cd sentiment-analyzer
pip install -r requirements.txt
python app.py
