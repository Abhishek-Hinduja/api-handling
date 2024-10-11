import frappe

def trigger_background_job():
    """Trigger the background job"""
    frappe.enqueue(
        'custom_app.tasks.long_running_job',  # Reference the method path
        queue='long',  # Specify the queue (short, default, or long)
        param1="Task A",  # First parameter
        param2="Task B",  # Second parameter
        job_name="My Long Running Job",  # Optional: name the job
        timeout=1500  # Optional: specify a custom timeout (in seconds)
    )
    return "Background job has been triggered!"

    
