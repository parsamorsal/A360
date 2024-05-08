import gradio as gr

def process_query(user_query):
    preset_text = "This is a preset response."
    return f"Query: {user_query}\nResponse: {preset_text}"

css = """
body { display: flex; justify-content: center; align-items: center; height: 100vh; }
.gradio-flag { display: none !important; }
"""

app = gr.Interface(
    fn=process_query,
    inputs=gr.Textbox(label="Enter your query", placeholder="Type something...", lines=2),
    outputs=gr.Textbox(label="Result", interactive=False, lines=5),
    title= "A360 <> Datatonic AI Editor",
    description="Your Gen AI Article Editor",
    css=css,
    allow_flagging="never"
)

app.launch()
