# ---------------------------------------------------------
# file:   $XDG_CONFIG_HOME/.config/qutebrowser/config.py
# author: michael haney
# ---------------------------------------------------------

# uncomment to configure with autoconfig.yml
# config.load_autoconfig()

# Aliases for commands. The keys of the given dictionary are the
# aliases, while the values are the commands they map to.
# Type: Dict
c.aliases = {'q': 'quit', 'w': 'session-save', 'wq': 'quit --save'}

# Always restore open sites when qutebrowser is reopened.
# Type: Bool
c.auto_save.session = True

# Enable/disable JavaScript.
c.content.javascript.enabled = True

c.content.javascript.prompt = False

# Background color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #888888, stop:1 #505050)'

# Foreground color of completion widget category headers.
# Type: QtColor
c.colors.completion.category.fg = '#dcdccc'

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = '#323232'

# Text color of the completion widget.
# Type: QtColor
c.colors.completion.fg = '#dcdccc'

# Foreground color of the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.fg = 'black'

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = '#4b4b4b'

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = '#000000'

# Foreground color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.fg = '#dcdccc'

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = '#5f7f5f'

# Foreground color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = '#dcdccc'

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = '#000000'

# Foreground color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.fg = '#dcdccc'

# Foreground color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.fg = '#dcdccc'

# Background color of the progress bar.
# Type: QssColor
c.colors.statusbar.progress.bg = '#dcdccc'

# Foreground color of the URL in the statusbar on error.
# Type: QssColor
c.colors.statusbar.url.error.fg = 'orange'

# Default foreground color of the URL in the statusbar.
# Type: QssColor
c.colors.statusbar.url.fg = '#dcdccc'

# Foreground color of the URL in the statusbar on successful load
# (http).
# Type: QssColor
c.colors.statusbar.url.success.http.fg = '#dcdccc'

# Foreground color of the URL in the statusbar on successful load
# (https).
# Type: QssColor
c.colors.statusbar.url.success.https.fg = '#dcdccc'

# Background color of the tab bar.
# Type: QtColor
c.colors.tabs.bar.bg = '#000000'

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = '#323232'

# Foreground color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.fg = '#dcdccc'

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = '#323232'

# Foreground color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.fg = '#dcdccc'

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = '#585858'

# Foreground color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.fg = '#dcdccc'

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = '#585858'

# Foreground color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.fg = '#dcdccc'

# Background color for webpages if unset (or empty to use the theme's
# color)
# Type: QtColor
c.colors.webpage.bg = '#dcdccc'

# Size of the HTTP network cache. Null to use the default value. With
# QtWebEngine, the maximum supported value is 2147483647 (~2 GB).
# Type: Int
c.content.cache.size = None

# List of URLs of lists which contain hosts to block.  The file can be
# in one of the following formats:  - An `/etc/hosts`-like file - One
# host per line - A zip-file of any of the above, with either only one
# file, or a file named   `hosts` (with any extension).
# Type: List of Url
c.content.host_blocking.lists = ['https://www.malwaredomainlist.com/hostslist/hosts.txt', 'http://someonewhocares.org/hosts/hosts', 'http://winhelp2002.mvps.org/hosts.zip', 'http://malwaredomains.lehigh.edu/files/justdomains.zip', 'https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&mimetype=plaintext']

# Whether images are automatically loaded in web pages.
# Type: Bool
c.content.images = True

# Enables or disables plugins in Web pages.
# Type: Bool
c.content.plugins = True

# The editor (and arguments) to use for the `open-editor` command. `{}`
# gets replaced by the filename of the file to be edited.
# Type: ShellCommand
c.editor.command = ['emacsclient', '-cn', '{}']

# Encoding to use for the editor.
# Type: Encoding
c.editor.encoding = 'utf-8'

# Font used in the completion categories.
# Type: Font
c.fonts.completion.category = 'bold 10pt monospace'

# Font used in the completion widget.
# Type: Font
c.fonts.completion.entry = '10pt monospace'

# Width of scrollbar in completion window (in px).
# Value of 0 disables scrollbar.
c.completion.scrollbar.width = 0

# Padding of scrollbar handle in completion window (in px).
c.completion.scrollbar.padding = 2

