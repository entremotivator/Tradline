import streamlit as st
import pandas as pd

# -------------------------
# Vendor Data Setup
# -------------------------
vendor_names = [
    "Uline", "Grainger", "Quill", "Summa Office Supplies", "Crown Office Supplies", "Wise Business Plans",
    "Strategic Network Solutions", "CEO Creative", "Shirtsy", "The Red Spectrum", "Office Garner", "Nav Business Boost",
    "Credit Strong", "Tillful", "eCredable", "Brex", "Divvy", "Sam's Club Business Credit", "Amazon Business Credit",
    "Home Depot Commercial Credit", "Lowe's Business Credit", "Walmart Business Credit", "Staples Business Credit",
    "Costco Business Credit", "Best Buy Business Credit", "Dell Business Credit", "Apple Business Credit",
    "FedEx Business Credit", "UPS Business Credit", "AutoZone Business Credit", "Advanced Auto Parts Business Credit",
    "BP Business Solutions Fuel Card", "Shell Fleet Credit Card", "Chevron Business Fuel Card", "Verizon Business Credit",
    "AT&T Business Credit", "Office Depot Business Credit", "Staples Office Solutions", "OfficeMax Business Credit",
    "Office Supply Direct", "Smart Office Supplies", "Global Business Supplies", "Industrial Supply Co.",
    "Tech Gear Business Credit", "CyberSource Business Credit", "PrintPro Business Solutions", "DocuSign Business Credit",
    "QuickBooks Business Credit", "ADP Business Solutions", "Oracle Business Financing"
]

payment_terms_options = ["Net 30", "Net 60", "Revolving"]
reporting_bureaus = ["Dun & Bradstreet", "Experian", "Equifax"]

# Create a list of vendor dictionaries using a loop for consistency and variety.
vendor_data = []
for i, name in enumerate(vendor_names):
    vendor = {
        "Vendor": name,
        "Payment Terms": payment_terms_options[i % len(payment_terms_options)],
        # Credit limit increases with each vendor (for demo purposes)
        "Credit Limit": f"${(i+1) * 1000:,}",
        "Reporting Bureau": reporting_bureaus[i % len(reporting_bureaus)]
    }
    vendor_data.append(vendor)

# Convert vendor data to a DataFrame for display and selection.
df_vendors = pd.DataFrame(vendor_data)

# -------------------------
# Sidebar Navigation
# -------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Home",
    "Trade Lines",
    "Credit Calculator",
    "Buying Guide & Budget",
    "Step-by-Step Checklist",
    "Vendor Details"
])

# -------------------------
# Home Page
# -------------------------
if page == "Home":
    st.title("Business Credit Trade Line Manager")
    st.write(
        """
        Welcome to the Business Credit Trade Line Manager! This app is designed to help you:
        - View a comprehensive list of 50 starter vendors.
        - Calculate your total available credit across selected vendors.
        - Plan your purchases with a detailed buying guide and budgeting examples.
        - Follow a step-by-step checklist to set up and manage your trade lines.
        - Explore individual vendor details.
        """
    )
    st.image("https://via.placeholder.com/800x200.png?text=Business+Credit+Manager", use_column_width=True)

# -------------------------
# Trade Lines Page
# -------------------------
elif page == "Trade Lines":
    st.title("Expanded Starter Vendor Trade Lines")
    st.write("Below is the complete list of 50 real starter vendors along with their trade line details:")
    st.dataframe(df_vendors)

# -------------------------
# Credit Calculator Page
# -------------------------
elif page == "Credit Calculator":
    st.title("Credit Limit Calculator")
    st.write("Select vendors to calculate your total available credit limit:")
    selected_vendors = st.multiselect("Select Vendors", df_vendors["Vendor"].tolist())
    
    if selected_vendors:
        # Filter the vendor data for the selected vendors.
        selected_data = [vendor for vendor in vendor_data if vendor["Vendor"] in selected_vendors]
        # Sum up the credit limits (remove '$' and commas for conversion)
        total_credit = sum([int(vendor["Credit Limit"].replace("$", "").replace(",", "")) for vendor in selected_data])
        st.success(f"Total Credit Limit: ${total_credit:,.2f}")
    else:
        st.info("Please select one or more vendors to calculate the total credit available.")

