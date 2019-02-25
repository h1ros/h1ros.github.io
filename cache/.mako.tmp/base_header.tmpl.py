# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1551071902.43621
_enable_loop = True
_template_filename = 'themes/mdl/templates/base_header.tmpl'
_template_uri = 'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_header', 'html_site_title', 'html_navigation_links', 'html_more_button']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def html_more_button():
            return render_html_more_button(context)
        mdl__multiple_header = _import_ns.get('mdl__multiple_header', context.get('mdl__multiple_header', UNDEFINED))
        mdl__header_waterfall_hide_top = _import_ns.get('mdl__header_waterfall_hide_top', context.get('mdl__header_waterfall_hide_top', UNDEFINED))
        mdl__navigation_large_screen_only = _import_ns.get('mdl__navigation_large_screen_only', context.get('mdl__navigation_large_screen_only', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        def html_navigation_links():
            return render_html_navigation_links(context)
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        mdl__header_waterfall = _import_ns.get('mdl__header_waterfall', context.get('mdl__header_waterfall', UNDEFINED))
        navigation_row_middle = _import_ns.get('navigation_row_middle', context.get('navigation_row_middle', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        top_nav_header = _import_ns.get('top_nav_header', context.get('top_nav_header', UNDEFINED))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def html_site_title():
            return render_html_site_title(context)
        mdl__header_transparent = _import_ns.get('mdl__header_transparent', context.get('mdl__header_transparent', UNDEFINED))
        mdl__header_seamed = _import_ns.get('mdl__header_seamed', context.get('mdl__header_seamed', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        mdl__header_scroll = _import_ns.get('mdl__header_scroll', context.get('mdl__header_scroll', UNDEFINED))
        title_row_middle = _import_ns.get('title_row_middle', context.get('title_row_middle', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <header id="header" class="mdl-layout__header site-header\n')
        if mdl__header_scroll:
            __M_writer('mdl-layout__header--scroll\n')
        if mdl__header_waterfall:
            __M_writer('mdl-layout__header--waterfall\n')
        if mdl__header_waterfall_hide_top:
            __M_writer('mdl-layout__header--waterfall-hide-top\n')
        if mdl__header_transparent:
            __M_writer('mdl-layout__header--transparent\n')
        if mdl__header_seamed:
            __M_writer('mdl-layout__header--seamed\n')
        __M_writer('    ">\n        <div class="mdl-layout__header-row site-header__title-row\n')
        if title_row_middle:
            __M_writer('site-header__row-middle\n')
        __M_writer('        ">\n            ')
        __M_writer(str(html_site_title()))
        __M_writer('\n')
        if mdl__multiple_header:
            __M_writer('        </div>\n        <div class="mdl-layout__header-row site-header__navigation-row\n')
            if mdl__navigation_large_screen_only:
                __M_writer('mdl-layout--large-screen-only\n')
            if navigation_row_middle:
                __M_writer('site-header__row-middle\n')
            __M_writer('        ">\n')
        else:
            __M_writer('            <div class="mdl-layout-spacer"></div>\n')
        if top_nav_header:
            __M_writer('            <span class="sr-only">main navigation</span>\n            <nav class="mdl-navigation site-header__navigation">\n')
            for url, text in navigation_links[lang]:
                if rel_link(permalink, url) == "#":
                    __M_writer('                      <a class="mdl-navigation__link is-active" href="')
                    __M_writer(str(permalink))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer(' <span class="sr-only">')
                    __M_writer(str(messages("(active)", lang)))
                    __M_writer('</span></a>\n')
                else:
                    __M_writer('                      <a class="mdl-navigation__link" href="')
                    __M_writer(str(url))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a>\n')
            __M_writer('              ')
            __M_writer(str(template_hooks['menu']()))
            __M_writer('\n              ')
            __M_writer(str(template_hooks['menu_alt']()))
            __M_writer('\n            </nav>\n')
        if search_form:
            __M_writer('                <div class="site-header__search" role="search">\n                    ')
            __M_writer(str(search_form))
            __M_writer('\n                </div>\n')
        __M_writer('            ')
        __M_writer(str(html_more_button()))
        __M_writer('\n        </div>\n    </header>\n    ')
        __M_writer(str(html_navigation_links()))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <h1 id="brand" class="mdl-layout__title site-title">\n        <a href="')
        __M_writer(str(abs_link(_link("root", None, lang))))
        __M_writer('" title="')
        __M_writer(filters.html_escape(str(blog_title)))
        __M_writer('" rel="home">\n')
        if logo_url:
            __M_writer('                <img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('" id="logo">\n')
        if show_blog_title:
            __M_writer('                <span id="blog-title" class="mdl-color-text--primary-contrast">')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</span>\n')
        __M_writer('        </a>\n    </h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        drawer_note = _import_ns.get('drawer_note', context.get('drawer_note', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        drawer_show_title = _import_ns.get('drawer_show_title', context.get('drawer_show_title', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        drawer_description = _import_ns.get('drawer_description', context.get('drawer_description', UNDEFINED))
        mdl__drawer_small_screen_only = _import_ns.get('mdl__drawer_small_screen_only', context.get('mdl__drawer_small_screen_only', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        drawer_logo_url = _import_ns.get('drawer_logo_url', context.get('drawer_logo_url', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        drawer_title = _import_ns.get('drawer_title', context.get('drawer_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <div id="drawer" class="mdl-layout__drawer site-drawer\n')
        if mdl__drawer_small_screen_only:
            __M_writer('mdl-layout--small-screen-only\n')
        __M_writer('    ">\n')
        if drawer_title:
            __M_writer('        <div class="mdl-layout__title site-drawer__title">\n')
            if drawer_logo_url:
                __M_writer('                <img src="')
                __M_writer(str(drawer_logo_url))
                __M_writer('" alt="')
                __M_writer(filters.html_escape(str(drawer_title)))
                __M_writer('">\n')
            if drawer_show_title:
                __M_writer('                <span>')
                __M_writer(filters.html_escape(str(drawer_title)))
                __M_writer('</span>\n')
            __M_writer('        </div>\n')
        if drawer_description:
            __M_writer('        <div class="site-drawer__description">\n            ')
            __M_writer(str(drawer_description))
            __M_writer('\n        </div>\n')
        __M_writer('        <span class="sr-only">side navigation</span>\n        <nav class="mdl-navigation site-drawer__navigation">\n')
        for url, text in navigation_links[lang]:
            if rel_link(permalink, url) == "#":
                __M_writer('                    <a class="mdl-navigation__link is-active" href="')
                __M_writer(str(permalink))
                __M_writer('">')
                __M_writer(str(text))
                __M_writer(' <span class="sr-only">')
                __M_writer(str(messages("(active)", lang)))
                __M_writer('</span></a>\n')
            else:
                __M_writer('                    <a class="mdl-navigation__link" href="')
                __M_writer(str(url))
                __M_writer('">')
                __M_writer(str(text))
                __M_writer('</a>\n')
        __M_writer('            ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n            ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n        </nav>\n')
        if drawer_note:
            __M_writer('        <div class="site-drawer__note">\n            ')
            __M_writer(str(drawer_note))
            __M_writer('\n        </div>\n')
        __M_writer('    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_more_button(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        more_button_header = _import_ns.get('more_button_header', context.get('more_button_header', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1 or more_button_header:
            __M_writer('        <button id="more-button"\n                class="mdl-button mdl-js-button mdl-button--icon mdl-js-ripple-effect site-header__more-button">\n            <i class="material-icons">more_vert</i>\n        </button>\n        <ul class="mdl-menu mdl-menu--bottom-right mdl-js-menu mdl-js-ripple-effect"\n            for="more-button">\n')
            if more_button_header:
                for url, title, text in more_button_header:
                    __M_writer('                <li class="mdl-menu__item">\n                    <a href="')
                    __M_writer(str(url))
                    __M_writer('" title="')
                    __M_writer(str(title))
                    __M_writer('" >')
                    __M_writer(str(text))
                    __M_writer('</a>\n                </li>\n')
            if len(translations) > 1:
                __M_writer('                <li class="mdl-menu__item">')
                __M_writer(str(messages("Languages:")))
                __M_writer('</li>\n                <li class="mdl-menu__item">')
                __M_writer(str(base.html_translations()))
                __M_writer('</li>\n')
            __M_writer('        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/mdl/templates/base_header.tmpl", "uri": "base_header.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "33": 2, "34": 65, "35": 78, "36": 119, "37": 142, "43": 4, "72": 4, "73": 6, "74": 7, "75": 9, "76": 10, "77": 12, "78": 13, "79": 15, "80": 16, "81": 18, "82": 19, "83": 21, "84": 23, "85": 24, "86": 26, "87": 27, "88": 27, "89": 28, "90": 29, "91": 31, "92": 32, "93": 34, "94": 35, "95": 37, "96": 38, "97": 39, "98": 41, "99": 42, "100": 44, "101": 45, "102": 46, "103": 46, "104": 46, "105": 46, "106": 46, "107": 46, "108": 46, "109": 47, "110": 48, "111": 48, "112": 48, "113": 48, "114": 48, "115": 51, "116": 51, "117": 51, "118": 52, "119": 52, "120": 55, "121": 56, "122": 57, "123": 57, "124": 60, "125": 60, "126": 60, "127": 63, "128": 63, "129": 64, "130": 64, "136": 67, "148": 67, "149": 69, "150": 69, "151": 69, "152": 69, "153": 70, "154": 71, "155": 71, "156": 71, "157": 71, "158": 71, "159": 73, "160": 74, "161": 74, "162": 74, "163": 76, "169": 80, "187": 80, "188": 82, "189": 83, "190": 85, "191": 86, "192": 87, "193": 88, "194": 89, "195": 89, "196": 89, "197": 89, "198": 89, "199": 91, "200": 92, "201": 92, "202": 92, "203": 94, "204": 96, "205": 97, "206": 98, "207": 98, "208": 101, "209": 103, "210": 104, "211": 105, "212": 105, "213": 105, "214": 105, "215": 105, "216": 105, "217": 105, "218": 106, "219": 107, "220": 107, "221": 107, "222": 107, "223": 107, "224": 110, "225": 110, "226": 110, "227": 111, "228": 111, "229": 113, "230": 114, "231": 115, "232": 115, "233": 118, "239": 121, "250": 121, "251": 122, "252": 123, "253": 129, "254": 130, "255": 131, "256": 132, "257": 132, "258": 132, "259": 132, "260": 132, "261": 132, "262": 136, "263": 137, "264": 137, "265": 137, "266": 138, "267": 138, "268": 140, "274": 268}}
__M_END_METADATA
"""
