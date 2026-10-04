from io import BytesIO

from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas


def generate_tournament_pdf(tournament):
    buffer = BytesIO()

    page_width, page_height = landscape(A4)

    pdf = canvas.Canvas(
        buffer,
        pagesize=landscape(A4),
    )

    pdf.setTitle(tournament["name"])

    margin = 24
    top = page_height - margin

    # Título
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(
        margin,
        top,
        tournament["name"],
    )

    pdf.setFont("Helvetica", 9)
    pdf.drawString(
        margin,
        top - 18,
        f"Participantes: {tournament['draw']['total_participants']}",
    )

    rounds = []

    if tournament["draw"]["preliminary_matches"]:
        rounds.append(
            {
                "name": "Ronda previa",
                "matches": tournament["draw"]["preliminary_matches"],
            }
        )

    rounds.extend(tournament["draw"]["rounds"])

    available_width = page_width - (2 * margin)
    column_width = available_width / len(rounds)

    start_y = top - 58
    usable_height = start_y - margin

    for round_index, round_data in enumerate(rounds):
        x = margin + (round_index * column_width)

        # Nombre de ronda
        pdf.setFont("Helvetica-Bold", 10)

        pdf.drawCentredString(
            x + (column_width / 2),
            start_y + 14,
            round_data["name"],
        )

        matches = round_data["matches"]
        match_count = len(matches)

        if match_count == 0:
            continue

        spacing = usable_height / match_count

        for match_index, match in enumerate(matches):
            center_y = (
                start_y
                - (match_index * spacing)
                - (spacing / 2)
            )

            box_height = min(42, spacing - 6)

            box_x = x + 4
            box_y = center_y - (box_height / 2)
            box_width = column_width - 8

            # Identificador del partido
            pdf.setFont("Helvetica-Bold", 8)

            pdf.drawString(
                box_x,
                box_y + box_height + 4,
                match["id"],
            )

            # Caja
            pdf.rect(
                box_x,
                box_y,
                box_width,
                box_height,
            )

            # Jugador 1
            pdf.setFont("Helvetica-Bold", 9)

            pdf.drawString(
                box_x + 5,
                box_y + box_height - 14,
                str(match["player1"]),
            )

            # Separador
            pdf.setFont("Helvetica", 7)

            pdf.drawString(
                box_x + 5,
                box_y + (box_height / 2) - 2,
                "vs",
            )

            # Jugador 2
            pdf.setFont("Helvetica-Bold", 9)

            pdf.drawString(
                box_x + 5,
                box_y + 6,
                str(match["player2"]),
            )

    pdf.showPage()
    pdf.save()

    buffer.seek(0)

    return buffer