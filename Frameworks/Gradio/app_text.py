import gradio as gr
 
def reverter_texto(texto):
    texto_revertido = texto[::-1]
    return texto_revertido, len (texto)


iface = gr.Interface(
    fn=reverter_texto,
    inputs="text",
    outputs=["text", "number"],
    title="Reverter texto",
    description="Interface que reverte um texto.",
    theme="default"
)

iface.launch()