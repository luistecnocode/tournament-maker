import pytest

from app.tournament.knockout import (
    create_knockout_draw,
    main_bracket_size,
    validate_participants,
)


def test_main_bracket_size():
    assert main_bracket_size(2) == 2
    assert main_bracket_size(3) == 2
    assert main_bracket_size(4) == 4
    assert main_bracket_size(5) == 4
    assert main_bracket_size(7) == 4
    assert main_bracket_size(8) == 8
    assert main_bracket_size(12) == 8
    assert main_bracket_size(16) == 16


def test_minimum_participants():
    with pytest.raises(ValueError):
        validate_participants(["Ana"])


def test_duplicate_participants():
    with pytest.raises(ValueError):
        validate_participants(["Ana", "ana"])


def test_8_participants_no_preliminary_round():
    participants = [
        "Ana",
        "Luis",
        "Pedro",
        "María",
        "Juan",
        "Laura",
        "Sergio",
        "Marta",
    ]

    draw = create_knockout_draw(participants)

    assert draw["main_bracket_size"] == 8
    assert len(draw["preliminary_matches"]) == 0
    assert len(draw["direct_entries"]) == 0
    assert len(draw["main_matches"]) == 4


def test_7_participants():
    participants = [
        "Ana",
        "Luis",
        "Pedro",
        "María",
        "Juan",
        "Laura",
        "Sergio",
    ]

    draw = create_knockout_draw(participants)

    assert draw["main_bracket_size"] == 4
    assert len(draw["preliminary_matches"]) == 3
    assert len(draw["direct_entries"]) == 1


def test_12_participants():
    participants = [f"Jugador {i}" for i in range(1, 13)]

    draw = create_knockout_draw(participants)

    assert draw["main_bracket_size"] == 8
    assert len(draw["preliminary_matches"]) == 4
    assert len(draw["direct_entries"]) == 4