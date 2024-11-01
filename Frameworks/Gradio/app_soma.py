import gradio as gr

def somar(x, y):
    return x + y

iface = gr.Interface(
    fn=somar,
    inputs=["number", "number"],
    outputs="number",
    title="Soma de dois números",
    description="Interface que soma dois números.",
    theme="default"
)

iface.launch()

