def sort(width, height, length, mass):
    if min(width, height, length, mass) < 0:
        raise ValueError("Dimensions and mass must be non-negative numbers.")

    volume = width * height * length
    bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"


# --- quick tests ---
def _run_tests():
    # STANDARD: neither bulky nor heavy
    assert sort(100, 10, 10, 5) == "STANDARD"

    # Bulky by volume
    assert sort(100, 100, 100, 5) == "SPECIAL"          # 1,000,000 cm³ (edge)
    assert sort(101, 100, 100, 1) == "SPECIAL"

    # Bulky by dimension
    assert sort(150, 10, 10, 1) == "SPECIAL"            # edge: dimension == 150

    # Heavy only
    assert sort(10, 10, 10, 20) == "SPECIAL"            # edge: mass == 20

    # REJECTED: both bulky and heavy
    assert sort(150, 150, 1, 25) == "REJECTED"
    assert sort(100, 100, 100, 20) == "REJECTED"        # exact thresholds

    # Non-negative check
    try:
        sort(-1, 10, 10, 1)
        assert False, "Expected ValueError for negative input"
    except ValueError:
        pass

if __name__ == "__main__":
    _run_tests()
    print("All tests passed.")