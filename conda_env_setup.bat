setlocal
set ENV_NAME="PythonAutomation101"
call conda create -n %ENV_NAME% python=3.8 -y
call conda activate %ENV_NAME%
call pip install selenium==3.141.0
call pip install pyautogui==0.9.50
call pip install pynput==1.6.8
call conda install pywin32==227 -y
endlocal
