"""
AQI Calculator

Calculates pollutant-specific AQI sub-indices and
the overall AQI using CPCB National AQI breakpoints.
"""

POLLUTANT_BREAKPOINTS = {
    "PM2.5": [
        (0, 30, 0, 50),
        (30, 60, 50, 100),
        (60, 90, 100, 200),
        (90, 120, 200, 300),
        (120, 250, 300, 400),
    ],

    "PM10": [
        (0, 50, 0, 50),
        (50, 100, 50, 100),
        (100, 250, 100, 200),
        (250, 350, 200, 300),
        (350, 430, 300, 400),
    ],

    "NO2": [
        (0, 40, 0, 50),
        (40, 80, 50, 100),
        (80, 180, 100, 200),
        (180, 280, 200, 300),
        (280, 400, 300, 400),
    ],

    "SO2": [
        (0, 40, 0, 50),
        (40, 80, 50, 100),
        (80, 380, 100, 200),
        (380, 800, 200, 300),
        (800, 1600, 300, 400),
    ],

    "CO": [
        (0, 1, 0, 50),
        (1, 2, 50, 100),
        (2, 10, 100, 200),
        (10, 17, 200, 300),
        (17, 34, 300, 400),
    ],

    "O3": [
        (0, 50, 0, 50),
        (50, 100, 50, 100),
        (100, 168, 100, 200),
        (168, 208, 200, 300),
        (208, 748, 300, 400),
    ],

    "NH3": [
        (0, 200, 0, 50),
        (200, 400, 50, 100),
        (400, 800, 100, 200),
        (800, 1200, 200, 300),
        (1200, 1800, 300, 400),
    ],

    "Pb": [
        (0, 0.5, 0, 50),
        (0.5, 1, 50, 100),
        (1, 2, 100, 200),
        (2, 3, 200, 300),
        (3, 3.5, 300, 400),
    ],
}


def calculate_sub_index(pollutant, concentration):
    """
    Calculate the AQI sub-index for one pollutant.
    """

    if pollutant not in POLLUTANT_BREAKPOINTS:
        raise ValueError(f"Unsupported pollutant: {pollutant}")

    if concentration < 0:
        raise ValueError("Concentration cannot be negative.")

    breakpoints = POLLUTANT_BREAKPOINTS[pollutant]

    for b_lo, b_hi, i_lo, i_hi in breakpoints:

        if b_lo <= concentration <= b_hi:

            sub_index = (
                ((i_hi - i_lo) / (b_hi - b_lo))
                * (concentration - b_lo)
                + i_lo
            )

            return round(sub_index, 2)

    # CPCB defines the final category as an open-ended
    # Severe range. AQI is capped at 500.
    if concentration > breakpoints[-1][1]:
        return 500.0

    raise ValueError(
        f"Concentration {concentration} is outside the supported "
        f"range for {pollutant}."
    )


def calculate_aqi(pollutant_data):
    """
    Calculate the overall AQI from pollutant concentrations.

    The overall AQI is determined by the highest
    pollutant sub-index.
    """

    if not pollutant_data:
        raise ValueError("Pollutant data cannot be empty.")

    sub_indices = {}

    for pollutant, concentration in pollutant_data.items():
        sub_indices[pollutant] = calculate_sub_index(
            pollutant,
            concentration
        )

    overall_aqi = max(sub_indices.values())

    return round(overall_aqi, 2), sub_indices


if __name__ == "__main__":

    sample_data = {
        "PM2.5": 42,
        "PM10": 78,
        "NO2": 25,
        "SO2": 12,
        "CO": 0.8,
        "O3": 35,
        "NH3": 10,
        "Pb": 0.2
    }

    aqi, sub_indices = calculate_aqi(sample_data)

    print("Pollutant Sub-Indices:")

    for pollutant, value in sub_indices.items():
        print(f"{pollutant}: {value}")

    print(f"\nOverall AQI: {aqi}")