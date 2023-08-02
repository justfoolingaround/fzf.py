import enum
from typing import Optional


class Algorithm(enum.Enum):
    V1 = "v1"
    V2 = "v2"


class TiebreakSetting(enum.Enum):
    LENGTH = "length"
    BEGIN = "begin"
    END = "end"
    INDEX = "index"


class Layout(enum.Enum):
    DEFAULT = "default"
    REVERSE = "reverse"
    REVERSE_LIST = "reverse-list"


class BorderStyle(enum.Enum):
    ROUNDED = "rounded"
    SHARP = "sharp"
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
    TOP = "top"
    BOTTOM = "bottom"
    LEFT = "left"
    RIGHT = "right"
    NONE = "none"


class InfoStyle(enum.Enum):
    DEFAULT = "default"
    INLINE = "inline"
    HIDDEN = "hidden"


def get_opts(
    extended: bool = True,
    match_exact: bool = False,
    case_insensitive: bool = True,
    normalise_literals: bool = True,
    algo_type: Algorithm = Algorithm.V2,
    field_index_expressions: Optional[str] = None,
    with_field_index_expressions: Optional[str] = None,
    delimiter: Optional[str] = None,
    disable_search: bool = False,
    sort_results: bool = True,
    reverse_results: bool = False,
    tiebreak_settings: Optional[TiebreakSetting] = None,
    multi=False,
    mouse=True,
    keybinds: Optional[str] = None,
    cycle=False,
    keep_right=False,
    scroll_off_lines: Optional[int] = None,
    disable_horizontal_scroll=False,
    filepath_word=False,
    jump_labels: Optional[str] = None,
    height: Optional[str] = None,
    minimum_height: Optional[str] = None,
    layout: Optional[Layout] = None,
    reversed_layout: bool = False,
    border_style: Optional[BorderStyle] = None,
    only_ascii_borders: bool = False,
    margin: Optional[str] = None,
    padding: Optional[str] = None,
    info_style: Optional[InfoStyle] = None,
    hide_info: bool = False,
    prompt_string: Optional[str] = None,
    pointer_string: Optional[str] = None,
    selected_string: Optional[str] = None,
    header: Optional[str] = None,
    header_lines: Optional[int] = None,
    header_first: bool = False,
    ansi: bool = False,
    tab_character_number: Optional[int] = None,
    color: Optional[str] = None,
    bold_off: bool = False,
    use_black_background: bool = False,
    history_file: Optional[str] = None,
    history_size: Optional[int] = None,
    preview: Optional[str] = None,
    preview_window_settings: Optional[str] = None,
    query: Optional[str] = None,
    select_first: bool = False,
    exit_when_empty: bool = False,
    filter_mode: Optional[str] = None,
    print_query: bool = False,
    expect_keys: Optional[str] = None,
    read0: bool = False,
    print0: bool = False,
    clear_screen: bool = True,
    sync: bool = False,
):
    opts = ()

    if extended:
        opts += ("-x",)
    else:
        opts += ("+x",)

    if match_exact:
        opts += ("-e",)

    if case_insensitive:
        opts += ("-i",)
    else:
        opts += ("+i",)

    if not normalise_literals:
        opts += ("--literals",)

    if algo_type is not None:
        opts += (f"--algo={algo_type.value}",)

    if field_index_expressions is not None:
        opts += (f"-n={field_index_expressions}",)

    if with_field_index_expressions is not None:
        opts += (f"--with-nth={with_field_index_expressions}",)

    if delimiter is not None:
        opts += (f"-d={delimiter}",)

    if disable_search:
        opts += ("--disabled",)

    if not sort_results:
        opts += ("+s",)

    if reverse_results:
        opts += ("--tac",)

    if tiebreak_settings is not None:
        opts += (f"--tiebreak={tiebreak_settings.value}",)

    if multi:
        opts += ("-m",)

    if not mouse:
        opts += ("--no-mouse",)

    if keybinds is not None:
        opts += (f"--bind={keybinds}",)

    if cycle:
        opts += ("--cycle",)

    if keep_right:
        opts += ("--keep-right",)

    if scroll_off_lines is not None:
        opts += (f"--scroll-off={scroll_off_lines}",)

    if disable_horizontal_scroll:
        opts += ("--no-hscroll",)

    if filepath_word:
        opts += ("--filepath-word",)

    if jump_labels is not None:
        opts += (f"--jump-labels={jump_labels}",)

    if height is not None:
        opts += (f"--height={height}",)

    if minimum_height is not None:
        opts += (f"--min-height={minimum_height}",)

    if layout is not None:
        opts += (f"--layout={layout.value}",)

    if reversed_layout:
        opts += ("--reverse",)

    if border_style is not None:
        opts += (f"--border={border_style.value}",)

    if only_ascii_borders:
        opts += ("--no-unicode",)

    if margin is not None:
        opts += (f"--margin={margin}",)

    if padding is not None:
        opts += (f"--padding={padding}",)

    if info_style is not None:
        opts += (f"--info={info_style.value}",)

    if hide_info:
        opts += ("--no-info",)

    if prompt_string is not None:
        opts += (f"--prompt={prompt_string}",)

    if pointer_string is not None:
        opts += (f"--pointer={pointer_string}",)

    if selected_string is not None:
        opts += (f"--selected={selected_string}",)

    if header is not None:
        opts += (f"--header={header}",)

    if header_lines is not None:
        opts += (f"--header-lines={header_lines}",)

    if header_first:
        opts += ("--header-first",)

    if ansi:
        opts += ("--ansi",)

    if tab_character_number is not None:
        opts += (f"--tabstop={tab_character_number}",)

    if color is not None:
        opts += (f"--color={color}",)

    if bold_off:
        opts += ("--no-bold",)

    if use_black_background:
        opts += ("--black",)

    if history_file is not None:
        opts += (f"--history-file={history_file}",)

    if history_size is not None:
        opts += (f"--history-size={history_size}",)

    if preview is not None:
        opts += (f"--preview={preview}",)

    if preview_window_settings is not None:
        opts += (f"--preview-window={preview_window_settings}",)

    if query is not None:
        opts += (f"--query={query}",)

    if select_first:
        opts += ("-1",)

    if exit_when_empty:
        opts += ("-0",)

    if filter_mode is not None:
        opts += (f"--filter={filter_mode}",)

    if print_query:
        opts += ("--print-query",)

    if expect_keys is not None:
        opts += (f"--expect={expect_keys}",)

    if read0:
        opts += ("--read0",)

    if print0:
        opts += ("--print0",)

    if not clear_screen:
        opts += ("--no-clear",)

    if sync:
        opts += ("--sync",)

    return opts
