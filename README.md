Latex Generator
===============

`latex_generator` is a python package to generate reports and slides from a python file. 

But why?
--------
* Because we can
* Sometimes it's easier to generate slides with for loop (for instance to do image based annimations).
* To conveniently blend markdown linguo and latex linguo
* The python script can orchestrate the whole compilation of the report of the presentation (à la MakeFile)
* To easily build automatic reports / slides generation from tests

Pre-requisits
-------------
* Python 2.7
* Pandoc
* Latex distribution
* Mac or Linux
 
Example:
--------
```python
rep = report()
rep.section('Introduction')
rep.addl('hello.')
rep.addl("EllipSys has run within {minutes} minutes over {ncpu} CPUs using the server called {srvname}.",
        minutes=10.0, srvname='servername', ncpu=72)
rep.fig('surf01.grd.png', caption='This is fabulous!', label='fig:fabfig')
rep.eq(r'x^2 = \int_a^b \ln{x} d x', label='eq:crazy_eq')
rep.subsection('My section')
rep.addl(r'Look at Eq.\ref{eq:crazy_eq} and Fig.\ref{fig:fabfig} if you are not convinced.')
rep.compile()
rep.clean()
rep.open_pdf()
```
