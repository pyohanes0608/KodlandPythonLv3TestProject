# commands.py Contains the bot commands and their logic
from discord.ext import commands
from database import add_task_to_db, delete_task_from_db, get_all_tasks, mark_task_as_completed

def register_commands(bot):

    @bot.command(name="add_task")
    async def add_task(ctx, *, description: str):
        task_id = add_task_to_db(description)
        await ctx.send(f"Task added with ID {task_id}: {description}")

    @bot.command(name="delete_task")
    async def delete_task(ctx, task_id: int):
        rows_deleted = delete_task_from_db(task_id)
        if rows_deleted > 0:
            await ctx.send(f"Task {task_id} deleted.")
        else:
            await ctx.send(f"Task {task_id} not found.")

    @bot.command(name="show_tasks")
    async def show_tasks(ctx):
        tasks = get_all_tasks()
        if not tasks:
            await ctx.send("No tasks available.")
            return

        task_list = [
            f"ID: {task[0]} | Description: {task[1]} | Completed: {'Yes' if task[2] else 'No'}"
            for task in tasks
        ]
        await ctx.send("\n".join(task_list))

    @bot.command(name="complete_task")
    async def complete_task(ctx, task_id: int):
        rows_updated = mark_task_as_completed(task_id)
        if rows_updated > 0:
            await ctx.send(f"Task {task_id} marked as completed.")
        else:
            await ctx.send(f"Task {task_id} not found.")
