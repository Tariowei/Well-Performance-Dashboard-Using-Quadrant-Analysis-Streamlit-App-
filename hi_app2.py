import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Well Quadrant Analysis")

# Upload file
file = st.file_uploader("2-production_history.txt")

if file is not None:

    # Read data
    data = pd.read_csv(file, sep="\t")

    # Select date
    dates = data['Date'].unique()
    selected_date = st.selectbox("Select Date", dates)

    # Filter data
    df = data[data['Date'] == selected_date].copy()

    # -------------------------
    # BASIC STATISTICS
    # -------------------------
    oil_avg = df['OIL'].mean()
    water_avg = df['WATER'].mean()
    gas_avg = df['GAS'].mean()
    hrs_avg = df['HOURS'].mean()

    # -------------------------
    # HEALTH INDEX
    # -------------------------
    df['HI_Oil'] = (df['OIL'] / oil_avg) - 1
    df['HI_Water'] = (df['WATER'] / water_avg) - 1
    df['HI_Gas'] = (df['GAS'] / gas_avg) - 1
    df['HI_Hours'] = (df['HOURS'] / hrs_avg) - 1

    # -------------------------
    # SHOW DATA
    # -------------------------
    st.subheader("Processed Data")
    st.dataframe(df)

    # -------------------------
    # HISTOGRAMS (NEW)
    # -------------------------
    st.subheader("Production Distribution")

    fig_hist1 = px.histogram(df, x="OIL", title="Oil Distribution")
    st.plotly_chart(fig_hist1)

    fig_hist2 = px.histogram(df, x="WATER", title="Water Distribution")
    st.plotly_chart(fig_hist2)

    # -------------------------
    # BAR CHART (NEW)
    # -------------------------
    st.subheader("Oil Production by Well")

    fig_bar = px.bar(df, x="UID", y="OIL", title="Oil Rate per Well")
    st.plotly_chart(fig_bar)

    # -------------------------
    # QUADRANT PLOTS
    # -------------------------
    st.subheader("Quadrant Analysis")

    fig1 = px.scatter(df, x='HI_Oil', y='HI_Water', color='UID',
                      title="Oil vs Water", template='none')
    st.plotly_chart(fig1)

    fig2 = px.scatter(df, x='HI_Gas', y='HI_Water', color='UID',
                      title="Gas vs Water", template='none')
    st.plotly_chart(fig2)

    # -------------------------
    # BAD WELLS
    # -------------------------
    bad = df[(df['HI_Oil'] < 0) & (df['HI_Water'] > 0)]

    st.subheader("Wells with Low Oil & High Water")
    st.dataframe(bad)

    # -------------------------
    # TIME TREND (IMPROVED)
    # -------------------------
    wells = bad['UID'].unique()
    df_hist = data[data['UID'].isin(wells)]

    if len(wells) > 0:
        st.subheader("Production Trend of Problem Wells")

        fig3 = px.line(df_hist, x='Date', y='OIL', color='UID',
                       title="Oil Production Over Time")
        st.plotly_chart(fig3)
    else:
        st.write("No problematic wells for this date.")

else:
    st.write("Please upload a dataset to start.")