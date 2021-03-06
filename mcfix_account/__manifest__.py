# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Multi Company Fix Account',
    'version': '11.0.1.0.0',
    'summary': 'Account fixes',
    'author': 'Eficent, Odoo Community Association (OCA)',
    'website': 'http://www.eficent.com',
    'license': 'LGPL-3',
    'depends': ['account', 'mcfix_product', 'mcfix_analytic'],
    'data': [
        'security/account_security.xml',
        'views/account_account_view.xml',
        'views/account_invoice_view.xml',
        'views/account_journal_dashboard_view.xml',
        'views/account_journal_view.xml',
        'views/account_move_view.xml',
        'views/account_payment_term_view.xml',
        'views/account_payment_view.xml',
        'views/account_tax_view.xml',
        'views/partner_view.xml',
        'views/product_view.xml',
        'views/reports.xml',
        'wizard/account_reports_views.xml',
        'wizard/wizard_tax_adjustments_views.xml',
    ],
    'sequence': 30,
    'installable': True,
    'application': False,
    'auto_install': True,
    'post_init_hook': 'post_init_hook',
}
