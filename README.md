This project covers all the requested bot functionalities: adding, deleting, displaying, and completing tasks using an SQLite database.

The code has been split into three separate files: bot.py, database.py, and commands.py. Each file has a specific responsibility:

bot.py: Initializes the bot and handles startup.
database.py: Manages all database operations.
commands.py: Contains the bot commands and their logic.

The test files have been divided and created for each functionality:

test_add_task.py: Tests adding tasks.
test_delete_task.py: Tests deleting tasks.
test_show_tasks.py: Tests displaying tasks.
test_complete_task.py: Tests marking tasks as completed.
These files ensure isolated unit testing for each function.

## Discord Task Bot

Discord Task Bot is a simple tool for managing tasks within small teams. It supports adding, deleting, displaying, and marking tasks as completed. Task data is stored in a SQLite database.

### Features
- **Add Task**: Add a new task with a description.
- **Delete Task**: Remove a task by its ID.
- **Show Tasks**: Display all tasks with their IDs and completion statuses.
- **Complete Task**: Mark a task as completed by its ID.

### Commands
| Command                  | Description                                   |
|--------------------------|-----------------------------------------------|
| `!add_task <description>` | Adds a task with the given description.      |
| `!delete_task <task_id>`  | Deletes a task with the specified ID.        |
| `!show_tasks`             | Displays a list of all tasks.                |
| `!complete_task <task_id>`| Marks the task with the specified ID as completed. |

### Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd KodlandPythonLv3TestProject
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the SQLite database:
    ```bash
    python -c "from database import init_db; init_db()"
    ```

4. Run the bot:
    ```bash
    python bot.py
    ```

### Environment Variables
- **DISCORD_BOT_TOKEN**: Set your Discord bot token as an environment variable or replace the placeholder in `bot.py`.

### Tests
The project includes tests for all key functionalities:
- **Add Task**: Verifies that tasks are added correctly to the database.
- **Delete Task**: Confirms that tasks can be deleted using their IDs.
- **Show Tasks**: Ensures all tasks are displayed properly.
- **Complete Task**: Validates marking tasks as completed.

To run the tests:
```bash
python -m unittest discover tests
```

### Project Structure
```
.
├── bot.py               # Main bot file
├── database.py          # Database management
├── commands.py          # Command definitions
├── tests/               # Unit tests
│   ├── test_add_task.py
│   ├── test_delete_task.py
│   ├── test_show_tasks.py
│   └── test_complete_task.py
├── requirements.txt     # Dependencies
└── README.md            # Documentation
