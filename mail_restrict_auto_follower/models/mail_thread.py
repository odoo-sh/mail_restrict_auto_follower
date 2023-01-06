# -*- coding: utf-8 -*-
# Copyright 2023 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

from odoo import api, models


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'


    @api.model_create_multi
    def create(self, vals_list):
        """'mail_create_nosubscribe': at create or message_post, do not subscribe
        uid to the record thread"""
        ir_model_id = self.env['ir.model'].search([('model', '=', self._name)], limit=1)
        if ir_model_id and ir_model_id.is_disable_auto_follower:
            self = self.with_context(mail_create_nosubscribe=True)
        return super(MailThread, self).create(vals_list)

    def _message_auto_subscribe_followers(self, updated_values, default_subtype_ids):
        """Disable adding automatic follower when create or update the salesperson for the model"""
        ir_model_id = self.env['ir.model'].search([('model', '=', self._name)], limit=1)
        if ir_model_id and ir_model_id.is_disable_auto_follower:
            return []
        return super(MailThread, self)._message_auto_subscribe_followers(updated_values, default_subtype_ids)
