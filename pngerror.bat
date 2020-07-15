set win=c:\windows\system32\
rem set python_path="C:\Users\AlexB\PycharmProjects\train\venv\Scripts\python.exe"
set magik_path="C:\Program Files\ImageMagick-7.0.10-Q16\imdisplay.exe"
pause
echo PREPARING ENVIRONNEMENT FOR PNG MODIFICATIONS ==== dl files
echo Comment the next line if magick is already installed
rem start https://www.techspot.com/downloads/downloadnow/5515/?evp=7daa0b52c44cabf34a2fc0fb7f3f5781&file=1
dir
set /P path=Choose repository with PNG images:
cd %path%
echo ************ USE THIS SCRIPT **************** 
%win%magick mogrify -format png *.png
echo png files corrected
pause