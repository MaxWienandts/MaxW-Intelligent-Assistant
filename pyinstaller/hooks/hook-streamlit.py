# Hook to use streamlit
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import copy_metadata
datas = copy_metadata('streamlit')
datas += [(
	  	"C:\\Users\\014206631\\AppData\\Local\\miniconda3\\envs\\llamaChat\\Lib/site-packages/streamlit/static",
	       	"./streamlit/static"
	 )]
datas += [(
	  	"C:\\Users\\014206631\\AppData\\Local\\miniconda3\\envs\\llamaChat\\Lib/site-packages/streamlit/runtime",
        	"./streamlit/runtime"
	 )]

datas += collect_data_files('altair')

