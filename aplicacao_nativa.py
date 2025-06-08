import tkinter as tk
from tkinter import ttk, messagebox
import requests
from typing import Any

API_URL = "https://gaia.tail9f339.ts.net"  # Altere para o endpoint real da sua API

def buscar_precatorio():
    cpf = cpf_entry.get()
    if not cpf:
        messagebox.showwarning("Atenção", "Digite um CPF.") # type: ignore
        return
    try:
        response = requests.get(API_URL, params={"cpf": cpf}, timeout=10)
        response.raise_for_status()
        resultado = response.json()
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, str(resultado))
    except Exception as e:
        messagebox = showerror("Erro", f"Erro ao buscar precatório:\n{e}")

def showerror(
    title: str | None = None,
    message: str | None = None,
    **options: dict[str, Any]
) -> str:
    "Show an error message"
    return messagebox . showerror(title, message, **options)

root = tk.Tk()
root.title("Buscador de Precatório")

mainframe = ttk.Frame(root, padding ="20")
mainframe.grid(row = 0, column = 0, sticky = (tk.W, tk.E, tk.N, tk.S)) # type: ignore

ttk.Label(mainframe, text="CPF:").grid(row=0, column=0, sticky=tk.W)
cpf_entry = ttk.Entry(mainframe, width=20)
cpf_entry.grid(row= 0, column=1, sticky = (tk.W, tk.E)) # type: ignore

buscar_btn = ttk.Button(mainframe, text="Buscar", command=buscar_precatorio)
buscar_btn.grid(row = 0, column = 2, padx = 5)

resultado_text = tk.Text(mainframe, width=60, height=15)
resultado_text.grid(row=1, column=0, columnspan=3, pady=10)

root.mainloop()