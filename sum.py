import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Streamlit page configuration for a cleaner look
st.set_page_config(page_title="Interactive Graph", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f4f6f9;
            padding: 20px;
        }
        .stApp {
            max-width: 900px;
            margin: auto;
        }
        h1 {
            font-family: 'Segoe UI', Arial, sans-serif;
            color: #1a3c61;
            text-align: center;
            font-size: 2em;
            margin-bottom: 10px;
        }
        .stNumberInput {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }
        .stNumberInput label {
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 1.1em;
            color: #333;
        }
        .stNumberInput input {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 8px;
            font-size: 1em;
            width: 100px;
            transition: border-color 0.3s;
        }
        .stNumberInput input:focus {
            border-color: #007bff;
            outline: none;
        }
        .plotly-container {
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            padding: 15px;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>Interactive Graph: Y = |x|^(2/3) + 0.9sin(kx)√(3-x²)</h1>", unsafe_allow_html=True)

# Input for k
k_value = st.number_input(
    "Enter k value:",
    min_value=-10.0,
    max_value=10.0,
    value=1.0,
    step=0.1,
    format="%.1f",
    key="k_input"
)

# Function to create the Plotly graph
def create_plot(k):
    # Generate x values in the domain [-√3, √3]
    x = np.linspace(-np.sqrt(3), np.sqrt(3), 1000)
    
    # Calculate y values
    try:
        y = np.power(np.abs(x), 2/3) + 0.9 * np.sin(k * x) * np.sqrt(3 - x**2)
    except Exception:
        y = np.zeros_like(x)  # Fallback for numerical errors

    # Create Plotly trace
    trace = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        name=f'k = {k}',
        line=dict(color='#007bff', width=2.5)
    )

    # Layout for the graph
    layout = go.Layout(
        title={
            'text': f'Y = |x|^(2/3) + 0.9sin({k:.1f}x)√(3-x²)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1a3c61'}
        },
        xaxis=dict(
            title='x',
            range=[-2, 2],
            gridcolor='rgba(200, 200, 200, 0.3)',
            zerolinecolor='rgba(100, 100, 100, 0.5)'
        ),
        yaxis=dict(
            title='Y',
            range=[-2, 3],
            gridcolor='rgba(200, 200, 200, 0.3)',
            zerolinecolor='rgba(100, 100, 100, 0.5)'
        ),
        showlegend=True,
        template='plotly_white',
        margin=dict(t=50, b=50, l=50, r=50),
        hovermode='closest',
        plot_bgcolor='white',
        paper_bgcolor='white'
    )

    # Create figure
    fig = go.Figure(data=[trace], layout=layout)
    return fig

# Generate and display the graph
fig = create_plot(k_value)

# Wrap the graph in a styled container
st.markdown('<div class="plotly-container">', unsafe_allow_html=True)
st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
