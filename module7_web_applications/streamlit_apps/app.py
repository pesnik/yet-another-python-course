import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import io
from datetime import datetime
import base64

# Configure page
st.set_page_config(
    page_title="CSV Data Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Excel-like styling
st.markdown("""
<style>
    .main {
        padding-top: 2rem;
    }
    
    .stDataFrame {
        border: 1px solid #e0e0e0;
    }
    
    .metric-container {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #007bff;
        margin: 0.5rem 0;
    }
    
    .excel-header {
        background: linear-gradient(90deg, #4CAF50 0%, #45a049 100%);
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        text-align: center;
        font-weight: bold;
    }
    
    .section-header {
        background-color: #f1f3f4;
        padding: 0.75rem;
        border-radius: 0.25rem;
        border-left: 3px solid #1f77b4;
        margin: 1rem 0 0.5rem 0;
        font-weight: 600;
        color: #333;
    }
    
    .filter-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #ffeaa7;
        margin: 0.5rem 0;
    }
    
    .download-button {
        background: linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 0.25rem;
        text-decoration: none;
        display: inline-block;
        margin: 0.25rem;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables"""
    if 'df' not in st.session_state:
        st.session_state.df = None
    if 'original_df' not in st.session_state:
        st.session_state.original_df = None
    if 'filtered_df' not in st.session_state:
        st.session_state.filtered_df = None
    if 'selected_columns' not in st.session_state:
        st.session_state.selected_columns = []

def load_csv_file():
    """Handle CSV file upload and loading"""
    st.markdown('<div class="excel-header">📊 Excel-like CSV Data Analyzer</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        uploaded_file = st.file_uploader(
            "Choose a CSV file",
            type=['csv'],
            help="Upload your CSV file to analyze and manipulate data"
        )
    
    with col2:
        skip_rows = st.number_input(
            "Skip rows",
            min_value=0,
            max_value=100,
            value=0,
            help="Number of rows to skip from the beginning"
        )
    
    if uploaded_file is not None:
        try:
            # Read CSV with progress
            with st.spinner("Loading CSV file..."):
                df = pd.read_csv(uploaded_file, skiprows=skip_rows)
                st.session_state.df = df
                st.session_state.original_df = df.copy()
                st.session_state.filtered_df = df.copy()
                
            st.success(f"✅ File loaded successfully! Found {len(df)} rows and {len(df.columns)} columns.")
            return True
            
        except Exception as e:
            st.error(f"❌ Error loading file: {str(e)}")
            return False
    
    return False

def display_data_overview():
    """Display data overview and basic statistics"""
    if st.session_state.df is None:
        return
        
    df = st.session_state.df
    
    st.markdown('<div class="section-header">📋 Data Overview</div>', unsafe_allow_html=True)
    
    # Basic metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric("Total Rows", f"{len(df):,}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric("Total Columns", len(df.columns))
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric("Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        missing_cells = df.isnull().sum().sum()
        st.metric("Missing Values", f"{missing_cells:,}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Data types overview
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Data Types")
        dtype_df = pd.DataFrame({
            'Column': df.columns,
            'Data Type': df.dtypes.astype(str),
            'Non-Null Count': df.count(),
            'Null Count': df.isnull().sum()
        })
        st.dataframe(dtype_df, use_container_width=True, height=300)
    
    with col2:
        st.subheader("🔢 Numeric Columns Summary")
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            st.dataframe(df[numeric_cols].describe(), use_container_width=True, height=300)
        else:
            st.info("No numeric columns found in the dataset.")

def create_data_filters():
    """Create interactive filters for data"""
    if st.session_state.df is None:
        return
        
    df = st.session_state.original_df
    
    st.markdown('<div class="section-header">🔍 Data Filters & Search</div>', unsafe_allow_html=True)
    
    with st.expander("🎛️ Filter Controls", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            # Column selection
            st.subheader("Select Columns")
            all_columns = df.columns.tolist()
            selected_columns = st.multiselect(
                "Choose columns to display",
                all_columns,
                default=all_columns[:10] if len(all_columns) > 10 else all_columns,
                help="Select which columns to show in the data table"
            )
            st.session_state.selected_columns = selected_columns if selected_columns else all_columns
        
        with col2:
            # Row filtering
            st.subheader("Filter Rows")
            max_rows = st.slider(
                "Maximum rows to display",
                min_value=10,
                max_value=min(len(df), 10000),
                value=min(1000, len(df)),
                step=10
            )
    
    # Advanced filtering
    with st.expander("🔧 Advanced Filters"):
        filter_column = st.selectbox("Filter by column", ["None"] + df.columns.tolist())
        
        if filter_column != "None":
            col_type = df[filter_column].dtype
            
            if pd.api.types.is_numeric_dtype(df[filter_column]):
                # Numeric filtering
                min_val = float(df[filter_column].min())
                max_val = float(df[filter_column].max())
                
                filter_range = st.slider(
                    f"Filter {filter_column} range",
                    min_value=min_val,
                    max_value=max_val,
                    value=(min_val, max_val)
                )
                
                mask = (df[filter_column] >= filter_range[0]) & (df[filter_column] <= filter_range[1])
                filtered_df = df[mask]
                
            else:
                # Text/Categorical filtering
                unique_values = df[filter_column].unique()
                selected_values = st.multiselect(
                    f"Select {filter_column} values",
                    unique_values,
                    default=unique_values[:10] if len(unique_values) > 10 else unique_values
                )
                
                if selected_values:
                    filtered_df = df[df[filter_column].isin(selected_values)]
                else:
                    filtered_df = df.copy()
        else:
            filtered_df = df.copy()
    
    # Apply filters
    filtered_df = filtered_df[st.session_state.selected_columns].head(max_rows)
    st.session_state.filtered_df = filtered_df
    
    # Search functionality
    search_term = st.text_input("🔎 Search in data", placeholder="Enter search term...")
    if search_term:
        mask = filtered_df.astype(str).apply(lambda x: x.str.contains(search_term, case=False, na=False)).any(axis=1)
        st.session_state.filtered_df = filtered_df[mask]

def display_excel_like_table():
    """Display data in Excel-like format"""
    if st.session_state.filtered_df is None:
        return
    
    df = st.session_state.filtered_df
    
    st.markdown('<div class="section-header">📋 Data Table (Excel-like View)</div>', unsafe_allow_html=True)
    
    # Table controls
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.info(f"Displaying {len(df)} rows × {len(df.columns)} columns")
    
    with col2:
        show_index = st.checkbox("Show row index", value=True)
    
    with col3:
        table_height = st.selectbox("Table height", [300, 400, 500, 600, 800], index=2)
    
    # Enhanced dataframe display
    try:
        # Format numeric columns for better display
        formatted_df = df.copy()
        for col in formatted_df.select_dtypes(include=[np.number]).columns:
            if formatted_df[col].dtype == 'float64':
                formatted_df[col] = formatted_df[col].round(4)
        
        # Display with styling
        st.dataframe(
            formatted_df,
            use_container_width=True,
            height=table_height,
            hide_index=not show_index
        )
        
        # Quick stats for current view
        if len(df) > 0:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Rows in view", len(df))
            with col2:
                numeric_cols = df.select_dtypes(include=[np.number]).columns
                st.metric("Numeric columns", len(numeric_cols))
            with col3:
                missing_in_view = df.isnull().sum().sum()
                st.metric("Missing values", missing_in_view)
        
    except Exception as e:
        st.error(f"Error displaying data: {str(e)}")

def create_data_actions():
    """Create data manipulation actions"""
    if st.session_state.df is None:
        return
    
    st.markdown('<div class="section-header">⚡ Data Actions</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📥 Export Data")
        
        # Download current view as CSV
        if st.session_state.filtered_df is not None:
            csv = st.session_state.filtered_df.to_csv(index=False)
            st.download_button(
                label="📄 Download Current View (CSV)",
                data=csv,
                file_name=f"filtered_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                help="Download the currently filtered data as CSV"
            )
        
        # Download full dataset
        full_csv = st.session_state.df.to_csv(index=False)
        st.download_button(
            label="📊 Download Full Dataset (CSV)",
            data=full_csv,
            file_name=f"full_dataset_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            help="Download the complete dataset as CSV"
        )
    
    with col2:
        st.subheader("🔧 Data Operations")
        
        if st.button("🔄 Reset Filters", help="Reset all filters and show original data"):
            st.session_state.filtered_df = st.session_state.original_df.copy()
            st.experimental_rerun()
        
        if st.button("📋 Copy Column Names", help="Copy all column names to clipboard"):
            columns_text = ", ".join(st.session_state.df.columns.tolist())
            st.code(columns_text)
            st.success("Column names displayed above!")
    
    with col3:
        st.subheader("📊 Quick Analysis")
        
        if st.button("📈 Generate Summary Report"):
            create_summary_report()

def create_summary_report():
    """Generate a comprehensive summary report"""
    if st.session_state.df is None:
        return
    
    df = st.session_state.df
    
    st.markdown('<div class="section-header">📊 Summary Report</div>', unsafe_allow_html=True)
    
    # Dataset overview
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Dataset Overview")
        overview_data = {
            "Metric": ["Total Rows", "Total Columns", "Memory Usage (MB)", "Complete Rows", "Duplicate Rows"],
            "Value": [
                f"{len(df):,}",
                len(df.columns),
                f"{df.memory_usage(deep=True).sum() / 1024**2:.2f}",
                f"{len(df.dropna()):,}",
                f"{df.duplicated().sum():,}"
            ]
        }
        st.table(pd.DataFrame(overview_data))
    
    with col2:
        st.subheader("Column Analysis")
        col_analysis = {
            "Data Type": df.dtypes.value_counts().to_dict(),
        }
        
        for dtype, count in col_analysis["Data Type"].items():
            st.metric(f"{dtype} columns", count)
    
    # Missing values analysis
    if df.isnull().sum().sum() > 0:
        st.subheader("Missing Values Analysis")
        missing_data = df.isnull().sum().sort_values(ascending=False)
        missing_data = missing_data[missing_data > 0]
        
        if len(missing_data) > 0:
            missing_df = pd.DataFrame({
                'Column': missing_data.index,
                'Missing Count': missing_data.values,
                'Missing Percentage': (missing_data.values / len(df) * 100).round(2)
            })
            st.dataframe(missing_df, use_container_width=True)

def create_visualizations():
    """Create data visualizations"""
    if st.session_state.df is None:
        return
    
    df = st.session_state.filtered_df
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    if len(numeric_cols) == 0 and len(categorical_cols) == 0:
        return
    
    st.markdown('<div class="section-header">📈 Data Visualizations</div>', unsafe_allow_html=True)
    
    viz_type = st.selectbox(
        "Choose visualization type",
        ["Correlation Heatmap", "Distribution Plot", "Box Plot", "Scatter Plot", "Bar Chart", "Line Chart"]
    )
    
    if viz_type == "Correlation Heatmap" and len(numeric_cols) > 1:
        fig = px.imshow(
            df[numeric_cols].corr(),
            text_auto=True,
            aspect="auto",
            color_continuous_scale='RdBu_r',
            title="Correlation Heatmap"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    elif viz_type == "Distribution Plot" and len(numeric_cols) > 0:
        selected_col = st.selectbox("Select column", numeric_cols)
        fig = px.histogram(df, x=selected_col, title=f"Distribution of {selected_col}")
        st.plotly_chart(fig, use_container_width=True)
    
    elif viz_type == "Box Plot" and len(numeric_cols) > 0:
        selected_col = st.selectbox("Select column", numeric_cols)
        fig = px.box(df, y=selected_col, title=f"Box Plot of {selected_col}")
        st.plotly_chart(fig, use_container_width=True)
    
    elif viz_type == "Scatter Plot" and len(numeric_cols) > 1:
        col1, col2 = st.columns(2)
        with col1:
            x_col = st.selectbox("X-axis", numeric_cols)
        with col2:
            y_col = st.selectbox("Y-axis", [col for col in numeric_cols if col != x_col])
        
        color_col = None
        if categorical_cols:
            color_col = st.selectbox("Color by (optional)", ["None"] + categorical_cols)
            color_col = None if color_col == "None" else color_col
        
        fig = px.scatter(df, x=x_col, y=y_col, color=color_col, title=f"{x_col} vs {y_col}")
        st.plotly_chart(fig, use_container_width=True)
    
    elif viz_type == "Bar Chart" and len(categorical_cols) > 0:
        selected_col = st.selectbox("Select categorical column", categorical_cols)
        value_counts = df[selected_col].value_counts().head(20)
        fig = px.bar(x=value_counts.index, y=value_counts.values, title=f"Top values in {selected_col}")
        st.plotly_chart(fig, use_container_width=True)

def main():
    """Main application function"""
    initialize_session_state()
    
    # Sidebar
    with st.sidebar:
        st.title("🎛️ Control Panel")
        
        if load_csv_file():
            st.success("✅ Data loaded successfully!")
            
            # Data overview in sidebar
            if st.session_state.df is not None:
                st.markdown("### Quick Stats")
                st.metric("Rows", len(st.session_state.df))
                st.metric("Columns", len(st.session_state.df.columns))
                
                # Navigation
                st.markdown("### Navigation")
                show_overview = st.checkbox("📋 Data Overview", True)
                show_filters = st.checkbox("🔍 Filters & Search", True)
                show_table = st.checkbox("📊 Data Table", True)
                show_actions = st.checkbox("⚡ Actions", True)
                show_viz = st.checkbox("📈 Visualizations", False)
        else:
            st.info("👆 Upload a CSV file to get started!")
    
    # Main content
    if st.session_state.df is not None:
        if 'show_overview' not in locals() or show_overview:
            display_data_overview()
        
        if 'show_filters' not in locals() or show_filters:
            create_data_filters()
        
        if 'show_table' not in locals() or show_table:
            display_excel_like_table()
        
        if 'show_actions' not in locals() or show_actions:
            create_data_actions()
        
        if 'show_viz' in locals() and show_viz:
            create_visualizations()
    
    else:
        # Welcome screen
        st.markdown("""
        <div style="text-align: center; padding: 3rem;">
            <h1>🎯 Welcome to CSV Data Analyzer</h1>
            <h3>Your Excel-like data exploration tool</h3>
            <p style="font-size: 1.2rem; color: #666;">
                Upload a CSV file using the sidebar to start analyzing your data with powerful features:
            </p>
            <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 2rem; margin: 2rem 0;">
                <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 0.5rem; min-width: 200px;">
                    <h4>📊 Rich Data Display</h4>
                    <p>Excel-like table views with formatting</p>
                </div>
                <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 0.5rem; min-width: 200px;">
                    <h4>🔍 Advanced Filtering</h4>
                    <p>Search, filter, and slice your data</p>
                </div>
                <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 0.5rem; min-width: 200px;">
                    <h4>📈 Interactive Charts</h4>
                    <p>Generate plots and visualizations</p>
                </div>
                <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 0.5rem; min-width: 200px;">
                    <h4>⚡ Quick Actions</h4>
                    <p>Export, analyze, and manipulate data</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()