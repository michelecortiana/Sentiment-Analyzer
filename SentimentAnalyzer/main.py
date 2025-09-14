import tkinter as tk
from tkinter import messagebox, filedialog
from transformers import pipeline
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Carico i modelli Hugging Face per sentiment e emozioni in italiano
emotion_analyzer = pipeline(
    "text-classification",
    model="MilaNLProc/feel-it-italian-emotion",
    return_all_scores=True
)

sentiment_analyzer = pipeline(
    "text-classification",
    model="MilaNLProc/feel-it-italian-sentiment",
    return_all_scores=False
)

theme = "light"  #Tema iniziale

def esegui_azione():
    """Analisi del testo inserito e mostra risultati + grafico."""
    testo_inserito = textbox.get("1.0", tk.END).strip()

    #Controlli input 
    if not testo_inserito:
        messagebox.showerror("Errore", "Inserisci del testo da analizzare!")
        return
    if len(testo_inserito) > 1000:
        messagebox.showerror("Errore", "Il testo è troppo lungo! Max 1000 caratteri.")
        return

    try:
        #Analisi del sentimento
        risultato_sentimento = sentiment_analyzer(testo_inserito)[0]
        sentimento = risultato_sentimento['label']
        conf_sent = risultato_sentimento['score']

        #Analisi delle emozioni
        emozioni = emotion_analyzer(testo_inserito)[0]
        labels = [e['label'] for e in emozioni]
        scores = [e['score'] for e in emozioni]

        #Mostra i risultati testuali in un popup
        risultato_emozioni = "\n".join(f"{label}: {score:.2f}" for label, score in zip(labels, scores))
        risultato = (
            f"Testo Analizzato: {testo_inserito}\n\n"
            f"Sentimento principale: {sentimento} (Confidenza: {conf_sent:.2f})\n\n"
            f"Emozioni:\n{risultato_emozioni}"
        )
        messagebox.showinfo("Risultato Analisi", risultato)

        #Mostra il grafico in una nuova finestra
        mostra_grafico(labels, scores)

    except Exception as e:
        messagebox.showerror("Errore", f"Errore durante l'analisi: {e}")

def mostra_grafico(labels, scores):
    """Finestra separata con grafico e opzioni di salvataggio."""
    grafico_win = tk.Toplevel(root) 
    grafico_win.title("Grafico Emozioni")
    grafico_win.geometry("850x800")
    grafico_win.configure(bg="#f2f2f2" if theme=="light" else "#333")

    #Creazione della figura matplotlib
    fig = plt.Figure(figsize=(8,6), dpi=100)
    ax = fig.add_subplot(111)
    bar_color = 'skyblue' if theme=="light" else 'orange'
    text_color = '#000' if theme=="light" else '#fff'
    bg_color = '#fff' if theme=="light" else '#333'

    #Personalizzazione grafico
    fig.patch.set_facecolor(bg_color)
    ax.bar(labels, scores, color=bar_color)
    ax.set_ylim(0,1)
    ax.set_ylabel("Confidenza", color=text_color)
    ax.set_title("Analisi delle Emozioni", color=text_color)
    ax.tick_params(axis='x', colors=text_color)
    ax.tick_params(axis='y', colors=text_color)

    #Inserimento grafico in finestra Tkinter
    canvas = FigureCanvasTkAgg(fig, master=grafico_win)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

    #Funzione interna per salvare il grafico
    def salva_grafico():
        file = filedialog.asksaveasfilename(
            filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg")],
            defaultextension=".png"
        )
        if file:
            fig.savefig(file)  # Salva immagine
            messagebox.showinfo("Salvataggio completato", f"Grafico salvato in:\n{file}")

    #Pulsante per chiudere la finestra grafico
    tk.Button(
        grafico_win,
        text="Torna all'interfaccia principale",
        command=grafico_win.destroy,
        font=("Arial", 12, "bold"),
        bg="#4caf50",
        fg="#fff",
        activebackground="#45a049",
        activeforeground="#fff",
        bd=0,
        padx=10,
        pady=5
    ).pack(pady=10)

    #Pulsante per salvare il grafico
    tk.Button(
        grafico_win,
        text="Salva il grafico!",
        command=salva_grafico,
        font=("Arial", 12, "bold"),
        bg="#4caf50",
        fg="#fff",
        activebackground="#45a049",
        activeforeground="#fff",
        bd=0,
        padx=10,
        pady=5
    ).pack(pady=10)

def cambia_tema():
    """Gestione tema della finestra principale (light/dark)."""
    global theme
    if theme=="light":
        theme="dark"
        root.configure(bg="#333")
        frame.configure(bg="#333")
        textbox.configure(bg="#555", fg="#fff", insertbackground="#fff")
    else:
        theme="light"
        root.configure(bg="#f2f2f2")
        frame.configure(bg="#f2f2f2")
        textbox.configure(bg="#fff", fg="#333", insertbackground="#000")

def main():
    """GUI principale."""
    global root, frame, textbox
    root = tk.Tk()
    root.title("Analisi del Sentimento (Italiano)")
    root.geometry("650x600")
    root.configure(bg="#f2f2f2")

    #Contenitore principale
    frame = tk.Frame(root, bg="#f2f2f2")
    frame.place(relx=0.5, rely=0.02, anchor="n")

    #Etichetta istruzioni
    tk.Label(
        frame,
        text="Inserisci il testo in italiano:",
        font=("Helvetica", 14, "bold"),
        bg="#f2f2f2",
        fg="#333"
    ).pack(pady=10)

    #Textbox per input utente
    textbox = tk.Text(
        frame,
        height=7,
        width=60,
        font=('Arial', 12),
        bg="#ffffff",
        fg="#333",
        bd=2,
        relief="solid"
    )
    textbox.pack(pady=5)

    #Pulsante analisi sentimento
    tk.Button(
        frame,
        text="Analizza Sentimento",
        command=esegui_azione,
        font=("Arial", 12, "bold"),
        bg="#4caf50",
        fg="#fff",
        activebackground="#45a049",
        activeforeground="#fff",
        bd=0,
        padx=10,
        pady=5
    ).pack(pady=5)

    #Pulsante cambio tema
    tk.Button(
        frame,
        text="Cambia Tema",
        command=cambia_tema,
        font=("Arial", 12, "bold"),
        bg="#555",
        fg="#fff",
        activebackground="#777",
        activeforeground="#fff",
        bd=0,
        padx=10,
        pady=5
    ).pack(pady=5)

    #Avvio del loop principale
    root.mainloop()

if __name__ == "__main__":
    main()
