import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

# 1. Page Configuration
st.set_page_config(
    page_title="Hyd to Warangal Shortest Path Finder",
    page_icon="🗺️",
    layout="wide"
)

def get_osrm_route(start_coords, end_coords):
    url = f"https://router.project-osrm.org/route/v1/driving/{start_coords[0]},{start_coords[1]};{end_coords[0]},{end_coords[1]}?overview=full&geometries=geojson"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data["routes"]:
                route = data["routes"][0]
                distance_km = route["distance"] / 1000
                duration_hrs = route["duration"] / 3600
                coordinates = route["geometry"]["coordinates"]
                latlon_coords = [[lat, lon] for lon, lat in coordinates]
                return distance_km, duration_hrs, latlon_coords
    except Exception as e:
        st.error(f"Error connecting to routing service: {e}")
    return None, None, None

def main():
    st.title("🗺️ Hyderabad to Warangal Shortest Path Finder")
    st.write("This application finds the optimal driving route between Hyderabad and Warangal instantly using live routing engines.")
    
    hyd_coords = (78.4867, 17.3850)
    warangal_coords = (79.5941, 17.9783)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Origin:** Hyderabad (Secunderabad/Center)")
    with col2:
        st.info("**Destination:** Warangal (City Center)")
        
    # Initialize session state variables to keep data persistent
    if "route_calculated" not in st.session_state:
        st.session_state.route_calculated = False
        st.session_state.distance = None
        st.session_state.duration = None
        st.session_state.route_coords = None

    if st.button("Calculate Optimal Route", type="primary"):
        with st.spinner("Calculating shortest path..."):
            distance, duration, route_coords = get_osrm_route(hyd_coords, warangal_coords)
            
            if distance is not None:
                # Save results to session state so they don't disappear
                st.session_state.route_calculated = True
                st.session_state.distance = distance
                st.session_state.duration = duration
                st.session_state.route_coords = route_coords
            else:
                st.error("Could not retrieve route data. Please check your internet connection.")

    # Display results and map if they have been calculated and saved in session state
    if st.session_state.route_calculated:
        m1, m2 = st.columns(2)
        m1.metric(label="Total Distance", value=f"{st.session_state.distance:.2f} km")
        m2.metric(label="Estimated Travel Time", value=f"{st.session_state.duration:.1f} hours")
        
        st.success("Route calculated successfully!")
        
        center_lat = (hyd_coords[1] + warangal_coords[1]) / 2
        center_lon = (hyd_coords[0] + warangal_coords[0]) / 2
        
        m = folium.Map(location=[center_lat, center_lon], zoom_start=9)
        
        folium.PolyLine(
            st.session_state.route_coords,
            color="red",
            weight=5,
            opacity=0.8
        ).add_to(m)
        
        folium.Marker(
            [hyd_coords[1], hyd_coords[0]],
            popup="Hyderabad",
            icon=folium.Icon(color="green", icon="play")
        ).add_to(m)
        
        folium.Marker(
            [warangal_coords[1], warangal_coords[0]],
            popup="Warangal",
            icon=folium.Icon(color="blue", icon="stop")
        ).add_to(m)
        
        st.subheader("Interactive Route Map")
        st_folium(m, width=1000, height=500, key="route_map")

if __name__ == "__main__":
    main()