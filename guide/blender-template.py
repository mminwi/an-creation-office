# AN Creation concept render template for Blender (5.x).
# The analyst copies this file next to the drawing, fills PARTS from the drawing's dimensions, and runs:
#   "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" -b -P <this file> -- <output.png>
# Units are inches. Keep it simple: boxes, cylinders and slots (cut-outs). This is a concept picture, not CAD.
import bpy, sys, math
from mathutils import Vector

# ---- FILL THIS IN -------------------------------------------------------------
TITLE = "concept"
COLOR = (0.62, 0.64, 0.66)      # matte plastic grey; change to the chosen finish
# Each part: kind = "box" | "cylinder" | "cut_box" (a slot or opening subtracted from the part named in 'from')
# size = (x, y, z) inches for box/cut_box; (diameter, length) for cylinder; loc = (x, y, z) centre in inches;
# rot = (x, y, z) degrees; bevel = edge rounding in inches.
PARTS = [
    {"name": "base", "kind": "box", "size": (18, 12, 0.25), "loc": (0, 0, 0.125), "bevel": 0.1},
    {"name": "lip_front", "kind": "box", "size": (18, 0.3, 1.5), "loc": (0, -6, 0.75), "bevel": 0.1},
    {"name": "slot_1", "kind": "cut_box", "from": "lip_front", "size": (3, 1, 0.8), "loc": (-5, -6, 0.6)},
]
# -------------------------------------------------------------------------------

IN = 0.0254
out = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else "render.png"

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.render.engine = "BLENDER_EEVEE_NEXT" if "BLENDER_EEVEE_NEXT" in [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items] else "BLENDER_EEVEE"
scene.render.resolution_x, scene.render.resolution_y = 1600, 1000
scene.render.film_transparent = False
world = bpy.data.worlds.new("w"); scene.world = world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.95, 0.95, 0.96, 1)
world.node_tree.nodes["Background"].inputs[1].default_value = 0.15
scene.view_settings.exposure = -1.2

mat = bpy.data.materials.new("plastic"); mat.use_nodes = True
bsdf = mat.node_tree.nodes["Principled BSDF"]
bsdf.inputs["Base Color"].default_value = (*COLOR, 1)
bsdf.inputs["Roughness"].default_value = 0.45

objs = {}
for p in PARTS:
    loc = Vector(p["loc"]) * IN
    if p["kind"] in ("box", "cut_box"):
        bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
        o = bpy.context.object
        o.scale = Vector(p["size"]) * IN
    elif p["kind"] == "cylinder":
        d, length = p["size"]
        bpy.ops.mesh.primitive_cylinder_add(radius=d * IN / 2, depth=length * IN, location=loc, vertices=64)
        o = bpy.context.object
    o.name = p["name"]
    if "rot" in p:
        o.rotation_euler = [math.radians(a) for a in p["rot"]]
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    objs[p["name"]] = o

for p in PARTS:
    if p["kind"] == "cut_box":
        target, cutter = objs[p["from"]], objs[p["name"]]
        m = target.modifiers.new("cut_" + p["name"], "BOOLEAN"); m.operation = "DIFFERENCE"; m.object = cutter
        bpy.context.view_layer.objects.active = target
        bpy.ops.object.modifier_apply(modifier=m.name)
        bpy.data.objects.remove(cutter, do_unlink=True); objs.pop(p["name"])

for p in PARTS:
    o = objs.get(p["name"])
    if not o:
        continue
    if p.get("bevel"):
        b = o.modifiers.new("bevel", "BEVEL"); b.width = p["bevel"] * IN; b.segments = 4
    o.data.materials.append(mat)
    bpy.context.view_layer.objects.active = o
    bpy.ops.object.shade_smooth()

# frame everything
pts = [o.matrix_world @ Vector(c) for o in objs.values() for c in o.bound_box]
lo = Vector((min(v.x for v in pts), min(v.y for v in pts), min(v.z for v in pts)))
hi = Vector((max(v.x for v in pts), max(v.y for v in pts), max(v.z for v in pts)))
centre, span = (lo + hi) / 2, max((hi - lo).length, 0.05)

bpy.ops.mesh.primitive_plane_add(size=span * 8, location=(centre.x, centre.y, lo.z - 0.0005))
floor = bpy.context.object
fm = bpy.data.materials.new("floor"); fm.use_nodes = True
fm.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.8, 0.8, 0.82, 1)
floor.data.materials.append(fm)

cam_loc = centre + Vector((span * 1.1, -span * 1.4, span * 0.9))
bpy.ops.object.camera_add(location=cam_loc)
cam = bpy.context.object
cam.rotation_euler = (centre - cam_loc).to_track_quat("-Z", "Y").to_euler()
cam.data.lens = 50
scene.camera = cam

k = (span / 0.5) ** 2  # light power scales with the size of the scene
for loc, energy, size in [((span, -span, span * 2), 40, span), ((-span * 1.5, -span * 0.5, span), 12, span * 1.5),
                          ((0, span * 1.5, span * 1.2), 20, span)]:
    bpy.ops.object.light_add(type="AREA", location=centre + Vector(loc))
    L = bpy.context.object
    L.data.energy = energy * k
    L.data.size = size
    L.rotation_euler = (centre - L.location).to_track_quat("-Z", "Y").to_euler()

scene.render.filepath = out
bpy.ops.render.render(write_still=True)
print("RENDERED", out, TITLE)
