# A3 - DataAnalyzer

## Script Information

- **Author**: Jay Annadurai
- **Title**: A3 - DataAnalyzer
- **Date**: 15 Feb 2024
- **Language**: Python
- **Project Version**: 1.0
- **Description**: Performs Exploratory Data Analysis of Differential Gene Expression

## Description

"A3 - DataAnalyzer" is a Python script developed for exploratory data analysis of differential gene expression. It is designed to process data from various file formats, including Excel, CSV, and TSV, to perform tasks such as merging data sets, calculating log fold changes, and visually exploring gene expression patterns. The tool is aimed at researchers and data analysts in the field of genomics to assist in uncovering significant gene interactions and expression dynamics, particularly in the context of tumor versus normal samples.

## Requirements

### Hardware

- Standard PC or Server capable of running Python.

### Software and Libraries

- Python 3.x
- Jupyter Notebook or Jupyter Lab
- Pandas, OpenPyXL, Seaborn, NumPy, SciPy, Matplotlib
- `fastcluster` (for optimizing cluster map computations)

### Running the Script

1. **Jupyter Notebook Environment**: Ensure you have access to a Jupyter Notebook environment where Python 3.x is available. This can be through local installations like Anaconda or online platforms that provide Jupyter Notebook services.
2. **Notebook Permissions**: Verify that the Jupyter Notebook has the necessary permissions to access the directories and files on your system.
3. **Directory Permissions**: The script and input files should be in directories where the Jupyter Notebook has read/write permissions. Typically, placing them in the same directory as the notebook or in a subdirectory like `Data/` is sufficient.
4. **Input Files**: Ensure the input files (`Gene_Expression_Data.xlsx`, `Gene_Information.csv`, `Sample_Information.tsv`) are stored in the specified `Data/` directory, which should match the file paths used in the notebook. These files were provided as part of the assignment specifications.
5. **Execution**: Run the cells in the Jupyter Notebook sequentially to execute the script and observe the outputs directly within the notebook environment. There are no separate output files, as all results are displayed and saved within the Jupyter Notebook itself.
6. **Cluster Map Optimization**: `fastcluster` is used to enhance the performance of generating cluster maps, particularly for large datasets. Ensure `fastcluster` is installed in your Python environment.

## Key Functions and Usage

1. **Data Merging and Preparation**: Integrates data from multiple sources and formats.
2. **Fold Change Calculation**: Utilizes log fold change to discern significantly expressed genes.
3. **Exploratory Data Analysis (EDA)**: Employs various plotting techniques to visualize data trends and anomalies.

## Notes

- The script is adaptable for different datasets and can be extended with more functionalities as needed.
- Large datasets may require optimization of the script to improve performance and efficiency.
