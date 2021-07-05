# import bpy
# from math import *
# import math

# def createMeshFromData(name, origin, verts, edges, faces):
#     # Create mesh and object
#     me = bpy.data.meshes.new(name+'Mesh')
#     ob = bpy.data.objects.new(name, me)
#     ob.location = origin
#     ob.show_name = False
#     # Link object to scene and make active
#     bpy.context.collection.objects.link(ob)
#     ob.select_set(True)

#     # Create mesh from given verts, faces.
#     me.from_pydata(verts, edges, faces)

#     # Update mesh with new data
#     me.update()

# C = 8.47799 # Sets x origin.

# # verts1 contains all xyz coordinates

# # default - derived from the math function : 4+cos(3*u)+sin(2*u)
# #verts1 = [[-4.0, 3.85449571210911, 0], [-3.959798994974874, 3.775320858367066, 0], [-3.919597989949749, 3.6913609177349316, 0], [-3.879396984924623, 3.603819138215969, 0], [-3.8391959798994977, 3.5140029145968708, 0], [-3.798994974874372, 3.4233045650796003, 0], [-3.758793969849246, 3.333180538984771, 0], [-3.7185929648241207, 3.245129361239188, 0], [-3.678391959798995, 3.1606686398537747, 0], [-3.6381909547738696, 3.0813114783151887, 0], [-3.5979899497487438, 3.0085426455131214, 0], [-3.557788944723618, 2.943794861337173, 0], [-3.5175879396984926, 2.8884255563088708, 0], [-3.477386934673367, 2.843694458550632, 0], [-3.4371859296482414, 2.8107423510957608, 0], [-3.3969849246231156, 2.7905713271503365, 0], [-3.35678391959799, 2.7840268506427126, 0], [-3.3165829145728645, 2.7917819045236842, 0], [-3.2763819095477387, 2.8143234801633197, 0], [-3.2361809045226133, 2.851941628243802, 0], [-3.1959798994974875, 2.9047212552432624, 0], [-3.1557788944723617, 2.972536810465134, 0], [-3.115577889447236, 3.055049967154617, 0], [-3.0753768844221105, 3.1517103581565307, 0], [-3.035175879396985, 3.2617593824302227, 0], [-2.9949748743718594, 3.3842370541871785, 0], [-2.9547738693467336, 3.517991822102217, 0], [-2.914572864321608, 3.6616932426142594, 0], [-2.8743718592964824, 3.813847349410389, 0], [-2.834170854271357, 3.9728145213893455, 0], [-2.7939698492462313, 4.1368296143099395, 0], [-2.7537688442211055, 4.304024087489989, 0], [-2.7135678391959797, 4.472449826830258, 0], [-2.6733668341708543, 4.640104339539525, 0], [-2.633165829145729, 4.804956974615976, 0], [-2.592964824120603, 4.964975806715139, 0], [-2.5527638190954773, 5.118154809754089, 0], [-2.5125628140703515, 5.26254094064017, 0], [-2.472361809045226, 5.396260752967843, 0], [-2.4321608040201004, 5.517546165419441, 0], [-2.391959798994975, 5.62475901987599, 0], [-2.351758793969849, 5.716414079756579, 0], [-2.3115577889447234, 5.791200139647179, 0], [-2.271356783919598, 5.84799894256737, 0], [-2.2311557788944723, 5.8859016309028975, 0], [-2.190954773869347, 5.904222490685992, 0], [-2.150753768844221, 5.902509786059261, 0], [-2.1105527638190953, 5.88055352088683, 0], [-2.07035175879397, 5.838390007009221, 0], [-2.030150753768844, 5.776303162971974, 0], [-1.9899497487437188, 5.694822512561358, 0], [-1.949748743718593, 5.594717898505709, 0], [-1.9095477386934672, 5.476990972591546, 0], [-1.8693467336683418, 5.342863568544905, 0], [-1.829145728643216, 5.193763107696298, 0], [-1.7889447236180902, 5.031305229058273, 0], [-1.7487437185929648, 4.857273874403049, 0], [-1.708542713567839, 4.673599094676816, 0], [-1.6683417085427137, 4.482332876115807, 0], [-1.6281407035175879, 4.285623312278437, 0], [-1.587939698492462, 4.085687471479545, 0], [-1.5477386934673367, 3.8847833274733663, 0], [-1.507537688442211, 3.685181134418745, 0], [-1.4673366834170856, 3.4891346349843717, 0], [-1.4271356783919598, 3.2988524928011564, 0], [-1.386934673366834, 3.116470337310106, 0], [-1.3467336683417086, 2.944023800431924, 0], [-1.3065326633165828, 2.7834229105229022, 0], [-1.2663316582914574, 2.63642818998033, 0], [-1.2261306532663316, 2.5046287788929478, 0], [-1.1859296482412058, 2.3894228786414278, 0], [-1.1457286432160805, 2.2920007767478716, 0], [-1.1055276381909547, 2.2133306780187736, 0], [-1.0653266331658293, 2.1541475276413204, 0], [-1.0251256281407035, 2.1149449699414538, 0], [-0.9849246231155777, 2.095970542593661, 0], [-0.9447236180904524, 2.0972241608142084, 0], [-0.9045226130653266, 2.1184599001179176, 0], [-0.8643216080402008, 2.159191040229106, 0], [-0.8241206030150754, 2.2186982873656786, 0], [-0.7839195979899496, 2.296041048007785, 0], [-0.7437185929648242, 2.3900715850462206, 0], [-0.7035175879396984, 2.499451847480713, 0], [-0.6633165829145726, 2.6226727281673696, 0], [-0.6231155778894473, 2.7580754710168254, 0], [-0.5829145728643215, 2.9038749199865737, 0], [-0.5427135678391961, 3.05818427760089, 0], [-0.5025125628140703, 3.21904102091327, 0], [-0.4623115577889445, 3.3844336080735506, 0], [-0.42211055276381915, 3.552328599176126, 0], [-0.38190954773869334, 3.720697810971518, 0], [-0.341708542713568, 3.8875451263681686, 0], [-0.3015075376884422, 4.050932586403482, 0], [-0.2613065326633164, 4.209005404413034, 0], [-0.22110552763819102, 4.360015559289627, 0], [-0.18090452261306522, 4.5023436467397335, 0], [-0.14070351758793986, 4.634518693985675, 0], [-0.10050251256281406, 4.755235674033832, 0], [-0.06030150753768826, 4.863370489979597, 0], [-0.0201005025125629, 4.957992237343947, 0], [0.020100502512562457, 5.03837259258391, 0], [0.06030150753768826, 5.103992218103028, 0], [0.10050251256281406, 5.154544117692346, 0], [0.14070351758793986, 5.189933920722438, 0], [0.18090452261306567, 5.2102771179369505, 0], [0.22110552763819058, 5.215893315721976, 0], [0.2613065326633164, 5.207297618605111, 0], [0.3015075376884422, 5.185189290853465, 0], [0.341708542713568, 5.1504378867975795, 0], [0.3819095477386938, 5.104067075350142, 0], [0.4221105527638196, 5.047236416599999, 0], [0.4623115577889445, 4.981221376879223, 0], [0.5025125628140703, 4.90739189291773, 0], [0.5427135678391961, 4.827189815273234, 0], [0.5829145728643219, 4.742105575879351, 0], [0.6231155778894477, 4.653654434089338, 0], [0.6633165829145726, 4.563352659879721, 0], [0.7035175879396984, 4.472694011866587, 0], [0.7437185929648242, 4.38312686150488, 0], [0.78391959798995, 4.2960323033915, 0], [0.8241206030150758, 4.212703575156423, 0], [0.8643216080402008, 4.134327089254502, 0], [0.9045226130653266, 4.061965353385714, 0], [0.9447236180904524, 3.9965420266590583, 0], [0.9849246231155782, 3.9388293254192144, 0], [1.025125628140704, 3.889437956371918, 0], [1.0653266331658289, 3.848809715814541, 0], [1.1055276381909547, 3.8172128529805605, 0], [1.1457286432160805, 3.7947402533463355, 0], [1.1859296482412063, 3.781310454851381, 0], [1.226130653266332, 3.77667146698483, 0], [1.266331658291457, 3.7804073202274995, 0], [1.3065326633165828, 3.7919472320391376, 0], [1.3467336683417086, 3.810577236054547, 0], [1.3869346733668344, 3.835454083984362, 0], [1.4271356783919602, 3.8656211954551916, 0], [1.4673366834170851, 3.900026400175366, 0], [1.507537688442211, 3.9375411898319705, 0], [1.5477386934673367, 3.97698117441011, 0], [1.5879396984924625, 4.017127419511671, 0], [1.6281407035175883, 4.0567483280051295, 0], [1.6683417085427132, 4.094621721155715, 0], [1.708542713567839, 4.1295567713870005, 0], [1.7487437185929648, 4.160415441054974, 0], [1.7889447236180906, 4.186133089041017, 0], [1.8291457286432165, 4.205737919481453, 0], [1.8693467336683414, 4.218368964363966, 0], [1.9095477386934672, 4.22329231377843, 0], [1.949748743718593, 4.219915333986216, 0], [1.9899497487437188, 4.20779864377874, 0], [2.0301507537688446, 4.186665653385618, 0], [2.0703517587939704, 4.1564095069665346, 0], [2.1105527638190953, 4.117097308935861, 0], [2.150753768844221, 4.068971555445605, 0], [2.190954773869347, 4.01244873468354, 0], [2.2311557788944727, 3.948115102602927, 0], [2.2713567839195985, 3.876719683652383, 0], [2.3115577889447234, 3.799164588382707, 0], [2.351758793969849, 3.7164927808443315, 0], [2.391959798994975, 3.629873467845126, 0], [2.432160804020101, 3.5405853188309226, 0], [2.4723618090452266, 3.4499977588337263, 0], [2.5125628140703515, 3.3595506071015024, 0], [2.5527638190954773, 3.2707323602265292, 0], [2.592964824120603, 3.185057440431927, 0], [2.633165829145729, 3.1040427468266785, 0], [2.6733668341708547, 3.0291838596357197, 0], [2.7135678391959797, 2.9619312544626837, 0], [2.7537688442211055, 2.9036668854333345, 0], [2.7939698492462313, 2.8556814925591354, 0], [2.834170854271357, 2.819152979891639, 0], [2.874371859296483, 2.795126197125697, 0], [2.914572864321608, 2.7844944384442374, 0], [2.9547738693467336, 2.7879829488438643, 0], [2.9949748743718594, 2.8061347002718393, 0], [3.035175879396985, 2.8392986680386127, 0], [3.075376884422111, 2.8876208026016155, 0], [3.115577889447236, 2.951037853453216, 0], [3.1557788944723617, 3.0292741610407763, 0], [3.1959798994974875, 3.1218414899882907, 0], [3.2361809045226133, 3.228041932994002, 0], [3.276381909547739, 3.346973870282353, 0], [3.316582914572864, 3.477540925037483, 0], [3.35678391959799, 3.618463811485271, 0], [3.3969849246231156, 3.7682949298589006, 0], [3.4371859296482414, 3.925435521998332, 0], [3.4773869346733672, 4.088155163388492, 0], [3.517587939698492, 4.254613332590783, 0], [3.557788944723618, 4.42288276777969, 0], [3.5979899497487438, 4.590974292921508, 0], [3.6381909547738696, 4.756862773428436, 0], [3.6783919597989954, 4.918513843226584, 0], [3.7185929648241203, 5.073911032360847, 0], [3.758793969849246, 5.221082916719447, 0], [3.798994974874372, 5.358129909316842, 0], [3.8391959798994977, 5.483250315868872, 0], [3.8793969849246235, 5.594765286092498, 0], [3.9195979899497493, 5.691142306151208, 0], [3.959798994974874, 5.7710168967558575, 0], [4.0, 5.833212205355873, 0]]


