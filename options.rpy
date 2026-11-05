
# ============================================
# GAME OPTIONS
# ============================================

# Game title
define config.name = _("Untitled")

# Show game title on main menu
define gui.show_name = True

# Game version
define config.version = "1.0"

# About screen description
define gui.about = _p("""
A visual novel about friendship, new beginnings,
and the unexpected moments that change everything.

Created by Iyin.
""")

# Build name
define build.name = "Untitled"


# ============================================
# SOUND AND MUSIC
# ============================================

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

# Main menu music (add later)
# define config.main_menu_music = "audio/main_theme.mp3"


# ============================================
# TRANSITIONS
# ============================================

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve

define config.after_load_transition = dissolve
define config.end_game_transition = dissolve


# ============================================
# DIALOGUE WINDOW
# ============================================

define config.window = "auto"

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


# ============================================
# TEXT PREFERENCES
# ============================================

# Text appears instantly by default
default preferences.text_cps = 0

# Auto-forward delay
default preferences.afm_time = 15


# ============================================
# SAVE DIRECTORY
# ============================================

# Keep this unchanged to preserve existing saves.
define config.save_directory = "Renpybasic-1793917359"


# ============================================
# GAME ICON
# ============================================

define config.window_icon = "gui/window_icon.png"


# ============================================
# BUILD CONFIGURATION
# ============================================

init python:

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.documentation('*.html')
    build.documentation('*.txt')
