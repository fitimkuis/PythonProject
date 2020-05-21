@echo on
setlocal EnableDelayedExpansion
rem Get path from first parameter
set robot_path = %1
set output = %2
set runpath = %3

echo %robot_path%
echo %outputdir%

rem Start pabot
cd %3
pabot --processes 5 --outputdir %2 %1