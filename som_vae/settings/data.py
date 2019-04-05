from collections import namedtuple
from enum import Enum


class _BehaviorLabel_(Enum):
    WALK_FORW = 0
    WALK_BACKW = 1
    PUSH_BALL = 2
    REST = 3
    GROOM_FLEG = 4
    GROOM_ANT = 5
    NONE = 6


__LabelledData__ = namedtuple('LabelledData', 'sequence, label, path')


__LABELLED_DATA_RAW__ = [((0, 140), _BehaviorLabel_.REST, '/180919_MDN_CsCh/Fly6/001_SG1'),
                         ((140, 460), _BehaviorLabel_.WALK_BACKW, '/180919_MDN_CsCh/Fly6/001_SG1'),
                         ((600, 750), _BehaviorLabel_.WALK_FORW, '/180919_MDN_CsCh/Fly6/001_SG1'),
                         ((750, 900), _BehaviorLabel_.REST, '/180919_MDN_CsCh/Fly6/001_SG1'),

                         ((0, 140), _BehaviorLabel_.REST, '/180919_MDN_CsCh/Fly6/002_SG1'),
                         ((140, 500), _BehaviorLabel_.WALK_BACKW, '/180919_MDN_CsCh/Fly6/002_SG1'),
                         ((630, 800), _BehaviorLabel_.WALK_FORW, '/180919_MDN_CsCh/Fly6/002_SG1'),
                         ((790, 900), _BehaviorLabel_.REST, '/180919_MDN_CsCh/Fly6/002_SG1'),

                         ([0, 140], _BehaviorLabel_.REST, '/180919_MDN_CsCh/Fly6/003_SG1'),
                         ((140, 500), _BehaviorLabel_.WALK_BACKW, '/180919_MDN_CsCh/Fly6/003_SG1'),
                         ((570, 750), _BehaviorLabel_.WALK_FORW, '/180919_MDN_CsCh/Fly6/003_SG1'),

                         ([0, 140], _BehaviorLabel_.REST, '/180919_MDN_CsCh/Fly6/004_SG1'),
                         ((140, 500), _BehaviorLabel_.WALK_BACKW, '/180919_MDN_CsCh/Fly6/004_SG1'),
                         ((600, 750), _BehaviorLabel_.WALK_FORW, '/180919_MDN_CsCh/Fly6/004_SG1'),

                         ([0, 140], _BehaviorLabel_.REST, '/180919_MDN_CsCh/Fly6/005_SG1'),
                         ((140, 500), _BehaviorLabel_.WALK_BACKW, '/180919_MDN_CsCh/Fly6/005_SG1'),
                         ((600, 750), _BehaviorLabel_.WALK_FORW, '/180919_MDN_CsCh/Fly6/005_SG1'),

                         ((0, 150), _BehaviorLabel_.GROOM_FLEG, '/180921_aDN_CsCh/Fly6/003_SG1'),
                         ((170, 350), _BehaviorLabel_.GROOM_ANT, '/180921_aDN_CsCh/Fly6/003_SG1'),
                         ((450, 600), _BehaviorLabel_.REST, '/180921_aDN_CsCh/Fly6/003_SG1'),

                         ((0, 150), _BehaviorLabel_.REST, '/180921_aDN_CsCh/Fly6/001_SG1'),
                         ((180, 350), _BehaviorLabel_.GROOM_ANT, '/180921_aDN_CsCh/Fly6/001_SG1'),
                         ((400, 580), _BehaviorLabel_.REST, '/180921_aDN_CsCh/Fly6/001_SG1'),

                         ((250, 600), _BehaviorLabel_.WALK_BACKW, '/180918_MDN_CsCh/Fly2/004_SG1'),

                         ((190, 300), _BehaviorLabel_.GROOM_ANT, '/180921_aDN_CsCh/Fly4/003_SG1'),

                         ((400, 900), _BehaviorLabel_.WALK_FORW, '/180918_MDN_PR/Fly1/003_SG1'),

                         ((0, 500), _BehaviorLabel_.REST, '/180918_MDN_PR/Fly1/004_SG1'),
                         ((650, 900), _BehaviorLabel_.WALK_FORW, '/180918_MDN_PR/Fly1/004_SG1'),

                         ((0, 500), _BehaviorLabel_.REST, '/180918_MDN_PR/Fly1/005_SG1'),
                         ((500, 900), _BehaviorLabel_.WALK_FORW, '/180918_MDN_PR/Fly1/005_SG1'),

                         ((0, 100), _BehaviorLabel_.PUSH_BALL, '/180918_MDN_PR/Fly2/001_SG1'),

                         ((350, 500), _BehaviorLabel_.GROOM_FLEG, '/180918_MDN_PR/Fly2/002_SG1'),

                         ((400, 530), _BehaviorLabel_.GROOM_FLEG, '/180918_MDN_PR/Fly2/003_SG1'),

                         ((150, 230), _BehaviorLabel_.GROOM_ANT, '/180921_aDN_CsCh/Fly3/001_SG1'),

                         #((170, 210), _BehaviorLabel_.WALK_BACKW, '/180919_MDN_CsCh/Fly4/005_SG1'),
                         #((210, 600), _BehaviorLabel_.WALK_FORW, '/180919_MDN_CsCh/Fly4/005_SG1'),
                         #((600, 700), _BehaviorLabel_.PUSH_BALL, '/180919_MDN_CsCh/Fly4/005_SG1'),
                 ]


__LABELLED_DATA_RAW__ 

LABELLED_DATA = [__LabelledData__._make(i) for i in __LABELLED_DATA_RAW__]

