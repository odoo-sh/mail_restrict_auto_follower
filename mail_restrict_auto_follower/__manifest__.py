# -*- coding: utf-8 -*-
# Copyright 2023 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    'name': "Mail Restrict Auto Follower",
    'summary': """
        This module is used to disable adding an auto follower and restrict the mail
        when creating a record or updating the salesperson.""",
    'version': '14.0.1.0.0',
    'category': 'Uncategorized',
    'website': "http://sodexis.com/",
    'author': "Sodexis",
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'views/ir_model_views.xml',
    ],
}
