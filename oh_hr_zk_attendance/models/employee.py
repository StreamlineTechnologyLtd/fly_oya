import pytz
import sys
import datetime
import logging
import binascii

from . import zklib
from .zkconst import *
from struct import unpack
from odoo import api, fields, models
from odoo import _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)
try:
    from zk import ZK, const
except ImportError:
    _logger.error("Please Install pyzk library.")

_logger = logging.getLogger(__name__)


class HrAttendance(models.Model):
    _inherit = 'hr.employee'

    uid = fields.Integer(string = 'Biometric device uid')
    
    def device_connect(self, zk):
        try:
            conn = zk.connect()
            return conn
        except:
            return False

    def create_user_biometric_device(self):
        for record in self:
            if not record.barcode:
                raise UserError('Please set Employee ID/Barcode first')
            devices = self.env['zk.machine'].search([])
            for device in devices:
                ip = device.name
                port = device.port_no
                zk = ZK(ip, port=port, timeout=5,ommit_ping=True)
                conn = zk.connect()
                users = conn.get_users()
                if (not record.uid or record.uid == 0) and len(users) == 0:
                    record.uid = 1
                    conn.set_user(name=record.name, password='12345678',group_id='', user_id = record.barcode, uid = record.uid)
                
                elif record.uid <= len(users):
                    conn.set_user(uid=record.uid,name=record.name, password='12345678',group_id='', user_id = record.barcode)
                else:
                    record.uid = len(users) + 1
                    conn.set_user(name=record.name, password='12345678',group_id='', user_id = record.barcode, uid = record.uid)
                conn.disconnect()
    

