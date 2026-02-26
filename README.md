📊 Financial Document Analyzer

AI-powered system for analyzing corporate financial reports using local LLMs with multi-agent orchestration.

Built with Ollama + CrewAI + FastAPI.

🚀 Overview

Financial Document Analyzer processes corporate financial reports (PDF format) such as quarterly earnings, annual reports, and investor updates.

The system extracts key financial metrics, evaluates risks, and generates structured investment insights using AI agents.

🏗 Architecture
User Upload (PDF)
        ↓
PDF Text Extraction
        ↓
Text Chunking
        ↓
AI Financial Analyst Agent
        ↓
Risk Assessment
        ↓
Investment Recommendation
🛠 Tech Stack

Python 3.10+

FastAPI

CrewAI

Ollama (Local LLM Runtime)

PyPDF

Uvicorn

📦 Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/financial-document-analyzer.git
cd financial-document-analyzer
2️⃣ Install Dependencies
pip install -r requirements.txt
🧠 Ollama Setup
Install Ollama

Download from: https://ollama.com

Start Ollama Server
ollama serve
Pull Required Model
ollama pull llama3

You may also use:

ollama pull mistral
▶️ Running the Application

Start the FastAPI server:

uvicorn main:app --reload

Access Swagger UI:

http://127.0.0.1:8000/docs

Upload a financial PDF using the /upload/ endpoint.

📄 Sample Document

You can test with a financial report such as Tesla’s quarterly update from:

https://www.tesla.com/investor-relations

Save it as:

data/sample.pdf
✅ Features

Upload financial documents (PDF)

Extract key financial metrics (Revenue, Net Income, EPS, Debt)

AI-powered financial analysis

Risk classification (Low / Medium / High)

Investment recommendation (Buy / Hold / Sell)

Structured analytical output

📁 Project Structure
financial-document-analyzer/
│
├── main.py
├── agents.py
├── tasks.py
├── utils.py
├── requirements.txt
├── data/
│   └── sample.pdf
└── README.md
⚠ Notes

Ensure Ollama server is running before starting the API.

Large PDFs are automatically chunked to prevent LLM context overflow.

Replace the placeholder PDF with a real financial report for proper testing.

🔮 Future Improvements

Multi-agent financial reasoning

Earnings call sentiment analysis

Historical financial comparison

Dashboard UI

Cloud deployment

Vector database integration
