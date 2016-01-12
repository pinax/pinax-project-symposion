# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_proposals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TalkProposal',
            fields=[
                ('proposalbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='symposion_proposals.ProposalBase')),
                ('audience_level', models.IntegerField(choices=[(1, b'Novice'), (3, b'Intermediate'), (2, b'Experienced')])),
                ('recording_release', models.BooleanField(default=True, help_text=b'By submitting your proposal, you agree to give permission to the conference organizers to record, edit, and release audio and/or video of your presentation. If you do not agree to this, please uncheck this box.')),
            ],
            options={
                'verbose_name': 'talk proposal',
            },
            bases=('symposion_proposals.proposalbase',),
        ),
        migrations.CreateModel(
            name='TutorialProposal',
            fields=[
                ('proposalbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='symposion_proposals.ProposalBase')),
                ('audience_level', models.IntegerField(choices=[(1, b'Novice'), (3, b'Intermediate'), (2, b'Experienced')])),
                ('recording_release', models.BooleanField(default=True, help_text=b'By submitting your proposal, you agree to give permission to the conference organizers to record, edit, and release audio and/or video of your presentation. If you do not agree to this, please uncheck this box.')),
            ],
            options={
                'verbose_name': 'tutorial proposal',
            },
            bases=('symposion_proposals.proposalbase',),
        ),
    ]
