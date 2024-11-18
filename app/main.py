from .test import render_test
from .modules.tool_01.v1.main import render_tool_01
from .modules.tool_02.v1.main import render_tool_02
import streamlit as st

def main():

    func_map = {"Test": render_test, "Tool 1": render_tool_01, "Tool 2": render_tool_02}

    pg = st.navigation([st.Page(v, title=k) for k, v in func_map.items()])
    pg.run()
