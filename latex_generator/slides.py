from report import *




def pdf_slide(filename, ratio=1.0, pagen=None):
    if pagen is not None:
        return background_pdf('%s%02d.pdf'%(filename[:-4],pagen), ratio)
    else:
        return background_pdf(filename, ratio)


clean_background = "\\usebackgroundtemplate{}"

class frame(latex_element):
    template = """%%%%%%%%%%%%%%%% FRAME #nb#: #title# %%%%%%%%%%%%%%%%%%%
\\frame{
\\frametitle{#title#}
#doc_main#
}"""
    title = ''
    nb = 1


class block(latex_element):
    template = """%%% BLOCK #order#: #title#  %%%%
\\begin{block}<#order#>{#title#}
#doc_main#
\\end{block}"""
    title = ''
    order = '1-'


class minipage(latex_element):
    template = """
 \\begin{minipage}#valign#{#ratio#\\textwidth}
 #doc_main#
\\end{minipage}"""
    ratio = '0.49'
    valign = ''

    def __init__(self, doc_main= [], **kwargs):
        if 'valign' in kwargs:
            kwargs['valign'] = '[' + kwargs['valign'] + ']'
        super(minipage, self).__init__(doc_main, **kwargs)


def anim(filename, ratio, frames):
    return formi("""
\\animategraphics[controls,autoplay,loop,width=#ratio#\\textwidth]{#nframes#}{#filename#}{#f1#}{#f2#}
""", dict(filename=filename, ratio=ratio, f1=frames[0], f2=frames[1], nframes=frames[1] - frames[0]))


class slides(report):
    template_filename = 'template/slides_header_template.tex'

    def __init__(self, **kwargs):
        super(slides, self).__init__(**kwargs)
        self.doc_main = []

    def f(self, title, doc):
        """ Add a frame to the slideshow"""
        self.addl(frame(doc_main=doc, title=title))

    def add_pdf_slide(self, title, filename, ratio=1.0, pagen=None, text=''):
        self.addl(pdf_slide(filename, pagen=pagen, ratio=ratio))
        self.f(title,text)
        self.addl(clean_background)

        # def outline(self, title='Outline', section=None):
        # if section:
        #         self.f(title, '\\tableofcontents[%s]'%(section))
        #     else:
        #         self.f(title, '\\tableofcontents')

        # def section(self, long_name, short_name='', label=None):
        #     super(slides, self).section(long_name, short_name, label)
        #     self.outline(section=long_name)


class columns(latex_element):
    template = """
\\begin{columns}[#position#]
#doc_main#
\\end{columns}    
"""
    position = 'c'
    c = []

    def __init__(self, c=[], widths=[], **kwargs):
        if len(c) > 0:
            self.c = []
            for i, e in enumerate(c):
                if len(widths) > 0:
                    w = '%f\\textwidth' % widths[i]
                else:
                    w = '%f\\textwidth' % (1.0 / len(c) - 0.01)
                self.c.append(_column(e, width=w, position=self.position))
        else:
            self.c = []
            for w in widths:
                self.c.append(column(width=w))
        super(columns, self).__init__(**kwargs)

    def __str__(self):
        self.doc_main = [''.join([tostr(c) for c in self.c])]
        return formi(self.template, self.build_dic())


class _column(latex_element):
    template = """
\\begin{column}[#position#]{#width#}
#doc_main#
\\end{column}    
"""
    width = '4.5cm'
    position = 'c'


def svg(filename, width=None, col=None):
    name_pdf = filename[:-3] + 'pdf'
    exep('inkscape -D -z --file={svg} --export-pdf={pdf} --export-latex'.format(svg=filename, pdf=name_pdf))
    out = "\\begin{figure}"
    out += "\\centering"
    if width is not None:
        out += "\\def\\svgwidth{%s}" % width
    if col is not None:
        out += color(col, "\\input{%s_tex}" % name_pdf)
    else:
        out += "\\input{%s_tex}" % name_pdf
    out += "\\end{figure}"
    return out

def split_pdfs(filename):
    base = filename[:-4]
    exep('/opt/pdflabs/pdftk/bin/pdftk {filename} burst output {base}%02d.pdf'.format(filename=filename, base=base))

def background_pdf(filename, ratio=1.0):
    return '\\usebackgroundtemplate{\\includegraphics[width=%f\\paperwidth,height=%f\\paperheight]{%s}}'%(ratio,ratio,filename)


def icontext(icon, link, text, iconratio=0.04):
    """ Make a line with an icon on the left and a link on the right.
    :param icon: file path to the icon
    :param link: http link of the text
    :param text: the text
    :param iconratio: the ratio beetween the icon size and the text width (default=0.04)
    :return: a list: [minipage(icon), minipage(href), '\\\\']
    """
    textratio=0.90-iconratio
    return [minipage(fig(icon), valign='c', ratio=iconratio),
            minipage(href(link,text), valign='c', ratio=textratio), '\\\\']

