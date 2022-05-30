from odoo import fields, models, api


class HospitalPatient(models.Model):
    _name = 'om_hospital.patient'
    _description = 'Hospital Patient Information'

    name = fields.Char()
