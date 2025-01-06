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
