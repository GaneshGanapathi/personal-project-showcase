# 🧮 FastAPI Simple Calculator

A clean and lightweight REST API built with **FastAPI** to perform basic arithmetic operations. The project separates the business logic (Calculator class) from the API layer for better maintainability.

## 🛠️ Installation

1. **Clone the repository** .

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi "uvicorn[standard]"
   ```

## 🚀 How to Run

Start the development server using Uvicorn:

```bash
uvicorn app:app --reload
```

The API will now be accessible at `http://127.X.X.X:YYYY`.