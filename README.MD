# 👋 Welcome to Testscripts for Saucedemo.com!

This testscripts for Saucedemo.com webpage designed using POM structure


## 📂 Project Structure

```
DEMO_POM/
├── .github/                # GitHub Actions configuration (if any)
├── pages/                  # Page Object files (each page behavior)
│   ├── base_page.py         # Base page with common methods
│   ├── home_page.py         # Home page elements and actions
│   ├── login_page.py        # Login page elements and actions
│
├── reports/                # Test reports (HTML, screenshots, logs)
│   └── assets/             # Assets for reports (images, CSS, etc.)
│
├── tests/                  # Test scripts organized by feature
│   ├── test_homepage_interactions.py  # Tests for homepage actions
│   ├── test_login_scenrios.py          # Tests for login scenarios
│
├── venv/                   # Virtual environment (not pushed to Git)
│
├── .env                    # Environment variables (base URL, credentials)
├── conftest.py             # Shared pytest fixtures and hooks
├── Jenkinsfile             # Jenkins pipeline configuration
├── requirements.txt        # Required Python packages
├── test-suit-tbtir-saucedemo.xlsx # Test suite documentation
```

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Mac/Linux
   .\venv\Scripts\activate   # For Windows
   ```

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the tests**
   ```bash
   pytest tests/
   ```

5. **(Optional) Generate an HTML report**
   ```bash
   pytest --html=reports/report.html
   ```
