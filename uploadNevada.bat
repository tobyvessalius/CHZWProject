@echo off
for %%i in (*.csv) do mongoimport --db NASAProject --collection Nevada --type csv --file %%i --headerline