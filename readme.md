# 🩺 AI Doctor with Vision and Voice

An AI-powered medical assistant that listens to your voice, analyzes medical images, and responds with informative, empathetic spoken feedback. Built using **GROQ Whisper**, **Meta LLaMA**, **ElevenLabs**, and **Gradio**.

---

## 🚀 Features

- 🎤 **Voice Input** – Speak your symptoms or health-related queries.
- 🖼️ **Image Analysis** – Upload X-rays, skin images, or scans for AI-based insights.
- 🧠 **AI Reasoning** – Leverages LLMs to generate helpful health observations.
- 🔊 **Voice Output** – AI replies with speech using ElevenLabs or gTTS.
- 💻 **Gradio Interface** – Web-based UI for interactive demos.

---

## 🧠 System Architecture

```
User Input (Voice + Image)
        │
        ▼
 [Speech Recognition (GROQ Whisper)]
        │
        ▼
   [Multimodal LLM Analysis]
        │
        ├──► [Image Encoding (Vision Module)]
        │
        ▼
 [Response Generation (Meta LLaMA)]
        │
        ▼
 [Text-to-Speech (ElevenLabs/gTTS)]
        │
        ▼
       Output (Text + Voice)
```

---

---

## ⚙️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/ai-doctor-voicebot.git
cd ai-doctor-voicebot
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Add API Keys

Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

Or edit `app.py` to insert keys directly if preferred (not recommended for production).

---

## ▶️ Running the App

```bash
python app.py
```

Then open your browser at `http://127.0.0.1:7860/`.

---

## ✅ Example Workflow

1. Speak a symptom: _“I have chest pain when I breathe.”_
2. Upload an image (e.g., chest X-ray).
3. The app:
   - Transcribes your voice.
   - Analyzes the image + text.
   - Responds with a gentle spoken and written explanation.
   - Encourages you to consult a doctor.

---

## ⚠️ Disclaimer

> This tool is for **educational and informational purposes only**. It does **not provide medical diagnoses**. Always consult a qualified healthcare professional for medical advice.

---

## 🛠️ Tech Stack

- 🧠 Meta LLaMA (via GROQ) – multimodal LLM
- 🗣️ GROQ Whisper – speech-to-text
- 🎤 ElevenLabs & gTTS – text-to-speech
- 🖼️ PIL / OpenCV – image preprocessing
- 🧪 Gradio – web interface

---

## 📜 License

This project is open-sourced under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [GROQ](https://groq.com/)
- [ElevenLabs](https://www.elevenlabs.io/)
- [Gradio](https://gradio.app/)
- [Meta AI – LLaMA](https://ai.meta.com/llama/)

---

## 💬 Contact & Contributions

Contributions, issues, and feedback are welcome!

- 📧 Email: rohit.xolo.00@gmail.com
