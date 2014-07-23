# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from zope.interface.interface import Interface
from zope.schema import Bool
from Products.GSProfile.interfaceCoreProfile import GSImage


class IGSProfileImage(Interface):

    image = GSImage(
        title='Image',
        description='The image you want others to see on your profile '
        'and posts, usually a photograph. The image must be a JPEG.',
        required=False,
        default=None)

    showImage = Bool(
        title='Show Image',
        description='If set, others can see your image.',
        required=False,
        default=True)
