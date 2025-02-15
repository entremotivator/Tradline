import streamlit as st
import pandas as pd

# Expanded Starter Vendors Data
data = [
    {"Vendor": "Uline", "Payment Terms": "Net 30", "Credit Limit": "$1,000", "Reporting Bureau": "Dun & Bradstreet"},
    {"Vendor": "Grainger", "Payment Terms": "Net 30", "Credit Limit": "$2,000", "Reporting Bureau": "Experian"},
    {"Vendor": "Quill", "Payment Terms": "Net 30", "Credit Limit": "$1,500", "Reporting Bureau": "Dun & Bradstreet"},
    {"Vendor": "Summa Office Supplies", "Payment Terms": "Net 30", "Credit Limit": "$1,000", "Reporting Bureau": "Equifax"},
    {"Vendor": "Crown Office Supplies", "Payment Terms": "Net 30", "Credit Limit": "$1,500", "Reporting Bureau": "Dun & Bradstreet"},
    {"Vendor": "Wise Business Plans", "Payment Terms": "Net 30", "Credit Limit": "$2,500", "Reporting Bureau": "Experian"},
    {"Vendor": "Strategic Network Solutions", "Payment Terms": "Net 30", "Credit Limit": "$1,000", "Reporting Bureau": "Equifax"},
    {"Vendor": "CEO Creative", "Payment Terms": "Net 30", "Credit Limit": "$2,000", "Reporting Bureau": "Dun & Bradstreet"},
    {"Vendor": "Shirtsy", "Payment Terms": "Net 30", "Credit Limit": "$1,500", "Reporting Bureau": "Experian"},
    {"Vendor": "The Red Spectrum", "Payment Terms": "Net 30", "Credit Limit": "$2,000", "Reporting Bureau": "Dun & Bradstreet"},
    {"Vendor": "Office Garner", "Payment Terms": "Net 30", "Credit Limit": "$1,500", "Reporting Bureau": "Equifax"},
    {"Vendor": "Nav Business Boost", "Payment Terms": "Net 30", "Credit Limit": "$2,500", "Reporting Bureau": "Experian"},
    {"Vendor": "Credit Strong", "Payment Terms": "Revolving", "Credit Limit": "$5,000", "Reporting Bureau": "Dun & Bradstreet"},
    {"Vendor": "Tillful", "Payment Terms": "Revolving", "Credit Limit": "$3,000", "Reporting Bureau": "Experian"},
    {"Vendor": "eCredable", "Payment Terms": "Net 30", "Credit Limit": "$2,000", "Reporting Bureau": "Equifax"},
    {"Vendor": "Brex", "Payment Terms": "Revolving", "Credit Limit": "$10,000", "Reporting Bureau": "Experian"},
    {"Vendor": "Divvy", "Payment Terms": "Revolving", "Credit Limit": "$15,000", "Reporting Bureau": "Dun & Bradstreet"},
    {"Vendor": "Sam's Club Business Credit", "Payment Terms": "Revolving", "Credit Limit": "$5,000", "Reporting Bureau": "Experian"},
    {"Vendor": "Amazon Business Credit", "Payment Terms": "Revolving", "Credit Limit": "$7,500", "Reporting Bureau": "Equifax"},
    {"Vendor": "Home Depot Commercial Credit", "Payment Terms": "Revolving", "Credit Limit": "$10,000", "Reporting Bureau": "Dun & Bradstreet"},
    {"Vendor": "Lowe's Business Credit", "Payment Terms": "Revolving", "Credit Limit": "$10,000", "Reporting Bureau": "Experian"},
    {"Vendor": "Walmart Business Credit", "Payment Terms": "Revolving", "Credit Limit": "$7,500", "Reporting Bureau": "Equifax"},
    {"Vendor": "Staples Business Credit", "Payment Terms": "Net 30", "Credit Limit": "$5,000", "Reporting Bureau": "Dun & Bradstreet"},
    {"Vendor": "Costco Business Credit", "Payment Terms": "Revolving", "Credit Limit": "$10,000", "Reporting Bureau": "Experian"},
    {"Vendor": "Best Buy Business Credit", "Payment Terms": "Revolving", "Credit Limit": "$7,500", "Reporting Bureau": "Equifax"},
    {"Vendor": "Dell Business Credit", "Payment Terms": "Revolving", "Credit Limit": "$15,000", "Reporting Bureau": "Dun & Bradstreet"},
    {"Vendor": "Apple Business Credit", "Payment Terms": "Revolving", "Credit Limit": "$10,000", "Reporting Bureau": "Experian"},
    {"Vendor": "FedEx Business Credit", "Payment Terms": "Net 30", "Credit Limit": "$3,000", "Reporting Bureau": "Equifax"},
    {"Vendor": "UPS Business Credit", "Payment Terms": "Net 30", "Credit Limit": "$3,500", "Reporting Bureau": "Dun & Bradstreet"},
    {"Vendor": "AutoZone Business Credit", "Payment Terms": "Net 30", "Credit Limit": "$4,000", "Reporting Bureau": "Experian"},
    {"Vendor": "Advanced Auto Parts Business Credit", "Payment Terms": "Net 30", "Credit Limit": "$3,500", "Reporting Bureau": "Dun & Bradstreet"},
    {"Vendor": "BP Business Solutions Fuel Card", "Payment Terms": "Net 30", "Credit Limit": "$5,000", "Reporting Bureau": "Experian"},
    {"Vendor": "Shell Fleet Credit Card", "Payment Terms": "Net 30", "Credit Limit": "$5,000", "Reporting Bureau": "Equifax"},
    {"Vendor": "Chevron Business Fuel Card", "Payment Terms": "Net 30", "Credit Limit": "$5,000", "Reporting Bureau": "Dun & Bradstreet"},
    {"Vendor": "Verizon Business Credit", "Payment Terms": "Net 30", "Credit Limit": "$7,000", "Reporting Bureau": "Experian"},
    {"Vendor": "AT&T Business Credit", "Payment Terms": "Net 30", "Credit Limit": "$7,500", "Reporting Bureau": "Equifax"}
]

# Convert to DataFrame
trade_lines = pd.DataFrame(data)

st.title("Trade Line List & Calculator")
st.subheader("Expanded Starter Vendor Trade Lines")
st.dataframe(trade_lines)
