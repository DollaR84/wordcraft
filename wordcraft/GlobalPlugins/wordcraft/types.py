from enum import Enum

import addonHandler


addonHandler.initTranslation()


class CorrectType(Enum):
    Simple = _('simple')
    Extended = _('extended')


class Languages(Enum):
    en = _("english")
    uk = _("ukrainian")
    pl = _("polish")
    cs = _("czech")
    de = _("german")
    fr = _("french")
    es = _("spanish")
