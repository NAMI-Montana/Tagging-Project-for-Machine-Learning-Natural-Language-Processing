from django.db import models


Categories = (
    ('Acute Threat ("Fear")', 'Acute Threat ("Fear")'),
    ('Potential Threat ("Anxiety")', 'Potential Threat ("Anxiety")'),
    ('Sustained Threat', 'Sustained Threat'),
    ('Loss', 'Loss'),
    ('Frustrative Nonreward', 'Frustrative Nonreward'),
    ('Approach Motivation: Reward Valuation', 'Approach Motivation: Reward Valuation'),
    ('Approach Motivation: Effort Valuation / Willingness to Work', 'Approach Motivation: Effort Valuation / Willingness to Work'),
    ('Approach Motivation: Expectancy / Reward Prediction Error', 'Approach Motivation: Expectancy / Reward Prediction Error'),
    ('Approach Motivation: Action Selection / Preference-Based Decision Making', 'Approach Motivation: Action Selection / Preference-Based Decision Making'),
    ('Initial Responsiveness to Reward Attainment', 'Initial Responsiveness to Reward Attainment'),
    ('Sustained/Longer-Term Responsiveness to Reward Attainment', 'Sustained/Longer-Term Responsiveness to Reward Attainment'),
    ('Reward Learning', 'Reward Learning'),
    ('Habit', 'Habit'),
    ('Attention', 'Attention'),
    ('Perception', 'Perception'),
    ('Declarative Memory', 'Declarative Memory'),
    ('Language', 'Language'),
    ('Cognitive Control', 'Cognitive Control'),
    ('Working Memory', 'Working Memory'),
    ('Affiliation and Attachment', 'Affiliation and Attachment'),
    ('Social Communication', 'Social Communication'),
    ('Perception and Understanding of Self: Agency', 'Perception and Understanding of Self: Agency'),
    ('Perception and Understanding of Self: Self-Knowledge', 'Perception and Understanding of Self: Self-Knowledge'),
    ('Perceptions and Understanding of Others: Animacy Perception', 'Perceptions and Understanding of Others: Animacy Perception'),
    ('Perceptions and Understanding of Others: Action Perception', 'Perceptions and Understanding of Others: Action Perception'),
    ('Perceptions and Understanding of Others: Understanding Mental States', 'Perceptions and Understanding of Others: Understanding Mental States'),
    ('Arousal', 'Arousal'),
    ('Circadian Rhythms', 'Circadian Rhythms'),
    ('Sleep-Wakefulness', 'Sleep-Wakefulness'),
)


class Article(models.Model):
    # id = models.AutoField(primary_key=True)
    link = models.URLField(max_length=255)
    category = models.CharField(max_length=255, choices=Categories)


