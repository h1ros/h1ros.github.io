# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1551072109.1257632
_enable_loop = True
_template_filename = 'themes/mdl/templates/helper.tmpl'
_template_uri = 'helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_js', 'extra_css']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n<script defer type="text/javascript"\n    src="/assets/js/custom.js" >\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_css(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        mdl__cachebusting = context.get('mdl__cachebusting', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<link rel="stylesheet" type="text/css"\n    href="/assets/css/custom.css?v=')
        __M_writer(str(mdl__cachebusting))
        __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/mdl/templates/helper.tmpl", "uri": "helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 7, "23": 12, "29": 3, "33": 3, "39": 9, "44": 9, "45": 11, "46": 11, "52": 46}}
__M_END_METADATA
"""
