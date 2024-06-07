A good pyInstaller instructions:
- https://www.youtube.com/watch?v=UZX5kH72Yx4

Some interesting discussions about how to use pyinstaller and streamlit together:
- https://discuss.streamlit.io/t/using-pyinstaller-or-similar-to-create-an-executable/902
- https://github.com/jvcss/PyInstallerStreamlit/tree/master

Some interesting discussions about how to use pyinstaller and llama.cpp together:
- https://github.com/ggerganov/llama.cpp/issues/2558
- https://github.com/abetlen/llama-cpp-python/pull/709/files

The command used to generate the .exe with pyinstaller is: \
cd "C:\Users\014206631\Python\Llama chat\pyinstaller"

conda activate llamaChat

pip install pyinstaller

pyinstaller --onefile -w main.py  

Remember to change the path to your directories. The user path may also appear inside the .py and .iss files.
