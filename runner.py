import sys
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "dashboard_livros_amazon.py"]
sys.exit(stcli.main())