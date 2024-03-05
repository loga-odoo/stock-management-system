{
    'name': "stock_transport",
    'version': '1.0',
    'depends': ['stock_picking_batch','fleet'],
    'author': "loga",
    'category': 'Category',
    'data' :['views/custom_fleet_views.xml',
             'views/custom_graph_view.xml',
             'views/custom_volume_views.xml',

    ],


    'application': True,

}