---
title: "Sequence Diagram Example"
description: "A diagram diagram template"
category: "diagrams"
type: "diagram"
source_file: "diagrams/sequence_decoded.xml"
tags: ["documentation", "diagram", "modeling", "drawio", "uml"]
---

# Sequence Diagram Example

A diagram diagram template

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="705" dy="1139" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="826" pageHeight="1169" background="#ffffff" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2" value=":Object" style="shape=umlLifeline;perimeter=lifelinePerimeter;container=1;collapsible=0;recursiveResize=0;rounded=0;shadow=0;strokeWidth=1;" vertex="1" parent="1">
      <mxGeometry x="95" y="80" width="100" height="300" as="geometry"/>
    </mxCell>
    <mxCell id="3" value="" style="points=[];perimeter=orthogonalPerimeter;rounded=0;shadow=0;strokeWidth=1;" vertex="1" parent="2">
      <mxGeometry x="45" y="70" width="10" height="190" as="geometry"/>
    </mxCell>
    <mxCell id="4" value="dispatch" style="verticalAlign=bottom;startArrow=oval;endArrow=block;startSize=8;shadow=0;strokeWidth=1;" edge="1" parent="2" target="3">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="-15" y="70" as="sourcePoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="5" value="" style="points=[];perimeter=orthogonalPerimeter;rounded=0;shadow=0;strokeWidth=1;" vertex="1" parent="2">
      <mxGeometry x="50" y="120" width="10" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="6" value=":Object" style="shape=umlLifeline;perimeter=lifelinePerimeter;container=1;collapsible=0;recursiveResize=0;rounded=0;shadow=0;strokeWidth=1;" vertex="1" parent="1">
      <mxGeometry x="275" y="80" width="100" height="300" as="geometry"/>
    </mxCell>
    <mxCell id="7" value="" style="points=[];perimeter=orthogonalPerimeter;rounded=0;shadow=0;strokeWidth=1;" vertex="1" parent="6">
      <mxGeometry x="45" y="80" width="10" height="160" as="geometry"/>
    </mxCell>
    <mxCell id="8" value="return" style="verticalAlign=bottom;endArrow=open;dashed=1;endSize=8;exitX=0;exitY=0.95;shadow=0;strokeWidth=1;" edge="1" source="7" target="3" parent="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="250" y="236" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="9" value="dispatch" style="verticalAlign=bottom;endArrow=block;entryX=0;entryY=0;shadow=0;strokeWidth=1;" edge="1" source="3" target="7" parent="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="250" y="160" as="sourcePoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="10" value="callback" style="verticalAlign=bottom;endArrow=block;entryX=1;entryY=0;shadow=0;strokeWidth=1;" edge="1" source="7" target="5" parent="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="215" y="200" as="sourcePoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="11" value="return" style="verticalAlign=bottom;endArrow=open;dashed=1;endSize=8;exitX=1;exitY=0.95;shadow=0;strokeWidth=1;" edge="1" source="5" target="7" parent="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="215" y="257" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
  </root>
</mxGraphModel>

```
