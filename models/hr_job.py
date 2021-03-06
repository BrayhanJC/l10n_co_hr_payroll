# -*- coding: utf-8 -*-
##############################################################################

##############################################################################
import logging
_logger = logging.getLogger(__name__)
from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp.osv import osv
from openerp.exceptions import UserError, ValidationError

import logging
_logger = logging.getLogger(__name__)


class hr_employee_category(models.Model):
    _inherit = 'hr.job' 
    
    riesgos_profesionales = fields.Many2one('hr.nivel.riesgos','Nivel Riesgos Laborales')       


class hr_nivel_riesgos(models.Model):
    _name = 'hr.nivel.riesgos' 

    name = fields.Char('Nivel de Riesgo')
    tarifa = fields.Float('Tarifa', digits=(3,4))   
