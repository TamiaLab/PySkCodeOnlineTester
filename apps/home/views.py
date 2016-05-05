"""
Home pages views for the home pages app.
"""

from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.utils.translation import ugettext_lazy as _
from django.template.response import TemplateResponse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.staticfiles.templatetags.staticfiles import static

from skcode import (parse_skcode,
                    render_to_html,
                    render_to_skcode,
                    render_to_text)
from skcode.tags import (ErroneousTextTagOptions,
                         TextTagOptions,
                         NewlineTagOptions,
                         HardNewlineTagOptions)
from skcode.utility import (make_paragraphs,
                            extract_footnotes,
                            render_footnotes_html,
                            render_footnotes_text,
                            extract_titles,
                            make_titles_hierarchy,
                            make_auto_title_ids,
                            render_titles_hierarchy_html,
                            render_titles_hierarchy_text,
                            setup_smileys_replacement,
                            setup_cosmetics_replacement,
                            setup_relative_urls_conversion)


from .forms import (TestSkCodeInputForm,
                    RENDERING_MODE_HTML,
                    RENDERING_MODE_TEXT,
                    RENDERING_MODE_SKCODE)


@never_cache
@csrf_protect
def home_page(request,
              template_name='home/home.html',
              test_input_form=TestSkCodeInputForm,
              extra_context=None):
    """
    PySkCode tester home page with form for testing the parser.
    :param request: The current request.
    :param template_name: The template name to be used.
    :param test_input_form: The test input form class to be used.
    :param extra_context: Any extra template context information.
    :return: TemplateResponse
    """

    # Default values
    output_content_html = ''
    output_content_text = ''
    summary_content_html = ''
    summary_content_text = ''
    footnotes_content_html = ''
    footnotes_content_text = ''

    # Handle the form
    if request.method == "POST":
        form = test_input_form(request.POST, request.FILES)
        if form.is_valid():

            # Parse the input text
            erroneous_text_opts = ErroneousTextTagOptions() if form.cleaned_data['preview_mode'] else TextTagOptions()
            newlines_opts = HardNewlineTagOptions() if form.cleaned_data['hard_newline'] else NewlineTagOptions()
            document = parse_skcode(form.cleaned_data['content'],
                                    allow_tagvalue_attr=form.cleaned_data['allow_tagvalue_attr'],
                                    allow_self_closing_tags=form.cleaned_data['allow_self_closing_tags'],
                                    erroneous_text_node_opts=erroneous_text_opts,
                                    newline_node_opts=newlines_opts,
                                    drop_unrecognized=form.cleaned_data['drop_unrecognized'],
                                    texturize_unclosed_tags=form.cleaned_data['texturize_unclosed_tags'])

            # Handle smileys and cosmetics
            if form.cleaned_data['replace_cosmetics']:
                setup_cosmetics_replacement(document)
            if form.cleaned_data['replace_smileys']:

                def _base_url(filename):
                    return static('images/smileys/' + filename)
                setup_smileys_replacement(document, _base_url)

            # Handle relative urls
            if form.cleaned_data['convert_relative_url_to_absolute']:
                current_site = get_current_site(request)
                setup_relative_urls_conversion(document, 'http://%s/' % current_site.domain)

            # Get requested render mode
            rendering_mode = form.cleaned_data['rendering_mode']

            # Apply paragraph utilities
            if form.cleaned_data['make_paragraphs']:
                make_paragraphs(document)

            # Apply footnotes utilities
            if form.cleaned_data['render_footnotes_html']:

                # Extract all footnotes
                footnotes = extract_footnotes(document)

                # Render all footnotes
                if rendering_mode == RENDERING_MODE_HTML:
                    footnotes_content_html = render_footnotes_html(footnotes)
                elif rendering_mode == RENDERING_MODE_TEXT:
                    footnotes_content_text = render_footnotes_text(footnotes)

            # Apply titles utilities (part 1 of 2)
            if form.cleaned_data['make_auto_title_ids']:
                make_auto_title_ids(document)

            # Apply titles utilities (part 2 of 2)
            if form.cleaned_data['extract_titles']:

                # Extract all titles
                titles = extract_titles(document)

                # Turn the titles list into a hierarchy
                titles_hierarchy = list(make_titles_hierarchy(titles))

                # Render the output
                if rendering_mode == RENDERING_MODE_HTML:
                    summary_content_html = render_titles_hierarchy_html(titles_hierarchy)
                elif rendering_mode == RENDERING_MODE_TEXT:
                    summary_content_text = render_titles_hierarchy_text(titles_hierarchy)

            # Render the document
            if rendering_mode == RENDERING_MODE_HTML:
                output_content_html = render_to_html(document)
            elif rendering_mode == RENDERING_MODE_TEXT:
                output_content_text = render_to_text(document)
            elif rendering_mode == RENDERING_MODE_SKCODE:
                output_content_text = render_to_skcode(document)
            else:
                output_content_text = 'ERROR'
    else:
        form = test_input_form()

    # Render the template
    context = {
        'form': form,
        'output_content_html': output_content_html,
        'output_content_text': output_content_text,
        'summary_content_html': summary_content_html,
        'summary_content_text': summary_content_text,
        'footnotes_content_html': footnotes_content_html,
        'footnotes_content_text': footnotes_content_text,
        'title': _('Home page'),
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)
