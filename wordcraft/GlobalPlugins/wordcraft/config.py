from dataclasses import dataclass, field

from .types import CorrectType, Languages


@dataclass
class Config:
    lang_default: Languages = Languages.en
    required_languages: list[Languages] = field(default_factory=list)

    correct_default: CorrectType = CorrectType.Extended
    variants_default: CorrectType = CorrectType.Extended

    need_auto_correct: bool = True
    need_copy_to_clipboard: bool = False
