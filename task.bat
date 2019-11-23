SET logfile="D:\Documents\Discordbot-Voter\log-voter.txt"
@echo off
@echo Starting Script at %date% %time%
"C:\Python27\python.exe" "D:\Documents\Discordbot-Voter\main.py"
@echo finished at %date% %time% >> %logfile%
