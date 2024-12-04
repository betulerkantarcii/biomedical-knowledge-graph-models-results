import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Biomedical Knowledge Graph Models Results Viewer", page_icon="📂")
st.title("📂 Biomedical Knowledge Graph Models Results Viewer")

# Define the mapping of dropdown selections to corresponding CSV files
# File names follow the pattern: {negative_sampling}_{model}_{frequency1}_{frequency2}.csv
csv_file_mapping = {
('Basic', 'TransD', 50, 50, 'repoDB Unapproved'): "data/basic_TransD_50_50_unapproved.csv",
('Basic', 'TransD', 50, 100, 'repoDB Unapproved'): "data/basic_TransD_50_100_unapproved.csv",
('Basic', 'TransD', 50, 200, 'repoDB Unapproved'): "data/basic_TransD_50_200_unapproved.csv",
('Basic', 'TransD', 75, 50, 'repoDB Unapproved'): "data/basic_TransD_75_50_unapproved.csv",
('Basic', 'TransD', 75, 100, 'repoDB Unapproved'): "data/basic_TransD_75_100_unapproved.csv",
('Basic', 'TransD', 75, 200, 'repoDB Unapproved'): "data/basic_TransD_75_200_unapproved.csv",
('Basic', 'TransD', 100, 50, 'repoDB Unapproved'): "data/basic_TransD_100_50_unapproved.csv",
('Basic', 'TransD', 100, 100, 'repoDB Unapproved'): "data/basic_TransD_100_100_unapproved.csv",
('Basic', 'TransD', 100, 200, 'repoDB Unapproved'): "data/basic_TransD_100_200_unapproved.csv",
('Basic', 'TransE', 50, 50, 'repoDB Unapproved'): "data/basic_TransE_50_50_unapproved.csv",
('Basic', 'TransE', 50, 100, 'repoDB Unapproved'): "data/basic_TransE_50_100_unapproved.csv",
('Basic', 'TransE', 50, 200, 'repoDB Unapproved'): "data/basic_TransE_50_200_unapproved.csv",
('Basic', 'TransE', 75, 50, 'repoDB Unapproved'): "data/basic_TransE_75_50_unapproved.csv",
('Basic', 'TransE', 75, 100, 'repoDB Unapproved'): "data/basic_TransE_75_100_unapproved.csv",
('Basic', 'TransE', 75, 200, 'repoDB Unapproved'): "data/basic_TransE_75_200_unapproved.csv",
('Basic', 'TransE', 100, 50, 'repoDB Unapproved'): "data/basic_TransE_100_50_unapproved.csv",
('Basic', 'TransE', 100, 100, 'repoDB Unapproved'): "data/basic_TransE_100_100_unapproved.csv",
('Basic', 'TransE', 100, 200, 'repoDB Unapproved'): "data/basic_TransE_100_200_unapproved.csv",
('Basic', 'TransF', 50, 50, 'repoDB Unapproved'): "data/basic_TransF_50_50_unapproved.csv",
('Basic', 'TransF', 50, 100, 'repoDB Unapproved'): "data/basic_TransF_50_100_unapproved.csv",
('Basic', 'TransF', 50, 200, 'repoDB Unapproved'): "data/basic_TransF_50_200_unapproved.csv",
('Basic', 'TransF', 75, 50, 'repoDB Unapproved'): "data/basic_TransF_75_50_unapproved.csv",
('Basic', 'TransF', 75, 100, 'repoDB Unapproved'): "data/basic_TransF_75_100_unapproved.csv",
('Basic', 'TransF', 75, 200, 'repoDB Unapproved'): "data/basic_TransF_75_200_unapproved.csv",
('Basic', 'TransF', 100, 50, 'repoDB Unapproved'): "data/basic_TransF_100_50_unapproved.csv",
('Basic', 'TransF', 100, 100, 'repoDB Unapproved'): "data/basic_TransF_100_100_unapproved.csv",
('Basic', 'TransF', 100, 200, 'repoDB Unapproved'): "data/basic_TransF_100_200_unapproved.csv",
('Basic', 'TransH', 50, 50, 'repoDB Unapproved'): "data/basic_TransH_50_50_unapproved.csv",
('Basic', 'TransH', 50, 100, 'repoDB Unapproved'): "data/basic_TransH_50_100_unapproved.csv",
('Basic', 'TransH', 50, 200, 'repoDB Unapproved'): "data/basic_TransH_50_200_unapproved.csv",
('Basic', 'TransH', 75, 50, 'repoDB Unapproved'): "data/basic_TransH_75_50_unapproved.csv",
('Basic', 'TransH', 75, 100, 'repoDB Unapproved'): "data/basic_TransH_75_100_unapproved.csv",
('Basic', 'TransH', 75, 200, 'repoDB Unapproved'): "data/basic_TransH_75_200_unapproved.csv",
('Basic', 'TransH', 100, 50, 'repoDB Unapproved'): "data/basic_TransH_100_50_unapproved.csv",
('Basic', 'TransH', 100, 100, 'repoDB Unapproved'): "data/basic_TransH_100_100_unapproved.csv",
('Basic', 'TransH', 100, 200, 'repoDB Unapproved'): "data/basic_TransH_100_200_unapproved.csv",
('Basic', 'TransR', 50, 50, 'repoDB Unapproved'): "data/basic_TransR_50_50_unapproved.csv",
('Basic', 'TransR', 50, 100, 'repoDB Unapproved'): "data/basic_TransR_50_100_unapproved.csv",
('Basic', 'TransR', 50, 200, 'repoDB Unapproved'): "data/basic_TransR_50_200_unapproved.csv",
('Basic', 'TransR', 75, 50, 'repoDB Unapproved'): "data/basic_TransR_75_50_unapproved.csv",
('Basic', 'TransR', 75, 100, 'repoDB Unapproved'): "data/basic_TransR_75_100_unapproved.csv",
('Basic', 'TransR', 75, 200, 'repoDB Unapproved'): "data/basic_TransR_75_200_unapproved.csv",
('Basic', 'TransR', 100, 50, 'repoDB Unapproved'): "data/basic_TransR_100_50_unapproved.csv",
('Basic', 'TransR', 100, 100, 'repoDB Unapproved'): "data/basic_TransR_100_100_unapproved.csv",
('Basic', 'TransR', 100, 200, 'repoDB Unapproved'): "data/basic_TransR_100_200_unapproved.csv",
('Basic', 'ProjE', 50, 50, 'repoDB Unapproved'): "data/basic_ProjE_50_50_unapproved.csv",
('Basic', 'ProjE', 50, 100, 'repoDB Unapproved'): "data/basic_ProjE_50_100_unapproved.csv",
('Basic', 'ProjE', 50, 200, 'repoDB Unapproved'): "data/basic_ProjE_50_200_unapproved.csv",
('Basic', 'ProjE', 75, 50, 'repoDB Unapproved'): "data/basic_ProjE_75_50_unapproved.csv",
('Basic', 'ProjE', 75, 100, 'repoDB Unapproved'): "data/basic_ProjE_75_100_unapproved.csv",
('Basic', 'ProjE', 75, 200, 'repoDB Unapproved'): "data/basic_ProjE_75_200_unapproved.csv",
('Basic', 'ProjE', 100, 50, 'repoDB Unapproved'): "data/basic_ProjE_100_50_unapproved.csv",
('Basic', 'ProjE', 100, 100, 'repoDB Unapproved'): "data/basic_ProjE_100_100_unapproved.csv",
('Basic', 'ProjE', 100, 200, 'repoDB Unapproved'): "data/basic_ProjE_100_200_unapproved.csv",
('Basic', 'Rescal', 50, 50, 'repoDB Unapproved'): "data/basic_Rescal_50_50_unapproved.csv",
('Basic', 'Rescal', 50, 100, 'repoDB Unapproved'): "data/basic_Rescal_50_100_unapproved.csv",
('Basic', 'Rescal', 50, 200, 'repoDB Unapproved'): "data/basic_Rescal_50_200_unapproved.csv",
('Basic', 'Rescal', 75, 50, 'repoDB Unapproved'): "data/basic_Rescal_75_50_unapproved.csv",
('Basic', 'Rescal', 75, 100, 'repoDB Unapproved'): "data/basic_Rescal_75_100_unapproved.csv",
('Basic', 'Rescal', 75, 200, 'repoDB Unapproved'): "data/basic_Rescal_75_200_unapproved.csv",
('Basic', 'Rescal', 100, 50, 'repoDB Unapproved'): "data/basic_Rescal_100_50_unapproved.csv",
('Basic', 'Rescal', 100, 100, 'repoDB Unapproved'): "data/basic_Rescal_100_100_unapproved.csv",
('Basic', 'Rescal', 100, 200, 'repoDB Unapproved'): "data/basic_Rescal_100_200_unapproved.csv",
('Custom', 'TransD', 50, 50, 'repoDB Unapproved'): "data/custom_TransD_50_50_unapproved.csv",
('Custom', 'TransD', 50, 100, 'repoDB Unapproved'): "data/custom_TransD_50_100_unapproved.csv",
('Custom', 'TransD', 50, 200, 'repoDB Unapproved'): "data/custom_TransD_50_200_unapproved.csv",
('Custom', 'TransD', 75, 50, 'repoDB Unapproved'): "data/custom_TransD_75_50_unapproved.csv",
('Custom', 'TransD', 75, 100, 'repoDB Unapproved'): "data/custom_TransD_75_100_unapproved.csv",
('Custom', 'TransD', 75, 200, 'repoDB Unapproved'): "data/custom_TransD_75_200_unapproved.csv",
('Custom', 'TransD', 100, 50, 'repoDB Unapproved'): "data/custom_TransD_100_50_unapproved.csv",
('Custom', 'TransD', 100, 100, 'repoDB Unapproved'): "data/custom_TransD_100_100_unapproved.csv",
('Custom', 'TransD', 100, 200, 'repoDB Unapproved'): "data/custom_TransD_100_200_unapproved.csv",
('Custom', 'TransE', 50, 50, 'repoDB Unapproved'): "data/custom_TransE_50_50_unapproved.csv",
('Custom', 'TransE', 50, 100, 'repoDB Unapproved'): "data/custom_TransE_50_100_unapproved.csv",
('Custom', 'TransE', 50, 200, 'repoDB Unapproved'): "data/custom_TransE_50_200_unapproved.csv",
('Custom', 'TransE', 75, 50, 'repoDB Unapproved'): "data/custom_TransE_75_50_unapproved.csv",
('Custom', 'TransE', 75, 100, 'repoDB Unapproved'): "data/custom_TransE_75_100_unapproved.csv",
('Custom', 'TransE', 75, 200, 'repoDB Unapproved'): "data/custom_TransE_75_200_unapproved.csv",
('Custom', 'TransE', 100, 50, 'repoDB Unapproved'): "data/custom_TransE_100_50_unapproved.csv",
('Custom', 'TransE', 100, 100, 'repoDB Unapproved'): "data/custom_TransE_100_100_unapproved.csv",
('Custom', 'TransE', 100, 200, 'repoDB Unapproved'): "data/custom_TransE_100_200_unapproved.csv",
('Custom', 'TransF', 50, 50, 'repoDB Unapproved'): "data/custom_TransF_50_50_unapproved.csv",
('Custom', 'TransF', 50, 100, 'repoDB Unapproved'): "data/custom_TransF_50_100_unapproved.csv",
('Custom', 'TransF', 50, 200, 'repoDB Unapproved'): "data/custom_TransF_50_200_unapproved.csv",
('Custom', 'TransF', 75, 50, 'repoDB Unapproved'): "data/custom_TransF_75_50_unapproved.csv",
('Custom', 'TransF', 75, 100, 'repoDB Unapproved'): "data/custom_TransF_75_100_unapproved.csv",
('Custom', 'TransF', 75, 200, 'repoDB Unapproved'): "data/custom_TransF_75_200_unapproved.csv",
('Custom', 'TransF', 100, 50, 'repoDB Unapproved'): "data/custom_TransF_100_50_unapproved.csv",
('Custom', 'TransF', 100, 100, 'repoDB Unapproved'): "data/custom_TransF_100_100_unapproved.csv",
('Custom', 'TransF', 100, 200, 'repoDB Unapproved'): "data/custom_TransF_100_200_unapproved.csv",
('Custom', 'TransH', 50, 50, 'repoDB Unapproved'): "data/custom_TransH_50_50_unapproved.csv",
('Custom', 'TransH', 50, 100, 'repoDB Unapproved'): "data/custom_TransH_50_100_unapproved.csv",
('Custom', 'TransH', 50, 200, 'repoDB Unapproved'): "data/custom_TransH_50_200_unapproved.csv",
('Custom', 'TransH', 75, 50, 'repoDB Unapproved'): "data/custom_TransH_75_50_unapproved.csv",
('Custom', 'TransH', 75, 100, 'repoDB Unapproved'): "data/custom_TransH_75_100_unapproved.csv",
('Custom', 'TransH', 75, 200, 'repoDB Unapproved'): "data/custom_TransH_75_200_unapproved.csv",
('Custom', 'TransH', 100, 50, 'repoDB Unapproved'): "data/custom_TransH_100_50_unapproved.csv",
('Custom', 'TransH', 100, 100, 'repoDB Unapproved'): "data/custom_TransH_100_100_unapproved.csv",
('Custom', 'TransH', 100, 200, 'repoDB Unapproved'): "data/custom_TransH_100_200_unapproved.csv",
('Custom', 'TransR', 50, 50, 'repoDB Unapproved'): "data/custom_TransR_50_50_unapproved.csv",
('Custom', 'TransR', 50, 100, 'repoDB Unapproved'): "data/custom_TransR_50_100_unapproved.csv",
('Custom', 'TransR', 50, 200, 'repoDB Unapproved'): "data/custom_TransR_50_200_unapproved.csv",
('Custom', 'TransR', 75, 50, 'repoDB Unapproved'): "data/custom_TransR_75_50_unapproved.csv",
('Custom', 'TransR', 75, 100, 'repoDB Unapproved'): "data/custom_TransR_75_100_unapproved.csv",
('Custom', 'TransR', 75, 200, 'repoDB Unapproved'): "data/custom_TransR_75_200_unapproved.csv",
('Custom', 'TransR', 100, 50, 'repoDB Unapproved'): "data/custom_TransR_100_50_unapproved.csv",
('Custom', 'TransR', 100, 100, 'repoDB Unapproved'): "data/custom_TransR_100_100_unapproved.csv",
('Custom', 'TransR', 100, 200, 'repoDB Unapproved'): "data/custom_TransR_100_200_unapproved.csv",
('Custom', 'ProjE', 50, 50, 'repoDB Unapproved'): "data/custom_ProjE_50_50_unapproved.csv",
('Custom', 'ProjE', 50, 100, 'repoDB Unapproved'): "data/custom_ProjE_50_100_unapproved.csv",
('Custom', 'ProjE', 50, 200, 'repoDB Unapproved'): "data/custom_ProjE_50_200_unapproved.csv",
('Custom', 'ProjE', 75, 50, 'repoDB Unapproved'): "data/custom_ProjE_75_50_unapproved.csv",
('Custom', 'ProjE', 75, 100, 'repoDB Unapproved'): "data/custom_ProjE_75_100_unapproved.csv",
('Custom', 'ProjE', 75, 200, 'repoDB Unapproved'): "data/custom_ProjE_75_200_unapproved.csv",
('Custom', 'ProjE', 100, 50, 'repoDB Unapproved'): "data/custom_ProjE_100_50_unapproved.csv",
('Custom', 'ProjE', 100, 100, 'repoDB Unapproved'): "data/custom_ProjE_100_100_unapproved.csv",
('Custom', 'ProjE', 100, 200, 'repoDB Unapproved'): "data/custom_ProjE_100_200_unapproved.csv",
('Custom', 'Rescal', 50, 50, 'repoDB Unapproved'): "data/custom_Rescal_50_50_unapproved.csv",
('Custom', 'Rescal', 50, 100, 'repoDB Unapproved'): "data/custom_Rescal_50_100_unapproved.csv",
('Custom', 'Rescal', 50, 200, 'repoDB Unapproved'): "data/custom_Rescal_50_200_unapproved.csv",
('Custom', 'Rescal', 75, 50, 'repoDB Unapproved'): "data/custom_Rescal_75_50_unapproved.csv",
('Custom', 'Rescal', 75, 100, 'repoDB Unapproved'): "data/custom_Rescal_75_100_unapproved.csv",
('Custom', 'Rescal', 75, 200, 'repoDB Unapproved'): "data/custom_Rescal_75_200_unapproved.csv",
('Custom', 'Rescal', 100, 50, 'repoDB Unapproved'): "data/custom_Rescal_100_50_unapproved.csv",
('Custom', 'Rescal', 100, 100, 'repoDB Unapproved'): "data/custom_Rescal_100_100_unapproved.csv",
('Custom', 'Rescal', 100, 200, 'repoDB Unapproved'): "data/custom_Rescal_100_200_unapproved.csv",
('Basic', 'TransD', 50, 50, 'Synthetic'): "data/basic_TransD_50_50_synthetic.csv",
('Basic', 'TransD', 50, 100, 'Synthetic'): "data/basic_TransD_50_100_synthetic.csv",
('Basic', 'TransD', 50, 200, 'Synthetic'): "data/basic_TransD_50_200_synthetic.csv",
('Basic', 'TransD', 75, 50, 'Synthetic'): "data/basic_TransD_75_50_synthetic.csv",
('Basic', 'TransD', 75, 100, 'Synthetic'): "data/basic_TransD_75_100_synthetic.csv",
('Basic', 'TransD', 75, 200, 'Synthetic'): "data/basic_TransD_75_200_synthetic.csv",
('Basic', 'TransD', 100, 50, 'Synthetic'): "data/basic_TransD_100_50_synthetic.csv",
('Basic', 'TransD', 100, 100, 'Synthetic'): "data/basic_TransD_100_100_synthetic.csv",
('Basic', 'TransD', 100, 200, 'Synthetic'): "data/basic_TransD_100_200_synthetic.csv",
('Basic', 'TransE', 50, 50, 'Synthetic'): "data/basic_TransE_50_50_synthetic.csv",
('Basic', 'TransE', 50, 100, 'Synthetic'): "data/basic_TransE_50_100_synthetic.csv",
('Basic', 'TransE', 50, 200, 'Synthetic'): "data/basic_TransE_50_200_synthetic.csv",
('Basic', 'TransE', 75, 50, 'Synthetic'): "data/basic_TransE_75_50_synthetic.csv",
('Basic', 'TransE', 75, 100, 'Synthetic'): "data/basic_TransE_75_100_synthetic.csv",
('Basic', 'TransE', 75, 200, 'Synthetic'): "data/basic_TransE_75_200_synthetic.csv",
('Basic', 'TransE', 100, 50, 'Synthetic'): "data/basic_TransE_100_50_synthetic.csv",
('Basic', 'TransE', 100, 100, 'Synthetic'): "data/basic_TransE_100_100_synthetic.csv",
('Basic', 'TransE', 100, 200, 'Synthetic'): "data/basic_TransE_100_200_synthetic.csv",
('Basic', 'TransF', 50, 50, 'Synthetic'): "data/basic_TransF_50_50_synthetic.csv",
('Basic', 'TransF', 50, 100, 'Synthetic'): "data/basic_TransF_50_100_synthetic.csv",
('Basic', 'TransF', 50, 200, 'Synthetic'): "data/basic_TransF_50_200_synthetic.csv",
('Basic', 'TransF', 75, 50, 'Synthetic'): "data/basic_TransF_75_50_synthetic.csv",
('Basic', 'TransF', 75, 100, 'Synthetic'): "data/basic_TransF_75_100_synthetic.csv",
('Basic', 'TransF', 75, 200, 'Synthetic'): "data/basic_TransF_75_200_synthetic.csv",
('Basic', 'TransF', 100, 50, 'Synthetic'): "data/basic_TransF_100_50_synthetic.csv",
('Basic', 'TransF', 100, 100, 'Synthetic'): "data/basic_TransF_100_100_synthetic.csv",
('Basic', 'TransF', 100, 200, 'Synthetic'): "data/basic_TransF_100_200_synthetic.csv",
('Basic', 'TransH', 50, 50, 'Synthetic'): "data/basic_TransH_50_50_synthetic.csv",
('Basic', 'TransH', 50, 100, 'Synthetic'): "data/basic_TransH_50_100_synthetic.csv",
('Basic', 'TransH', 50, 200, 'Synthetic'): "data/basic_TransH_50_200_synthetic.csv",
('Basic', 'TransH', 75, 50, 'Synthetic'): "data/basic_TransH_75_50_synthetic.csv",
('Basic', 'TransH', 75, 100, 'Synthetic'): "data/basic_TransH_75_100_synthetic.csv",
('Basic', 'TransH', 75, 200, 'Synthetic'): "data/basic_TransH_75_200_synthetic.csv",
('Basic', 'TransH', 100, 50, 'Synthetic'): "data/basic_TransH_100_50_synthetic.csv",
('Basic', 'TransH', 100, 100, 'Synthetic'): "data/basic_TransH_100_100_synthetic.csv",
('Basic', 'TransH', 100, 200, 'Synthetic'): "data/basic_TransH_100_200_synthetic.csv",
('Basic', 'TransR', 50, 50, 'Synthetic'): "data/basic_TransR_50_50_synthetic.csv",
('Basic', 'TransR', 50, 100, 'Synthetic'): "data/basic_TransR_50_100_synthetic.csv",
('Basic', 'TransR', 50, 200, 'Synthetic'): "data/basic_TransR_50_200_synthetic.csv",
('Basic', 'TransR', 75, 50, 'Synthetic'): "data/basic_TransR_75_50_synthetic.csv",
('Basic', 'TransR', 75, 100, 'Synthetic'): "data/basic_TransR_75_100_synthetic.csv",
('Basic', 'TransR', 75, 200, 'Synthetic'): "data/basic_TransR_75_200_synthetic.csv",
('Basic', 'TransR', 100, 50, 'Synthetic'): "data/basic_TransR_100_50_synthetic.csv",
('Basic', 'TransR', 100, 100, 'Synthetic'): "data/basic_TransR_100_100_synthetic.csv",
('Basic', 'TransR', 100, 200, 'Synthetic'): "data/basic_TransR_100_200_synthetic.csv",
('Basic', 'ProjE', 50, 50, 'Synthetic'): "data/basic_ProjE_50_50_synthetic.csv",
('Basic', 'ProjE', 50, 100, 'Synthetic'): "data/basic_ProjE_50_100_synthetic.csv",
('Basic', 'ProjE', 50, 200, 'Synthetic'): "data/basic_ProjE_50_200_synthetic.csv",
('Basic', 'ProjE', 75, 50, 'Synthetic'): "data/basic_ProjE_75_50_synthetic.csv",
('Basic', 'ProjE', 75, 100, 'Synthetic'): "data/basic_ProjE_75_100_synthetic.csv",
('Basic', 'ProjE', 75, 200, 'Synthetic'): "data/basic_ProjE_75_200_synthetic.csv",
('Basic', 'ProjE', 100, 50, 'Synthetic'): "data/basic_ProjE_100_50_synthetic.csv",
('Basic', 'ProjE', 100, 100, 'Synthetic'): "data/basic_ProjE_100_100_synthetic.csv",
('Basic', 'ProjE', 100, 200, 'Synthetic'): "data/basic_ProjE_100_200_synthetic.csv",
('Basic', 'Rescal', 50, 50, 'Synthetic'): "data/basic_Rescal_50_50_synthetic.csv",
('Basic', 'Rescal', 50, 100, 'Synthetic'): "data/basic_Rescal_50_100_synthetic.csv",
('Basic', 'Rescal', 50, 200, 'Synthetic'): "data/basic_Rescal_50_200_synthetic.csv",
('Basic', 'Rescal', 75, 50, 'Synthetic'): "data/basic_Rescal_75_50_synthetic.csv",
('Basic', 'Rescal', 75, 100, 'Synthetic'): "data/basic_Rescal_75_100_synthetic.csv",
('Basic', 'Rescal', 75, 200, 'Synthetic'): "data/basic_Rescal_75_200_synthetic.csv",
('Basic', 'Rescal', 100, 50, 'Synthetic'): "data/basic_Rescal_100_50_synthetic.csv",
('Basic', 'Rescal', 100, 100, 'Synthetic'): "data/basic_Rescal_100_100_synthetic.csv",
('Basic', 'Rescal', 100, 200, 'Synthetic'): "data/basic_Rescal_100_200_synthetic.csv",
('Custom', 'TransD', 50, 50, 'Synthetic'): "data/custom_TransD_50_50_synthetic.csv",
('Custom', 'TransD', 50, 100, 'Synthetic'): "data/custom_TransD_50_100_synthetic.csv",
('Custom', 'TransD', 50, 200, 'Synthetic'): "data/custom_TransD_50_200_synthetic.csv",
('Custom', 'TransD', 75, 50, 'Synthetic'): "data/custom_TransD_75_50_synthetic.csv",
('Custom', 'TransD', 75, 100, 'Synthetic'): "data/custom_TransD_75_100_synthetic.csv",
('Custom', 'TransD', 75, 200, 'Synthetic'): "data/custom_TransD_75_200_synthetic.csv",
('Custom', 'TransD', 100, 50, 'Synthetic'): "data/custom_TransD_100_50_synthetic.csv",
('Custom', 'TransD', 100, 100, 'Synthetic'): "data/custom_TransD_100_100_synthetic.csv",
('Custom', 'TransD', 100, 200, 'Synthetic'): "data/custom_TransD_100_200_synthetic.csv",
('Custom', 'TransE', 50, 50, 'Synthetic'): "data/custom_TransE_50_50_synthetic.csv",
('Custom', 'TransE', 50, 100, 'Synthetic'): "data/custom_TransE_50_100_synthetic.csv",
('Custom', 'TransE', 50, 200, 'Synthetic'): "data/custom_TransE_50_200_synthetic.csv",
('Custom', 'TransE', 75, 50, 'Synthetic'): "data/custom_TransE_75_50_synthetic.csv",
('Custom', 'TransE', 75, 100, 'Synthetic'): "data/custom_TransE_75_100_synthetic.csv",
('Custom', 'TransE', 75, 200, 'Synthetic'): "data/custom_TransE_75_200_synthetic.csv",
('Custom', 'TransE', 100, 50, 'Synthetic'): "data/custom_TransE_100_50_synthetic.csv",
('Custom', 'TransE', 100, 100, 'Synthetic'): "data/custom_TransE_100_100_synthetic.csv",
('Custom', 'TransE', 100, 200, 'Synthetic'): "data/custom_TransE_100_200_synthetic.csv",
('Custom', 'TransF', 50, 50, 'Synthetic'): "data/custom_TransF_50_50_synthetic.csv",
('Custom', 'TransF', 50, 100, 'Synthetic'): "data/custom_TransF_50_100_synthetic.csv",
('Custom', 'TransF', 50, 200, 'Synthetic'): "data/custom_TransF_50_200_synthetic.csv",
('Custom', 'TransF', 75, 50, 'Synthetic'): "data/custom_TransF_75_50_synthetic.csv",
('Custom', 'TransF', 75, 100, 'Synthetic'): "data/custom_TransF_75_100_synthetic.csv",
('Custom', 'TransF', 75, 200, 'Synthetic'): "data/custom_TransF_75_200_synthetic.csv",
('Custom', 'TransF', 100, 50, 'Synthetic'): "data/custom_TransF_100_50_synthetic.csv",
('Custom', 'TransF', 100, 100, 'Synthetic'): "data/custom_TransF_100_100_synthetic.csv",
('Custom', 'TransF', 100, 200, 'Synthetic'): "data/custom_TransF_100_200_synthetic.csv",
('Custom', 'TransH', 50, 50, 'Synthetic'): "data/custom_TransH_50_50_synthetic.csv",
('Custom', 'TransH', 50, 100, 'Synthetic'): "data/custom_TransH_50_100_synthetic.csv",
('Custom', 'TransH', 50, 200, 'Synthetic'): "data/custom_TransH_50_200_synthetic.csv",
('Custom', 'TransH', 75, 50, 'Synthetic'): "data/custom_TransH_75_50_synthetic.csv",
('Custom', 'TransH', 75, 100, 'Synthetic'): "data/custom_TransH_75_100_synthetic.csv",
('Custom', 'TransH', 75, 200, 'Synthetic'): "data/custom_TransH_75_200_synthetic.csv",
('Custom', 'TransH', 100, 50, 'Synthetic'): "data/custom_TransH_100_50_synthetic.csv",
('Custom', 'TransH', 100, 100, 'Synthetic'): "data/custom_TransH_100_100_synthetic.csv",
('Custom', 'TransH', 100, 200, 'Synthetic'): "data/custom_TransH_100_200_synthetic.csv",
('Custom', 'TransR', 50, 50, 'Synthetic'): "data/custom_TransR_50_50_synthetic.csv",
('Custom', 'TransR', 50, 100, 'Synthetic'): "data/custom_TransR_50_100_synthetic.csv",
('Custom', 'TransR', 50, 200, 'Synthetic'): "data/custom_TransR_50_200_synthetic.csv",
('Custom', 'TransR', 75, 50, 'Synthetic'): "data/custom_TransR_75_50_synthetic.csv",
('Custom', 'TransR', 75, 100, 'Synthetic'): "data/custom_TransR_75_100_synthetic.csv",
('Custom', 'TransR', 75, 200, 'Synthetic'): "data/custom_TransR_75_200_synthetic.csv",
('Custom', 'TransR', 100, 50, 'Synthetic'): "data/custom_TransR_100_50_synthetic.csv",
('Custom', 'TransR', 100, 100, 'Synthetic'): "data/custom_TransR_100_100_synthetic.csv",
('Custom', 'TransR', 100, 200, 'Synthetic'): "data/custom_TransR_100_200_synthetic.csv",
('Custom', 'ProjE', 50, 50, 'Synthetic'): "data/custom_ProjE_50_50_synthetic.csv",
('Custom', 'ProjE', 50, 100, 'Synthetic'): "data/custom_ProjE_50_100_synthetic.csv",
('Custom', 'ProjE', 50, 200, 'Synthetic'): "data/custom_ProjE_50_200_synthetic.csv",
('Custom', 'ProjE', 75, 50, 'Synthetic'): "data/custom_ProjE_75_50_synthetic.csv",
('Custom', 'ProjE', 75, 100, 'Synthetic'): "data/custom_ProjE_75_100_synthetic.csv",
('Custom', 'ProjE', 75, 200, 'Synthetic'): "data/custom_ProjE_75_200_synthetic.csv",
('Custom', 'ProjE', 100, 50, 'Synthetic'): "data/custom_ProjE_100_50_synthetic.csv",
('Custom', 'ProjE', 100, 100, 'Synthetic'): "data/custom_ProjE_100_100_synthetic.csv",
('Custom', 'ProjE', 100, 200, 'Synthetic'): "data/custom_ProjE_100_200_synthetic.csv",
('Custom', 'Rescal', 50, 50, 'Synthetic'): "data/custom_Rescal_50_50_synthetic.csv",
('Custom', 'Rescal', 50, 100, 'Synthetic'): "data/custom_Rescal_50_100_synthetic.csv",
('Custom', 'Rescal', 50, 200, 'Synthetic'): "data/custom_Rescal_50_200_synthetic.csv",
('Custom', 'Rescal', 75, 50, 'Synthetic'): "data/custom_Rescal_75_50_synthetic.csv",
('Custom', 'Rescal', 75, 100, 'Synthetic'): "data/custom_Rescal_75_100_synthetic.csv",
('Custom', 'Rescal', 75, 200, 'Synthetic'): "data/custom_Rescal_75_200_synthetic.csv",
('Custom', 'Rescal', 100, 50, 'Synthetic'): "data/custom_Rescal_100_50_synthetic.csv",
('Custom', 'Rescal', 100, 100, 'Synthetic'): "data/custom_Rescal_100_100_synthetic.csv",
('Custom', 'Rescal', 100, 200, 'Synthetic'): "data/custom_Rescal_100_200_synthetic.csv",
}

