"""
Tests suite for the bootstrap forms app.
"""

from django import forms
from django.test import SimpleTestCase
from django.template import Context, Template


class TestForm(forms.Form):
    """ Test form """

    # To be tested
    # - Non field errors
    # - Hidden fields
    # - Visible required / optional fields
    # - With / without errors
    # - With help text

    # Hidden field
    hidden_field = forms.CharField(initial='initial value',
                                   widget=forms.HiddenInput())

    # Test single checkbox
    bool_field = forms.BooleanField(label='Boolean field',
                                    required=False)
    bool_field_required = forms.BooleanField(label='Boolean field')
    bool_field_help = forms.BooleanField(label='Boolean field',
                                         required=False,
                                         help_text='This is a test')

    # Test generic text field
    char_field = forms.CharField(label='Char field',
                                 required=False)
    char_field_required = forms.CharField(label='Char field')
    char_field_help = forms.CharField(label='Char field',
                                      required=False,
                                      help_text='This is a test')

    # Test generic text-area
    text_field = forms.CharField(label='Text field',
                                 required=False,
                                 widget=forms.Textarea())
    text_field_required = forms.CharField(label='Text field',
                                          widget=forms.Textarea())
    text_field_help = forms.CharField(label='Text field',
                                      required=False,
                                      widget=forms.Textarea(),
                                      help_text='This is a test')

    # Test select field
    choices = (
        ('A', 'Choice A'),
        ('B', 'Choice B'),
        ('C', 'Choice C'),
    )
    choice_field = forms.ChoiceField(label='Choices field',
                                     required=False,
                                     choices=choices)
    choice_field_required = forms.ChoiceField(label='Choices field',
                                              choices=choices)
    choice_field_help = forms.ChoiceField(label='Choices field',
                                          required=False,
                                          help_text='This is a test',
                                          choices=choices)

    # Test radio buttons group
    radio_choice_field = forms.ChoiceField(label='Radio fields',
                                           required=False,
                                           widget=forms.RadioSelect(),
                                           choices=choices)
    radio_choice_field_required = forms.ChoiceField(label='Radio fields',
                                                    widget=forms.RadioSelect(),
                                                    choices=choices)
    radio_choice_field_help = forms.ChoiceField(label='Radio fields',
                                                required=False,
                                                widget=forms.RadioSelect(),
                                                help_text='This is a test',
                                                choices=choices)

    # Test multiple checkbox
    checkbox_choice_field = forms.ChoiceField(label='Checkbox fields',
                                              required=False,
                                              widget=forms.CheckboxSelectMultiple(),
                                              choices=choices)
    checkbox_choice_field_required = forms.ChoiceField(label='Checkbox fields',
                                                       widget=forms.CheckboxSelectMultiple(),
                                                       choices=choices)
    checkbox_choice_field_help = forms.ChoiceField(label='Checkbox fields',
                                                   required=False,
                                                   widget=forms.CheckboxSelectMultiple(),
                                                   help_text='This is a test',
                                                   choices=choices)

    # Test file input
    file_field = forms.FileField(label='File field', required=False)
    file_field_required = forms.FileField(label='File field')
    file_field_help = forms.FileField(label='File field',
                                      required=False,
                                      help_text='This is a test')

    # Test non field errors
    def clean(self):
        raise forms.ValidationError('This is a non field error', code='test_error')


