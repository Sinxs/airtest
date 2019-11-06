@echo off
start /min D:\AirtestIDE\AutoTest_Project_DRInland\platform\startdjango.bat
start /min D:\AirtestIDE\AutoTest_Project_DRInland\platform\atxserver2\rethinkdb\rethinkdb-2.3.6\rethinkdb.exe
cd D:\AirtestIDE\AutoTest_Project_DRInland\platform\atxserver2\atxserver2
start /min D:\AirtestIDE\AutoTest_Project_DRInland\platform\atxserver2\atxserver2\startatxserver2.bat
start /min D:\AirtestIDE\AutoTest_Project_DRInland\platform\atxserver2\atxserver2\startatxserver2-android-provider.bat
