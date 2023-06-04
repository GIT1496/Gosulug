from controlcenter import Dashboard, widgets
from core.models import Reestr_1

class Reest1ItemList(widgets.ItemList):
    model = Reestr_1
    list_display = ('id', 'namber', 'date_creation', 'date_rendering', 'predpr', 'vid', 'dejat')
class MyDashboard(Dashboard):
    widgets = (
        Reest1ItemList,
    )