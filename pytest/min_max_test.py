import subprocess
import algo

def test_min():
    values = (2, 3, 1, 4, 6)
    val = algo.min(values)
    assert val == 1

def test_max():
    values = (2, 3, 1, 4, 6)
    val = algo.max(values)
    assert val == 6

def execute_pytest():
    subprocess.call([r'C:\Users\fitim\IdeaProjects\PythonProject\PythonProject\pytest\run_pytest.bat'])

#execute_pytest()