:: Turns off echo
ECHO OFF

:: Sets a logfile
SET logfile=voter-log.txt

:: Starts the script while echoing the date and time
ECHO [+] Starting Script at %date% %time%....
python main.py
:: Leaves a line for the next sentence, makes it more readable.
ECHO:

:: Saves logs to the logfile
ECHO [+] Script completed! Saving logfile....

:: Saves a minimal log to the logfile
ECHO finished at %date% %TIME% >> %logfile%
PAUSE
