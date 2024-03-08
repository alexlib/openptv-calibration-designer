# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to OpenPTV 3D calibration target designer 👋")

    st.sidebar.success("Select the page on the left, start by loading the 3D points CSV")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.

        OpenPTV is an open-source 3D particle tracking velocimetry software

        **👈 Select a step from the sidebar** 

        ### Want to learn more about Streamlit? 
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)

        ### Want to learn more about OpenPTV? 
        - Check out [www.openptv.net](https://www.openptv.net)
        - Jump into our documentation [openptv-docs](https://openptv-python.readthedocs.io/en/latest/)
    """
    )


if __name__ == "__main__":
    run()
