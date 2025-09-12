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


def convert_df_to_csv(df):
    """
    Simple df to csv conversion.

    Args:
        df (pd.DataFrame): The dataframe

    Returns:
        bytes: Csv file on bytes format.
    """
    return df.to_csv(index=False).encode("utf-8")


def make_csv_download_button(df, filename="data.csv", description="Download table as CSV", key=None):
    """
    Makes a simple download button for a dataframe.

    Args:
        df (pd.DataFrame): The df to download.
        filename (str): Filename of the file to be downloaded.
        description (str, optional): Text to be in button. Defaults to "Download table as CSV".
        key (str): Streamlit key identifier. Streamlit usually makes unique keys, but can fail if the object is called
            in multiple times in similar context. The key need to be unique for each item.
    """
    st.download_button(
        label=description,
        data=convert_df_to_csv(df),
        file_name=filename,
        mime="text/csv",  # Multipurpose Internet Mail Extensions
        key=key,
    )


def make_excel_download_button(excel_data, filename="data.xlsx", description="Download table as Excel", key=None):
    """
    Makes a button for downloading excel data.

    Args:
        excel_data (bytes): The table on bytes format. Use functions from src.utils.excel_utils.py for this.
        filename (str): Filename of the file to be downloaded.
        description (str, optional): Text to be in button. Defaults to "Download table as CSV".
        key (str): Streamlit key identifier. Streamlit usually makes unique keys, but can fail if the object is called
            in multiple times in similar context. The key need to be unique for each item.
    """
    st.download_button(
        label=description,
        data=excel_data,
        file_name=filename,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        key=key,
    )


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
