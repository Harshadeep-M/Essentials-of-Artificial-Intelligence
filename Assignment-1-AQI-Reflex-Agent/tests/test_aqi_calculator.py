from src.aqi_calculator import calculate_sub_index, calculate_aqi


def test_pm25_sub_index():
    result = calculate_sub_index("PM2.5", 42)
    assert result == 70.0


def test_overall_aqi():
    pollutant_data = {
        "PM2.5": 42,
        "PM10": 78,
        "NO2": 25,
        "SO2": 12,
        "CO": 0.8,
        "O3": 35,
        "NH3": 10,
        "Pb": 0.2
    }

    aqi, sub_indices = calculate_aqi(pollutant_data)

    assert aqi == 78.0
    assert sub_indices["PM10"] == 78.0