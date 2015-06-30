from django.db import models
from django.utils.translation import ugettext_lazy as _

from symposion.proposals.models import ProposalBase


class Proposal(ProposalBase):

    AUDIENCE_LEVEL_NOVICE = 1
    AUDIENCE_LEVEL_EXPERIENCED = 2
    AUDIENCE_LEVEL_INTERMEDIATE = 3

    AUDIENCE_LEVELS = [
        (AUDIENCE_LEVEL_NOVICE, _("Novice")),
        (AUDIENCE_LEVEL_INTERMEDIATE, _("Intermediate")),
        (AUDIENCE_LEVEL_EXPERIENCED, _("Experienced")),
    ]

    audience_level = models.IntegerField(choices=AUDIENCE_LEVELS)

    recording_release = models.BooleanField(
        default=True,
        help_text=_("By submitting your proposal, you agree to give permission to the conference organizers to record, edit, and release audio and/or video of your presentation. If you do not agree to this, please uncheck this box.")
    )

    class Meta:
        abstract = True


class TalkProposal(Proposal):
    class Meta:
        verbose_name = _("talk proposal")


class TutorialProposal(Proposal):
    class Meta:
        verbose_name = _("tutorial proposal")
