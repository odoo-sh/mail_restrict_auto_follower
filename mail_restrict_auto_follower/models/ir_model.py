# -*- coding: utf-8 -*-
# Copyright 2023 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

from odoo import fields, models


class IrModel(models.Model):
    _inherit = 'ir.model'

    is_disable_auto_follower = fields.Boolean(
        string="Disable Automatic Follower", default=False,
        help="Whether this model supports automatic follower when create or update the salesperson.",
    )
