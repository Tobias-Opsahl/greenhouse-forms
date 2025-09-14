# These are the official DNB colors, from https://eufemia.dnb.no/quickguide-designer/colors/.
# Do not change them, change the `colors` dictionary instead.
DNB_COLORS = {
    "profile": {
        "seagreen": "#007272",
        "mintgreen": "#a5e1d2",
        "summergreen": "#28b482",
        "emeraldgreen": "#14555a",
        "oceangreen": "#00343e",
        "accent-yellow": "#fdbb31",
        "indigo": "#23195a",
        "violet": "#6e2382",
        "skyblue": "#4bbed2",
        "lavender": "#f2f2f5",
        "sand-yellow": "#fbf6ec",
        "pistachio": "#f2f4ec",
    },
    "ux": {
        "seagreen-30": "#b3d5d5",
        "mintgreen-50": "#d2f0e9",
        "mintgreen-25": "#e9f8f4",
        "mintgreen-12": "#f3fbf9",
        "accent-yellow-30": "#feebc1",
        "fire-red": "#dc2a2a",
        "fire-red-8": "#fdeeee",
        "success-green": "#007b5e",
        "signal-orange": "#ff5400",
        "black": "#000",
        "black-80": "#333",
        "black-55": "#737373",
        "black-20": "#ccc",
        "black-8": "#ebebeb",
        "black-3": "#f8f8f8",
        "white": "#fff",
        # Aliases for black color names:
        "coal": "#333",
        "dark-gray": "#737373",
        "soft-gray": "#ccc",
        "outline-gray": "#ebebeb",
        "subtle-gray": "#f8f8f8",
    },
}

# Additional colors. These were needed to supply the DNB-colors. Do not change these, change `colors` instead.
ADDITIONAL_COLORS = {
    "smooth-white": "#fafafa",  # Smoother white.
    "smooth-black": "#2e2e2e",  # Smoother black.
}

# These are the colors that are used. If they are changed, so will the colors of the app be.
# The values should refer to `DNB_COLORS` or `ADDITIONAL_COLORS`. If other colors is needed, add them
# to `ADDITIONAL_COLORS`.
colors = {
    "background-color": DNB_COLORS["ux"]["mintgreen-50"],
    "sidebar-background": DNB_COLORS["ux"]["mintgreen-25"],
    "container-background": ADDITIONAL_COLORS["smooth-white"],
    "container-outline": ADDITIONAL_COLORS["smooth-white"],
    "hover-option": DNB_COLORS["ux"]["mintgreen-50"],
    "clicked-option": DNB_COLORS["ux"]["mintgreen-50"],
    "selected-tab": DNB_COLORS["ux"]["coal"],
    "hovered-tab": DNB_COLORS["ux"]["coal"],
    "button-color": DNB_COLORS["ux"]["mintgreen-50"],
    "hovered-button": DNB_COLORS["profile"]["mintgreen"],
    "expander-color": ADDITIONAL_COLORS["smooth-white"],
    "expander-border": ADDITIONAL_COLORS["smooth-white"],
    "fail-red": DNB_COLORS["ux"]["fire-red"],
    "smooth-white": ADDITIONAL_COLORS["smooth-white"],
    "smooth-black": ADDITIONAL_COLORS["smooth-black"],
}
