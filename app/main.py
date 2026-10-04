from flask import Flask, redirect, render_template, request, url_for

from app.database import (
    delete_tournament,
    get_tournament,
    init_db,
    list_tournaments,
    save_tournament,
)
from app.tournament.knockout import create_knockout_draw

app = Flask(__name__)

init_db()


@app.route("/", methods=["GET", "POST"])
def index():
    draw = None
    error = None
    participants_text = ""
    tournament_name = ""

    if request.method == "POST":
        tournament_name = request.form.get("tournament_name", "").strip()
        participants_text = request.form.get("participants", "")

        participants = [
            line.strip()
            for line in participants_text.splitlines()
            if line.strip()
        ]

        try:
            draw = create_knockout_draw(participants)

            if request.form.get("action") == "save":
                if not tournament_name:
                    raise ValueError("Debes indicar un nombre para el torneo.")

                tournament_id = save_tournament(
                    tournament_name,
                    participants,
                    draw,
                )

                return redirect(
                    url_for("view_tournament", tournament_id=tournament_id)
                )

        except ValueError as exc:
            error = str(exc)

    return render_template(
        "index.html",
        draw=draw,
        error=error,
        participants_text=participants_text,
        tournament_name=tournament_name,
    )


@app.route("/torneos")
def tournaments():
    return render_template(
        "tournaments.html",
        tournaments=list_tournaments(),
    )


@app.route("/torneos/<int:tournament_id>")
def view_tournament(tournament_id):
    tournament = get_tournament(tournament_id)

    if tournament is None:
        return "Torneo no encontrado", 404

    return render_template(
        "tournament.html",
        tournament=tournament,
    )


@app.route("/torneos/<int:tournament_id>/borrar", methods=["POST"])
def remove_tournament(tournament_id):
    delete_tournament(tournament_id)
    return redirect(url_for("tournaments"))