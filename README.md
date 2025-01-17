# TaskScheduler

TaskScheduler is a Python program designed to automate the running of scripts or programs at specific times on Windows. This can be particularly useful for scheduling repetitive tasks or automating routine operations.

## Features

- Schedule scripts to run at specific times.
- Supports daily and hourly repetition of tasks.
- Simple and easy-to-use interface for adding and managing tasks.

## Requirements

- Python 3.x
- `schedule` module

You can install the `schedule` module using pip:

```bash
pip install schedule
```

## Usage

1. Clone the repository or download the `taskscheduler.py` file.

2. Ensure you have Python installed on your Windows machine.

3. Open `taskscheduler.py` in a text editor and add your scripts and desired schedules using the `add_task` method:

```python
scheduler.add_task('example_script.py', '15:00', repeat=True, interval='daily')
```

4. Run the TaskScheduler script:

```bash
python taskscheduler.py
```

5. The program will run in the background and execute your tasks according to the schedule.

## Example

Here's how you can add a task to run `example_script.py` every day at 15:00:

```python
scheduler = TaskScheduler()
scheduler.add_task('example_script.py', '15:00', repeat=True, interval='daily')
scheduler.run()
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## Contact

For any questions or inquiries, please contact `your-email@example.com`.