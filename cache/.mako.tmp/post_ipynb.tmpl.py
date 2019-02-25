# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1551074712.828073
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
        code = context.get('code', UNDEFINED)
        post = context.get('post', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        math = _mako_get_namespace(context, 'math')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
        def content():
            return render_content(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        helper = _mako_get_namespace(context, 'helper')
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
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
        post = context.get('post', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        helper = _mako_get_namespace(context, 'helper')
        math = _mako_get_namespace(context, 'math')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        __M_writer('    <meta name="author" content="')
        __M_writer(filters.html_escape(str(post.author())))
        __M_writer('">\n')
        if post.prev_post:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(post.prev_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.prev_post.title())))
            __M_writer('" type="text/html">\n')
        if post.next_post:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(post.next_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.next_post.title())))
            __M_writer('" type="text/html">\n')
        if post.is_draft:
            __M_writer('        <meta name="robots" content="noindex">\n')
        __M_writer('    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\n    ')
        __M_writer(str(math.math_styles_ifpost(post)))
        __M_writer('\n    \n    <script type="text/javascript" src="https://code.jquery.com/jquery.min.js"></script>\n    <script src="/assets/js/bootyper.js"></script>    \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        code = context.get('code', UNDEFINED)
        post = context.get('post', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
        def content():
            return render_content(context)
        helper = _mako_get_namespace(context, 'helper')
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="post-')
        __M_writer(str(post.meta('type')))
        __M_writer(' h-entry hentry postpage" itemscope="itemscope" itemtype="http://schema.org/Article">\n    ')
        __M_writer(str(pheader.html_post_header()))
        __M_writer('\n\n')
        if needs_ipython_css:
            __M_writer("    <div>\n\n\n\n<script>\n\n//console.log(code_show);\n//\n//if (typeof code_show == 'undefined') {\n//    code_show = true\n//  } else {\n//    code_show = false\n//    }\n//\n//console.log(code_show);\n\n\n//function code_toggle() {\n//    console.log('code_toggle');\n//    console.log(code_show);\t\n//\n// if (!code_show){\n// $('div.input').hide();\n// $('div.prompt.output_prompt').hide();\n// } else {\n// $('div.input').show();\n// }\n// code_show = !code_show\n//}\n\n")
            if code == "False":
                __M_writer('     code_show = false;\n')
            else:
                __M_writer('     code_show = true;\n')
            __M_writer('console.log(code_show)\n$( document ).ready(toggle_setup);\n$( document ).ready(code_toggle);\n\n// if the image in the window of browser when the page is loaded, show that image (fade in)\n$(document).ready(function(){\n        showImages(\'article img\');\n});\n\n// if the image in the window of browser when scrolling the page, show that image\n$(window).scroll(function() {\n        showImages(\'article img\');\n});\n</script>\n\n\n</script>\n<form id="toggle-button" action="javascript:code_toggle()"><input type="submit" class="btn btn-primary" value="Click here to toggle on/off the raw code."></form>\n    </div>\n')
        __M_writer('    \n\n    <div class="e-content entry-content" itemprop="articleBody text">\n    ')
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
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
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
{"filename": "themes/bootstrap3-gradients/templates/post_ipynb.tmpl", "uri": "post_ipynb.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "38": 0, "60": 2, "61": 3, "62": 4, "63": 5, "64": 6, "69": 30, "74": 112, "84": 8, "94": 8, "95": 9, "96": 9, "97": 10, "98": 11, "99": 11, "100": 11, "101": 13, "102": 13, "103": 13, "104": 14, "105": 15, "106": 15, "107": 15, "108": 15, "109": 15, "110": 17, "111": 18, "112": 18, "113": 18, "114": 18, "115": 18, "116": 20, "117": 21, "118": 23, "119": 23, "120": 23, "121": 24, "122": 24, "123": 25, "124": 25, "125": 26, "126": 26, "132": 32, "147": 32, "148": 33, "149": 33, "150": 34, "151": 34, "152": 36, "153": 37, "154": 67, "155": 68, "156": 69, "157": 70, "158": 72, "159": 92, "160": 95, "161": 95, "162": 99, "163": 99, "164": 100, "165": 100, "166": 103, "167": 104, "168": 105, "169": 105, "170": 106, "171": 106, "172": 109, "173": 109, "174": 109, "175": 111, "176": 111, "182": 114, "191": 114, "192": 115, "193": 116, "194": 117, "195": 117, "196": 117, "197": 117, "203": 197}}
__M_END_METADATA
"""
