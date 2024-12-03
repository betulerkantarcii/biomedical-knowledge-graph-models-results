# 📂 **Biomedical Knowledge Graph Models Result Viewer**

A Streamlit-based web application for visualizing and analyzing results from Biomedical Knowledge Graph models. The app dynamically loads specific CSV files based on user-selected criteria and provides an interactive interface for filtering and downloading model results.

---

## **Features**
- **Dynamic Model Results Viewer**: Select and view results from various Knowledge Graph models.
- **Dropdown Filters**: Filter data by:
  - Negative Sampling Type
  - Model Name
  - Frequency Threshold
  - Embedding Dimension
- **Interactive Table**: Explore filtered results in a user-friendly table.
- **CSV Download**: Download the filtered data for further analysis.
- **Customizable**: Easily extend to include additional models, sampling types, frequencies, and embeddings.

---

## **Selection Criteria**
The app selects CSV files based on the following dropdown options:
1. **Negative Sampling**:
   - `basic`, `custom`, `none`
2. **Model Name**:
   - `TransD`, `TransE`, `TransF`, `TransH`, `TransR`, `ProjE`, `Rescal`
3. **Frequency Threshold**:
   - `50`, `75`, `100`
4. **Embedding Dimension**:
   - `50`, `100`, `200`

---

## **File Naming Convention**
CSV files must be named following this pattern:
```bash
{negative_sampling}_{model}_{frequency}_{embedding}.csv