class BootstrapFormsTestCase(SimpleTestCase):
    """
    Tests suite for the bootstrap forms app.
    """

    def setUp(self):
        self.maxDiff = None

    def test_output_without_errors(self):
        """ Test the HTML output without errors """
        template = Template("{% load bootstrapform %}{{ form|bootstrapform }}")
        form = TestForm()
        context = Context({"form": form})
        html_output = template.render(context)
        html_expected = """<input id="id_hidden_field" name="hidden_field" type="hidden" value="initial value" />
<div class="form-group">
    <div class="checkbox">
        <label>
        <input id="id_bool_field" name="bool_field" type="checkbox" />
        Boolean field
        </label>
    </div>
</div>
<div class="form-group">
    <div class="checkbox">
        <label>
        <input id="id_bool_field_required" name="bool_field_required" type="checkbox" />
        Boolean field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup>
        </label>
    </div>
</div>
<div class="form-group">
    <div class="checkbox">
        <label>
        <input id="id_bool_field_help" name="bool_field_help" type="checkbox" />
        Boolean field
        </label>
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_char_field">Char field</label>
    <div class="">
        <input class=" form-control" id="id_char_field" name="char_field" type="text" />
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_char_field_required">Char field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="">
        <input class=" form-control" id="id_char_field_required" name="char_field_required" type="text" />
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_char_field_help">Char field</label>
    <div class="">
        <input class=" form-control" id="id_char_field_help" name="char_field_help" type="text" />
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_text_field">Text field</label>
    <div class="">
        <textarea class=" form-control" cols="40" id="id_text_field" name="text_field" rows="10"></textarea>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_text_field_required">Text field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="">
        <textarea class=" form-control" cols="40" id="id_text_field_required" name="text_field_required" rows="10"></textarea>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_text_field_help">Text field</label>
    <div class="">
        <textarea class=" form-control" cols="40" id="id_text_field_help" name="text_field_help" rows="10"></textarea>
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_choice_field">Choices field</label>
    <div class="">
        <select class=" form-control" id="id_choice_field" name="choice_field">
            <option value="A">Choice A</option>
            <option value="B">Choice B</option>
            <option value="C">Choice C</option>
        </select>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_choice_field_required">Choices field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="">
        <select class=" form-control" id="id_choice_field_required" name="choice_field_required">
            <option value="A">Choice A</option>
            <option value="B">Choice B</option>
            <option value="C">Choice C</option>
        </select>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_choice_field_help">Choices field</label>
    <div class="">
        <select class=" form-control" id="id_choice_field_help" name="choice_field_help">
            <option value="A">Choice A</option>
            <option value="B">Choice B</option>
            <option value="C">Choice C</option>
        </select>
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_radio_choice_field">Radio fields</label>
    <div class="radio">
        <label>
        <input id="id_radio_choice_field_0" name="radio_choice_field" type="radio" value="A" />
        Choice A
        </label>
    </div>
    <div class="radio">
        <label>
        <input id="id_radio_choice_field_1" name="radio_choice_field" type="radio" value="B" />
        Choice B
        </label>
    </div>
    <div class="radio">
        <label>
        <input id="id_radio_choice_field_2" name="radio_choice_field" type="radio" value="C" />
        Choice C
        </label>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_radio_choice_field_required">Radio fields <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="radio">
        <label>
        <input id="id_radio_choice_field_required_0" name="radio_choice_field_required" type="radio" value="A" />
        Choice A
        </label>
    </div>
    <div class="radio">
        <label>
        <input id="id_radio_choice_field_required_1" name="radio_choice_field_required" type="radio" value="B" />
        Choice B
        </label>
    </div>
    <div class="radio">
        <label>
        <input id="id_radio_choice_field_required_2" name="radio_choice_field_required" type="radio" value="C" />
        Choice C
        </label>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_radio_choice_field_help">Radio fields</label>
    <div class="radio">
        <label>
        <input id="id_radio_choice_field_help_0" name="radio_choice_field_help" type="radio" value="A" />
        Choice A
        </label>
    </div>
    <div class="radio">
        <label>
        <input id="id_radio_choice_field_help_1" name="radio_choice_field_help" type="radio" value="B" />
        Choice B
        </label>
    </div>
    <div class="radio">
        <label>
        <input id="id_radio_choice_field_help_2" name="radio_choice_field_help" type="radio" value="C" />
        Choice C
        </label>
    </div>
    <span class="help-block">This is a test</span>
</div>
<div class="form-group">
    <label class="control-label" for="id_checkbox_choice_field">Checkbox fields</label>
    <div class=" multiple-checkbox">
        <ul id="id_checkbox_choice_field">
            <li><label for="id_checkbox_choice_field_0"><input id="id_checkbox_choice_field_0" name="checkbox_choice_field" type="checkbox" value="A" /> Choice A</label></li>
            <li><label for="id_checkbox_choice_field_1"><input id="id_checkbox_choice_field_1" name="checkbox_choice_field" type="checkbox" value="B" /> Choice B</label></li>
            <li><label for="id_checkbox_choice_field_2"><input id="id_checkbox_choice_field_2" name="checkbox_choice_field" type="checkbox" value="C" /> Choice C</label></li>
        </ul>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_checkbox_choice_field_required">Checkbox fields <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class=" multiple-checkbox">
        <ul id="id_checkbox_choice_field_required">
            <li><label for="id_checkbox_choice_field_required_0"><input id="id_checkbox_choice_field_required_0" name="checkbox_choice_field_required" type="checkbox" value="A" /> Choice A</label></li>
            <li><label for="id_checkbox_choice_field_required_1"><input id="id_checkbox_choice_field_required_1" name="checkbox_choice_field_required" type="checkbox" value="B" /> Choice B</label></li>
            <li><label for="id_checkbox_choice_field_required_2"><input id="id_checkbox_choice_field_required_2" name="checkbox_choice_field_required" type="checkbox" value="C" /> Choice C</label></li>
        </ul>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_checkbox_choice_field_help">Checkbox fields</label>
    <div class=" multiple-checkbox">
        <ul id="id_checkbox_choice_field_help">
            <li><label for="id_checkbox_choice_field_help_0"><input id="id_checkbox_choice_field_help_0" name="checkbox_choice_field_help" type="checkbox" value="A" /> Choice A</label></li>
            <li><label for="id_checkbox_choice_field_help_1"><input id="id_checkbox_choice_field_help_1" name="checkbox_choice_field_help" type="checkbox" value="B" /> Choice B</label></li>
            <li><label for="id_checkbox_choice_field_help_2"><input id="id_checkbox_choice_field_help_2" name="checkbox_choice_field_help" type="checkbox" value="C" /> Choice C</label></li>
        </ul>
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_file_field">File field</label>
    <div class="">
        <input id="id_file_field" name="file_field" type="file" />
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_file_field_required">File field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="">
        <input id="id_file_field_required" name="file_field_required" type="file" />
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_file_field_help">File field</label>
    <div class="">
        <input id="id_file_field_help" name="file_field_help" type="file" />
        <span class="help-block">This is a test</span>
    </div>
</div>
<p><small><i class="fa fa-asterisk" aria-hidden="true"></i> Mandatory fields</small></p>"""
        self.assertHTMLEqual(html_expected, html_output)

    def test_output_with_errors(self):
        """ Test the HTML output without errors """
        template = Template("{% load bootstrapform %}{{ form|bootstrapform }}")
        form = TestForm(data={}, files={})
        form.is_valid()
        context = Context({"form": form})
        html_output = template.render(context)
        html_expected = """<div class="alert alert-danger">
    <ul>
        <li>
            <p>This is a non field error</p>
        </li>
    </ul>
</div>
<input id="id_hidden_field" name="hidden_field" type="hidden" />
<div class="form-group">
    <div class="checkbox">
        <label>
        <input id="id_bool_field" name="bool_field" type="checkbox" />
        Boolean field
        </label>
    </div>
</div>
<div class="form-group has-error">
    <div class="checkbox">
        <label>
        <input id="id_bool_field_required" name="bool_field_required" type="checkbox" />
        Boolean field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup>
        </label>
        <span class="help-block">Ce champ est obligatoire.</span>
    </div>
</div>
<div class="form-group">
    <div class="checkbox">
        <label>
        <input id="id_bool_field_help" name="bool_field_help" type="checkbox" />
        Boolean field
        </label>
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_char_field">Char field</label>
    <div class="">
        <input class=" form-control" id="id_char_field" name="char_field" type="text" />
    </div>
</div>
<div class="form-group has-error">
    <label class="control-label" for="id_char_field_required">Char field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="">
        <input class=" form-control" id="id_char_field_required" name="char_field_required" type="text" />
        <span class="help-block">Ce champ est obligatoire.</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_char_field_help">Char field</label>
    <div class="">
        <input class=" form-control" id="id_char_field_help" name="char_field_help" type="text" />
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_text_field">Text field</label>
    <div class="">
        <textarea class=" form-control" cols="40" id="id_text_field" name="text_field" rows="10"></textarea>
    </div>
</div>
<div class="form-group has-error">
    <label class="control-label" for="id_text_field_required">Text field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="">
        <textarea class=" form-control" cols="40" id="id_text_field_required" name="text_field_required" rows="10"></textarea>
        <span class="help-block">Ce champ est obligatoire.</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_text_field_help">Text field</label>
    <div class="">
        <textarea class=" form-control" cols="40" id="id_text_field_help" name="text_field_help" rows="10"></textarea>
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_choice_field">Choices field</label>
    <div class="">
        <select class=" form-control" id="id_choice_field" name="choice_field">
            <option value="A">Choice A</option>
            <option value="B">Choice B</option>
            <option value="C">Choice C</option>
        </select>
    </div>
</div>
<div class="form-group has-error">
    <label class="control-label" for="id_choice_field_required">Choices field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="">
        <select class=" form-control" id="id_choice_field_required" name="choice_field_required">
            <option value="A">Choice A</option>
            <option value="B">Choice B</option>
            <option value="C">Choice C</option>
        </select>
        <span class="help-block">Ce champ est obligatoire.</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_choice_field_help">Choices field</label>
    <div class="">
        <select class=" form-control" id="id_choice_field_help" name="choice_field_help">
            <option value="A">Choice A</option>
            <option value="B">Choice B</option>
            <option value="C">Choice C</option>
        </select>
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_radio_choice_field">Radio fields</label>
    <div class="radio">
        <label>
        <input id="id_radio_choice_field_0" name="radio_choice_field" type="radio" value="A" />
        Choice A
        </label>
    </div>
    <div class="radio">
        <label>
        <input id="id_radio_choice_field_1" name="radio_choice_field" type="radio" value="B" />
        Choice B
        </label>
    </div>
    <div class="radio">
        <label>
        <input id="id_radio_choice_field_2" name="radio_choice_field" type="radio" value="C" />
        Choice C
        </label>
    </div>
</div>
<div class="form-group has-error">
    <label class="control-label" for="id_radio_choice_field_required">Radio fields <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="radio">
        <label>
        <input id="id_radio_choice_field_required_0" name="radio_choice_field_required" type="radio" value="A" />
        Choice A
        </label>
    </div>
    <div class="radio">
        <label>
        <input id="id_radio_choice_field_required_1" name="radio_choice_field_required" type="radio" value="B" />
        Choice B
        </label>
    </div>
    <div class="radio">
        <label>
        <input id="id_radio_choice_field_required_2" name="radio_choice_field_required" type="radio" value="C" />
        Choice C
        </label>
    </div>
    <span class="help-block">Ce champ est obligatoire.</span>
</div>
<div class="form-group">
    <label class="control-label" for="id_radio_choice_field_help">Radio fields</label>
    <div class="radio">
        <label>
        <input id="id_radio_choice_field_help_0" name="radio_choice_field_help" type="radio" value="A" />
        Choice A
        </label>
    </div>
    <div class="radio">
        <label>
        <input id="id_radio_choice_field_help_1" name="radio_choice_field_help" type="radio" value="B" />
        Choice B
        </label>
    </div>
    <div class="radio">
        <label>
        <input id="id_radio_choice_field_help_2" name="radio_choice_field_help" type="radio" value="C" />
        Choice C
        </label>
    </div>
    <span class="help-block">This is a test</span>
</div>
<div class="form-group">
    <label class="control-label" for="id_checkbox_choice_field">Checkbox fields</label>
    <div class=" multiple-checkbox">
        <ul id="id_checkbox_choice_field">
            <li><label for="id_checkbox_choice_field_0"><input id="id_checkbox_choice_field_0" name="checkbox_choice_field" type="checkbox" value="A" /> Choice A</label></li>
            <li><label for="id_checkbox_choice_field_1"><input id="id_checkbox_choice_field_1" name="checkbox_choice_field" type="checkbox" value="B" /> Choice B</label></li>
            <li><label for="id_checkbox_choice_field_2"><input id="id_checkbox_choice_field_2" name="checkbox_choice_field" type="checkbox" value="C" /> Choice C</label></li>
        </ul>
    </div>
</div>
<div class="form-group has-error">
    <label class="control-label" for="id_checkbox_choice_field_required">Checkbox fields <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class=" multiple-checkbox">
        <ul id="id_checkbox_choice_field_required">
            <li><label for="id_checkbox_choice_field_required_0"><input id="id_checkbox_choice_field_required_0" name="checkbox_choice_field_required" type="checkbox" value="A" /> Choice A</label></li>
            <li><label for="id_checkbox_choice_field_required_1"><input id="id_checkbox_choice_field_required_1" name="checkbox_choice_field_required" type="checkbox" value="B" /> Choice B</label></li>
            <li><label for="id_checkbox_choice_field_required_2"><input id="id_checkbox_choice_field_required_2" name="checkbox_choice_field_required" type="checkbox" value="C" /> Choice C</label></li>
        </ul>
        <span class="help-block">Ce champ est obligatoire.</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_checkbox_choice_field_help">Checkbox fields</label>
    <div class=" multiple-checkbox">
        <ul id="id_checkbox_choice_field_help">
            <li><label for="id_checkbox_choice_field_help_0"><input id="id_checkbox_choice_field_help_0" name="checkbox_choice_field_help" type="checkbox" value="A" /> Choice A</label></li>
            <li><label for="id_checkbox_choice_field_help_1"><input id="id_checkbox_choice_field_help_1" name="checkbox_choice_field_help" type="checkbox" value="B" /> Choice B</label></li>
            <li><label for="id_checkbox_choice_field_help_2"><input id="id_checkbox_choice_field_help_2" name="checkbox_choice_field_help" type="checkbox" value="C" /> Choice C</label></li>
        </ul>
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_file_field">File field</label>
    <div class="">
        <input id="id_file_field" name="file_field" type="file" />
    </div>
</div>
<div class="form-group has-error">
    <label class="control-label" for="id_file_field_required">File field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="">
        <input id="id_file_field_required" name="file_field_required" type="file" />
        <span class="help-block">Ce champ est obligatoire.</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label" for="id_file_field_help">File field</label>
    <div class="">
        <input id="id_file_field_help" name="file_field_help" type="file" />
        <span class="help-block">This is a test</span>
    </div>
</div>
<p><small><i class="fa fa-asterisk" aria-hidden="true"></i> Mandatory fields</small></p>"""
        self.assertHTMLEqual(html_expected, html_output)

    def test_output_without_errors_horizontal(self):
        """ Test the HTML output without errors """
        template = Template('{% load bootstrapform %}{{ form|bootstrapform:"horizontal" }}')
        form = TestForm()
        context = Context({"form": form})
        html_output = template.render(context)
        html_expected = """<input id="id_hidden_field" name="hidden_field" type="hidden" value="initial value" />
<div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
        <div class="checkbox">
            <label>
            <input id="id_bool_field" name="bool_field" type="checkbox" />
            Boolean field
            </label>
        </div>
    </div>
</div>
<div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
        <div class="checkbox">
            <label>
            <input id="id_bool_field_required" name="bool_field_required" type="checkbox" />
            Boolean field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup>
            </label>
        </div>
    </div>
</div>
<div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
        <div class="checkbox">
            <label>
            <input id="id_bool_field_help" name="bool_field_help" type="checkbox" />
            Boolean field
            </label>
            <span class="help-block">This is a test</span>
        </div>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_char_field">Char field</label>
    <div class="col-sm-10">
        <input class=" form-control" id="id_char_field" name="char_field" type="text" />
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_char_field_required">Char field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="col-sm-10">
        <input class=" form-control" id="id_char_field_required" name="char_field_required" type="text" />
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_char_field_help">Char field</label>
    <div class="col-sm-10">
        <input class=" form-control" id="id_char_field_help" name="char_field_help" type="text" />
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_text_field">Text field</label>
    <div class="col-sm-10">
        <textarea class=" form-control" cols="40" id="id_text_field" name="text_field" rows="10"></textarea>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_text_field_required">Text field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="col-sm-10">
        <textarea class=" form-control" cols="40" id="id_text_field_required" name="text_field_required" rows="10"></textarea>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_text_field_help">Text field</label>
    <div class="col-sm-10">
        <textarea class=" form-control" cols="40" id="id_text_field_help" name="text_field_help" rows="10"></textarea>
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_choice_field">Choices field</label>
    <div class="col-sm-10">
        <select class=" form-control" id="id_choice_field" name="choice_field">
            <option value="A">Choice A</option>
            <option value="B">Choice B</option>
            <option value="C">Choice C</option>
        </select>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_choice_field_required">Choices field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="col-sm-10">
        <select class=" form-control" id="id_choice_field_required" name="choice_field_required">
            <option value="A">Choice A</option>
            <option value="B">Choice B</option>
            <option value="C">Choice C</option>
        </select>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_choice_field_help">Choices field</label>
    <div class="col-sm-10">
        <select class=" form-control" id="id_choice_field_help" name="choice_field_help">
            <option value="A">Choice A</option>
            <option value="B">Choice B</option>
            <option value="C">Choice C</option>
        </select>
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_radio_choice_field">Radio fields</label>
    <div class="col-sm-10">
        <div class="radio">
            <label>
            <input id="id_radio_choice_field_0" name="radio_choice_field" type="radio" value="A" />
            Choice A
            </label>
        </div>
        <div class="radio">
            <label>
            <input id="id_radio_choice_field_1" name="radio_choice_field" type="radio" value="B" />
            Choice B
            </label>
        </div>
        <div class="radio">
            <label>
            <input id="id_radio_choice_field_2" name="radio_choice_field" type="radio" value="C" />
            Choice C
            </label>
        </div>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_radio_choice_field_required">Radio fields <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="col-sm-10">
        <div class="radio">
            <label>
            <input id="id_radio_choice_field_required_0" name="radio_choice_field_required" type="radio" value="A" />
            Choice A
            </label>
        </div>
        <div class="radio">
            <label>
            <input id="id_radio_choice_field_required_1" name="radio_choice_field_required" type="radio" value="B" />
            Choice B
            </label>
        </div>
        <div class="radio">
            <label>
            <input id="id_radio_choice_field_required_2" name="radio_choice_field_required" type="radio" value="C" />
            Choice C
            </label>
        </div>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_radio_choice_field_help">Radio fields</label>
    <div class="col-sm-10">
        <div class="radio">
            <label>
            <input id="id_radio_choice_field_help_0" name="radio_choice_field_help" type="radio" value="A" />
            Choice A
            </label>
        </div>
        <div class="radio">
            <label>
            <input id="id_radio_choice_field_help_1" name="radio_choice_field_help" type="radio" value="B" />
            Choice B
            </label>
        </div>
        <div class="radio">
            <label>
            <input id="id_radio_choice_field_help_2" name="radio_choice_field_help" type="radio" value="C" />
            Choice C
            </label>
        </div>
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_checkbox_choice_field">Checkbox fields</label>
    <div class="col-sm-10 multiple-checkbox">
        <ul id="id_checkbox_choice_field">
            <li><label for="id_checkbox_choice_field_0"><input id="id_checkbox_choice_field_0" name="checkbox_choice_field" type="checkbox" value="A" /> Choice A</label></li>
            <li><label for="id_checkbox_choice_field_1"><input id="id_checkbox_choice_field_1" name="checkbox_choice_field" type="checkbox" value="B" /> Choice B</label></li>
            <li><label for="id_checkbox_choice_field_2"><input id="id_checkbox_choice_field_2" name="checkbox_choice_field" type="checkbox" value="C" /> Choice C</label></li>
        </ul>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_checkbox_choice_field_required">Checkbox fields <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="col-sm-10 multiple-checkbox">
        <ul id="id_checkbox_choice_field_required">
            <li><label for="id_checkbox_choice_field_required_0"><input id="id_checkbox_choice_field_required_0" name="checkbox_choice_field_required" type="checkbox" value="A" /> Choice A</label></li>
            <li><label for="id_checkbox_choice_field_required_1"><input id="id_checkbox_choice_field_required_1" name="checkbox_choice_field_required" type="checkbox" value="B" /> Choice B</label></li>
            <li><label for="id_checkbox_choice_field_required_2"><input id="id_checkbox_choice_field_required_2" name="checkbox_choice_field_required" type="checkbox" value="C" /> Choice C</label></li>
        </ul>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_checkbox_choice_field_help">Checkbox fields</label>
    <div class="col-sm-10 multiple-checkbox">
        <ul id="id_checkbox_choice_field_help">
            <li><label for="id_checkbox_choice_field_help_0"><input id="id_checkbox_choice_field_help_0" name="checkbox_choice_field_help" type="checkbox" value="A" /> Choice A</label></li>
            <li><label for="id_checkbox_choice_field_help_1"><input id="id_checkbox_choice_field_help_1" name="checkbox_choice_field_help" type="checkbox" value="B" /> Choice B</label></li>
            <li><label for="id_checkbox_choice_field_help_2"><input id="id_checkbox_choice_field_help_2" name="checkbox_choice_field_help" type="checkbox" value="C" /> Choice C</label></li>
        </ul>
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_file_field">File field</label>
    <div class="col-sm-10">
        <input id="id_file_field" name="file_field" type="file" />
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_file_field_required">File field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="col-sm-10">
        <input id="id_file_field_required" name="file_field_required" type="file" />
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_file_field_help">File field</label>
    <div class="col-sm-10">
        <input id="id_file_field_help" name="file_field_help" type="file" />
        <span class="help-block">This is a test</span>
    </div>
</div>
<p class="col-sm-12"><small><i class="fa fa-asterisk" aria-hidden="true"></i> Mandatory fields</small></p>"""
        self.assertHTMLEqual(html_expected, html_output)

    def test_output_with_errors_horizontal(self):
        """ Test the HTML output without errors """
        template = Template('{% load bootstrapform %}{{ form|bootstrapform:"horizontal" }}')
        form = TestForm(data={}, files={})
        form.is_valid()
        context = Context({"form": form})
        html_output = template.render(context)
        html_expected = """<div class="alert alert-danger col-sm-12">
    <ul>
        <li>
            <p>This is a non field error</p>
        </li>
    </ul>
</div>
<input id="id_hidden_field" name="hidden_field" type="hidden" />
<div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
        <div class="checkbox">
            <label>
            <input id="id_bool_field" name="bool_field" type="checkbox" />
            Boolean field
            </label>
        </div>
    </div>
</div>
<div class="form-group has-error">
    <div class="col-sm-offset-2 col-sm-10">
        <div class="checkbox">
            <label>
            <input id="id_bool_field_required" name="bool_field_required" type="checkbox" />
            Boolean field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup>
            </label>
            <span class="help-block">Ce champ est obligatoire.</span>
        </div>
    </div>
</div>
<div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
        <div class="checkbox">
            <label>
            <input id="id_bool_field_help" name="bool_field_help" type="checkbox" />
            Boolean field
            </label>
            <span class="help-block">This is a test</span>
        </div>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_char_field">Char field</label>
    <div class="col-sm-10">
        <input class=" form-control" id="id_char_field" name="char_field" type="text" />
    </div>
</div>
<div class="form-group has-error">
    <label class="control-label col-sm-2" for="id_char_field_required">Char field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="col-sm-10">
        <input class=" form-control" id="id_char_field_required" name="char_field_required" type="text" />
        <span class="help-block">Ce champ est obligatoire.</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_char_field_help">Char field</label>
    <div class="col-sm-10">
        <input class=" form-control" id="id_char_field_help" name="char_field_help" type="text" />
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_text_field">Text field</label>
    <div class="col-sm-10">
        <textarea class=" form-control" cols="40" id="id_text_field" name="text_field" rows="10"></textarea>
    </div>
</div>
<div class="form-group has-error">
    <label class="control-label col-sm-2" for="id_text_field_required">Text field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="col-sm-10">
        <textarea class=" form-control" cols="40" id="id_text_field_required" name="text_field_required" rows="10"></textarea>
        <span class="help-block">Ce champ est obligatoire.</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_text_field_help">Text field</label>
    <div class="col-sm-10">
        <textarea class=" form-control" cols="40" id="id_text_field_help" name="text_field_help" rows="10"></textarea>
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_choice_field">Choices field</label>
    <div class="col-sm-10">
        <select class=" form-control" id="id_choice_field" name="choice_field">
            <option value="A">Choice A</option>
            <option value="B">Choice B</option>
            <option value="C">Choice C</option>
        </select>
    </div>
</div>
<div class="form-group has-error">
    <label class="control-label col-sm-2" for="id_choice_field_required">Choices field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="col-sm-10">
        <select class=" form-control" id="id_choice_field_required" name="choice_field_required">
            <option value="A">Choice A</option>
            <option value="B">Choice B</option>
            <option value="C">Choice C</option>
        </select>
        <span class="help-block">Ce champ est obligatoire.</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_choice_field_help">Choices field</label>
    <div class="col-sm-10">
        <select class=" form-control" id="id_choice_field_help" name="choice_field_help">
            <option value="A">Choice A</option>
            <option value="B">Choice B</option>
            <option value="C">Choice C</option>
        </select>
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_radio_choice_field">Radio fields</label>
    <div class="col-sm-10">
        <div class="radio">
            <label>
            <input id="id_radio_choice_field_0" name="radio_choice_field" type="radio" value="A" />
            Choice A
            </label>
        </div>
        <div class="radio">
            <label>
            <input id="id_radio_choice_field_1" name="radio_choice_field" type="radio" value="B" />
            Choice B
            </label>
        </div>
        <div class="radio">
            <label>
            <input id="id_radio_choice_field_2" name="radio_choice_field" type="radio" value="C" />
            Choice C
            </label>
        </div>
    </div>
</div>
<div class="form-group has-error">
    <label class="control-label col-sm-2" for="id_radio_choice_field_required">Radio fields <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="col-sm-10">
        <div class="radio">
            <label>
            <input id="id_radio_choice_field_required_0" name="radio_choice_field_required" type="radio" value="A" />
            Choice A
            </label>
        </div>
        <div class="radio">
            <label>
            <input id="id_radio_choice_field_required_1" name="radio_choice_field_required" type="radio" value="B" />
            Choice B
            </label>
        </div>
        <div class="radio">
            <label>
            <input id="id_radio_choice_field_required_2" name="radio_choice_field_required" type="radio" value="C" />
            Choice C
            </label>
        </div>
        <span class="help-block">Ce champ est obligatoire.</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_radio_choice_field_help">Radio fields</label>
    <div class="col-sm-10">
        <div class="radio">
            <label>
            <input id="id_radio_choice_field_help_0" name="radio_choice_field_help" type="radio" value="A" />
            Choice A
            </label>
        </div>
        <div class="radio">
            <label>
            <input id="id_radio_choice_field_help_1" name="radio_choice_field_help" type="radio" value="B" />
            Choice B
            </label>
        </div>
        <div class="radio">
            <label>
            <input id="id_radio_choice_field_help_2" name="radio_choice_field_help" type="radio" value="C" />
            Choice C
            </label>
        </div>
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_checkbox_choice_field">Checkbox fields</label>
    <div class="col-sm-10 multiple-checkbox">
        <ul id="id_checkbox_choice_field">
            <li><label for="id_checkbox_choice_field_0"><input id="id_checkbox_choice_field_0" name="checkbox_choice_field" type="checkbox" value="A" /> Choice A</label></li>
            <li><label for="id_checkbox_choice_field_1"><input id="id_checkbox_choice_field_1" name="checkbox_choice_field" type="checkbox" value="B" /> Choice B</label></li>
            <li><label for="id_checkbox_choice_field_2"><input id="id_checkbox_choice_field_2" name="checkbox_choice_field" type="checkbox" value="C" /> Choice C</label></li>
        </ul>
    </div>
</div>
<div class="form-group has-error">
    <label class="control-label col-sm-2" for="id_checkbox_choice_field_required">Checkbox fields <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="col-sm-10 multiple-checkbox">
        <ul id="id_checkbox_choice_field_required">
            <li><label for="id_checkbox_choice_field_required_0"><input id="id_checkbox_choice_field_required_0" name="checkbox_choice_field_required" type="checkbox" value="A" /> Choice A</label></li>
            <li><label for="id_checkbox_choice_field_required_1"><input id="id_checkbox_choice_field_required_1" name="checkbox_choice_field_required" type="checkbox" value="B" /> Choice B</label></li>
            <li><label for="id_checkbox_choice_field_required_2"><input id="id_checkbox_choice_field_required_2" name="checkbox_choice_field_required" type="checkbox" value="C" /> Choice C</label></li>
        </ul>
        <span class="help-block">Ce champ est obligatoire.</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_checkbox_choice_field_help">Checkbox fields</label>
    <div class="col-sm-10 multiple-checkbox">
        <ul id="id_checkbox_choice_field_help">
            <li><label for="id_checkbox_choice_field_help_0"><input id="id_checkbox_choice_field_help_0" name="checkbox_choice_field_help" type="checkbox" value="A" /> Choice A</label></li>
            <li><label for="id_checkbox_choice_field_help_1"><input id="id_checkbox_choice_field_help_1" name="checkbox_choice_field_help" type="checkbox" value="B" /> Choice B</label></li>
            <li><label for="id_checkbox_choice_field_help_2"><input id="id_checkbox_choice_field_help_2" name="checkbox_choice_field_help" type="checkbox" value="C" /> Choice C</label></li>
        </ul>
        <span class="help-block">This is a test</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_file_field">File field</label>
    <div class="col-sm-10">
        <input id="id_file_field" name="file_field" type="file" />
    </div>
</div>
<div class="form-group has-error">
    <label class="control-label col-sm-2" for="id_file_field_required">File field <sup><i class="fa fa-asterisk" title="Mandatory field" aria-hidden="true"></i></sup></label>
    <div class="col-sm-10">
        <input id="id_file_field_required" name="file_field_required" type="file" />
        <span class="help-block">Ce champ est obligatoire.</span>
    </div>
</div>
<div class="form-group">
    <label class="control-label col-sm-2" for="id_file_field_help">File field</label>
    <div class="col-sm-10">
        <input id="id_file_field_help" name="file_field_help" type="file" />
        <span class="help-block">This is a test</span>
    </div>
</div>
<p class="col-sm-12"><small><i class="fa fa-asterisk" aria-hidden="true"></i> Mandatory fields</small></p>"""
        self.assertHTMLEqual(html_expected, html_output)
