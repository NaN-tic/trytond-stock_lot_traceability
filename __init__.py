# This file is part stock_lot_traceability module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .stock import *

def register():
    Pool.register(
        StockLotSearchProduction,
        module='stock_lot_traceability', type_='wizard')
