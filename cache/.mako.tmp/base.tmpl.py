# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1551072002.933816
_enable_loop = True
_template_filename = 'themes/mdl/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

    ns = runtime.TemplateNamespace('header', context._clean_inheritance_tokens(), templateuri='base_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'header')] = ns

    ns = runtime.TemplateNamespace('footer', context._clean_inheritance_tokens(), templateuri='base_footer.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'footer')] = ns

    ns = runtime.TemplateNamespace('annotations', context._clean_inheritance_tokens(), templateuri='annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'annotations')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        base = _mako_get_namespace(context, 'base')
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        mdl__no_drawer_button = _import_ns.get('mdl__no_drawer_button', context.get('mdl__no_drawer_button', UNDEFINED))
        mdl__late_load_css = _import_ns.get('mdl__late_load_css', context.get('mdl__late_load_css', UNDEFINED))
        mdl__no_desktop_drawer_button = _import_ns.get('mdl__no_desktop_drawer_button', context.get('mdl__no_desktop_drawer_button', UNDEFINED))
        footer = _mako_get_namespace(context, 'footer')
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        header = _mako_get_namespace(context, 'header')
        mdl__fixed_header = _import_ns.get('mdl__fixed_header', context.get('mdl__fixed_header', UNDEFINED))
        mdl__fixed_drawer = _import_ns.get('mdl__fixed_drawer', context.get('mdl__fixed_drawer', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n</head>\n<body>\n    <a href="#content" class="sr-only sr-only-focusable">')
        __M_writer(str(messages("Skip to main content")))
        __M_writer('</a>\n    <div id="container" class="site mdl-layout mdl-js-layout\n')
        if mdl__fixed_header:
            __M_writer('mdl-layout--fixed-header\n')
        if mdl__fixed_drawer:
            __M_writer('mdl-layout--fixed-drawer\n')
        if mdl__no_drawer_button:
            __M_writer('mdl-layout--no-drawer-button\n')
        if mdl__no_desktop_drawer_button:
            __M_writer('mdl-layout--no-desktop-drawer-button\n')
        __M_writer('    ">\n         ')
        __M_writer(str(header.html_header()))
        __M_writer('\n         <main id="content" class="mdl-layout__content">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n            ')
        __M_writer(str(footer.html_footer()))
        __M_writer('\n         </main>\n    </div>\n')
        if mdl__late_load_css:
            __M_writer('        ')
            __M_writer(str(base.late_load_css()))
            __M_writer('\n')
        __M_writer('    ')
        __M_writer(str(base.late_load_js()))
        __M_writer('\n    ')
        __M_writer(str(body_end))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/mdl/templates/base.tmpl", "uri": "base.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "35": 0, "61": 2, "62": 3, "63": 4, "64": 5, "65": 6, "66": 6, "67": 7, "68": 7, "73": 10, "74": 11, "75": 11, "76": 14, "77": 14, "78": 16, "79": 17, "80": 19, "81": 20, "82": 22, "83": 23, "84": 25, "85": 26, "86": 28, "87": 29, "88": 29, "93": 31, "94": 32, "95": 32, "96": 35, "97": 36, "98": 36, "99": 36, "100": 38, "101": 38, "102": 38, "103": 39, "104": 39, "105": 40, "106": 40, "112": 8, "122": 8, "128": 31, "143": 128}}
__M_END_METADATA
"""
