import frappe
import time

def long_running_job(param1, param2):
    """Example of a background job that takes some time to run"""
    for i in range(1, 6):
        # Simulate long-running task
        frappe.logger().info(f'Processing step {i} for {param1} and {param2}')
        time.sleep(2)  # Pause for 2 seconds to simulate a long-running task
    frappe.logger().info(f'Background Job Complete: {param1}, {param2}')
