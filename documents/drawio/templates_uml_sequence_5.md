---
title: "Sequence 5 Diagram"
description: "A diagram diagram template"
category: "templates/uml"
type: "diagram"
source_file: "templates/uml/sequence_5_decoded.xml"
tags: ["software", "template", "modeling", "drawio", "uml"]
---

# Sequence 5 Diagram

A diagram diagram template

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="850" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="3c9198fc6dad6e78-2" value="" style="shape=umlLifeline;participant=umlControl;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;verticalAlign=top;spacingTop=36;labelBackgroundColor=#ffffff;outlineConnect=0;rounded=0;shadow=0;comic=0;strokeColor=#000000;strokeWidth=1;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="330" y="120" width="40" height="300" as="geometry"/>
    </mxCell>
    <mxCell id="3c9198fc6dad6e78-3" value="" style="shape=umlLifeline;participant=umlEntity;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;verticalAlign=top;spacingTop=36;labelBackgroundColor=#ffffff;outlineConnect=0;rounded=0;shadow=0;comic=0;strokeColor=#000000;strokeWidth=1;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="490" y="120" width="40" height="300" as="geometry"/>
    </mxCell>
    <mxCell id="3c9198fc6dad6e78-8" value="" style="html=1;points=[];perimeter=orthogonalPerimeter;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=1;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="3c9198fc6dad6e78-3" vertex="1">
      <mxGeometry x="15" y="100" width="10" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="3c9198fc6dad6e78-15" value="" style="shape=umlDestroy;whiteSpace=wrap;html=1;strokeWidth=3;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="3c9198fc6dad6e78-3" vertex="1">
      <mxGeometry x="13" y="133" width="15" height="15" as="geometry"/>
    </mxCell>
    <mxCell id="3c9198fc6dad6e78-4" value="" style="shape=umlLifeline;participant=umlEntity;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;verticalAlign=top;spacingTop=36;labelBackgroundColor=#ffffff;outlineConnect=0;rounded=0;shadow=0;comic=0;strokeColor=#000000;strokeWidth=1;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="660" y="120" width="40" height="300" as="geometry"/>
    </mxCell>
    <mxCell id="3c9198fc6dad6e78-11" value="" style="html=1;points=[];perimeter=orthogonalPerimeter;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=1;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="3c9198fc6dad6e78-4" vertex="1">
      <mxGeometry x="15" y="170" width="10" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="3c9198fc6dad6e78-5" value=":Object" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=1;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="800" y="120" width="100" height="300" as="geometry"/>
    </mxCell>
    <mxCell id="3c9198fc6dad6e78-12" value="" style="html=1;points=[];perimeter=orthogonalPerimeter;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=1;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="3c9198fc6dad6e78-5" vertex="1">
      <mxGeometry x="45" y="210" width="10" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="3c9198fc6dad6e78-7" value="" style="html=1;points=[];perimeter=orthogonalPerimeter;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=1;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="345" y="200" width="10" height="180" as="geometry"/>
    </mxCell>
    <mxCell id="3c9198fc6dad6e78-9" value="dispatch" style="html=1;verticalAlign=bottom;endArrow=block;entryX=0;entryY=0;labelBackgroundColor=none;fontFamily=Verdana;fontSize=12;" parent="1" source="3c9198fc6dad6e78-7" target="3c9198fc6dad6e78-8" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="435" y="220" as="sourcePoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="3c9198fc6dad6e78-13" value="dispatch" style="html=1;verticalAlign=bottom;endArrow=block;labelBackgroundColor=none;fontFamily=Verdana;fontSize=12;" parent="1" source="3c9198fc6dad6e78-7" target="3c9198fc6dad6e78-11" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="500" y="295" as="sourcePoint"/>
        <mxPoint x="650" y="295" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="3c9198fc6dad6e78-14" value="dispatch" style="html=1;verticalAlign=bottom;endArrow=block;labelBackgroundColor=none;fontFamily=Verdana;fontSize=12;" parent="1" source="3c9198fc6dad6e78-7" target="3c9198fc6dad6e78-12" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="365" y="300" as="sourcePoint"/>
        <mxPoint x="685" y="300" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
  </root>
</mxGraphModel>

```
