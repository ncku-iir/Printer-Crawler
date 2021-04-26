@echo off
call C:{}\miniconda3\Scripts\activate.bat
call conda activate {}
call python J:{}\main.py