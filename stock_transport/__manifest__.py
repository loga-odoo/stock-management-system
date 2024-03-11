{
    'name': "stock_transport",
    'version': '1.0',
    'depends': ['stock_picking_batch','fleet'],
    'author': "loga",
    'category': 'Category',
    'data' :['security/ir.model.access.csv',
             'views/custom_fleet_views.xml',
             'views/custom_graph_view.xml',
             'views/stock_picking_batch_form.xml',
             'views/stock_picking_views.xml',

    ],


    'application': True,

}