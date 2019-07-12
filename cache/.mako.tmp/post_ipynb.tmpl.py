# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1562973196.8938172
_enable_loop = True
_template_filename = 'themes/bootstrap3-gradients/templates/post_ipynb.tmpl'
_template_uri = 'post_ipynb.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        math = _mako_get_namespace(context, 'math')
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        helper = _mako_get_namespace(context, 'helper')
        def content():
            return render_content(context._locals(__M_locals))
        pheader = _mako_get_namespace(context, 'pheader')
        parent = context.get('parent', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        math = _mako_get_namespace(context, 'math')
        helper = _mako_get_namespace(context, 'helper')
        parent = context.get('parent', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        __M_writer('\n\n')
        if post.prev_post:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(post.prev_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.prev_post.title())))
            __M_writer('" type="text/html">\n')
        __M_writer('\n')
        if post.next_post:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(post.next_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.next_post.title())))
            __M_writer('" type="text/html">\n')
        __M_writer('\n')
        if post.is_draft:
            __M_writer('        <meta name="robots" content="noindex">\n')
        __M_writer('    \n    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\n    ')
        __M_writer(str(math.math_styles_ifpost(post)))
        __M_writer('\n    \n    <script type="text/javascript" src="https://code.jquery.com/jquery.min.js"></script>\n    \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        math = _mako_get_namespace(context, 'math')
        comments = _mako_get_namespace(context, 'comments')
        helper = _mako_get_namespace(context, 'helper')
        pheader = _mako_get_namespace(context, 'pheader')
        def content():
            return render_content(context)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="post-')
        __M_writer(str(post.meta('type')))
        __M_writer(' h-entry hentry postpage" itemscope="itemscope" itemtype="http://schema.org/Article">\n    ')
        __M_writer(str(pheader.html_post_header()))
        __M_writer('\n\n\n    <div class="e-content entry-content" itemprop="articleBody text">\n    ')
        __M_writer(str(post.text()))
        __M_writer('\n    </div>\n    <aside class="postpromonav">\n    <nav>\n    ')
        __M_writer(str(helper.html_tags(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\n    </nav>\n    </aside>\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('        <section class="comments hidden-print">\n        <h2>')
            __M_writer(str(messages("Comments")))
            __M_writer('</h2>\n        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\n        </section>\n')
        __M_writer('    ')
        __M_writer(str(math.math_scripts_ifpost(post)))
        __M_writer('\n</article>\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('    <li>\n    <a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bootstrap3-gradients/templates/post_ipynb.tmpl", "uri": "post_ipynb.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "38": 0, "58": 2, "59": 3, "60": 4, "61": 5, "62": 6, "67": 34, "72": 59, "82": 8, "92": 8, "93": 9, "94": 9, "95": 10, "96": 11, "97": 11, "98": 11, "99": 13, "100": 15, "101": 16, "102": 16, "103": 16, "104": 16, "105": 16, "106": 18, "107": 19, "108": 20, "109": 20, "110": 20, "111": 20, "112": 20, "113": 22, "114": 23, "115": 24, "116": 26, "117": 27, "118": 27, "119": 28, "120": 28, "121": 29, "122": 29, "123": 30, "124": 30, "130": 36, "143": 36, "144": 37, "145": 37, "146": 38, "147": 38, "148": 42, "149": 42, "150": 46, "151": 46, "152": 47, "153": 47, "154": 50, "155": 51, "156": 52, "157": 52, "158": 53, "159": 53, "160": 56, "161": 56, "162": 56, "163": 58, "164": 58, "170": 61, "179": 61, "180": 62, "181": 63, "182": 64, "183": 64, "184": 64, "185": 64, "191": 185}}
__M_END_METADATA
"""
