import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import re
import json
import io
from typing import Dict, List, Any, Optional

# Configure page
st.set_page_config(
    page_title="Chat with Your Data",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .chat-container {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        max-height: 600px;
        overflow-y: auto;
    }
    
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 12px 16px;
        border-radius: 18px;
        margin: 8px 0;
        max-width: 80%;
        margin-left: auto;
        text-align: right;
    }
    
    .bot-message {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 12px 16px;
        border-radius: 18px;
        margin: 8px 0;
        max-width: 80%;
        margin-right: auto;
    }
    
    .data-preview {
        background-color: #e3f2fd;
        border: 1px solid #90caf9;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
    }
    
    .insight-box {
        background: linear-gradient(45deg, #4CAF50, #45a049);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
        margin: 5px;
    }
    
    .chat-input {
        position: sticky;
        bottom: 0;
        background: white;
        padding: 10px;
        border-top: 1px solid #ddd;
    }
    
    .suggestion-chip {
        display: inline-block;
        background-color: #e1f5fe;
        color: #0277bd;
        padding: 8px 12px;
        border-radius: 20px;
        margin: 4px;
        cursor: pointer;
        border: 1px solid #81d4fa;
        font-size: 0.9em;
    }
    
    .suggestion-chip:hover {
        background-color: #b3e5fc;
    }
</style>
""", unsafe_allow_html=True)

class DataChatbot:
    def __init__(self):
        self.df = None
        self.conversation_history = []
        
    def load_data(self, uploaded_file, skip_rows=0):
        """Load CSV/Excel file"""
        try:
            if uploaded_file.name.endswith('.csv'):
                self.df = pd.read_csv(uploaded_file, skiprows=skip_rows)
            elif uploaded_file.name.endswith(('.xlsx', '.xls')):
                self.df = pd.read_excel(uploaded_file, skiprows=skip_rows)
            else:
                raise ValueError("Unsupported file format")
            return True, f"Successfully loaded {len(self.df)} rows and {len(self.df.columns)} columns"
        except Exception as e:
            return False, f"Error loading file: {str(e)}"
    
    def get_data_summary(self):
        """Get basic data summary"""
        if self.df is None:
            return "No data loaded"
        
        summary = {
            "rows": len(self.df),
            "columns": len(self.df.columns),
            "column_names": list(self.df.columns),
            "data_types": self.df.dtypes.to_dict(),
            "missing_values": self.df.isnull().sum().to_dict(),
            "numeric_columns": list(self.df.select_dtypes(include=[np.number]).columns),
            "categorical_columns": list(self.df.select_dtypes(include=['object']).columns)
        }
        return summary
    
    def analyze_query(self, query: str) -> Dict[str, Any]:
        """Analyze user query and determine intent"""
        query_lower = query.lower()
        
        # Intent detection patterns (Heuristic Engine)
        patterns = {
            "show_data": r"show|display|view|see.*data|table|rows",
            "summary": r"summary|describe|overview|info|statistics|stats",
            "count": r"count|how many|number of",
            "filter": r"filter|where|find|search|show.*where|rows.*where",
            "plot": r"plot|chart|graph|visualize|show.*chart",
            "correlation": r"correlation|correlate|relationship|relate",
            "mean": r"mean|average|avg",
            "max": r"max|maximum|highest|largest",
            "min": r"min|minimum|lowest|smallest",
            "null": r"null|missing|nan|empty",
            "unique": r"unique|distinct|different",
            "group": r"group|by|aggregate"
        }
        
        detected_intents = []
        for intent, pattern in patterns.items():
            if re.search(pattern, query_lower):
                detected_intents.append(intent)
        
        # Extract column names mentioned in query
        mentioned_columns = []
        if self.df is not None:
            for col in self.df.columns:
                if col.lower() in query_lower:
                    mentioned_columns.append(col)
        
        return {
            "intents": detected_intents,
            "mentioned_columns": mentioned_columns,
            "original_query": query
        }
    
    def execute_query(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the analyzed query"""
        if self.df is None:
            return {"type": "error", "message": "No data loaded. Please upload a file first."}
        
        intents = analysis["intents"]
        mentioned_columns = analysis["mentioned_columns"]
        query = analysis["original_query"]
        
        try:
            # Show data
            if "show_data" in intents:
                return self._show_data(mentioned_columns, query)
            
            # Summary statistics
            elif "summary" in intents:
                return self._get_summary(mentioned_columns)
            
            # Count operations
            elif "count" in intents:
                return self._count_operations(mentioned_columns, query)
            
            # Filter operations
            elif "filter" in intents:
                return self._filter_data(query, mentioned_columns)
            
            # Plot/visualization
            elif "plot" in intents:
                return self._create_plot(mentioned_columns, query)
            
            # Correlation analysis
            elif "correlation" in intents:
                return self._correlation_analysis(mentioned_columns)
            
            # Statistical operations
            elif any(stat in intents for stat in ["mean", "max", "min"]):
                return self._statistical_operations(intents, mentioned_columns)
            
            # Null/missing value analysis
            elif "null" in intents:
                return self._null_analysis(mentioned_columns)
            
            # Unique values
            elif "unique" in intents:
                return self._unique_analysis(mentioned_columns)
            
            # Group operations
            elif "group" in intents:
                return self._group_operations(mentioned_columns, query)
            
            else:
                return self._general_response(query, mentioned_columns)
                
        except Exception as e:
            return {"type": "error", "message": f"Error executing query: {str(e)}"}
    
    def _show_data(self, columns, query):
        """Show data with optional column filtering"""
        if columns:
            data = self.df[columns].head(10)
            return {
                "type": "dataframe",
                "data": data,
                "message": f"Here are the first 10 rows of {', '.join(columns)}:"
            }
        else:
            data = self.df.head(10)
            return {
                "type": "dataframe", 
                "data": data,
                "message": "Here are the first 10 rows of your data:"
            }
    
    def _get_summary(self, columns):
        """Get summary statistics"""
        if columns:
            target_cols = [col for col in columns if col in self.df.columns]
            if target_cols:
                summary_data = self.df[target_cols].describe()
                return {
                    "type": "dataframe",
                    "data": summary_data,
                    "message": f"Summary statistics for {', '.join(target_cols)}:"
                }
        
        # General summary
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            summary_data = self.df[numeric_cols].describe()
            return {
                "type": "dataframe",
                "data": summary_data,
                "message": "Summary statistics for numeric columns:"
            }
        else:
            return {
                "type": "text",
                "message": "No numeric columns found for summary statistics."
            }
    
    def _count_operations(self, columns, query):
        """Handle count operations"""
        if columns:
            col = columns[0]
            if "unique" in query.lower() or "distinct" in query.lower():
                count = self.df[col].nunique()
                return {
                    "type": "metric",
                    "value": count,
                    "message": f"Number of unique values in {col}: {count}"
                }
            else:
                count = len(self.df[col].dropna())
                return {
                    "type": "metric",
                    "value": count,
                    "message": f"Number of non-null values in {col}: {count}"
                }
        else:
            total_rows = len(self.df)
            return {
                "type": "metric",
                "value": total_rows,
                "message": f"Total number of rows: {total_rows}"
            }
    
    def _create_plot(self, columns, query):
        """Create visualizations"""
        if not columns:
            return {"type": "error", "message": "Please specify which columns to plot."}
        
        if len(columns) == 1:
            col = columns[0]
            if self.df[col].dtype in ['object']:
                # Bar chart for categorical
                fig = px.bar(self.df[col].value_counts().head(10))
                return {
                    "type": "plot",
                    "figure": fig,
                    "message": f"Bar chart showing top 10 values in {col}:"
                }
            else:
                # Histogram for numeric
                fig = px.histogram(self.df, x=col)
                return {
                    "type": "plot",
                    "figure": fig,
                    "message": f"Distribution of {col}:"
                }
        
        elif len(columns) == 2:
            # Scatter plot
            fig = px.scatter(self.df, x=columns[0], y=columns[1])
            return {
                "type": "plot",
                "figure": fig,
                "message": f"Scatter plot: {columns[0]} vs {columns[1]}"
            }
        
        return {"type": "error", "message": "Please specify 1-2 columns for plotting."}
    
    def _correlation_analysis(self, columns):
        """Analyze correlations"""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        if len(numeric_cols) < 2:
            return {"type": "error", "message": "Need at least 2 numeric columns for correlation analysis."}
        
        if columns:
            target_cols = [col for col in columns if col in numeric_cols]
            if len(target_cols) >= 2:
                corr_matrix = self.df[target_cols].corr()
            else:
                corr_matrix = self.df[numeric_cols].corr()
        else:
            corr_matrix = self.df[numeric_cols].corr()
        
        fig = px.imshow(corr_matrix, text_auto=True, aspect="auto")
        
        return {
            "type": "plot",
            "figure": fig,
            "message": "Correlation matrix for numeric columns:"
        }
    
    def _statistical_operations(self, intents, columns):
        """Handle statistical operations"""
        if not columns:
            return {"type": "error", "message": "Please specify a column for statistical analysis."}
        
        col = columns[0]
        if col not in self.df.select_dtypes(include=[np.number]).columns:
            return {"type": "error", "message": f"{col} is not a numeric column."}
        
        results = {}
        if "mean" in intents:
            results["Mean"] = self.df[col].mean()
        if "max" in intents:
            results["Maximum"] = self.df[col].max()
        if "min" in intents:
            results["Minimum"] = self.df[col].min()
        
        return {
            "type": "metrics",
            "data": results,
            "message": f"Statistics for {col}:"
        }
    
    def _null_analysis(self, columns):
        """Analyze null/missing values"""
        if columns:
            null_counts = {col: self.df[col].isnull().sum() for col in columns if col in self.df.columns}
        else:
            null_counts = self.df.isnull().sum().to_dict()
        
        return {
            "type": "metrics",
            "data": null_counts,
            "message": "Missing values count:"
        }
    
    def _unique_analysis(self, columns):
        """Analyze unique values"""
        if not columns:
            return {"type": "error", "message": "Please specify a column to analyze unique values."}
        
        col = columns[0]
        unique_count = self.df[col].nunique()
        unique_values = self.df[col].unique()[:10]  # Show first 10
        
        return {
            "type": "text",
            "message": f"{col} has {unique_count} unique values. First 10: {', '.join(map(str, unique_values))}"
        }
    
    def _group_operations(self, columns, query):
        """Handle group operations"""
        if len(columns) < 2:
            return {"type": "error", "message": "Please specify at least 2 columns for grouping."}
        
        group_col = columns[0]
        value_col = columns[1]
        
        if "count" in query.lower():
            result = self.df.groupby(group_col).size().head(10)
        elif "mean" in query.lower():
            result = self.df.groupby(group_col)[value_col].mean().head(10)
        elif "sum" in query.lower():
            result = self.df.groupby(group_col)[value_col].sum().head(10)
        else:
            result = self.df.groupby(group_col)[value_col].count().head(10)
        
        return {
            "type": "dataframe",
            "data": result.to_frame(),
            "message": f"Grouped analysis: {group_col} by {value_col}"
        }
    
    def _filter_data(self, query, columns):
        """Handle data filtering"""
        # Simple filtering logic - can be enhanced
        if not columns:
            return {"type": "error", "message": "Please specify a column to filter by."}
        
        col = columns[0]
        
        # Extract comparison operators and values from query
        if ">" in query:
            try:
                value = float(re.search(r'>\s*(\d+\.?\d*)', query).group(1))
                filtered_data = self.df[self.df[col] > value].head(10)
                return {
                    "type": "dataframe",
                    "data": filtered_data,
                    "message": f"Rows where {col} > {value}:"
                }
            except:
                return {"type": "error", "message": "Could not parse filter condition."}
        
        return {
            "type": "dataframe", 
            "data": self.df.head(10),
            "message": "Showing first 10 rows (filtering logic can be enhanced):"
        }
    
    def _general_response(self, query, columns):
        """General response for unrecognized queries"""
        suggestions = [
            "Show me the first 10 rows",
            "What's the summary of this data?",
            "How many rows are there?",
            "Show me a plot of [column_name]",
            "What are the missing values?",
            "Show correlation between columns"
        ]
        
        return {
            "type": "suggestions",
            "message": "I'm not sure how to help with that. Here are some things you can ask:",
            "suggestions": suggestions
        }

def initialize_session_state():
    """Initialize session state"""
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = DataChatbot()
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'data_loaded' not in st.session_state:
        st.session_state.data_loaded = False

def render_message(message, is_user=False):
    """Render a chat message"""
    css_class = "user-message" if is_user else "bot-message"
    icon = "🧑" if is_user else "🤖"
    
    st.markdown(f"""
    <div class="{css_class}">
        {icon} {message}
    </div>
    """, unsafe_allow_html=True)

def render_response(response):
    """Render chatbot response based on type"""
    if response["type"] == "dataframe":
        st.markdown(f"🤖 {response['message']}")
        st.dataframe(response["data"], use_container_width=True)
    
    elif response["type"] == "plot":
        st.markdown(f"🤖 {response['message']}")
        st.plotly_chart(response["figure"], use_container_width=True)
    
    elif response["type"] == "metric":
        st.markdown(f"🤖 {response['message']}")
        st.metric("Result", response["value"])
    
    elif response["type"] == "metrics":
        st.markdown(f"🤖 {response['message']}")
        cols = st.columns(len(response["data"]))
        for i, (key, value) in enumerate(response["data"].items()):
            with cols[i]:
                st.metric(key, value)
    
    elif response["type"] == "suggestions":
        st.markdown(f"🤖 {response['message']}")
        for suggestion in response["suggestions"]:
            if st.button(suggestion, key=f"suggestion_{hash(suggestion)}"):
                st.session_state.user_input = suggestion
                st.experimental_rerun()
    
    elif response["type"] == "error":
        st.error(f"🤖 {response['message']}")
    
    else:
        st.markdown(f"🤖 {response['message']}")

def main():
    initialize_session_state()
    
    st.title("🤖 Chat with Your Data")
    st.markdown("Upload your CSV/Excel file and start having conversations with your data!")
    
    # Sidebar for file upload
    with st.sidebar:
        st.header("📂 Data Upload")
        
        uploaded_file = st.file_uploader(
            "Choose a CSV or Excel file",
            type=['csv', 'xlsx', 'xls'],
            help="Upload your data file to start chatting!"
        )
        
        skip_rows = st.number_input("Skip rows", min_value=0, max_value=100, value=0)
        
        if uploaded_file is not None:
            if st.button("Load Data") or not st.session_state.data_loaded:
                success, message = st.session_state.chatbot.load_data(uploaded_file, skip_rows)
                if success:
                    st.success(message)
                    st.session_state.data_loaded = True
                    
                    # Show data info
                    summary = st.session_state.chatbot.get_data_summary()
                    st.markdown("### Data Info")
                    st.write(f"**Rows:** {summary['rows']:,}")
                    st.write(f"**Columns:** {summary['columns']}")
                    
                    with st.expander("Column Details"):
                        st.write("**Columns:**")
                        for col in summary['column_names']:
                            st.write(f"• {col}")
                else:
                    st.error(message)
        
        # Quick examples
        if st.session_state.data_loaded:
            st.markdown("### 💡 Quick Examples")
            examples = [
                "Show me the data",
                "What's the summary?",
                "How many rows?",
                "Show missing values",
                "Plot a histogram"
            ]
            
            for example in examples:
                if st.button(example, key=f"example_{hash(example)}"):
                    # Add to chat
                    st.session_state.chat_history.append({"user": example, "bot": None})
                    
                    # Process query
                    analysis = st.session_state.chatbot.analyze_query(example)
                    response = st.session_state.chatbot.execute_query(analysis)
                    
                    # Add response to history
                    st.session_state.chat_history[-1]["bot"] = response
                    st.experimental_rerun()
    
    # Main chat interface
    if st.session_state.data_loaded:
        # Chat history
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        
        for chat in st.session_state.chat_history:
            render_message(chat["user"], is_user=True)
            if chat["bot"]:
                render_response(chat["bot"])
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Chat input
        with st.container():
            col1, col2 = st.columns([4, 1])
            
            with col1:
                user_input = st.text_input(
                    "Ask me anything about your data...",
                    placeholder="e.g., 'Show me the first 10 rows' or 'What's the average of column X?'",
                    key="chat_input"
                )
            
            with col2:
                send_button = st.button("Send 📤", use_container_width=True)
            
            if send_button and user_input:
                # Add user message to history
                st.session_state.chat_history.append({"user": user_input, "bot": None})
                
                # Process query
                analysis = st.session_state.chatbot.analyze_query(user_input)
                response = st.session_state.chatbot.execute_query(analysis)
                
                # Add bot response to history
                st.session_state.chat_history[-1]["bot"] = response
                
                # Clear input and rerun
                st.rerun()
    
    else:
        # Welcome message
        st.markdown("""
        <div style="text-align: center; padding: 3rem;">
            <h2>🎯 Welcome to Your Data Assistant!</h2>
            <p style="font-size: 1.2rem; color: #666; margin: 2rem 0;">
                Upload your CSV or Excel file using the sidebar to start having intelligent conversations with your data.
            </p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin: 3rem 0;">
                <div class="metric-card">
                    <h3>🔍 Ask Questions</h3>
                    <p>Natural language queries like "Show me sales data" or "What's the average price?"</p>
                </div>
                <div class="metric-card">
                    <h3>📊 Get Insights</h3>
                    <p>Automatic analysis, statistics, and visualizations based on your questions</p>
                </div>
                <div class="metric-card">
                    <h3>📈 Create Charts</h3>
                    <p>Generate plots and charts just by asking "Plot sales by region"</p>
                </div>
                <div class="metric-card">
                    <h3>🎯 Smart Responses</h3>
                    <p>Get contextual answers with data tables, metrics, and visualizations</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()