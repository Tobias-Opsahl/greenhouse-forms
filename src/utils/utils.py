import base64
from pathlib import Path

import streamlit as st

from src.utils.constants import FONTS_FOLDER_PATH


def load_font(font_filename, font_folder_path=FONTS_FOLDER_PATH):
    """
    Loads a font on base64 format, `.woff2` filename ending.

    Args:
        font_filename (str): Filename of the font
        font_folder_path (Path or str, optional): Path to the folder where the fonts are saved.
            Defaults to FONTS_FOLDER_PATH.

    Returns:
        str: The font decoded in UTF-8.
    """
    font_path = Path(font_folder_path) / font_filename
    with open(font_path, "rb") as infile:
        data = infile.read()
    encoded = base64.b64encode(data).decode("utf-8")
    return encoded


def safe_render(render_function, show_expander, *args, **kwargs):
    """
    Try to render a part of a dashboard in a safe way, that catches exceptions and displays them on a readable format.

    Args:
        render_function (callable): The function to call
        show_expander (bool): Wehter or not to display the full Error message.

    Returns:
        any / None: The return of the callable, or None of it fails.
    """
    try:
        return render_function(*args, **kwargs)

    except Exception as error:  # Anything else has failed
        message = "An unexpected error has occoured."
        st.error(message)
        if show_expander:
            with st.expander("Detailed error message"):
                st.write(error)
