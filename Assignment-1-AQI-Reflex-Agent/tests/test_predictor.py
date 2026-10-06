from src.predictor import predict_tomorrow_aqi


def test_normal_conditions():
    predicted_aqi, category = predict_tomorrow_aqi(
        78,
        32,
        1.2
    )

    assert predicted_aqi == 78
    assert category == "Satisfactory"


def test_high_temperature():
    predicted_aqi, category = predict_tomorrow_aqi(
        78,
        40,
        1.2
    )

    assert predicted_aqi == 88
    assert category == "Satisfactory"


def test_low_air_density():
    predicted_aqi, category = predict_tomorrow_aqi(
        78,
        32,
        1.0
    )

    assert predicted_aqi == 88
    assert category == "Satisfactory"