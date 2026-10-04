from flask import Flask, render_template, request

from app.tournament.knockout import create_knockout_draw

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    draw = None
    error = None
    participants_text = ""

    if request.method == "POST":
        participants_text = request.form.get("participants", "")

        participants = [
            line.strip()
            for line in participants_text.splitlines()
            if line.strip()
        ]

        try:
            draw = create_knockout_draw(participants)
        except ValueError as exc:
            error = str(exc)

    return render_template(
        "index.html",
        draw=draw,
        error=error,
        participants_text=participants_text,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)