echo on
set filename=%1
FOR /L %%A IN (1,1,2) DO (
  python -m robot.run %filename%
  ECHO %%A
)