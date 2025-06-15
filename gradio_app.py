import os
import gradio as gr

from brain_of_the_doctor import encode_image
from brain_of_the_doctor import analyze_image_with_query
from voice_of_the_patient import record_audio,transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts,text_to_speech_with_elevenlabs

system_prompt = """You are an AI medical assistant analyzing medical images. When examining images:

1. Describe what you observe in the image clearly and objectively
2. If you notice any potential medical concerns, mention them as observations only
3. Suggest when professional medical consultation might be helpful
4. Provide general health information when relevant

IMPORTANT GUIDELINES:
- Always clarify that you cannot provide definitive medical diagnoses
- Recommend consulting healthcare professionals for proper evaluation
- Keep responses informative but not overly technical
- Be empathetic and supportive in your tone
- If the image is unclear or not medical in nature, explain what you can and cannot analyze

Format your response in 2-3 clear paragraphs. Always end by encouraging professional medical consultation when appropriate."""

def process_inputs(audio_filepath,image_filepath):
    speech_to_text_output=transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
                                              audio_filepath=audio_filepath,
                                               stt_model="whisper-large-v3")
    #handle the image input
    if image_filepath:
        doctor_response=analyze_image_with_query(query=system_prompt+speech_to_text_output,encoded_image=encode_image(image_filepath),model="meta-llama/llama-4-scout-17b-16e-instruct")
    else:
        doctor_response="No image provided for me to analyze"
    
    voice_of_doctor=text_to_speech_with_gtts(doctor_response,"final.mp3")

    return speech_to_text_output,doctor_response,voice_of_doctor
    pass

#create interface
iface=gr.Interface(
    fn=process_inputs,
    inputs = [
    gr.Audio(sources=["microphone"], type="filepath"),
    gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctors Response"),
        gr.Audio("Temp.mp3")
    ],
    title="AI Doctor With Vision and Voice"
)
iface.launch(debug=True)