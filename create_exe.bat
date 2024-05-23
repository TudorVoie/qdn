del notification.exe
pyinstaller --onefile --noconsole notification.py
rmdir /S /Q build
cd dist
move notification.exe ..
cd ..
rmdir /S /Q dist
del notification.spec
echo Finished!
pause