---
title: "Sequence Diagram Example"
description: "A diagram diagram template"
category: "templates/basic"
type: "diagram"
source_file: "templates/basic/sequence_decoded.xml"
tags: ["fundamental", "simple", "template", "basic", "modeling", "drawio", "uml"]
---

# Sequence Diagram Example

A diagram diagram template

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1223" dy="1182" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="3nuBFxr9cyL0pnOWT2aG-1" value=":Object" style="shape=umlLifeline;perimeter=lifelinePerimeter;container=1;collapsible=0;recursiveResize=0;rounded=0;shadow=0;strokeWidth=1;" vertex="1" parent="1">
      <mxGeometry x="120" y="80" width="100" height="300" as="geometry"/>
    </mxCell>
    <mxCell id="3nuBFxr9cyL0pnOWT2aG-2" value="" style="points=[];perimeter=orthogonalPerimeter;rounded=0;shadow=0;strokeWidth=1;" vertex="1" parent="3nuBFxr9cyL0pnOWT2aG-1">
      <mxGeometry x="45" y="70" width="10" height="190" as="geometry"/>
    </mxCell>
    <mxCell id="3nuBFxr9cyL0pnOWT2aG-3" value="dispatch" style="verticalAlign=bottom;startArrow=oval;endArrow=block;startSize=8;shadow=0;strokeWidth=1;" edge="1" parent="3nuBFxr9cyL0pnOWT2aG-1" target="3nuBFxr9cyL0pnOWT2aG-2">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="-15" y="70" as="sourcePoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="3nuBFxr9cyL0pnOWT2aG-4" value="" style="points=[];perimeter=orthogonalPerimeter;rounded=0;shadow=0;strokeWidth=1;" vertex="1" parent="3nuBFxr9cyL0pnOWT2aG-1">
      <mxGeometry x="50" y="120" width="10" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="3nuBFxr9cyL0pnOWT2aG-5" value=":Object" style="shape=umlLifeline;perimeter=lifelinePerimeter;container=1;collapsible=0;recursiveResize=0;rounded=0;shadow=0;strokeWidth=1;" vertex="1" parent="1">
      <mxGeometry x="300" y="80" width="100" height="300" as="geometry"/>
    </mxCell>
    <mxCell id="3nuBFxr9cyL0pnOWT2aG-6" value="" style="points=[];perimeter=orthogonalPerimeter;rounded=0;shadow=0;strokeWidth=1;" vertex="1" parent="3nuBFxr9cyL0pnOWT2aG-5">
      <mxGeometry x="45" y="80" width="10" height="160" as="geometry"/>
    </mxCell>
    <mxCell id="3nuBFxr9cyL0pnOWT2aG-7" value="return" style="verticalAlign=bottom;endArrow=open;dashed=1;endSize=8;exitX=0;exitY=0.95;shadow=0;strokeWidth=1;" edge="1" source="3nuBFxr9cyL0pnOWT2aG-6" target="3nuBFxr9cyL0pnOWT2aG-2" parent="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="275" y="236" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="3nuBFxr9cyL0pnOWT2aG-8" value="dispatch" style="verticalAlign=bottom;endArrow=block;entryX=0;entryY=0;shadow=0;strokeWidth=1;" edge="1" source="3nuBFxr9cyL0pnOWT2aG-2" target="3nuBFxr9cyL0pnOWT2aG-6" parent="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="275" y="160" as="sourcePoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="3nuBFxr9cyL0pnOWT2aG-9" value="callback" style="verticalAlign=bottom;endArrow=block;entryX=1;entryY=0;shadow=0;strokeWidth=1;" edge="1" source="3nuBFxr9cyL0pnOWT2aG-6" target="3nuBFxr9cyL0pnOWT2aG-4" parent="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="240" y="200" as="sourcePoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="3nuBFxr9cyL0pnOWT2aG-10" value="return" style="verticalAlign=bottom;endArrow=open;dashed=1;endSize=8;exitX=1;exitY=0.95;shadow=0;strokeWidth=1;" edge="1" source="3nuBFxr9cyL0pnOWT2aG-4" target="3nuBFxr9cyL0pnOWT2aG-6" parent="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="240" y="257" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
  </root>
</mxGraphModel>

```
