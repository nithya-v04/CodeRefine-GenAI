CodeRefine AI
CodeRefine AI is an autonomous AI-powered Pull Request review system that acts as a virtual senior developer for student teams, startups, and small organizations.
It integrates with GitHub repositories and automatically analyzes pull request code changes using Large Language Models (LLMs).

Problem Statement:
Small teams often lack experienced developers to perform thorough code reviews. Manual PR reviews can be:
- Time-consuming
- Inconsistent
- Prone to missing bugs or security issues
CodeRefine AI solves this by automating intelligent code analysis.

How It Works:
Developer opens Pull Request  
- GitHub Webhook triggers backend  
- FastAPI fetches PR diff  
- AI model analyzes code  
- Code Health Score generated  
- Live Dashboard updates  

Key Features
- Automated PR Review
- Bug Detection
- Performance Analysis
- Security Checks
- Best Practice Suggestions
- Code Health Score
- Live Dashboard
- Secure API Key Management
- Event-driven architecture (Webhooks)

Architecture
- FastAPI Backend
- GitHub Webhooks
- Groq LLaMA Models (Primary AI)
- Gemini (Optional Model)
- Ngrok for local tunneling
- Jinja2 Dashboard UI

Code Health Score
A heuristic scoring system calculates a quality score based on detected issues in:
- Bugs
- Security
- Performance
Score ranges from 0–100.

Security
API keys are managed securely using environment variables.

Tech Stack
- Python
- FastAPI
- Groq API
- GitHub Webhooks
- Jinja2 Templates
- Ngrok

Use Cases
- Student project teams
- Startup codebases
- Hackathon teams
- Open-source maintainers

Future Improvements
- Auto-comment on PR
- Severity tagging (Critical / Warning / Suggestion)
- Multi-model aggregation
- Persistent review history
- Cloud deployment

Built For Hackathon
CodeRefine AI demonstrates practical integration of Generative AI into DevOps workflows to improve code reliability and development efficiency.
