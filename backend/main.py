from fastapi import FastAPI, Request, BackgroundTasks
import requests
from groq_model import review_code_groq
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()

templates = Jinja2Templates(directory="templates")

latest_review = {
    "score": None,
    "review": "No reviews yet."
}


@app.post("/webhook")
async def webhook(request: Request, background_tasks: BackgroundTasks):
    data = await request.json()

    print("Webhook triggered!")
    print("Event:", request.headers.get("x-github-event"))
    print("Action:", data.get("action"))

    if request.headers.get("x-github-event") == "pull_request":

        action = data.get("action")

        if action in ["opened", "reopened", "synchronize"]:

            diff_url = data["pull_request"]["diff_url"]
            print("Fetching diff from:", diff_url)

            diff = requests.get(diff_url).text

            background_tasks.add_task(run_ai, diff)

    return {"status": "ok"}


# ------------------------------
# AI PROCESSING
# ------------------------------


def run_ai(diff):

    global latest_review

    print("Running Groq (Primary)...")
    groq_review = review_code_groq(diff)

    score = calculate_score(groq_review)

    final_review = f"""
## 🤖 CodeRefine AI Review

### 📊 Code Health Score: {score}/100

---

{groq_review}
"""

    latest_review["score"] = score
    latest_review["review"] = groq_review

    print("FINAL REVIEW:")
    print(final_review)



# ------------------------------
# SCORING SYSTEM
# ------------------------------

def calculate_score(review_text):

    bugs = review_text.lower().count("bug")
    security = review_text.lower().count("security")
    performance = review_text.lower().count("performance")

    score = 100 - (bugs * 10) - (security * 8) - (performance * 5)

    if score < 0:
        score = 0

    return score

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "score": latest_review["score"],
            "review": latest_review["review"],
        },
    )
