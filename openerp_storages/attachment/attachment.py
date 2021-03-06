# -*- coding: utf-8 -*-
##########################################################################
# Aquasys G.K.

# Copyright (C) 20012-2013.

#

# This program is free software: you can redistribute it and/or modify

# it under the terms of the GNU Affero General Public License as

# published by the Free Software Foundation, either version 3 of the

# License, or (at your option) any later version.

#

# This program is distributed in the hope that it will be useful,

# but WITHOUT ANY WARRANTY; without even the implied warranty of

# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

# GNU Affero General Public License for more details.

#

# You should have received a copy of the GNU Affero General Public License

# along with this program. If not, see <http://www.gnu.org/licenses/>.
#########################################################################
from openerp.osv import osv, fields


class ir_attachment(osv.osv):
    _inherit = 'ir.attachment'
    _columns = {'db_datas': fields.binary('Database Data', store='s3'),
                }

    #Unlink Method to delete related records of attachements from
    #AWS S3 Lookup table of openerp
    def unlink(self, cr, uid, ids, context=None):
        lookup_obj = self.pool.get('lookup')
        lookup_ids = lookup_obj.search(cr, uid, [('res_id', 'in', ids)])
        lookup_obj.unlink(cr, uid, lookup_ids, context=context)
        return super(ir_attachment, self).unlink(cr, uid, ids, context=context)
ir_attachment()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
