from src.reflex_agent import classify_aqi


def test_good_aqi():
    assert classify_aqi(50) == "Good"


def test_satisfactory_aqi():
    assert classify_aqi(78) == "Satisfactory"


def test_moderately_polluted_aqi():
    assert classify_aqi(150) == "Moderately Polluted"


def test_poor_aqi():
    assert classify_aqi(250) == "Poor"


def test_very_poor_aqi():
    assert classify_aqi(350) == "Very Poor"


def test_severe_aqi():
    assert classify_aqi(450) == "Severe"