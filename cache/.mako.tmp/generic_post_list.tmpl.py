# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1560996993.2667992
_enable_loop = True
_template_filename = 'themes/bootstrap3/templates/generic_post_list.tmpl'
_template_uri = 'generic_post_list.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        posts = context.get('posts', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        post_list_id = context.get('post_list_id', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        posts = context.get('posts', UNDEFINED)
        def content():
            return render_content(context)
        post_list_id = context.get('post_list_id', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!-- Begin post-list ')
        __M_writer(str(post_list_id))
        __M_writer(' -->\n<div id="')
        __M_writer(str(post_list_id))
        __M_writer('" class="post-list">\n')
        if posts:
            __M_writer('    <ul class="post-list">\n')
            for post in posts:
                __M_writer('            <li class="post-list-item">\n            <a href="')
                __M_writer(str(post.permalink(lang)))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.title(lang))))
                __M_writer('</a>\n            </li>\n')
            __M_writer('    </ul>\n')
        __M_writer('</div>\n<!-- End post-list ')
        __M_writer(str(post_list_id))
        __M_writer(' -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bootstrap3/templates/generic_post_list.tmpl", "uri": "generic_post_list.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "35": 2, "44": 2, "45": 3, "46": 3, "47": 4, "48": 4, "49": 5, "50": 6, "51": 7, "52": 8, "53": 9, "54": 9, "55": 9, "56": 9, "57": 12, "58": 14, "59": 15, "60": 15, "66": 60}}
__M_END_METADATA
"""
