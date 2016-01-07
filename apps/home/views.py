"""
Home pages views for the home pages app.
"""

from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.utils.translation import ugettext_lazy as _
from django.template.response import TemplateResponse

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
                            setup_smileys_replacement,
                            setup_cosmetics_replacement)


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

    # Default value
    output_content = ''
    output_keep_newlines = False

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
                from django.contrib.staticfiles.templatetags.staticfiles import static

                def _base_url(filename):
                    return static('images/smileys/' + filename)
                setup_smileys_replacement(document, _base_url)

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
                    footnotes_content = '<hr>\n' + render_footnotes_html(footnotes)
                elif rendering_mode == RENDERING_MODE_TEXT:
                    footnotes_content = '----------\n' + render_footnotes_text(footnotes)
                else:
                    footnotes_content = ''

            else:
                footnotes_content = ''

            # Apply titles utilities (part 1 of 2)
            if form.cleaned_data['make_auto_title_ids']:
                make_auto_title_ids(document)

            # Apply titles utilities (part 2 of 2)
            if form.cleaned_data['extract_titles']:

                # Extract all titles
                titles = extract_titles(document)

                # Turn the titles list into a hierarchy
                titles_hierarchy = make_titles_hierarchy(titles)

                # Recursive helper for HTML rendering
                def _recur_render_title_html(title_groups, output):
                    for parent_title, sub_titles in title_groups:
                        title_id, tree_node, title_level = parent_title
                        output.append('<li>')
                        output.append('<a href="#%s">%s</a>' % (title_id, tree_node.get_raw_content()))
                        if sub_titles:
                            output.append('<ul>')
                            _recur_render_title_html(sub_titles, output)
                            output.append('</ul>')
                        output.append('</li>')

                # Recursive helper for text rendering
                def _recur_render_title_text(title_groups, output, indent=0):
                    for parent_title, sub_titles in title_groups:
                        title_id, tree_node, title_level = parent_title
                        output.append('%s %s' % ('#' * indent, tree_node.get_raw_content()))
                        _recur_render_title_text(sub_titles, output, indent + 1)

                # Render the output
                summary_content = ['Sommaire :']
                if rendering_mode == RENDERING_MODE_HTML:
                    summary_content.append('<ul>')
                    _recur_render_title_html(titles_hierarchy, summary_content)
                    summary_content.append('</ul>')
                    summary_content.append('<hr>')
                elif rendering_mode == RENDERING_MODE_TEXT:
                    _recur_render_title_text(titles_hierarchy, summary_content)

                # Craft the output
                summary_content.append('')
                summary_content = '\n'.join(summary_content)

            else:
                summary_content = ''

            # Render the document
            if rendering_mode == RENDERING_MODE_HTML:
                content = render_to_html(document)
            elif rendering_mode == RENDERING_MODE_TEXT:
                content = render_to_text(document)
                output_keep_newlines = True
            elif rendering_mode == RENDERING_MODE_SKCODE:
                content = render_to_skcode(document)
                output_keep_newlines = True
            else:
                content = 'ERROR'

            # Craft the final HTML
            output_content = '%s\n%s\n%s' % (summary_content, content, footnotes_content)

    else:
        form = test_input_form()

    # Render the template
    context = {
        'form': form,
        'output_content': output_content,
        'output_keep_newlines': output_keep_newlines,
        'title': _('Home page'),
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)
