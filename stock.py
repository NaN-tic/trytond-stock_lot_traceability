# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.wizard import Wizard, StateAction
from trytond.pool import Pool
from trytond.pyson import PYSONEncoder
from trytond.transaction import Transaction

__all__ = ['StockLotSearchProduction']


class StockLotSearchProduction(Wizard):
    'Stock Lot Search Production'
    __name__ = 'stock.lot.search.production'
    start_state = 'open_'
    open_ = StateAction('stock_lot_traceability.act_production_form')

    def do_open_(self, action):
        pool = Pool()
        StockLot = pool.get('stock.lot')
        Production = pool.get('production')

        transaction = Transaction()
        context = transaction.context

        lot = StockLot(context.get('active_id'))
        productions = Production.search([
            ['OR', 
                ('inputs.lot.number', '=', lot.number),
                ('outputs.lot.number', '=', lot.number),
                ]
            ])

        encoder = PYSONEncoder()
        action['pyson_domain'] = encoder.encode(
            [('id', 'in', [p.id for p in productions])])
        action['name'] = action['name'] + ' - ' + lot.rec_name

        return action, {}

    def transition_open_(self):
        return 'end'

