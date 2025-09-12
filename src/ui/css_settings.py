from src.ui.colors import colors
from src.utils.utils import load_font

font_light = load_font("DNB-Light.woff2")
font_regular = load_font("DNB-Regular.woff2")
font_medium = load_font("DNB-Medium.woff2")
font_bold = load_font("DNB-Bold.woff2")


GLOBAL_CSS = f"""
<style>

/* Define DNB fonts */
@font-face {{
    font-family: 'DNB-FontFamily';
    src: url(data:font/woff2;charset=utf-8;base64,{font_light}) format('woff2');
    font-weight: 300; /* Light */
    font-style: normal;
}}
@font-face {{
    font-family: 'DNB-FontFamily';
    src: url(data:font/woff2;charset=utf-8;base64,{font_regular}) format('woff2');
    font-weight: 400; /* Regular */
    font-style: normal;
}}
@font-face {{
    font-family: 'DNB-FontFamily';
    src: url(data:font/woff2;charset=utf-8;base64,{font_medium}) format('woff2');
    font-weight: 500; /* Medium */
    font-style: normal;
}}
@font-face {{
    font-family: 'DNB-FontFamily';
    src: url(data:font/woff2;charset=utf-8;base64,{font_bold}) format('woff2');
    font-weight: 700; /* Bold */
    font-style: normal;
}}

/* Overwrite (almost) everything to DNB font */
* {{
    font-family: 'DNB-FontFamily', sans-serif !important;
    font-weight: 400;
}}

/* Target classes for optional light, medium and bold text */
.light-text {{
    font-family: 'DNB-FontFamily';
    font-weight: 300;
}}

.medium-text {{
    font-family: 'DNB-FontFamily';
    font-weight: 500;
}}

.bold-text {{
    font-family: 'DNB-FontFamily';
    font-weight: 700;
}}

/* Customize colors and streamlit elements */
.stApp {{
    background-color: {colors["background-color"]};
}}

/* Color of upper banner with Streamlit content */
[data-testid="stHeader"] {{
    background: {colors["background-color"]};
}}

/* Expanders */
div[data-testid="stExpander"] {{
    background-color: {colors["expander-color"]};
    border: 0.1px solid {colors["expander-border"]};
    border-radius: 5px;  /* Adjust the roundness of the corners */
    box-shadow: none;  /* Remove shadow */
}}

/* Style the expander header */
div[data-testid="stExpander"] > div:first-child {{
    background-color: {colors["expander-color"]};
    border: none;
}}

/* Make expander border invisible (or none-existent) */
[data-testid="stExpander"] details {{
    border-style: none;
}}

/* Change background color of the Streamlit sidebar. */
[data-testid=stSidebar] {{
    background-color: {colors["sidebar-background"]};
}}

/* Change color of text in tab when it is clicked. */
.st-dn:focus {{
    color: {colors["selected-tab"]};
}}

.stTabs [aria-selected="true"] {{
    color: {colors["selected-tab"]};
}}

/* Change color of text in tab when it is hovered over. */
.st-dh:hover {{
    color: {colors["hovered-tab"]};
}}

/* Change color of Streamlit download button. */
div.stDownloadButton button {{
    background-color: {colors["button-color"]};
    color: {colors["smooth-black"]};
    border: none;
}}

/* Change color when hovered over. */
div.stDownloadButton button:hover {{
    background-color: {colors["hovered-button"]};
    color: {colors["smooth-black"]};
}}

.calendar-legend {{
    height: 8em;
    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 5;
    -webkit-box-orient: vertical;
}}
</style>
"""

OPTION_MENU_CSS = {
    "container": {"background-color": colors["sidebar-background"]},
    # "icon": {"color": "orange"},
    "nav-link": {
        "--hover-color": colors["hover-option"],
        "color": "black",
        "font-family": "'DNB-FontFamily', sans-serif",
        "font-weight": "400",
    },
    "nav-link-selected": {
        "background-color": colors["clicked-option"],
        "font-family": "'DNB-FontFamily', sans-serif",
        "font-weight": "700",
    },
}

CONTAINER_CSS = f"""{{
    border: 1px solid {colors["container-outline"]};
    border-radius: 0.5rem;
    padding: calc(1em - 1px);
    background-color: {colors["container-background"]};
}}
"""

ST_AGGRID_CSS = {
    ".ag-row": {"font-family": "'DNB-FontFamily', sans-serif !important", "font-weight": "400 !important"},
    ".ag-row-hover": {
        "background-color": f"{colors['hover-option']} !important",
        "font-family": "'DNB-FontFamily', sans-serif !important",
        "font-weight": "400 !important",
    },
    ".ag-header-cell-label": {
        "font-family": "'DNB-FontFamily', sans-serif !important",
        "font-weight": "700 !important",
    },
    ".ag-cell": {"font-family": "'DNB-FontFamily', sans-serif !important", "font-weight": "400 !important"},
}

# TODO: Update with updated settings.
CALENDAR_CSS = """
.fc-event-past {
    opacity: 0.8;
}
.fc-event-time {
    font-style: italic;
}
.fc-event-title {
    font-weight: 500;
}
.fc-toolbar-title {
    font-size: 2rem;
}
"""
