import gradio as gr
import requests

def fetch_data_from_api(user_input):
    # Replace with your actual API endpoint
    api_endpoint = "https://your-api-endpoint.com/endpoint"
    response = requests.post(api_endpoint, json={"text": user_input})
    if response.status_code == 200:
        data = response.json()  # assuming the response is a JSON list
        return data
    else:
        return ["Error: Unable to fetch data from API"]

def display_table(user_input):
    data = fetch_data_from_api(user_input)
    if "Error" in data[0]:
        return data
    else:
        table_data = [[i] for i in data]
        return table_data

with gr.Blocks() as demo:
    input_text = gr.Textbox(label="Enter your text here", lines=10, placeholder="Type something...")
    output_table = gr.Dataframe(headers=["Result"], elem_id="output_table")
    submit_button = gr.Button("Submit")

    submit_button.click(display_table, inputs=input_text, outputs=output_table)

demo.launch()
