import os
import psycopg
import requests

def generate_monthly_customer_reports(conn, customer_ids):
    cursor = conn.cursor()
    customer_reports = []

    # ISSUE 1 (MEDIUM): N+1 Query Loop
    # Querying the database inside an iteration loop degrades database performance at scale.
    # It should be refactored into a single batch query: "WHERE id = ANY(%s)"
    for cust_id in customer_ids:
        cursor.execute("SELECT id, full_name, email FROM customers WHERE id = %s", (cust_id,))
        customer = cursor.fetchone()
        if customer:
            customer_reports.append(customer)

    # ISSUE 2 (MEDIUM): Unmanaged File Resource
    # File handle opened directly without a `with` context manager.
    # If an exception occurs, the file descriptor remains unclosed in memory.
    audit_file = open("reports/audit_log.txt", "a")
    audit_file.write(f"Generated {len(customer_reports)} customer reports.\n")
    audit_file.close()

    # ISSUE 3 (LOW / MEDIUM): Missing Request Timeout
    # Calling an external REST API without specifying `timeout=...` can cause thread hangs.
    resp = requests.get("https://api.exchangerate.host/latest")
    
    return customer_reports
