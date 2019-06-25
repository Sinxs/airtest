@echo off
for /l %%i in (1,1,2) do (
	taskkill /f /fi "WINDOWTITLE eq start_auto"
)