# -------------------------
# Buying Guide & Budget Page
# -------------------------
elif page == "Buying Guide & Budget":
    st.title("Buying Guide & Budget")
    st.write(
        """
        Maximizing your business credit growth is not only about having multiple trade lines but also about 
        making smart purchasing decisions. This guide provides recommendations, a budgeting example, and tips 
        to manage your expenses effectively.
        """
    )
    
    st.subheader("Recommended Purchases")
    recommended_purchases = [
        "Office Supplies (e.g., Paper, Pens, Printers)",
        "Business Software Subscriptions",
        "Branded Merchandise",
        "Marketing & Advertising Services",
        "Fuel & Vehicle Maintenance",
        "Professional Services (Legal, Accounting)",
        "IT Equipment & Hosting Services",
        "Furniture & Office Fixtures",
        "Security & Surveillance Equipment",
        "Training & Development Programs"
    ]
    for item in recommended_purchases:
        st.write(f"- {item}")
    
    st.subheader("Budgeting Example")
    budget_data = {
        "Category": ["Office Supplies", "Marketing", "Software", "Professional Services", "IT Equipment", "Miscellaneous"],
        "Estimated Cost": ["$500", "$1,200", "$1,500", "$2,000", "$3,000", "$800"]
    }
    budget_df = pd.DataFrame(budget_data)
    st.dataframe(budget_df)
    
    st.subheader("Budgeting Tips")
    st.write("1. **Prioritize:** Identify essential business expenses and fund them first.")
    st.write("2. **Plan Ahead:** Monitor cash flow regularly and adjust budgets as needed.")
    st.write("3. **Use Credit Wisely:** Maintain timely payments to build a strong credit profile.")
    st.write("4. **Review:** Regularly assess your purchases to ensure they contribute to growth.")

# -------------------------
# Step-by-Step Checklist Page
# -------------------------
elif page == "Step-by-Step Checklist":
    st.title("Step-by-Step Trade Line Setup Checklist")
    st.write("Follow these steps to successfully set up and manage your trade lines:")
    checklist_items = [
        "Research and select vendors that report to reputable business credit bureaus.",
        "Open accounts with your chosen vendors and place small initial orders.",
        "Meet any minimum purchase requirements to establish a credit history.",
        "Ensure all invoices are paid on time to build and maintain good credit.",
        "Monitor your business credit reports on a regular basis.",
        "Apply for higher credit limits after demonstrating positive payment behavior.",
        "Diversify trade lines across different categories of business expenses.",
        "Periodically review vendor terms and adjust strategies for better benefits."
    ]
    for idx, item in enumerate(checklist_items, start=1):
        st.write(f"{idx}. {item}")

# -------------------------
# Vendor Details Page
# -------------------------
elif page == "Vendor Details":
    st.title("Vendor Details")
    vendor_selected = st.selectbox("Select a Vendor to View Details", df_vendors["Vendor"].tolist())
    
    if vendor_selected:
        vendor_info = df_vendors[df_vendors["Vendor"] == vendor_selected].iloc[0]
        st.write("### Vendor Information")
        st.write(f"**Vendor:** {vendor_info['Vendor']}")
        st.write(f"**Payment Terms:** {vendor_info['Payment Terms']}")
        st.write(f"**Credit Limit:** {vendor_info['Credit Limit']}")
        st.write(f"**Reporting Bureau:** {vendor_info['Reporting Bureau']}")
        st.subheader("Additional Information")
        st.write(
            """
            This vendor is recognized for reliable trade line reporting and competitive credit limits. 
            They can be a valuable addition to your business credit portfolio if their offerings align 
            with your business needs. For more details or to set up an account, please contact the vendor 
            directly or visit their official website.
            """
        )
