# 🗺️ Hyderabad to Warangal Shortest Path Finder

A lightweight, interactive web application built with **Streamlit**, **OSRM (Open Source Routing Machine)**, and **Folium** that finds and visualizes the optimal driving route between Hyderabad and Warangal.

---

## ✨ Features
* **Lightning-Fast Routing:** Uses live OSRM public API routing engines to bypass heavy local graph downloads and prevent API timeouts.
* **Interactive Map Visualization:** Displays a fully zoomable and pannable map with custom markers for Hyderabad and Warangal.
* **Persistent UI (Session State):** Results, distance metrics, and maps stay on screen persistently even after interactions.
* **Travel Metrics:** Instantly calculates total distance in kilometers and estimated travel time in hours.

---

## 📦 Prerequisites & Required Packages

Make sure you have **Python** installed on your system. Open your terminal or command prompt and install the necessary dependencies by running:

```bash
pip install streamlit requests folium streamlit-folium

cd "C:\Users\aravi\OneDrive\Documents\Desktop\MAP_APP"

python -m streamlit run hyd_warangal_map_app.py