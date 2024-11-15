from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS

app = Flask(_name_)
CORS(app, resources={"/*": {"origins": "https://lal826717.wixsite.com/echotext-1"}})  # Replace with your Wix domain
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()
    transcribed_text = data.get("transcribed_text", "")
    
    if not transcribed_text:
        return jsonify({"error": "No transcribed text provided"}), 400
    
    # Perform summarization
    summary = summarizer(transcribed_text, max_length=130, min_length=30, do_sample=False)
    summary_text = summary[0]['summary_text']
    
    return jsonify({"summary": summary_text})

if _name_ == '_main_':
    app.run()