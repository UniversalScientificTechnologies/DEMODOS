#%%

from build123d import *
import build123d as bd
from ocp_vscode import show

import cadquery as cq

# %%

#with bd.BuildPart() as base:

length = 100-2
width = 70-2

with BuildSketch() as ci:
    Circle(150)
    #with PolarLocations(102, 80):
    #    Circle(3, mode=Mode.SUBTRACT)


with BuildPart() as part:
    with BuildSketch() as base:
        Rectangle(length, width)
        
        with Locations((0, width/2+150-5), (0, -(width/2+150-5))):
            add(ci, mode=Mode.SUBTRACT)

        fillet(base.vertices(), radius=8)
    
    extrude(amount=22)

    fillet(faces().sort_by(Axis.Z)[0].edges(), 4)
    fillet(faces().sort_by(Axis.Z)[-1].edges(), 4)
        
    #fillet(ex16_sk.vertices(), radius=130 / 10)

    #Box(length-8, 40, 15, mode=Mode.SUBTRACT, align=(Align.CENTER, Align.CENTER, Align.MIN))

    with Locations((20, 0, 0)):
        Box(29, 29, 50, mode=Mode.SUBTRACT)
        #Box(29+20, 29+20, 43, mode=Mode.SUBTRACT)
        Box(45, 32, 43, mode=Mode.SUBTRACT)

    Box(29+60, 29+20, 41, mode=Mode.SUBTRACT)
        # Box(29+50, 29+10, 40, mode=Mode.SUBTRACT)

    with Locations((0, -20, 11), (0, 20, 11)):
        Cylinder(1.2, 200, mode=Mode.SUBTRACT, rotation=(0, 90, 0))

    if False:
        with Locations((20-30, 0+14, 10)):
            Cylinder(radius=1, height=40, mode=Mode.SUBTRACT)


with BuildPart() as cover:
    Box(89-0.5, 49-0.5, 43/2-0.4, align=(Align.CENTER, Align.CENTER, Align.MIN))

    with Locations((00, 0, 1)):
        Box(89-0.5-2, 49-0.5-2, 43/2, align=(Align.CENTER, Align.CENTER, Align.MIN), mode=Mode.SUBTRACT)

    chamfer(edges().filter_by(Axis.Z), 0.5)

    with Locations((00, 0, 4)):
        Box(89-0.5-2+5, 15, 43/2, align=(Align.CENTER, Align.CENTER, Align.MIN), mode=Mode.SUBTRACT)


    with Locations((0, -20, 11), (0, 20, 11)):
        Cylinder(1.2, 200, mode=Mode.SUBTRACT, rotation=(0, 90, 0))




show([part, cover], measure_tools=True)

# %% 
part.part.export_step("DEMODOS_BOX.stp")

cover.part.export_step("DEMODOS_COVER.stp")

# %%

face = part.part.faces().filter_by(Axis.Z)[0]
crop = offset(face, amount=-1)

exporter = ExportSVG(unit=Unit.MM, line_weight=0.5)
exporter.add_layer("Stick_area", line_color=(0, 0, 255))
exporter.add_shape(face, layer="Stick_area")
exporter.add_layer("crop", fill_color=(255, 0, 0), line_color=(0, 0, 255))
exporter.add_shape(crop, layer="crop")
exporter.write("sticker_parameters.svg")

show(face, crop)


# %% 

# Extrude pro vytvoření základní desky
solid = base.extrude(2)

# Definujte profil, který chcete aplikovat na hrany
edge_profile = cq.Workplane("YZ").moveTo(0, 0).polyline([(0, 0), (2, 0), (2, 2), (0, 2)]).close()

# Sweep around the edges
#solid = solid.edges().fillet(1)

# Můžete také vytvořit povrchový profil a aplikovat ho
solid = solid.faces(">Z").wires().toPending().sweep(edge_profile, isFrenet=True)

show(solid)
# %%
