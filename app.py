import streamlit as st

# Page configuration
st.set_page_config(page_title="Olist AI Insight Bot", page_icon="🤖")

st.title("🤖 Olist E-Commerce - AI Insights Bot")
st.write("Ask me anything about the Olist Customer Lifecycle & Cohort Analytics project!")

# Project Knowledge Base (The data chatbot will refer to this)
project_knowledge = {
    "revenue": "The total revenue generated across the platform is $13,218,400.",
    "customers": "The project analyzes data for over 93,336 unique customers.",
    "frequency": "The platform's average order frequency is 1.033, which means nearly 97% of users buy only once.",
    "retention": "The Cohort Retention Heatmap shows a massive drop-off in Month 2 (Cohort Index 1), with retention dropping to single digits (1% - 2%).",
    "segments": "Customers are divided into 4 main RFM segments: VIP/Champions, Loyal Customers, New Customers, and Lost Customers / At Risk.",
    "recommendation": "Recommendations include: 1) Automated win-back discount email loops for 'Lost Customers'. 2) A milestone loyalty point system for 'New Customers' to trigger a 2nd purchase within 30 days."
}

# User Input
user_query = st.text_input("Type your question here (e.g., total revenue, retention trend, customer segments):").lower()

if user_query:
    response_found = False
    for key, value in project_knowledge.items():
        if key in user_query:
            st.success(value)
            response_found = True
            break
            
    if not response_found:
        st.warning("I couldn't find that specific metric. Try asking about 'revenue', 'total customers', 'retention', 'segments', or 'recommendations'!")