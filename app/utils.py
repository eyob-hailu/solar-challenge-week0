import pandas as pd
import plotly.express as px
import streamlit as st

@st.cache_data
def load_and_process_data(uploaded_files):
    """
    Loads, parses, and combines multiple uploaded CSV files.
    This function is cached to prevent re-running on every interaction.
    Adds a 'Country' column based on the filename.
    """
    data_frames = []
    
    for f in uploaded_files:
        # Extract country name from filename (e.g., 'benin_clean.csv' -> 'Benin')
        try:
            country_name = f.name.split('_')[0].capitalize()
        except IndexError:
            country_name = f.name.replace(".csv", "")

        try:
            df = pd.read_csv(f)
            
            # Convert Timestamp column to datetime, coercing errors
            if 'Timestamp' in df.columns:
                df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
            
            # Add the 'Country' identifier
            df['Country'] = country_name
            data_frames.append(df)
            
        except Exception as e:
            st.warning(f"Skipping file {f.name} due to loading error: {e}")
            
    if data_frames:
        return pd.concat(data_frames, ignore_index=True)
    return None

def create_boxplot(df, metric, selected_countries):
    """
    Creates a Plotly boxplot comparing a metric across selected countries.
    """
    if df is None or not selected_countries:
        return None

    # Filter data based on sidebar selection
    df_filtered = df[df['Country'].isin(selected_countries)]
    
    if df_filtered.empty:
        st.warning("No data to display. Please select at least one country.")
        return None
    
    if metric not in df_filtered.columns or 'Country' not in df_filtered.columns:
        st.warning(f"Required columns ({metric} or Country) are missing.")
        return None

    # Plotly boxplot
    fig = px.box(
        df_filtered, 
        x='Country', 
        y=metric, 
        color='Country',
        title=f'Distribution of {metric} Across Selected Countries',
        labels={metric: f'{metric} (W/m²)'},
        height=500
    )
    fig.update_layout(showlegend=False)
    return fig

def generate_summary_table(df, metrics):
    """Calculates and returns the cross-country summary statistics."""
    if df is None:
        return None
        
    metrics_to_summarize = [m for m in metrics if m in df.columns]
    
    if metrics_to_summarize:
        return df.groupby('Country')[metrics_to_summarize].agg(['mean', 'median', 'std'])
    return None

def generate_ranking_table(df):
    """Calculates and returns the country ranking based on average GHI."""
    if df is None or 'GHI' not in df.columns:
        return None
        
    top_ranking = df.groupby('Country')['GHI'].mean().sort_values(ascending=False).reset_index()
    top_ranking.columns = ['Country', 'Average GHI (W/m²)']
    return top_ranking