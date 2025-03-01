import streamlit as st
from datetime import datetime, time
import calendar


def calculate_invoice(contract_value, start_date, end_date, current_month,
  days_off):
  # Convert dates to datetime objects
  # start = datetime.strptime(start_date, '%Y-%m-%d')
  # end = datetime.strptime(end_date, '%Y-%m-%d')
  start = datetime.combine(start_date, time())
  end = datetime.combine(end_date, time())

  current = datetime.strptime(f"{current_month} {datetime.now().year}", '%B %Y')

  # Calculate total contract days
  total_days = (end - start).days + 1

  # Calculate daily rate
  daily_rate = contract_value / total_days

  # Get working days in current month
  _, num_days = calendar.monthrange(current.year, current.month)
  month_start = current.replace(day=1)
  month_end = current.replace(day=num_days)

  # Adjust for contract start/end dates
  if month_start < start:
    month_start = start
  if month_end > end:
    month_end = end

  working_days = (month_end - month_start).days + 1

  # Calculate billable days (working days minus days off)
  billable_days = working_days - days_off

  # Calculate invoice amount
  invoice_amount = billable_days * daily_rate

  return round(invoice_amount, 2)

st.title("Invoicing Calculator")
contract_value = st.number_input("Total Contract Value")
start_date = st.date_input("Contract start date")
end_date = st.date_input("Contract end date")
months = list(calendar.month_name)[1:]
current_month = st.selectbox("Select Month", options=months)

days_off = st.number_input("Days off")

if st.button("Calculate"):
  invoice = calculate_invoice(contract_value, start_date, end_date,
    current_month, days_off)
  st.write("Result:", invoice)
