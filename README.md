# 📹 Video Summarizer

A **multimodal AI-powered video summarizer** that allows users to upload videos, analyze their content, and generate meaningful insights using Google's **Gemini AI**.

## 🚀 Features
- Upload videos for AI-based analysis
- Extract transcripts and key insights
- Provide user-specific queries for customized summaries
- Utilize web search for additional context

---

## 🛠️ Tech Stack
### **Frontend & UI**
- [Streamlit](https://streamlit.io/) – Interactive UI for video upload and query input

### **Backend & AI Processing**
- [Google Gemini API](https://ai.google.dev/) – For AI-powered video analysis
- [Phidata AI](https://phi-data.ai/) – AI agent framework
- [DuckDuckGo Search API](https://duckduckgo.com/) – For fetching external information

### **Utilities & Deployment**
- [Google Generative AI SDK](https://github.com/google/generative-ai-python) – Handling Gemini API requests
- [Python-dotenv](https://pypi.org/project/python-dotenv/) – Managing API keys securely
- [Vercel](https://vercel.com/) – Deployment platform

---

## ⚙️ Workflow
### **1️⃣ Upload Video**
- User uploads a video file (**mp4, mov, avi** formats supported)
- Video is saved temporarily for processing

### **2️⃣ AI-Based Video Processing**
- The uploaded video is sent to **Google Gemini API** for analysis
- If needed, the AI extracts **transcripts** and key information
- User can provide custom questions for more refined insights

### **3️⃣ Generate Summary & Insights**
- The AI processes the video and provides a **detailed summary**
- If required, **DuckDuckGo API** fetches additional information

### **4️⃣ Display Results**
- The AI-generated summary is displayed on the Streamlit UI
- Users can interact further by refining their queries

---

## 🛠️ Setup & Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/video-summariser.git
cd video-summariser
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Set Up API Keys**
Create a `.env` file and add:
```bash
GOOGLE_API_KEY=your_google_api_key
```

### **4️⃣ Run the Streamlit App**
```bash
streamlit run app.py
```

---

## 🌍 Deployment on Vercel
```bash
vercel
```
Make sure your `vercel.json` is configured properly.

---

## 📌 Future Improvements
- 🔹 Support for **multiple languages** in transcripts
- 🔹 More **detailed visual insights** using AI models
- 🔹 Option to **export summaries as text/PDF**

---

## 🎯 Contributing
Feel free to open issues and PRs to improve this project! 🚀
