# AQI Reflex Agent

A simple Artificial Intelligence project that calculates the Air Quality Index (AQI), classifies air quality using a Simple Reflex Agent, and predicts tomorrow's AQI using a basic rule-based approach.

## Project Objective

The objective of this project is to develop a Simple Reflex Agent for AQI that:

- Takes environmental pollutant data as input.
- Calculates AQI sub-indices for different pollutants.
- Determines the overall AQI.
- Classifies air quality based on predefined rules.
- Provides a simple prediction of tomorrow's AQI using current AQI, temperature, and air density.

## AI Concept

This project demonstrates a **Simple Reflex Agent**.

The agent receives the current AQI as its percept and selects an action using predefined condition-action rules:

| AQI | Category |
|---|---|
| 0–50 | Good |
| 51–100 | Satisfactory |
| 101–200 | Moderately Polluted |
| 201–300 | Poor |
| 301–400 | Very Poor |
| 401–500 | Severe |

The agent does not learn from previous data. It responds to the current input using predefined rules.

## AQI Calculation

The system considers the following pollutants:

- PM2.5
- PM10
- NO2
- SO2
- CO
- O3
- NH3
- Pb

For each pollutant, an AQI sub-index is calculated using concentration and AQI breakpoints. The overall AQI is determined from the highest pollutant sub-index.

The general interpolation formula is:

I = [(I_HI - I_LO) / (B_HI - B_LO)] × (C - B_LO) + I_LO

Tomorrow's AQI Prediction

The project also contains a simple rule-based prediction component.

It considers:

- Current AQI
- Temperature
- Air density

Based on predefined rules, the current AQI is adjusted to estimate tomorrow's AQI.

This prediction is intended for educational purposes and is not an official CPCB forecasting model or a machine-learning model.

Project Structure

AQI-Reflex-Agent/
│
├── src/
│   ├── aqi_calculator.py
│   ├── reflex_agent.py
│   ├── predictor.py
│   └── main.py
│
├── tests/
│   ├── test_aqi_calculator.py
│   ├── test_reflex_agent.py
│   └── test_predictor.py
│
├── data/
├── docs/
├── .gitignore
├── requirements.txt
└── README.md

How to Run

Create and activate the virtual environment:
python -m venv .venv
.venv\Scripts\Activate.ps1

Install dependencies:
python -m pip install -r requirements.txt

Run the application:
python src/main.py

Testing

The project uses pytest for automated testing.
python -m pytest

The tests cover:

- AQI calculation
- AQI classification
- Tomorrow's AQI prediction

Sample Result

Current AQI: 78.0
Category: Satisfactory

Predicted AQI: 78.0
Predicted Category: Satisfactory

Software Engineering Practices

The project follows basic software engineering principles:

- Modular design
- Separation of concerns
- Input validation
- Automated unit testing
- Clear naming and documentation
- Version control using Git/GitHub

Limitations

- The prediction component is a simplified rule-based approach.
- No real-time AQI or weather data is used.
- The system does not perform machine-learning-based forecasting.
- The prediction is intended for academic demonstration only.
