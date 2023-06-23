# -*- coding: utf-8 -*-

from odoo import models, api


class HrLeaveReport(models.Model):
    _inherit = 'hr.leave.report'

    @api.model
    def action_time_off_analysis_all_employee(self):
        domain = [('holiday_type', '=', 'employee'), ('state', '=', 'validate')]

        return {
            'name': "Congés restant",
            'type': 'ir.actions.act_window',
            'res_model': 'hr.leave.report',
            'view_mode': 'pivot',
            'search_view_id': self.env.ref('hr_holidays.view_hr_holidays_filter_report').id,
            'views': [(self.env.ref('index_holidays_custom.pivot_employee_holiday_type').id, 'pivot')],
            'domain': domain,
            'context': {
                'search_default_group_type': False,
                'search_default_group_employee': True,
                'search_default_year': False,
            }
        }
