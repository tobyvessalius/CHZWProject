@echo off
for %%i in (*.csv) do mongoimport --db NASAProject --collection NewMexico --type csv --file %%i --headerline