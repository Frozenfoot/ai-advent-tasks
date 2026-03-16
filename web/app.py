"""
Веб-интерфейс: Claude + OpenAI в одном Flask-приложении
Запуск из корня проекта: python -m web.app
Открыть в браузере: http://localhost:5000
"""
from flask import Flask, render_template, request, jsonify
from providers import claude_api, openai_api

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    prompt = data.get("prompt", "")
    provider = data.get("provider", "claude")

    try:
        r = claude_api.ask(prompt) if provider == "claude" else openai_api.ask(prompt)
        return jsonify(
            text=r.text,
            model=r.model,
            input_tokens=r.input_tokens,
            output_tokens=r.output_tokens,
        )
    except Exception as e:
        return jsonify(error=str(e)), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
