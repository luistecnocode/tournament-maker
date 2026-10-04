import random


def validate_participants(participants):
    cleaned = [name.strip() for name in participants if name.strip()]

    if len(cleaned) < 2:
        raise ValueError("Se necesitan al menos 2 participantes.")

    normalized = [name.lower() for name in cleaned]

    if len(normalized) != len(set(normalized)):
        raise ValueError("No puede haber participantes duplicados.")

    return cleaned


def main_bracket_size(num_participants):
    size = 1

    while size * 2 <= num_participants:
        size *= 2

    return size


def create_knockout_draw(participants):
    participants = validate_participants(participants)

    shuffled = participants.copy()
    random.shuffle(shuffled)

    total = len(shuffled)
    bracket_size = main_bracket_size(total)

    if total == bracket_size:
        preliminary_matches = []
        direct_entries = shuffled
    else:
        preliminary_players = 2 * (total - bracket_size)
        direct_entries_count = total - preliminary_players

        direct_entries = shuffled[:direct_entries_count]
        preliminary = shuffled[direct_entries_count:]

        preliminary_matches = []

        for i in range(0, len(preliminary), 2):
            preliminary_matches.append(
                {
                    "player1": preliminary[i],
                    "player2": preliminary[i + 1],
                }
            )

    return {
        "total_participants": total,
        "main_bracket_size": bracket_size,
        "preliminary_matches": preliminary_matches,
        "direct_entries": direct_entries,
    }