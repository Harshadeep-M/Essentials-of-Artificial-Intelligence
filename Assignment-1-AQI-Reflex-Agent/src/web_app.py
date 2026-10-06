from flask import Flask, render_template, request

from aqi_calculator import calculate_aqi
from reflex_agent import classify_aqi
from predictor import predict_tomorrow_aqi


app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


def category_class(category):
    """Convert AQI category into a CSS-friendly class name."""
    return category.lower().replace(" ", "-")


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        pollutant_data = {
            "PM2.5": float(request.form["pm25"]),
            "PM10": float(request.form["pm10"]),
            "NO2": float(request.form["no2"]),
            "SO2": float(request.form["so2"]),
            "CO": float(request.form["co"]),
            "O3": float(request.form["o3"]),
            "NH3": float(request.form["nh3"]),
            "Pb": float(request.form["pb"])
        }

        temperature = float(request.form["temperature"])
        air_density = float(request.form["air_density"])

        aqi, sub_indices = calculate_aqi(pollutant_data)

        category = classify_aqi(aqi)

        dominant_pollutant = max(
            sub_indices,
            key=sub_indices.get
        )

        predicted_aqi, predicted_category = predict_tomorrow_aqi(
            aqi,
            temperature,
            air_density
        )

        

        result = {
            "aqi": aqi,
            "category": category,
            "category_class": category_class(category),
            "dominant_pollutant": dominant_pollutant,
            "sub_indices": sub_indices,
            "predicted_aqi": predicted_aqi,
            "predicted_category": predicted_category,
            "predicted_category_class": category_class(
                predicted_category
            )
        }

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)