import streamlit as st
import subprocess
import os
import sys

# Updated page config
st.set_page_config(
    page_title="FMCG Research Analytics — Data Science Project",
    layout="centered"
)

# Updated main title
st.title("📊 FMCG Research Analytics — Data Science Project")
st.markdown("Choose any app below and launch it in a new tab.")

# App map
apps = {
    "📊 EDA Dashboard 1": "EDA.py",
    "📈 EDA Dashboard 2": "EDA2.py",
    "🧠 Unsupervised ML": "app.py",
    "🤖 Supervised ML": "app2.py"
}

# Dropdown to select the app
choice = st.selectbox("Pick a Streamlit App to Run:", list(apps.keys()))

# Button to launch
if st.button("🚀 Launch Selected App"):
    app_to_run = apps[choice]

    full_path = os.path.join(os.path.dirname(__file__), app_to_run)

    if os.path.exists(full_path):
        st.success(f"Launching **{app_to_run}**...")

        # Launch it in a separate process
        subprocess.Popen(
            ["streamlit", "run", full_path],
            shell=sys.platform.startswith("win"),
        )
        st.markdown("✅ You can close this tab. The app is opening in a new tab or terminal.")
    else:
        st.error(f"❌ File not found: {app_to_run}")
