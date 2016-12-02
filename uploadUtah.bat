@echo off
for %%i in (*.csv) do mongoimport --db NASAProject --collection Utah --type csv --file %%i --headerline