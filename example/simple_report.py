from latex_generator.report import report

rep = report()
rep.section('Introduction')
rep.addl('hello.')
rep.addl("EllipSys has run within {minutes} minutes over {ncpu} CPUs using the server called {srvname}.",
        minutes=10.0, srvname='servername', ncpu=72)
#rep.fig('surf01.grd.png', caption='This is fabulous!', label='fig:fabfig')
rep.eq(r'x^2 = \int_a^b \ln{x} d x', label='eq:crazy_eq')
rep.subsection('My section')
rep.addl(r'Look at Eq.\ref{eq:crazy_eq} and Fig.\ref{fig:fabfig} if you are not convinced.')
rep.compile()
rep.clean()
rep.open_pdf()
