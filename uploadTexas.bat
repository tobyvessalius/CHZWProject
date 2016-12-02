@echo off
for %%i in (*.csv) do mongoimport --db NASAProject --collection Texas --type csv --file %%i --headerline