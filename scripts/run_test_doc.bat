cd C:\Users\fitim\IdeaProjects\PythonProject\PythonProject\testcases
set filename=%1
set html=%2
set curpath=%3
echo %filename%
python -m robot.testdoc %curpath%\%filename% %html%