# Font used for the debugging console.
# Type: QtFont
c.fonts.debug_console = '10pt monospace'

# Font used for the downloadbar.
# Type: Font
c.fonts.downloads = '10pt monospace'

# Font used for the hints.
# Type: Font
c.fonts.hints = 'bold 10pt DejaVu Sans Mono'

c.hints.chars = "asdfghjkl"

# Font used in the keyhint widget.
# Type: Font
c.fonts.keyhint = '10pt monospace'

# Font used for error messages.
# Type: Font
c.fonts.messages.error = '10pt monospace'

# Font used for info messages.
# Type: Font
c.fonts.messages.info = '10pt monospace'

# Font used for warning messages.
# Type: Font
c.fonts.messages.warning = '10pt monospace'

# Font used for prompts.
# Type: Font
c.fonts.prompts = '10pt sans-serif'

# Font used in the statusbar.
# Type: Font
c.fonts.statusbar = 'bold 9pt DejaVu Sans Mono'

# Font used in the tab bar.
# Type: QtFont
c.fonts.tabs = 'bold 8.5pt DejaVu Sans Mono'

# Font family for standard fonts.
# Type: FontFamily
c.fonts.web.family.standard = None

# Padding for the statusbar.
# Type: Padding
c.statusbar.padding = {'bottom': 1, 'left': 1, 'right': 5, 'top': 1}

# The position of the status bar.
# Type: VerticalPosition
# Valid values:
#   - top
#   - bottom
c.statusbar.position = 'bottom'

# Hide statusbar unless a message is shown.
# Valid values: bool
c.statusbar.hide = False

# Open new tabs (middleclick/ctrl+click) in the background.
# Type: Bool
c.tabs.background = False

# Scaling for favicons in the tab bar. The tab size is unchanged, so big
# favicons also require extra `tabs.padding`.
# Type: Float
c.tabs.favicons.scale = 1.3

# Show favicons in the tab bar.
# Type: Bool
c.tabs.favicons.show = True

# Padding for tab indicators
# Type: Padding
c.tabs.indicator_padding = {'bottom': 3, 'left': 1, 'right': 5, 'top': 3}

# Behavior when the last tab is closed.
# Type: String
# Valid values:
#   - ignore: Don't do anything.
#   - blank: Load a blank page.
#   - startpage: Load the start page.
#   - default-page: Load the default page.
#   - close: Close the window.
c.tabs.last_close = 'close'

# Padding around text for tabs
# Type: Padding
c.tabs.padding = {'bottom': 2, 'left': 0, 'right': 0, 'top': 2}

# The position of the tab bar.
# Type: Position
# Valid values:
#   - top
#   - bottom
#   - left
#   - right
c.tabs.position = 'left'

# Which tab to select when the focused tab is removed.
# Type: SelectOnRemove
# Valid values:
#   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
#   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
#   - last-used: Select the previously selected tab.
c.tabs.select_on_remove = 'prev'

# When to show the tab bar.
# Type: String
# Valid values:
#   - always: Always show the tab bar.
#   - never: Always hide the tab bar.
#   - multiple: Hide the tab bar if only one tab is open.
#   - switching: Show the tab bar when switching tabs.
c.tabs.show = 'multiple'

# Time to show the tab bar before hiding it when tabs.show is set to
# 'switching'.
# Type: Int
c.tabs.show_switching_delay = 400

# Open a new window for every tab.
# Type: Bool
c.tabs.tabs_are_windows = False

# The format to use for the tab title. The following placeholders are
# defined:  * `{perc}`: The percentage as a string like `[10%]`. *
# `{perc_raw}`: The raw percentage, e.g. `10` * `{title}`: The title of
# the current web page * `{title_sep}`: The string ` - ` if a title is
# set, empty otherwise. * `{index}`: The index of this tab. * `{id}`:
# The internal tab ID of this tab. * `{scroll_pos}`: The page scroll
# position. * `{host}`: The host of the current web page. * `{backend}`:
# Either ''webkit'' or ''webengine'' * `{private}` : Indicates when
# private mode is enabled.
# Type: FormatString
c.tabs.title.format = '{title}'

# The width of the tab bar if it's vertical, in px or as percentage of
# the window.
# Type: PercOrInt
c.tabs.width.bar = '11%'

