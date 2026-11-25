from enum import Enum, auto


class Ending(Enum):
    CLARITY = auto()
    DELUSION = auto()
    COLLAPSE = auto()
    RESIGNATION = auto()


def update_stats(stats, sanity_change=0, doubt_change=0, attachment_change=0):
    for name, change in (
        ("sanity", sanity_change),
        ("doubt", doubt_change),
        ("attachment", attachment_change),
    ):
        stats[name] = max(0, min(100, stats[name] + change))


def select_ending(sanity, doubt, attachment):
    if sanity > 80 and doubt > 50:
        return Ending.CLARITY
    if attachment >= 45:
        return Ending.DELUSION
    if sanity <= 55:
        return Ending.COLLAPSE
    return Ending.RESIGNATION