# # This calculates the edges based on the verts1 array
# edges1 = [[len(verts1) - 1, 0]]
# for i in range( 0, len(verts1)-1):
#     edges1.append( [i, i+1] )


# # Generate the actual Blender geometry:(name, origin, verts, edges, faces)
# createMeshFromData( 'Geometry', [0, 0, 0], verts1, edges1, [] )

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# new

import bpy
from math import *
import math

def createMeshFromData(name, origin, verts, edges, faces):
    # Create mesh and object
    me = bpy.data.meshes.new(name+'Mesh')
    ob = bpy.data.objects.new(name, me)
    ob.location = origin
    ob.show_name = False
    # Link object to scene and make active
    bpy.context.collection.objects.link(ob)
    ob.select_set(True)

    # Create mesh from given verts, faces.
    me.from_pydata(verts, edges, faces)

    # Update mesh with new data
    me.update()

C = 8.47799 # Sets x origin.

# verts1 contains all xyz coordinates

# default - derived from the math function : 4+cos(3*u)+sin(2*u)
#verts1 = [[-4.0, 3.85449571210911, 0], [-3.959798994974874, 3.775320858367066, 0], [-3.919597989949749, 3.6913609177349316, 0], [-3.879396984924623, 3.603819138215969, 0], [-3.8391959798994977, 3.5140029145968708, 0], [-3.798994974874372, 3.4233045650796003, 0], [-3.758793969849246, 3.333180538984771, 0], [-3.7185929648241207, 3.245129361239188, 0], [-3.678391959798995, 3.1606686398537747, 0], [-3.6381909547738696, 3.0813114783151887, 0], [-3.5979899497487438, 3.0085426455131214, 0], [-3.557788944723618, 2.943794861337173, 0], [-3.5175879396984926, 2.8884255563088708, 0], [-3.477386934673367, 2.843694458550632, 0], [-3.4371859296482414, 2.8107423510957608, 0], [-3.3969849246231156, 2.7905713271503365, 0], [-3.35678391959799, 2.7840268506427126, 0], [-3.3165829145728645, 2.7917819045236842, 0], [-3.2763819095477387, 2.8143234801633197, 0], [-3.2361809045226133, 2.851941628243802, 0], [-3.1959798994974875, 2.9047212552432624, 0], [-3.1557788944723617, 2.972536810465134, 0], [-3.115577889447236, 3.055049967154617, 0], [-3.0753768844221105, 3.1517103581565307, 0], [-3.035175879396985, 3.2617593824302227, 0], [-2.9949748743718594, 3.3842370541871785, 0], [-2.9547738693467336, 3.517991822102217, 0], [-2.914572864321608, 3.6616932426142594, 0], [-2.8743718592964824, 3.813847349410389, 0], [-2.834170854271357, 3.9728145213893455, 0], [-2.7939698492462313, 4.1368296143099395, 0], [-2.7537688442211055, 4.304024087489989, 0], [-2.7135678391959797, 4.472449826830258, 0], [-2.6733668341708543, 4.640104339539525, 0], [-2.633165829145729, 4.804956974615976, 0], [-2.592964824120603, 4.964975806715139, 0], [-2.5527638190954773, 5.118154809754089, 0], [-2.5125628140703515, 5.26254094064017, 0], [-2.472361809045226, 5.396260752967843, 0], [-2.4321608040201004, 5.517546165419441, 0], [-2.391959798994975, 5.62475901987599, 0], [-2.351758793969849, 5.716414079756579, 0], [-2.3115577889447234, 5.791200139647179, 0], [-2.271356783919598, 5.84799894256737, 0], [-2.2311557788944723, 5.8859016309028975, 0], [-2.190954773869347, 5.904222490685992, 0], [-2.150753768844221, 5.902509786059261, 0], [-2.1105527638190953, 5.88055352088683, 0], [-2.07035175879397, 5.838390007009221, 0], [-2.030150753768844, 5.776303162971974, 0], [-1.9899497487437188, 5.694822512561358, 0], [-1.949748743718593, 5.594717898505709, 0], [-1.9095477386934672, 5.476990972591546, 0], [-1.8693467336683418, 5.342863568544905, 0], [-1.829145728643216, 5.193763107696298, 0], [-1.7889447236180902, 5.031305229058273, 0], [-1.7487437185929648, 4.857273874403049, 0], [-1.708542713567839, 4.673599094676816, 0], [-1.6683417085427137, 4.482332876115807, 0], [-1.6281407035175879, 4.285623312278437, 0], [-1.587939698492462, 4.085687471479545, 0], [-1.5477386934673367, 3.8847833274733663, 0], [-1.507537688442211, 3.685181134418745, 0], [-1.4673366834170856, 3.4891346349843717, 0], [-1.4271356783919598, 3.2988524928011564, 0], [-1.386934673366834, 3.116470337310106, 0], [-1.3467336683417086, 2.944023800431924, 0], [-1.3065326633165828, 2.7834229105229022, 0], [-1.2663316582914574, 2.63642818998033, 0], [-1.2261306532663316, 2.5046287788929478, 0], [-1.1859296482412058, 2.3894228786414278, 0], [-1.1457286432160805, 2.2920007767478716, 0], [-1.1055276381909547, 2.2133306780187736, 0], [-1.0653266331658293, 2.1541475276413204, 0], [-1.0251256281407035, 2.1149449699414538, 0], [-0.9849246231155777, 2.095970542593661, 0], [-0.9447236180904524, 2.0972241608142084, 0], [-0.9045226130653266, 2.1184599001179176, 0], [-0.8643216080402008, 2.159191040229106, 0], [-0.8241206030150754, 2.2186982873656786, 0], [-0.7839195979899496, 2.296041048007785, 0], [-0.7437185929648242, 2.3900715850462206, 0], [-0.7035175879396984, 2.499451847480713, 0], [-0.6633165829145726, 2.6226727281673696, 0], [-0.6231155778894473, 2.7580754710168254, 0], [-0.5829145728643215, 2.9038749199865737, 0], [-0.5427135678391961, 3.05818427760089, 0], [-0.5025125628140703, 3.21904102091327, 0], [-0.4623115577889445, 3.3844336080735506, 0], [-0.42211055276381915, 3.552328599176126, 0], [-0.38190954773869334, 3.720697810971518, 0], [-0.341708542713568, 3.8875451263681686, 0], [-0.3015075376884422, 4.050932586403482, 0], [-0.2613065326633164, 4.209005404413034, 0], [-0.22110552763819102, 4.360015559289627, 0], [-0.18090452261306522, 4.5023436467397335, 0], [-0.14070351758793986, 4.634518693985675, 0], [-0.10050251256281406, 4.755235674033832, 0], [-0.06030150753768826, 4.863370489979597, 0], [-0.0201005025125629, 4.957992237343947, 0], [0.020100502512562457, 5.03837259258391, 0], [0.06030150753768826, 5.103992218103028, 0], [0.10050251256281406, 5.154544117692346, 0], [0.14070351758793986, 5.189933920722438, 0], [0.18090452261306567, 5.2102771179369505, 0], [0.22110552763819058, 5.215893315721976, 0], [0.2613065326633164, 5.207297618605111, 0], [0.3015075376884422, 5.185189290853465, 0], [0.341708542713568, 5.1504378867975795, 0], [0.3819095477386938, 5.104067075350142, 0], [0.4221105527638196, 5.047236416599999, 0], [0.4623115577889445, 4.981221376879223, 0], [0.5025125628140703, 4.90739189291773, 0], [0.5427135678391961, 4.827189815273234, 0], [0.5829145728643219, 4.742105575879351, 0], [0.6231155778894477, 4.653654434089338, 0], [0.6633165829145726, 4.563352659879721, 0], [0.7035175879396984, 4.472694011866587, 0], [0.7437185929648242, 4.38312686150488, 0], [0.78391959798995, 4.2960323033915, 0], [0.8241206030150758, 4.212703575156423, 0], [0.8643216080402008, 4.134327089254502, 0], [0.9045226130653266, 4.061965353385714, 0], [0.9447236180904524, 3.9965420266590583, 0], [0.9849246231155782, 3.9388293254192144, 0], [1.025125628140704, 3.889437956371918, 0], [1.0653266331658289, 3.848809715814541, 0], [1.1055276381909547, 3.8172128529805605, 0], [1.1457286432160805, 3.7947402533463355, 0], [1.1859296482412063, 3.781310454851381, 0], [1.226130653266332, 3.77667146698483, 0], [1.266331658291457, 3.7804073202274995, 0], [1.3065326633165828, 3.7919472320391376, 0], [1.3467336683417086, 3.810577236054547, 0], [1.3869346733668344, 3.835454083984362, 0], [1.4271356783919602, 3.8656211954551916, 0], [1.4673366834170851, 3.900026400175366, 0], [1.507537688442211, 3.9375411898319705, 0], [1.5477386934673367, 3.97698117441011, 0], [1.5879396984924625, 4.017127419511671, 0], [1.6281407035175883, 4.0567483280051295, 0], [1.6683417085427132, 4.094621721155715, 0], [1.708542713567839, 4.1295567713870005, 0], [1.7487437185929648, 4.160415441054974, 0], [1.7889447236180906, 4.186133089041017, 0], [1.8291457286432165, 4.205737919481453, 0], [1.8693467336683414, 4.218368964363966, 0], [1.9095477386934672, 4.22329231377843, 0], [1.949748743718593, 4.219915333986216, 0], [1.9899497487437188, 4.20779864377874, 0], [2.0301507537688446, 4.186665653385618, 0], [2.0703517587939704, 4.1564095069665346, 0], [2.1105527638190953, 4.117097308935861, 0], [2.150753768844221, 4.068971555445605, 0], [2.190954773869347, 4.01244873468354, 0], [2.2311557788944727, 3.948115102602927, 0], [2.2713567839195985, 3.876719683652383, 0], [2.3115577889447234, 3.799164588382707, 0], [2.351758793969849, 3.7164927808443315, 0], [2.391959798994975, 3.629873467845126, 0], [2.432160804020101, 3.5405853188309226, 0], [2.4723618090452266, 3.4499977588337263, 0], [2.5125628140703515, 3.3595506071015024, 0], [2.5527638190954773, 3.2707323602265292, 0], [2.592964824120603, 3.185057440431927, 0], [2.633165829145729, 3.1040427468266785, 0], [2.6733668341708547, 3.0291838596357197, 0], [2.7135678391959797, 2.9619312544626837, 0], [2.7537688442211055, 2.9036668854333345, 0], [2.7939698492462313, 2.8556814925591354, 0], [2.834170854271357, 2.819152979891639, 0], [2.874371859296483, 2.795126197125697, 0], [2.914572864321608, 2.7844944384442374, 0], [2.9547738693467336, 2.7879829488438643, 0], [2.9949748743718594, 2.8061347002718393, 0], [3.035175879396985, 2.8392986680386127, 0], [3.075376884422111, 2.8876208026016155, 0], [3.115577889447236, 2.951037853453216, 0], [3.1557788944723617, 3.0292741610407763, 0], [3.1959798994974875, 3.1218414899882907, 0], [3.2361809045226133, 3.228041932994002, 0], [3.276381909547739, 3.346973870282353, 0], [3.316582914572864, 3.477540925037483, 0], [3.35678391959799, 3.618463811485271, 0], [3.3969849246231156, 3.7682949298589006, 0], [3.4371859296482414, 3.925435521998332, 0], [3.4773869346733672, 4.088155163388492, 0], [3.517587939698492, 4.254613332590783, 0], [3.557788944723618, 4.42288276777969, 0], [3.5979899497487438, 4.590974292921508, 0], [3.6381909547738696, 4.756862773428436, 0], [3.6783919597989954, 4.918513843226584, 0], [3.7185929648241203, 5.073911032360847, 0], [3.758793969849246, 5.221082916719447, 0], [3.798994974874372, 5.358129909316842, 0], [3.8391959798994977, 5.483250315868872, 0], [3.8793969849246235, 5.594765286092498, 0], [3.9195979899497493, 5.691142306151208, 0], [3.959798994974874, 5.7710168967558575, 0], [4.0, 5.833212205355873, 0]]


read_mesh = open("C:\\Users\chris\ChrisdeMontigny\\Nefari0 Repository\Python\Blender\mesh_data.txt","r")
is_read = read_mesh.read()
read_mesh.close()

read_list = list(is_read.split('>>')) # converts to python array
# list_index = read_list.split('<')
#new_coords = []
verts1 = []

for i in range(len(read_list)-1):
    list_index = read_list[i].split('<') # converts each array element into floats, stores in new_coord array
    coords = [float(list_index[1]),float(list_index[3]),float(list_index[5])]
    verts1.append(coords)

print(verts1)

# This calculates the edges based on the verts1 array
edges1 = [[len(verts1) - 1, 0]]
for i in range( 0, len(verts1)-1):
    edges1.append( [i, i+1] )


# Generate the actual Blender geometry:(name, origin, verts, edges, faces)
createMeshFromData( 'Geometry', [0, 0, 0], verts1, edges1, [] )