# Width of the progress indicator (0 to disable).
# Type: Int
c.tabs.width.indicator = 0

# The page to open if :open -t/-b/-w is used without URL. Use
# `about:blank` for a blank page.
# Type: FuzzyUrl
c.url.default_page = 'about:blank'

# Definitions of search engines which can be used via the address bar.
# Maps a searchengine name (such as `DEFAULT`, or `ddg`) to a URL with a
# `{}` placeholder. The placeholder will be replaced by the search term,
# use `{{` and `}}` for literal `{`/`}` signs. The searchengine named
# `DEFAULT` is used when `url.auto_search` is turned on and something
# else than a URL was entered to be opened. Other search engines can be
# used by prepending the search engine name to the search term, e.g.
# `:open google qutebrowser`.
# Type: Dict

# c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}',
#                        'ao': 'http://web.archive.org/web/*/{}',
#                        'aw': 'https://wiki.archlinux.org/?search={}',
#                        'ra': 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/archlinux',
#                        'rb': 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/bioinformatics',
#                        're': 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/emacs',
#                        'ri': 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/i3wm',
#                        'rl': 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/linux',
#                        'ro': 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/orgmode',
#                        'rq': 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/qutebrowser',
#                        'rr': 'https://duckduckgo.com/?q={}+site%3Areddit.com',
#                        'rs': 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/startpages',
#                        'rt': 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/thinkpad',
#                        'ru': 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/unixporn'}

c.url.searchengines['gh'] = 'https://github.com/search?q={}&type=Code'
c.url.searchengines['ra'] = 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/archlinux'
c.url.searchengines['rb'] = 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/bioinformatics'
c.url.searchengines['re'] = 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/emacs'
c.url.searchengines['ri'] = 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/i3wm'
c.url.searchengines['rl'] = 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/linux'
c.url.searchengines['ro'] = 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/orgmode'
c.url.searchengines['rq'] = 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/qutebrowser'
c.url.searchengines['rr'] = 'https://duckduckgo.com/?q={}+site%3Areddit.com'
c.url.searchengines['rs'] = 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/startpages'
c.url.searchengines['rt'] = 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/thinkpad'
c.url.searchengines['ru'] = 'https://duckduckgo.com/?q={}+site%3Areddit.com/r/unixporn'
c.url.searchengines['wa'] = 'https://wiki.archlinux.org/?search={}'
c.url.searchengines['y'] = 'https://www.youtube.com/results?search_query={}'

# The page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = 'about:blank'

# The format to use for the window title. The following placeholders are
# defined:  * `{perc}`: The percentage as a string like `[10%]`. *
# `{perc_raw}`: The raw percentage, e.g. `10` * `{title}`: The title of
# the current web page * `{title_sep}`: The string ` - ` if a title is
# set, empty otherwise. * `{id}`: The internal window ID of this window.
# * `{scroll_pos}`: The page scroll position. * `{host}`: The host of
# the current web page. * `{backend}`: Either ''webkit'' or
# ''webengine'' * `{private}` : Indicates when private mode is enabled.
# Type: FormatString
c.window.title_format = '{perc}{title}'

# The default zoom level.
# Type: Perc
c.zoom.default = '80'

# The available zoom levels.
# Type: List of Perc
c.zoom.levels = ['25%', '33%', '50%', '67%', '75%', '90%', '100%', '110%', '125%', '150%', '175%', '200%', '250%', '300%', '400%', '500%']

# Bindings for normal mode
config.bind(',I', 'set content.images false ;; reload')
config.bind(',i', 'set content.images true ;; reload')
config.bind(',p', 'hint links spawn curl {hint-url}')
config.bind('m', 'hint links spawn nohup mpv {hint-url}')
config.bind('wa', 'open https://web.archive.org/web/{url}')
config.bind('po', 'open https://getpocket.com/edit?url={url}')

# No idea what this does
# config.bind('gi', 'enter-mode insert ;; jseval --quiet var inputs = document.getElementsByTagName("input"); for(var i = 0; i < inputs.length; i++) { var hidden = false; for(var j = 0; j < inputs[i].attributes.length; j++) { hidden = hidden || inputs[i].attributes[j].value.includes("hidden"); }; if(!hidden) { inputs[i].focus(); break; } }')
