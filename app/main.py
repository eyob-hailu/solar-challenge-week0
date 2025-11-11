import streamlit as st
import pandas as pd
import plotly.express as px
# Import all required functions from the utility file
from utils import load_and_process_data, create_boxplot, generate_summary_table, generate_ranking_table

# --- Constants ---
ANALYSIS_METRICS = ['GHI', 'DNI', 'DHI']

# --- Streamlit Page Setup ---
st.set_page_config(
    page_title="Cross-Country Solar Data Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Main Dashboard Structure ---
st.title("☀️ Cross-Country Solar Farm Analysis")
st.markdown("A dashboard to compare the solar irradiance potential (GHI, DNI, DHI) across Benin, Sierra Leone, and Togo.")

# --- Sidebar for File Upload and Country Selection (Interactive Elements) ---
with st.sidebar:
    st.header("Data Input")
    uploaded_files = st.file_uploader(
        "Upload CLEANED country CSVs",
        type="csv",
        accept_multiple_files=True
    )
    
    combined_df = None
    if uploaded_files:
        # Load and process data using the utility function
        combined_df = load_and_process_data(uploaded_files)
        st.success(f"Loaded and combined data from {len(uploaded_files)} sources.")
    else:
        st.info("Please upload your cleaned CSV files above.")
    
    
    # --- Country Selection Widget (Minimum Essential To Do) ---
    st.header("Filter & Compare")
    selected_countries = []
    if combined_df is not None:
        all_countries = combined_df['Country'].unique().tolist()
        selected_countries = st.multiselect(
            "Select Countries for Visualization:",
            options=all_countries,
            default=all_countries
        )

# --- Main Content Area ---
if combined_df is not None and selected_countries:
    
    # Identify relevant columns
    available_metrics = [col for col in ANALYSIS_METRICS if col in combined_df.columns]
    
    # --- Interactive Metric Selector ---
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Interactive Plot Settings")
        if available_metrics:
            metric_to_plot = st.selectbox(
                "Select Metric for Boxplot:",
                options=available_metrics,
                index=available_metrics.index('GHI') if 'GHI' in available_metrics else 0
            )
        else:
            st.error("Missing GHI, DNI, or DHI columns in the uploaded data.")
            metric_to_plot = None
            
    # --- Boxplot of GHI or other plots (Minimum Essential To Do) ---
    with col2:
        if metric_to_plot:
            # Generate boxplot using the utility function
            boxplot_fig = create_boxplot(combined_df, metric_to_plot, selected_countries)
            if boxplot_fig:
                st.plotly_chart(boxplot_fig, use_container_width=True)

    st.markdown("---")
    
    st.header("Key Insights & Ranking")
    
    # --- Summary Statistics Table ---
    st.subheader("Cross-Country Summary Statistics (Mean, Median, Std)")
    summary_table = generate_summary_table(combined_df, ANALYSIS_METRICS)
    if summary_table is not None:
        st.dataframe(summary_table.style.format("{:.2f}"))
    else:
        st.warning("Could not generate summary table due to missing data.")

    # --- Top Regions Table (Minimum Essential To Do) ---
    st.subheader("Top Regions Ranking (By Average GHI)")
    ranking_table = generate_ranking_table(combined_df)
    
    if ranking_table is not None:
        # Display the ranking with styling
        st.dataframe(
            ranking_table.style.background_gradient(
                cmap='YlGnBu', 
                subset=['Average GHI (W/m²)']
            ).format(
                {'Average GHI (W/m²)': '{:.2f}'}
            ),
            use_container_width=True
        )
    else:
        st.info("GHI column required to generate the Top Regions Ranking table.")

else:
    # Placeholder image if no data is loaded
    st.image("https://placehold.co/1000x300/a3e635/000?text=Upload+files+to+start+analysis", use_container_width=True)