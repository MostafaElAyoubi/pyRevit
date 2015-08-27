__doc__ = 'Deducts selection from memory keeping the rest.\nWorks like the M- button in a calculator.\nThis is a project-dependent (Revit *.rvt) memory. Every project has its own memory save in user temp folder as *.sel files.'

__window__.Close()
# from Autodesk.Revit.DB import ElementId
import os
import os.path as op
import pickle as pl

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

usertemp = os.getenv('Temp')
prjname = op.splitext( op.basename( doc.PathName ) )[0]
datafile = usertemp + '\\' + prjname + '_pySaveRevitSelection.sel'

selection = { elId.ToString() for elId in uidoc.Selection.GetElementIds() }

try: 
	f = open(datafile, 'r')
	prevsel = pl.load(f)
	newsel = prevsel.difference( selection )
	f.close()
	f = open(datafile, 'w')
	pl.dump(newsel, f)
	f.close()
except:
	f = open(datafile, 'w')
	prevsel = set([])
	pl.dump( prevsel, f)
	f.close()
