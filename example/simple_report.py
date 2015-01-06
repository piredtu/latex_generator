from latex_generator.slides import *

s = slides(
  tex_filename= 'slide_show.tex',
  short_title = 'sorter title',
  title = "The title",
  date = 'the date',
  author= "Your list of names",
  short_author = "Shorter name",
  university = "university",
  institute = "Institute",
)


### Create the outline of the presentation using the sections and subsections
s.f('Table of Contents','\\tableofcontents')

s.section('Section name', 'Shorter name')
s.subsection('Introduction')
s.f('Overview of DTU\'s Wind Farm Flow Models',
    ('hello'  # A paranthesis without a comma creates a string in python
     '\\\\' # This is a end of line sign
     'This is now a list\n'
     """
     * hello
     * what
     * is going on
     """ # Tripple quote allows to have a comment over several lines, including end-of-line characters
         # some markdown stuff is automatically detected in the text and translated into latex using a custom function
     )
    )
s.section('Section name 2', 'Shorter name 2')

s.f('Title',
("""
This is the body of the text \\\\
New line

Another new line

* Some itememized
* Text

"""
# add some text
#+ cfig('/Users/pire/git/latex_generator/example/template/AAUlogo-eps-converted-to.pdf', '3cm')
))

s.compile()
s.clean()
s.open_pdf()
