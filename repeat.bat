@echo off
for %%i in (*.csv) do mongoimport --db NASAProject --type csv --file %%i --headerline