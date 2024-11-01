import gradio as gr
import math

def fatorial(x):
    if x < 0:
        return "Erro: número negativo."
    return math.factorial(x)

iface = gr.Interface(
    fn=fatorial,
    inputs="number",
    outputs="text",
    title="Fatorial de um número",
    description="Interface que calcula o fatorial de um número.",
    theme="default"
)

iface.launch()