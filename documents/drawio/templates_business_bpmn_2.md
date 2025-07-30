---
title: "Bpmn 2 Flowchart"
description: "A flowchart diagram showing process flow and decision points"
category: "templates/business"
type: "flowchart"
source_file: "templates/business/bpmn_2_decoded.xml"
---

# Bpmn 2 Flowchart

A flowchart diagram showing process flow and decision points

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="850" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="3d7c0b7366173e4a-30" value="Pool" style="swimlane;html=1;childLayout=stackLayout;horizontal=0;startSize=20;horizontalStack=0;" parent="1" vertex="1">
      <mxGeometry x="88" y="75" width="2025" height="700" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-31" value="Lane 1" style="swimlane;html=1;startSize=20;horizontal=0;" parent="3d7c0b7366173e4a-30" vertex="1">
      <mxGeometry x="20" width="2005" height="180" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-40" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="3d7c0b7366173e4a-31" source="3d7c0b7366173e4a-9" target="3d7c0b7366173e4a-12" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-9" value="Sub-Process" style="html=1;whiteSpace=wrap;rounded=1;" parent="3d7c0b7366173e4a-31" vertex="1">
      <mxGeometry x="282" y="48" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-10" value="" style="html=1;shape=plus;" parent="3d7c0b7366173e4a-9" vertex="1">
      <mxGeometry x="0.5" y="1" width="14" height="14" relative="1" as="geometry">
        <mxPoint x="-7" y="-14" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-39" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="3d7c0b7366173e4a-31" source="3d7c0b7366173e4a-11" target="3d7c0b7366173e4a-9" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-11" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=eventInt;symbol=message;" parent="3d7c0b7366173e4a-31" vertex="1">
      <mxGeometry x="142" y="63" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-41" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="3d7c0b7366173e4a-31" source="3d7c0b7366173e4a-12" target="3d7c0b7366173e4a-13" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-12" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=rhombusPerimeter;background=gateway;outline=none;symbol=parallelGw;" parent="3d7c0b7366173e4a-31" vertex="1">
      <mxGeometry x="482" y="63" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-42" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="3d7c0b7366173e4a-31" source="3d7c0b7366173e4a-13" target="3d7c0b7366173e4a-37" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-13" value="Sub-Process" style="html=1;whiteSpace=wrap;rounded=1;" parent="3d7c0b7366173e4a-31" vertex="1">
      <mxGeometry x="612" y="48" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-14" value="" style="html=1;shape=plus;" parent="3d7c0b7366173e4a-13" vertex="1">
      <mxGeometry x="0.5" y="1" width="14" height="14" relative="1" as="geometry">
        <mxPoint x="-7" y="-14" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-57" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="3d7c0b7366173e4a-31" source="3d7c0b7366173e4a-27" target="3d7c0b7366173e4a-29" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-27" value="Sub-Process" style="html=1;whiteSpace=wrap;rounded=1;" parent="3d7c0b7366173e4a-31" vertex="1">
      <mxGeometry x="1582" y="48" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-28" value="" style="html=1;shape=plus;" parent="3d7c0b7366173e4a-27" vertex="1">
      <mxGeometry x="0.5" y="1" width="14" height="14" relative="1" as="geometry">
        <mxPoint x="-7" y="-14" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-29" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=end;symbol=general;" parent="3d7c0b7366173e4a-31" vertex="1">
      <mxGeometry x="1792" y="63" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-37" value="Sub-Process" style="html=1;whiteSpace=wrap;rounded=1;" parent="3d7c0b7366173e4a-31" vertex="1">
      <mxGeometry x="922" y="47.99999999999994" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-38" value="" style="html=1;shape=plus;" parent="3d7c0b7366173e4a-37" vertex="1">
      <mxGeometry x="0.5" y="1" width="14" height="14" relative="1" as="geometry">
        <mxPoint x="-7" y="-14" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-32" value="Lane 2" style="swimlane;html=1;startSize=20;horizontal=0;" parent="3d7c0b7366173e4a-30" vertex="1">
      <mxGeometry x="20" y="180" width="2005" height="170" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-44" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="3d7c0b7366173e4a-32" source="3d7c0b7366173e4a-15" target="3d7c0b7366173e4a-17" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-15" value="Sub-Process" style="html=1;whiteSpace=wrap;rounded=1;" parent="3d7c0b7366173e4a-32" vertex="1">
      <mxGeometry x="612" y="45" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-16" value="" style="html=1;shape=plus;" parent="3d7c0b7366173e4a-15" vertex="1">
      <mxGeometry x="0.5" y="1" width="14" height="14" relative="1" as="geometry">
        <mxPoint x="-7" y="-14" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-45" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="3d7c0b7366173e4a-32" source="3d7c0b7366173e4a-17" target="3d7c0b7366173e4a-18" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-17" value="" style="rhombus;whiteSpace=wrap;html=1;" parent="3d7c0b7366173e4a-32" vertex="1">
      <mxGeometry x="802" y="60" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-46" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="3d7c0b7366173e4a-32" source="3d7c0b7366173e4a-18" target="3d7c0b7366173e4a-20" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-18" value="Sub-Process" style="html=1;whiteSpace=wrap;rounded=1;" parent="3d7c0b7366173e4a-32" vertex="1">
      <mxGeometry x="922.0000000000007" y="45" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-19" value="" style="html=1;shape=plus;" parent="3d7c0b7366173e4a-18" vertex="1">
      <mxGeometry x="0.5" y="1" width="14" height="14" relative="1" as="geometry">
        <mxPoint x="-7" y="-14" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-20" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=rhombusPerimeter;background=gateway;outline=none;symbol=parallelGw;" parent="3d7c0b7366173e4a-32" vertex="1">
      <mxGeometry x="1122" y="60" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-33" value="Lane 3" style="swimlane;html=1;startSize=20;horizontal=0;" parent="3d7c0b7366173e4a-30" vertex="1">
      <mxGeometry x="20" y="350" width="2005" height="170" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-55" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="3d7c0b7366173e4a-33" source="3d7c0b7366173e4a-23" target="3d7c0b7366173e4a-25" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-23" value="Sub-Process" style="html=1;whiteSpace=wrap;rounded=1;" parent="3d7c0b7366173e4a-33" vertex="1">
      <mxGeometry x="1212" y="45" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-24" value="" style="html=1;shape=plus;" parent="3d7c0b7366173e4a-23" vertex="1">
      <mxGeometry x="0.5" y="1" width="14" height="14" relative="1" as="geometry">
        <mxPoint x="-7" y="-14" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-25" value="Sub-Process" style="html=1;whiteSpace=wrap;rounded=1;" parent="3d7c0b7366173e4a-33" vertex="1">
      <mxGeometry x="1422" y="45" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-26" value="" style="html=1;shape=plus;" parent="3d7c0b7366173e4a-25" vertex="1">
      <mxGeometry x="0.5" y="1" width="14" height="14" relative="1" as="geometry">
        <mxPoint x="-7" y="-14" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-35" value="Sub-Process" style="html=1;whiteSpace=wrap;rounded=1;" parent="3d7c0b7366173e4a-33" vertex="1">
      <mxGeometry x="612" y="44.99999999999992" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-36" value="" style="html=1;shape=plus;" parent="3d7c0b7366173e4a-35" vertex="1">
      <mxGeometry x="0.5" y="1" width="14" height="14" relative="1" as="geometry">
        <mxPoint x="-7" y="-14" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-34" value="Lane 3" style="swimlane;html=1;startSize=20;horizontal=0;" parent="3d7c0b7366173e4a-30" vertex="1">
      <mxGeometry x="20" y="520" width="2005" height="180" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-21" value="Sub-Process" style="html=1;whiteSpace=wrap;rounded=1;" parent="3d7c0b7366173e4a-34" vertex="1">
      <mxGeometry x="922.0000000000007" y="50" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-22" value="" style="html=1;shape=plus;" parent="3d7c0b7366173e4a-21" vertex="1">
      <mxGeometry x="0.5" y="1" width="14" height="14" relative="1" as="geometry">
        <mxPoint x="-7" y="-14" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-53" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="3d7c0b7366173e4a-34" source="3d7c0b7366173e4a-48" target="3d7c0b7366173e4a-21" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-48" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=rhombusPerimeter;background=gateway;outline=none;symbol=parallelGw;" parent="3d7c0b7366173e4a-34" vertex="1">
      <mxGeometry x="802" y="65" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-43" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="3d7c0b7366173e4a-30" source="3d7c0b7366173e4a-12" target="3d7c0b7366173e4a-15" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="527" y="265"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-49" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="3d7c0b7366173e4a-30" source="3d7c0b7366173e4a-17" target="3d7c0b7366173e4a-48" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="862" y="545" as="targetPoint"/>
        <Array as="points"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-50" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="3d7c0b7366173e4a-30" source="3d7c0b7366173e4a-15" target="3d7c0b7366173e4a-35" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-51" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="3d7c0b7366173e4a-30" source="3d7c0b7366173e4a-21" target="3d7c0b7366173e4a-18" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-52" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="3d7c0b7366173e4a-30" source="3d7c0b7366173e4a-35" target="3d7c0b7366173e4a-48" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="782" y="605" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="692" y="610"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-54" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="3d7c0b7366173e4a-30" source="3d7c0b7366173e4a-20" target="3d7c0b7366173e4a-23" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-56" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="3d7c0b7366173e4a-30" source="3d7c0b7366173e4a-25" target="3d7c0b7366173e4a-27" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="3d7c0b7366173e4a-58" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="3d7c0b7366173e4a-30" source="3d7c0b7366173e4a-37" target="3d7c0b7366173e4a-20" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="1151.9999999999995" y="245" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1167" y="90"/>
        </Array>
      </mxGeometry>
    </mxCell>
  </root>
</mxGraphModel>

```
