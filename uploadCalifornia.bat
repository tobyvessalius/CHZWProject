@echo off
for %%i in (*.csv) do mongoimport --db NASAProject --collection California --type csv --file %%i --headerline