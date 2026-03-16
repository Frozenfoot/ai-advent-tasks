"""
Веб-интерфейс: Claude + OpenAI в одном Flask-приложении
Запуск из корня проекта: python -m web.app
Открыть в браузере: http://localhost:5000
"""
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from providers import claude_api, openai_api

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    prompt = data.get("prompt", "")
    provider = data.get("provider", "claude")

    try:
        r = claude_api.ask(prompt) if provider == "claude" else openai_api.ask(prompt)
        return jsonify(
            text=r.text,
            model=r.model,
            input_tokens=r.input_tokens,
            output_tokens=r.output_tokens,
            elapsed=round(r.elapsed, 2) if r.elapsed is not None else None,
        )
    except Exception as e:
        return jsonify(error=str(e)), 500


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug, port=5000)