# Dropdowns for filtering

model_name = st.selectbox(
    "Select Model Name:",
    ["TransD", "TransE", "TransF", "TransH", "TransR", "ProjE", "Rescal"],
    help="Choose the model name"
)

test_dataset = st.selectbox(
    "Select Test Dataset:",
    ["Synthetic", "repoDB Unapproved"],
    help="Choose the test dataset type"
)

frequency = st.selectbox(
    "Select Frequency:",
    [50, 75, 100],
    help="Choose the frequency filter for positive dataset"
)

negative_sampling = st.selectbox(
    "Select Negative Sampling:",
    ["Basic", "Custom"],
    help="Choose the negative sampling type"
)

embedding = st.selectbox(
    "Select Embedding:",
    [100, 50, 200],
    help="Choose the embedding filter"
)



# Check if the combination exists in the mapping
selection_key = (negative_sampling, model_name, frequency, embedding, test_dataset)

if selection_key in csv_file_mapping:
    # Load the corresponding CSV file
    file_path = csv_file_mapping[selection_key]
    try:
        df = pd.read_csv(file_path)
        st.write(f"### Data from `{file_path}`:")
        st.dataframe(df, use_container_width=True)
        
        # Filter specific columns and show in another table
        desired_columns = st.multiselect("Select Columns to Display in a Separate Table", df.columns)
        if desired_columns:
            filtered_df = df[desired_columns]
            st.write("### Filtered Data Table")
            st.dataframe(filtered_df, use_container_width=True)

        # Show the top 5 "SUBJECT_NAME"-"OBJECT_NAME" combinations
        if "SUBJECT_NAME" in df.columns and "OBJECT_NAME" in df.columns:
            top_combinations = (
                df.head(10)
                .groupby(["SUBJECT_NAME", "OBJECT_NAME"])
                .size()
                .reset_index(name="count")
                .sort_values(by="count", ascending=False)
                .head(5)
            )
            st.write("### Graph")
            # Collect relevant files based on `test_dataset`
            # Select files for table display based on negative_sampling
            table_keys = [
                key for key in csv_file_mapping if key[0] == negative_sampling and key[4] == test_dataset
            ]
            table_files = [csv_file_mapping[key] for key in table_keys]

            # Process the selected files for table display
            table_data = []
            for file in table_files:
                try:
                    temp_df = pd.read_csv(file)
                    table_data.append(temp_df)
                except FileNotFoundError:
                    st.warning(f"File `{file}` not found. Skipping...")

            # Add dropdown for graph creation
            graph_choice = st.selectbox(
                "Select Graph Type for Analysis:",
                ["Basic", "Custom", "Both"],
                index=["Basic", "Custom"].index(negative_sampling),  # Default to match negative_sampling
                help="Choose the data type for graph analysis"
            )

            # Select files for graph display based on graph_choice
            if graph_choice == "Both":
                graph_keys = [
                    key for key in csv_file_mapping if  key[4] == test_dataset
                ]
            else:
                graph_keys = [
                    key for key in csv_file_mapping if key[0] == graph_choice and key[4] == test_dataset
                ]
            graph_files = [csv_file_mapping[key] for key in graph_keys]

            # Process the selected files for graph display
            graph_data = []
            for file in graph_files:
                try:
                    temp_df = pd.read_csv(file)
                    # Sort by Model Score and select top 10 rows
                    if "Model Score" in temp_df.columns:
                        top_10 = temp_df.head(10)
                        graph_data.append(top_10)
                except FileNotFoundError:
                    st.warning(f"File `{file}` not found. Skipping...")

            if graph_data:
                combined_graph_df = pd.concat(graph_data, ignore_index=True)

                # Group by SUBJECT_NAME and OBJECT_NAME
                if "SUBJECT_NAME" in combined_graph_df.columns and "OBJECT_NAME" in combined_graph_df.columns:
                    top_common = (
                        combined_graph_df
                        .groupby(["SUBJECT_NAME", "OBJECT_NAME"])
                        .size()
                        .reset_index(name="count")
                        .sort_values(by="count", ascending=False)
                        .head(5)
                    )

                    st.write(f"### Top 5 Common Relationships Among Top 10 Ranked Results ('{graph_choice}' Negative Sampling, '{test_dataset}')")
                    st.dataframe(top_common)

                    # Prepare data for the bar chart
                    top_common["Combination"] = top_common["SUBJECT_NAME"] + " - " + top_common["OBJECT_NAME"]
                    chart_data = top_common[["Combination", "count"]].set_index("Combination")

                    # Plot the bar chart using Streamlit
                    st.bar_chart(chart_data, use_container_width=True)
                else:
                    st.warning("The required columns ('SUBJECT_NAME', 'OBJECT_NAME') are missing in the files.")
            
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
    st.warning(f"No CSV file matches the selected combination '{selection_key}'. Please check your selections.")
