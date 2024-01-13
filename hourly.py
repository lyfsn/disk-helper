from apscheduler.schedulers.blocking import BlockingScheduler
import os
import datetime

def every_two_hours_job():
    # Log the start of the job
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"Job started at {current_time}\n"
    with open("job_log.txt", "a") as log_file:
        log_file.write(log_message)

    # Define shell commands to execute
    shell_commands = [
        "echo 1 > /var/lib/docker/containers/be707e3dac8190f5113d8c769d67513e441c297f7ca678502c7ba51626d606fb/be707e3dac8190f5113d8c769d67513e441c297f7ca678502c7ba51626d606fb-json.log",
        "echo 1 > /var/lib/docker/containers/cdaaa20a83878aea17bce1a4af461c96ec43fbc114f63e8003ac0fac15cfb92f/cdaaa20a83878aea17bce1a4af461c96ec43fbc114f63e8003ac0fac15cfb92f-json.log",
    ]

    # Execute each command and log it
    for command in shell_commands:
        os.system(command)
        with open("job_log.txt", "a") as log_file:
            log_file.write(f"Executed command: {command}\n")

    # Log the end of the job
    log_message = f"Job finished at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    with open("job_log.txt", "a") as log_file:
        log_file.write(log_message)

# Create a scheduler instance
scheduler = BlockingScheduler()

# Schedule the job to run every two hours at the beginning of the hour
scheduler.add_job(every_two_hours_job, 'cron', hour='*/2', minute=0)

# Start the scheduler
scheduler.start()
