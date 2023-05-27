class Default_value:
    def get_default_context(self):
        return {'title': 'Страница'}

    def add_default_context(self, context : dict) -> dict:
        context['title'] = 'Страница по умолчанию'
        return context

    def add_title_context(self, context : dict, title_name : str) -> dict:
        context['title'] = title_name
        return context