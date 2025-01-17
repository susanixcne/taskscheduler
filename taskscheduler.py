import subprocess
import os
import datetime
import time
import schedule

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, script_path, scheduled_time, repeat=False, interval=None):
        if not os.path.exists(script_path):
            raise FileNotFoundError(f"The script {script_path} does not exist.")
        self.tasks.append({
            'script_path': script_path,
            'scheduled_time': scheduled_time,
            'repeat': repeat,
            'interval': interval
        })
        print(f"Task added: {script_path} at {scheduled_time}, repeat: {repeat}, interval: {interval}")

    def run_script(self, script_path):
        try:
            subprocess.run(["python", script_path], check=True)
            print(f"Successfully ran script: {script_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running script: {script_path}. Error: {e}")

    def schedule_tasks(self):
        for task in self.tasks:
            script_path = task['script_path']
            scheduled_time = task['scheduled_time']
            repeat = task['repeat']
            interval = task['interval']

            print(f"Scheduling task: {script_path} at {scheduled_time}, repeat: {repeat}, interval: {interval}")

            if repeat and interval:
                if interval == "daily":
                    schedule.every().day.at(scheduled_time).do(self.run_script, script_path)
                elif interval == "hourly":
                    schedule.every().hour.at(scheduled_time).do(self.run_script, script_path)
            else:
                schedule.every().day.at(scheduled_time).do(self.run_script, script_path)

    def run(self):
        self.schedule_tasks()
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    scheduler = TaskScheduler()
    scheduler.add_task('example_script.py', '15:00', repeat=True, interval='daily')
    scheduler.run()