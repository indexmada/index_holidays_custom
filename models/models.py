# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class index_holidays_custom(models.Model):
#     _name = 'index_holidays_custom.index_holidays_custom'
#     _description = 'index_holidays_custom.index_holidays_custom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
