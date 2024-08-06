import re
from collections import defaultdict


def markdown_sections_to_dict(md_text, break_on_level: int = 1) -> dict:
    header_regex = re.compile(r'^(#{1,6})\s*(.*)')
    sections = defaultdict(str)
    current_section = None

    for line in md_text.split('\n'):
        header_match = header_regex.match(line)
        if header_match:
            header_level = len(header_match.group(1))
            if header_level == break_on_level:
                header = header_match.group(2).strip()
                current_section = header
        elif current_section:
            sections[current_section] += line + '\n'

    return sections


def page_range_iterator(md_text: str, pages_per_iteration: int = 2) -> iter:
    text_splits = md_text.split('-----')
    for i in range(0, len(text_splits), pages_per_iteration):
        page_batch = " ".join(text_splits[i:i + pages_per_iteration])
        if page_batch:  # If the current page is not empty
            yield page_batch
