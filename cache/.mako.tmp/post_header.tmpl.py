# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1551072002.9060721
_enable_loop = True
_template_filename = 'themes/mdl/templates/post_header.tmpl'
_template_uri = 'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_title', 'html_translations', 'html_sourcelink', 'html_metalink', 'html_post_header', 'html_post_metadata', 'html_post_actions']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <div class="mdl-card__title">\n        <h1 class="mdl-card__title-text p-name entry-title"\n            itemprop="headline name">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</h1>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        sorted = context.get('sorted', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(post.translated_to) > 1:
            __M_writer('        <div class="metadata posttranslations translations">\n            <h2 class="posttranslations-intro">')
            __M_writer(str(messages("Also available in:")))
            __M_writer('</h2>\n')
            for langname in sorted(translations):
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('                <p><a href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('" rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('">')
                    __M_writer(str(messages("LANGUAGE", langname)))
                    __M_writer('</a></p>\n')
            __M_writer('        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('    <a class="mdl-button mdl-js-button mdl-js-ripple-effect mdl-button--colored mdl-button--accent site-post__source-link" rel="tag" title="')
            __M_writer(str(messages('Source')))
            __M_writer('" href="')
            __M_writer(str(post.source_link()))
            __M_writer('">')
            __M_writer(str(messages('Source')))
            __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_metalink(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.meta('link'):
            __M_writer('    <a class="mdl-button mdl-js-button mdl-js-ripple-effect mdl-button--colored mdl-button--accent metadata-original-site-link" rel="tag" title="')
            __M_writer(str(messages('Original site')))
            __M_writer('" href="')
            __M_writer(str(post.meta('link')))
            __M_writer('">')
            __M_writer(str(messages('Original site')))
            __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_post_header(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_title():
            return render_html_title(context)
        def html_translations(post):
            return render_html_translations(context,post)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(html_title()))
        __M_writer('\n')
        if post.description():
            __M_writer('    <meta name="description" itemprop="description" content="')
            __M_writer(filters.html_escape(str(post.description())))
            __M_writer('">\n')
        __M_writer('    ')
        __M_writer(str(html_translations(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_post_metadata(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        date_format = context.get('date_format', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="mdl-grid mdl-card__supporting-text mdl-card--border metadata">\n        <div class="mdl-cell mdl-cell--1-col">\n          <button class="mdl-button mdl-js-button mdl-button--fab mdl-button--colored mdl-js-ripple-effect">')
        __M_writer(str("".join([x[0].upper() for x in post.author().split()])))
        __M_writer('</button>\n        </div>\n        <div class="mdl-grid mdl-cell mdl-cell--9-col">\n            <span class="mdl-cell mdl-cell--12-col site-post__author no-margin-bottom">\n')
        if author_pages_generated:
            __M_writer('                <a href="')
            __M_writer(str(_link('author', post.author())))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.author())))
            __M_writer('</a>\n')
        else:
            __M_writer('                ')
            __M_writer(filters.html_escape(str(post.author())))
            __M_writer('\n')
        __M_writer('            </span>\n            <span class="mdl-cell mdl-cell--12-col site-post__date">\n                <time class="published dt-published" datetime="')
        __M_writer(str(post.formatted_date('webiso')))
        __M_writer('" itemprop="datePublished" title="')
        __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
        __M_writer('">')
        __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
        __M_writer('\n                </time>\n            </span>\n        </div>\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('        <span class="mdl-cell mdl-cell--2-col site-post__total-comment">\n                ')
            __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
            __M_writer('\n        </span>\n')
        __M_writer('    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_post_actions(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        helper = _mako_get_namespace(context, 'helper')
        def html_sourcelink(post):
            return render_html_sourcelink(context,post)
        def html_metalink(post):
            return render_html_metalink(context,post)
        __M_writer = context.writer()
        __M_writer('\n    <div class="mdl-grid mdl-card__actions mdl-card--border">\n        ')
        __M_writer(str(helper.html_tags(post)))
        __M_writer('\n        <div class="section-spacer"></div>\n        ')
        __M_writer(str(html_sourcelink(post)))
        __M_writer('\n        ')
        __M_writer(str(html_metalink(post)))
        __M_writer('\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/mdl/templates/post_header.tmpl", "uri": "post_header.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 0, "34": 2, "35": 3, "36": 12, "37": 25, "38": 31, "39": 37, "40": 45, "41": 71, "42": 80, "48": 5, "54": 5, "55": 6, "56": 7, "57": 9, "58": 9, "64": 14, "73": 14, "74": 15, "75": 16, "76": 17, "77": 17, "78": 18, "79": 19, "80": 20, "81": 20, "82": 20, "83": 20, "84": 20, "85": 20, "86": 20, "87": 23, "93": 27, "99": 27, "100": 28, "101": 29, "102": 29, "103": 29, "104": 29, "105": 29, "106": 29, "107": 29, "113": 33, "118": 33, "119": 34, "120": 35, "121": 35, "122": 35, "123": 35, "124": 35, "125": 35, "126": 35, "132": 39, "140": 39, "141": 40, "142": 40, "143": 41, "144": 42, "145": 42, "146": 42, "147": 44, "148": 44, "149": 44, "155": 47, "164": 47, "165": 50, "166": 50, "167": 54, "168": 55, "169": 55, "170": 55, "171": 55, "172": 55, "173": 56, "174": 57, "175": 57, "176": 57, "177": 59, "178": 61, "179": 61, "180": 61, "181": 61, "182": 61, "183": 61, "184": 65, "185": 66, "186": 67, "187": 67, "188": 70, "194": 73, "203": 73, "204": 75, "205": 75, "206": 77, "207": 77, "208": 78, "209": 78, "215": 209}}
__M_END_METADATA
"""
