"""
Simple AQI Predictor.

Predicts tomorrow's AQI category using current environmental conditions.
This is a simple rule-based prediction for educational purposes.
"""


def predict_tomorrow_aqi(current_aqi, temperature, air_density):
    """
    Predict tomorrow's AQI category based on current conditions.

    Parameters:
        current_aqi (float): Current AQI value.
        temperature (float): Current temperature in Celsius.
        air_density (float): Air density in kg/m^3.

    Returns:
        str: Predicted AQI category for tomorrow.
    """

    predicted_aqi = current_aqi

    # High temperature can contribute to poorer air quality conditions.
    if temperature > 35:
        predicted_aqi += 10

    elif temperature < 15:
        predicted_aqi -= 5

    # Lower air density is used here as a simple indicator
    # for potentially poorer dispersion conditions.
    if air_density < 1.1:
        predicted_aqi += 10

    elif air_density > 1.3:
        predicted_aqi -= 5

    # Keep AQI within the valid range.
    predicted_aqi = max(0, min(predicted_aqi, 500))

    if predicted_aqi <= 50:
        category = "Good"

    elif predicted_aqi <= 100:
        category = "Satisfactory"

    elif predicted_aqi <= 200:
        category = "Moderately Polluted"

    elif predicted_aqi <= 300:
        category = "Poor"

    elif predicted_aqi <= 400:
        category = "Very Poor"

    else:
        category = "Severe"

    return round(predicted_aqi, 2), category


if __name__ == "__main__":

    current_aqi = 78
    temperature = 32
    air_density = 1.2

    predicted_aqi, category = predict_tomorrow_aqi(
        current_aqi,
        temperature,
        air_density
    )

    print(f"Current AQI: {current_aqi}")
    print(f"Temperature: {temperature} °C")
    print(f"Air Density: {air_density} kg/m³")
    print()
    print(f"Predicted Tomorrow AQI: {predicted_aqi}")
    print(f"Predicted Category: {category}")