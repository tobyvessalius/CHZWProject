@echo off
for %%i in (*.csv) do mongoimport --db NASAProject --collection Arizona --type csv --file %%i --headerline