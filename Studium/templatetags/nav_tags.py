from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, view_name):
    """
    Tag szablonu Django używany do określenia, czy dany widok jest aktualnie aktywny.

    Używany w szablonach HTML do dodania klasy 'active' do linków nawigacyjnych,
    które odpowiadają aktualnie wyświetlanej stronie. Funkcja porównuje ścieżkę
    aktualnego żądania z odwróconym adresem URL dla podanej nazwy widoku.

    Args:
        context (dict): Kontekst szablonu, z którego można uzyskać aktualny request.
        view_name (str): Nazwa widoku (tak jak zdefiniowana w URLach), dla którego sprawdzamy, czy jest aktywny.

    Returns:
        str: Zwraca 'active' jeśli widok jest aktywny, w przeciwnym razie pusty string.
    """
    request = context['request']
    if request.path == reverse(view_name):
        return 'active'
    return ''
