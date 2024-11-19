# -*- coding: utf-8 -*-
from odoo import models, fields
#from odoo import tools


class agent(models.Model):
     _name = 'agent.agent'
     _description = 'This is agent profile'

     name = fields.Char()
     name1 = fields.Char()
     name2 = fields.Char()
     name3 = fields.Char()
     #value = fields.Integer()
   # value2 = fields.Float(compute="_value_pc", store=True)
  #  description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

