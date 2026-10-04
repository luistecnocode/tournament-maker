import json
import sqlite3
from pathlib import Path


DB_PATH = Path("data/tournaments.db")


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    return connection


def init_db():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tournaments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                participants TEXT NOT NULL,
                draw TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def save_tournament(name, participants, draw):
    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO tournaments (name, participants, draw)
            VALUES (?, ?, ?)
            """,
            (
                name,
                json.dumps(participants, ensure_ascii=False),
                json.dumps(draw, ensure_ascii=False),
            ),
        )

        return cursor.lastrowid


def list_tournaments():
    with get_connection() as connection:
        return connection.execute(
            """
            SELECT id, name, created_at
            FROM tournaments
            ORDER BY created_at DESC
            """
        ).fetchall()


def get_tournament(tournament_id):
    with get_connection() as connection:
        row = connection.execute(
            """
            SELECT *
            FROM tournaments
            WHERE id = ?
            """,
            (tournament_id,),
        ).fetchone()

    if row is None:
        return None

    return {
        "id": row["id"],
        "name": row["name"],
        "participants": json.loads(row["participants"]),
        "draw": json.loads(row["draw"]),
        "created_at": row["created_at"],
    }


def delete_tournament(tournament_id):
    with get_connection() as connection:
        connection.execute(
            """
            DELETE FROM tournaments
            WHERE id = ?
            """,
            (tournament_id,),
        )