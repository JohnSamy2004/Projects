import io
import sys
from project import add, view, mark, delete

def test_add():
    tasks = []
    assert add(tasks, "Study Python") == True
    assert add(tasks, "  ") == False
    assert tasks == ["Study Python"]

def test_mark():
    tasks = ["Study Python", "Clean room"]
    done_tasks = []

    # Mark first task
    result = mark(tasks, done_tasks, 1)
    assert result == 'Task "Study Python" marked as done!'
    assert done_tasks == ["Study Python"]

    # Try marking same task again
    result = mark(tasks, done_tasks, 1)
    assert result == "This task is already marked as done!"

    # Try marking invalid number
    result = mark(tasks, done_tasks, 5)
    assert result == "Invalid number!"

def test_delete():
    tasks = ["Study Python", "Clean room"]
    done_tasks = ["Clean room"]

    result = delete(tasks, done_tasks, 2)
    assert result == "Task Clean room deleted successfully!"
    assert tasks == ["Study Python"]
    assert done_tasks == []

    # Try deleting invalid number
    result = delete(tasks, done_tasks, 5)
    assert result == "Task number not found! Try again."

def test_view(capsys):
    tasks = ["Study Python", "Clean room"]
    done_tasks = ["Clean room"]
    view(tasks, done_tasks)
    captured = capsys.readouterr()
    assert "1. Study Python" in captured.out
    assert "2. Clean room [Done]" in captured.out


if __name__ == "__main__":
    print("✅ Running tests...")
    test_add()
    test_mark()
    test_delete()

    # capsys only works with pytest, so we simulate view test manually
    sys.stdout = io.StringIO()
    view(["Study Python", "Clean room"], ["Clean room"])
    output = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__
    assert "1. Study Python" in output
    assert "2. Clean room [Done]" in output
    print("✅ All tests passed successfully!")
