import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Dynamic CSV Viewer", page_icon="📂")
st.title("📂 Dynamic CSV Viewer with Filters")

# Define the mapping of dropdown selections to corresponding CSV files
# File names follow the pattern: {negative_sampling}_{model}_{frequency1}_{frequency2}.csv
csv_file_mapping = {
    ("basic", "TransD", 50, 50): "data/basic_TransD_50_50.csv",
    ("basic", "TransE", 50, 50): "data/basic_TransE_50_50.csv",
    # Add all combinations of files in this format
    # Example:
    # ("basic", "TransF", 75, 100): "data/basic_TransF_75_100.csv",
    # ("custom", "TransH", 100, 200): "data/custom_TransH_100_200.csv",
    # ...
}

# Dropdowns for filtering
negative_sampling = st.selectbox(
    "Select Negative Sampling:",
    ["basic", "custom", "none"],
    help="Choose the negative sampling type"
)

model_name = st.selectbox(
    "Select Model Name:",
    ["TransD", "TransE", "TransF", "TransH", "TransR", "ProjE", "Rescal"],
    help="Choose the model name"
)

frequency1 = st.selectbox(
    "Select Frequency:",
    [50, 75, 100],
    help="Choose the first frequency filter"
)

frequency2 = st.selectbox(
    "Select Embedding:",
    [50, 100, 200],
    help="Choose the second frequency filter"
)

# Check if the combination exists in the mapping
selection_key = (negative_sampling, model_name, frequency1, frequency2)

if selection_key in csv_file_mapping:
    # Load the corresponding CSV file
    file_path = csv_file_mapping[selection_key]
    try:
        df = pd.read_csv(file_path)
        st.write(f"### Data from `{file_path}`:")
        st.dataframe(df, use_container_width=True)
        
        # Option to download filtered data
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download Data as CSV",
            data=csv,
            file_name=file_path.split("/")[-1],
            mime="text/csv",
        )
    except FileNotFoundError:
        st.error(f"File `{file_path}` not found. Please check the file path or upload the file.")
else:
    st.warning("No CSV file matches the selected combination. Please check your selections.")
