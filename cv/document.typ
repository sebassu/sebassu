#import "@preview/imprecv:1.0.1": *

#let cvdata = yaml("data.yml")

#let uservars = (
  headingfont: "Libertinus Serif",
  headingsmallcaps: true,
  bodyfont: "Libertinus Serif",
  fontsize: 10pt,
  linespacing: 6pt,
  sectionspacing: 12pt,
  showAddress: true,
  showNumber: true,
  showTitle: true,
)

#let customrules(document) = {
  set page(
    paper: "a4",
    number-align: center,
    margin: 1.25cm,
  )
  document
}

#let cvinit(document) = {
  document = setrules(uservars, document)
  document = showrules(uservars, document)
  document = customrules(document)
  document
}

#show: document => cvinit(document)
#cvheading(cvdata, uservars)
#cvwork(cvdata)
#cveducation(cvdata)
#cvprojects(cvdata)
#cvskills(cvdata)
