"""
Forms for the home pages app.
"""

from django import forms
from django.utils.translation import ugettext_lazy as _


# Rendering modes
RENDERING_MODE_HTML = 'html'
RENDERING_MODE_TEXT = 'text'
RENDERING_MODE_SKCODE = 'skcode'
RENDERING_MODE_CHOICES = (
    (RENDERING_MODE_HTML, _('HTML')),
    (RENDERING_MODE_TEXT, _('Text')),
    (RENDERING_MODE_SKCODE, _('SkCode')),
)


class TestSkCodeInputForm(forms.Form):
    """
    Test form for the ``PySkCode`` project.
    """

    # Content
    content = forms.CharField(label=_('Content'),
                              widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}),
                              help_text=_('This field accept the SkCode syntax.'))

    rendering_mode = forms.ChoiceField(label=_('Rendering mode'),
                                       choices=RENDERING_MODE_CHOICES)

    preview_mode = forms.BooleanField(required=False,
                                      initial=True,
                                      label=_('Preview mode'),
                                      help_text=_('In preview mode erroneous tags are displayed in a bold red font.'))

    hard_newline = forms.BooleanField(required=False,
                                      initial=False,
                                      label=_('Hard newline'),
                                      help_text=_('Tick to enable hard newlines.'))

    # Parser options
    allow_tagvalue_attr = forms.BooleanField(required=False,
                                             initial=True,
                                             label=_('Allow tagname=value shortcut'),
                                             help_text=_('Untick to fallback into a HTML-like mode.'))

    allow_self_closing_tags = forms.BooleanField(required=False,
                                                 initial=True,
                                                 label=_('Allow self closing tags'),
                                                 help_text=_('Untick to restrict the parser from allowing XHTML-like tags.'))

    drop_unrecognized = forms.BooleanField(required=False,
                                           initial=False,
                                           label=_('Drop unrecognized tags'),
                                           help_text=_('Tick to drop unrecognized tags instead of making them bold red.'))

    texturize_unclosed_tags = forms.BooleanField(required=False,
                                                 initial=False,
                                                 label=_('Texturize unclosed tags'),
                                                 help_text=_('Tick to turn unclosed tags into raw text.'))

    # Utilities options
    make_paragraphs = forms.BooleanField(required=False,
                                         initial=True,
                                         label=_('Make paragraphs'),
                                         help_text=_('Untick to disable the auto-paragraphs feature.'))

    render_footnotes_html = forms.BooleanField(required=False,
                                               initial=True,
                                               label=_('Render footnotes'),
                                               help_text=_('Untick to disable the rendering of footnotes.'))

    extract_titles = forms.BooleanField(required=False,
                                        initial=True,
                                        label=_('Extract titles'),
                                        help_text=_('Untick to disable the auto-summary feature.'))

    make_auto_title_ids = forms.BooleanField(required=False,
                                             initial=True,
                                             label=_('Auto title IDs'),
                                             help_text=_('Untick to disable the auto-generation of title IDs.'))
