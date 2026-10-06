"""
Simple Reflex Agent for AQI Classification.

The agent receives the current AQI as its percept
and selects an action using predefined condition-action rules.
"""


def classify_aqi(aqi):
    """
    Classify AQI using predefined condition-action rules.
    """

    if aqi < 0:
        raise ValueError("AQI cannot be negative.")

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Satisfactory"

    elif aqi <= 200:
        return "Moderately Polluted"

    elif aqi <= 300:
        return "Poor"

    elif aqi <= 400:
        return "Very Poor"

    else:
        return "Severe"


if __name__ == "__main__":

    test_aqi = 78

    category = classify_aqi(test_aqi)

    print(f"AQI: {test_aqi}")
    print(f"Category: {category}")