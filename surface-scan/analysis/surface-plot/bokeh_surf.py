"""
Read WHAM free energy data and make an interactvive 3D surface plot.
"""
import os
import numpy as np
import yaml
from bokeh.core.properties import Instance, String
from bokeh.models import ColumnDataSource, LayoutDOM
from bokeh.io import save


####################################################################################################
SCAN = input('Enter scan name: ')
with open('%s-data.yaml' % SCAN, 'r') as yf:
    DATA = yaml.load(yf)
X, Y, Z = np.array(DATA['x']), np.array(DATA['y']), np.array(DATA['z'])
Z[np.isinf(Z)] = 0
####################################################################################################

JS_CODE = """
import * as p from "core/properties"
import {LayoutDOM, LayoutDOMView} from "models/layouts/layout_dom"

OPTIONS =
  width:  '1200px'
  height: '800px'
  style: 'surface'
  showPerspective: true
  showGrid: true
  showShadow: true
  keepAspectRatio: true
  verticalRatio: 1.0
  showLegend: true
  legendLabel: 'Free Energy (kcal/mol)'
  xLabel: 'x (Å)'
  yLabel: 'y (Å)'
  zLabel: 'Free Energy (kcal/mol)'
  cameraPosition:
    horizontal: -0.8
    vertical: 0.1
    distance: 1.8
  tooltip: (point) -> return 'x: <b>' + Math.round(point.x * 100) / 100 + '</b>  y: <b>' + Math.round(point.y * 100) / 100 + '</b><br>F: <b>' + Math.round(point.z * 100) / 100 + '</b>'

export class Surface3dView extends LayoutDOMView

  initialize: (options) ->
    super(options)

    url = "https://cdnjs.cloudflare.com/ajax/libs/vis/4.16.1/vis.min.js"

    script = document.createElement('script')
    script.src = url
    script.async = false
    script.onreadystatechange = script.onload = () => @_init()
    document.querySelector("head").appendChild(script)

  _init: () ->
    @_graph = new vis.Graph3d(@el, @get_data(), OPTIONS)

    # Set a listener so that when the Bokeh data source has a change
    # event, we can process the new data
    @connect(@model.data_source.change, () =>
        @_graph.setData(@get_data())
    )

  # This is the callback executed when the Bokeh data has an change. Its basic
  # function is to adapt the Bokeh data source to the vis.js DataSet format.
  get_data: () ->
    data = new vis.DataSet()
    source = @model.data_source
    for i in [0...source.get_length()]
      data.add({
        x:     source.get_column(@model.x)[i]
        y:     source.get_column(@model.y)[i]
        z:     source.get_column(@model.z)[i]
      })
    return data

export class Surface3d extends LayoutDOM

  # This is usually boilerplate. In some cases there may not be a view.
  default_view: Surface3dView

  # The ``type`` class attribute should generally match exactly the name
  # of the corresponding Python class.
  type: "Surface3d"

  # The @define block adds corresponding "properties" to the JS model. These
  # should basically line up 1-1 with the Python model class. Most property
  # types have counterparts, e.g. ``bokeh.core.properties.String`` will be
  # ``p.String`` in the JS implementatin. Where the JS type system is not yet
  # as rich, you can use ``p.Any`` as a "wildcard" property type.
  @define {
    x:           [ p.String           ]
    y:           [ p.String           ]
    z:           [ p.String           ]
    data_source: [ p.Instance         ]
  }
"""


class Surface3d(LayoutDOM):
    __implementation__ = JS_CODE
    data_source = Instance(ColumnDataSource)
    x = String
    y = String
    z = String


source = ColumnDataSource(data=dict(x=X, y=Y, z=Z))
surface = Surface3d(x="x", y="y", z="z", data_source=source)
save(surface)
os.rename('bokeh_surf.html', '%s.html' % SCAN)
