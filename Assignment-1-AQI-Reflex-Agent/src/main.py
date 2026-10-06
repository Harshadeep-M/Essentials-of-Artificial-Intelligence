from aqi_calculator import calculate_aqi
from reflex_agent import classify_aqi
from predictor import predict_tomorrow_aqi


def main():

    # Current environmental data
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

    temperature = 32
    air_density = 1.2

    # Calculate current AQI
    aqi, sub_indices = calculate_aqi(pollutant_data)

    # Classify current AQI using the reflex agent
    current_category = classify_aqi(aqi)

    # Predict tomorrow's AQI
    predicted_aqi, predicted_category = predict_tomorrow_aqi(
        aqi,
        temperature,
        air_density
    )

    print("=" * 40)
    print("          AQI REFLEX AGENT")
    print("=" * 40)

    print("\nCurrent Environmental Data")
    print("-" * 40)

    for pollutant, concentration in pollutant_data.items():
        print(f"{pollutant}: {concentration}")

    print(f"Temperature: {temperature} °C")
    print(f"Air Density: {air_density} kg/m³")

    print("\nPollutant Sub-Indices")
    print("-" * 40)

    for pollutant, value in sub_indices.items():
        print(f"{pollutant}: {value}")

    print("\nCurrent AQI")
    print("-" * 40)
    print(f"AQI: {aqi}")
    print(f"Category: {current_category}")

    print("\nTomorrow's Prediction")
    print("-" * 40)
    print(f"Predicted AQI: {predicted_aqi}")
    print(f"Predicted Category: {predicted_category}")


if __name__ == "__main__":
    main()