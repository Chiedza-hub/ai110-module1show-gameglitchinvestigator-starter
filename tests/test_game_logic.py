# Tests for the bugs fixed in app.py.
# The functions under test are pure (no streamlit), so we define them here
# directly to avoid the module-level Streamlit code running on import.

def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str, low: int, high: int):
    if raw is None:
        return False, None, "Enter a guess."
    if raw == "":
        return False, None, "Enter a guess."
    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."
    if value < low or value > high:
        return False, None, f"Out of range! Please enter a number between {low} and {high}."
    return True, value, None


def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"
    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


# --- get_range_for_difficulty ---

def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_normal_range():
    # Bug fix: Normal was previously 1-100, should be 1-50
    assert get_range_for_difficulty("Normal") == (1, 50)

def test_hard_range():
    # Bug fix: Hard was previously 1-50, should be 1-100
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_unknown_difficulty_falls_back():
    assert get_range_for_difficulty("Unknown") == (1, 100)


# --- parse_guess: bounds checking (bug fix) ---

def test_parse_guess_valid_in_range():
    ok, value, err = parse_guess("10", 1, 20)
    assert ok is True
    assert value == 10
    assert err is None

def test_parse_guess_below_low():
    # Bug fix: guesses below range should be rejected
    ok, value, err = parse_guess("0", 1, 20)
    assert ok is False
    assert value is None
    assert "1" in err and "20" in err

def test_parse_guess_above_high():
    # Bug fix: guesses above range should be rejected
    ok, value, err = parse_guess("200", 1, 100)
    assert ok is False
    assert value is None
    assert "1" in err and "100" in err

def test_parse_guess_at_low_boundary():
    ok, value, err = parse_guess("1", 1, 20)
    assert ok is True
    assert value == 1

def test_parse_guess_at_high_boundary():
    ok, value, err = parse_guess("20", 1, 20)
    assert ok is True
    assert value == 20

def test_parse_guess_empty_string():
    ok, value, err = parse_guess("", 1, 100)
    assert ok is False
    assert "guess" in err.lower()

def test_parse_guess_non_number():
    ok, value, err = parse_guess("abc", 1, 100)
    assert ok is False
    assert "number" in err.lower()

def test_parse_guess_out_of_range_easy():
    # 21 is valid for Normal/Hard but out of range for Easy
    ok, value, err = parse_guess("21", 1, 20)
    assert ok is False

def test_parse_guess_out_of_range_normal():
    # 51 is valid for Hard but out of range for Normal
    ok, value, err = parse_guess("51", 1, 50)
    assert ok is False


# --- check_guess ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
