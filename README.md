# Greenfield University — AI Admission Agent
**Powered by IBM Watsonx.ai (Granite 13B) · Flask · Streamlit · RAG Architecture**

---

## 📁 Project Structure

```
College Admission/
├── app.py                    # Flask backend + Watsonx.ai integration (student-facing)
├── streamlit_app.py          # Streamlit admin dashboard + AI chat (staff/analytics)
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variable template
├── .env                      # Your credentials (DO NOT commit)
├── data/
│   └── admission_data.py     # RAG knowledge base (institutional data)
├── templates/
│   └── index.html            # Main frontend template (Jinja2)
├── static/
│   ├── css/
│   │   └── style.css         # Custom CSS (dark mode, animations)
│   └── js/
│       └── main.js           # Frontend logic (chat, markdown, UI)
└── README.md
```

---

## ⚡ Quick Start (Local)

### 1. Clone / Download the project

```bash
cd "College Admission"
```

### 2. Create & activate a Python virtual environment

```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure credentials

Copy `.env.example` to `.env` and fill in your IBM credentials:

```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

Edit `.env`:

```env
WATSONX_API_KEY=<your IBM Cloud API key>
WATSONX_PROJECT_ID=<your Watsonx project ID>
WATSONX_URL=https://us-south.ml.cloud.ibm.com
FLASK_SECRET_KEY=<random secure string>
FLASK_ENV=development
FLASK_DEBUG=True
APP_PORT=5000
```

> **How to get IBM credentials:**
> 1. Go to [cloud.ibm.com](https://cloud.ibm.com) → Manage → Access (IAM) → API Keys → **Create**.
> 2. Open [dataplatform.cloud.ibm.com](https://dataplatform.cloud.ibm.com) → New Project → copy the **Project ID** from project settings.

### 5. Run the application

```bash
python app.py
```

Open your browser at **http://localhost:5000**

### 6. Run the Streamlit Admin Dashboard (separate terminal)

```bash
streamlit run streamlit_app.py
```

Open your browser at **http://localhost:8501**

> The Streamlit dashboard and Flask app share the same `data/admission_data.py` knowledge base and both connect to IBM Watsonx.ai using the same `.env` credentials.

---

## 🔑 Environment Variables

| Variable | Required | Description |
|---|---|---|
| `WATSONX_API_KEY` | Yes | IBM Cloud API key |
| `WATSONX_PROJECT_ID` | Yes | Watsonx.ai project ID |
| `WATSONX_URL` | No | Watsonx endpoint (default: us-south) |
| `FLASK_SECRET_KEY` | Yes | Flask session encryption key |
| `FLASK_DEBUG` | No | Enable debug mode (default: True) |
| `APP_PORT` | No | Flask HTTP port (default: 5000) |
| `STREAMLIT_PORT` | No | Streamlit port (default: 8501) |

---

## 🤖 AI Architecture

```
Student Query
     │
     ▼
┌─────────────────────────────────────────────┐
│  Flask /api/chat endpoint                   │
│                                             │
│  1. Receive user message                    │
│  2. Inject RAG context (admission_data.py)  │
│  3. Build structured prompt                 │
│  4. Call IBM Watsonx.ai Granite 13B API     │
│  5. Return formatted response               │
└─────────────────────────────────────────────┘
     │
     ▼
IBM Watsonx.ai — ibm/granite-13b-instruct-v2
```

**RAG Context includes:**
- All courses, eligibility, cutoffs, fees
- Admission deadlines
- Scholarship programmes
- Required documents
- Campus facilities
- Contact information

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Main web UI |
| `POST` | `/api/chat` | Chat with AI agent |
| `GET` | `/api/courses` | JSON list of all courses |
| `GET` | `/api/deadlines` | JSON list of deadlines |
| `GET` | `/api/health` | Health + model status check |

### Chat API Example

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What are the eligibility criteria for B.Tech CSE?"}'
```

Response:
```json
{
  "reply": "**B.Tech Computer Science & Engineering** requires...",
  "model": "ibm/granite-13b-instruct-v2",
  "timestamp": "14:32"
}
```

---

## 🚀 Deployment

### Option A — Gunicorn (Linux/macOS Production)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Option B — IBM Code Engine

```bash
# Install IBM CLI
ibmcloud login --apikey $WATSONX_API_KEY -r us-south

# Push as container app
ibmcloud ce app create \
  --name admission-agent \
  --image icr.io/your-namespace/admission-agent \
  --port 5000 \
  --env-from-secret admission-secrets
```

### Option C — Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
```

```bash
docker build -t admission-agent .
docker run -p 5000:5000 --env-file .env admission-agent
```

### Option D — Railway / Render (Free Tier)

1. Push this project to a GitHub repository.
2. Connect Railway/Render to the repo.
3. Set environment variables in the dashboard.
4. Deploy — the platform auto-detects Flask via `requirements.txt`.

---

## 🎨 Features

### Flask App (Student-Facing · `app.py`)

| Feature | Details |
|---|---|
| AI Chat | IBM Granite 13B Instruct via Watsonx.ai |
| RAG | Institutional knowledge injected as context |
| Dark Mode | Auto-detects system preference, toggle button |
| Responsive | Mobile-first Bootstrap 5.3 layout |
| Animations | Fade-in-up on scroll, bubble entrance |
| Markdown | Bot responses rendered with bold, lists, code |
| Quick Prompts | One-click pre-filled questions |
| Course Dashboard | Sortable/filterable cutoff table |
| Deadline Timeline | With past-deadline visual indicator |
| Demo Mode | Runs without credentials for UI preview |
| Health Check | `/api/health` shows live/demo status |

### Streamlit Dashboard (Admin/Analytics · `streamlit_app.py`)

| Feature | Details |
|---|---|
| AI Chat | Native Streamlit chat UI with IBM Granite |
| Analytics | Placement trends, application stats, seat distribution charts |
| Course Explorer | Filterable table with progress-bar cutoffs + expandable detail cards |
| Deadlines | Timeline view of all admission dates |
| Scholarships | Card view of all financial aid programmes |
| FAQ Browser | Searchable FAQ with category grouping |
| Contact | All contact info with working tel/mailto/web links |
| Flask Status | Live health-check indicator for the Flask API |
| Demo Mode | Works without IBM credentials (mock responses) |

---

## 🔒 Security Notes

- Never commit `.env` to version control — add it to `.gitignore`.
- Rotate your IBM API key regularly.
- In production set `FLASK_DEBUG=False` and use a strong `FLASK_SECRET_KEY`.
- User input is limited to 1000 characters server-side to prevent abuse.

---

## 📦 Dependencies

```
flask>=3.0.0          — Web framework (student-facing UI)
streamlit>=1.35.0     — Admin dashboard + analytics UI
pandas>=2.1.0         — Data tables and chart data
python-dotenv>=1.0.0  — .env loader
ibm-watsonx-ai>=0.2.6 — IBM Watsonx SDK
requests>=2.31.0      — HTTP client / Flask health check
gunicorn>=21.2.0      — WSGI production server
```

---

## 🛠️ Customisation

To adapt for a different institution:
1. Edit `data/admission_data.py` — update `INSTITUTION_NAME`, courses, deadlines, scholarships, fees.
2. The RAG context is automatically rebuilt from these dictionaries on startup.
3. No changes to `app.py` or frontend are required for content updates.

---

*Built with IBM Watsonx.ai · Granite · Flask · Streamlit · Bootstrap 5*
