# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1551071284.658794
_enable_loop = True
_template_filename = 'themes/mdl/templates/post_helper.tmpl'
_template_uri = 'post_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['meta_translations', 'html_tags', 'html_pager', 'open_graph_metadata', 'twitter_card_information', 'mathjax_script']


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
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            for langname in sorted(translations):
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('                <link rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('" href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.tags:
            for tag in post.tags:
                if tag not in hidden_tags:
                    __M_writer('              <a class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--colored mdl-button--accent site-post__tag" rel="tag" title="')
                    __M_writer(filters.html_escape(str(tag)))
                    __M_writer('" href="')
                    __M_writer(str(_link('tag', tag)))
                    __M_writer('">')
                    __M_writer(filters.html_escape(str(tag)))
                    __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.prev_post or post.next_post:
            __M_writer('        <nav class="site-navigation hidden-print pager mdl-cell mdl-cell--12-col">\n')
            if post.prev_post:
                __M_writer('                <a href="')
                __M_writer(str(post.prev_post.permalink()))
                __M_writer('" class="site-navigation__button site-navigation__previous" rel="prev" title="')
                __M_writer(filters.html_escape(str(post.prev_post.title())))
                __M_writer('">\n                  <button class="mdl-button mdl-js-button mdl-button--icon mdl-js-ripple-effect">\n                    <i class="material-icons" role="presentation">arrow_back</i>\n                  </button>\n                  ')
                __M_writer(str(messages("Previous post")))
                __M_writer('\n                </a>\n')
            __M_writer('            <div class="section-spacer"></div>\n')
            if post.next_post:
                __M_writer('                <a href="')
                __M_writer(str(post.next_post.permalink()))
                __M_writer('" class="site-navigation__button site-navigation__next" rel="next" title="')
                __M_writer(filters.html_escape(str(post.next_post.title())))
                __M_writer('">\n                  ')
                __M_writer(str(messages("Next post")))
                __M_writer('\n                  <button class="mdl-button mdl-js-button mdl-button--icon mdl-js-ripple-effect">\n                    <i class="material-icons" role="presentation">arrow_forward</i>\n                  </button>\n                </a>\n')
            __M_writer('        </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_open_graph_metadata(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_open_graph:
            __M_writer('    <meta property="og:site_name" content="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('">\n    <meta property="og:title" content="')
            __M_writer(filters.html_escape(str(post.title()[:70])))
            __M_writer('">\n    <meta property="og:url" content="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
            if post.description():
                __M_writer('    <meta property="og:description" content="')
                __M_writer(filters.html_escape(str(post.description()[:200])))
                __M_writer('">\n')
            else:
                __M_writer('    <meta property="og:description" content="')
                __M_writer(filters.html_escape(str(post.text(strip_html=True)[:200])))
                __M_writer('">\n')
            if post.previewimage:
                __M_writer('    <meta property="og:image" content="')
                __M_writer(str(url_replacer(permalink, post.previewimage, lang, 'absolute')))
                __M_writer('">\n')
            __M_writer('    <meta property="og:type" content="article">\n')
            if post.date.isoformat():
                __M_writer('    <meta property="article:published_time" content="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('">\n')
            if post.tags:
                for tag in post.tags:
                    __M_writer('           <meta property="article:tag" content="')
                    __M_writer(filters.html_escape(str(tag)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_twitter_card_information(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        twitter_card = context.get('twitter_card', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if twitter_card and twitter_card['use_twitter_cards']:
            __M_writer('    <meta name="twitter:card" content="')
            __M_writer(filters.html_escape(str(twitter_card.get('card', 'summary'))))
            __M_writer('">\n')
            if 'site:id' in twitter_card:
                __M_writer('    <meta name="twitter:site:id" content="')
                __M_writer(str(twitter_card['site:id']))
                __M_writer('">\n')
            elif 'site' in twitter_card:
                __M_writer('    <meta name="twitter:site" content="')
                __M_writer(str(twitter_card['site']))
                __M_writer('">\n')
            if 'creator:id' in twitter_card:
                __M_writer('    <meta name="twitter:creator:id" content="')
                __M_writer(str(twitter_card['creator:id']))
                __M_writer('">\n')
            elif 'creator' in twitter_card:
                __M_writer('    <meta name="twitter:creator" content="')
                __M_writer(str(twitter_card['creator']))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_katex = context.get('use_katex', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.has_math:
            if use_katex:
                __M_writer('            <script async src="//cdnjs.cloudflare.com/ajax/libs/KaTeX/0.3.0/katex.min.js"></script>\n            <script async src="//cdnjs.cloudflare.com/ajax/libs/KaTeX/0.3.0/contrib/auto-render.min.js"></script>\n            <script>\n                renderMathInElement(document.body);\n            </script>\n')
            else:
                __M_writer('            <script async type="text/javascript" src="//cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"> </script>\n            <script type="text/x-mathjax-config">\n            MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$latex \',\'$\'], [\'\\\\(\',\'\\\\)\']]}});\n            </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/mdl/templates/post_helper.tmpl", "uri": "post_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 11, "23": 21, "24": 45, "25": 74, "26": 90, "27": 107, "33": 3, "41": 3, "42": 4, "43": 5, "44": 6, "45": 7, "46": 7, "47": 7, "48": 7, "49": 7, "55": 13, "61": 13, "62": 14, "63": 15, "64": 16, "65": 17, "66": 17, "67": 17, "68": 17, "69": 17, "70": 17, "71": 17, "77": 23, "82": 23, "83": 24, "84": 25, "85": 26, "86": 27, "87": 27, "88": 27, "89": 27, "90": 27, "91": 31, "92": 31, "93": 34, "94": 35, "95": 36, "96": 36, "97": 36, "98": 36, "99": 36, "100": 37, "101": 37, "102": 43, "108": 47, "118": 47, "119": 48, "120": 49, "121": 49, "122": 49, "123": 50, "124": 50, "125": 51, "126": 51, "127": 52, "128": 53, "129": 53, "130": 53, "131": 54, "132": 55, "133": 55, "134": 55, "135": 57, "136": 58, "137": 58, "138": 58, "139": 60, "140": 65, "141": 66, "142": 66, "143": 66, "144": 68, "145": 69, "146": 70, "147": 70, "148": 70, "154": 76, "159": 76, "160": 77, "161": 78, "162": 78, "163": 78, "164": 79, "165": 80, "166": 80, "167": 80, "168": 81, "169": 82, "170": 82, "171": 82, "172": 84, "173": 85, "174": 85, "175": 85, "176": 86, "177": 87, "178": 87, "179": 87, "185": 92, "190": 92, "191": 93, "192": 94, "193": 95, "194": 100, "195": 101, "201": 195}}
__M_END_METADATA
"""
