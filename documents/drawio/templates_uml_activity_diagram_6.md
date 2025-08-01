---
title: "Activity Diagram 6 Flowchart"
description: "A flowchart diagram showing process flow and decision points"
category: "templates/uml"
type: "flowchart"
source_file: "templates/uml/activity_diagram_6_decoded.xml"
tags: ["logic", "software", "template", "modeling", "venn", "drawio", "uml"]
---

# Activity Diagram 6 Flowchart

A flowchart diagram showing process flow and decision points

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="826" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2" value="Thread 1" style="swimlane;whiteSpace=wrap" parent="1" vertex="1">
      <mxGeometry x="164.5" y="128" width="280" height="570" as="geometry"/>
    </mxCell>
    <mxCell id="5" value="" style="ellipse;shape=startState;fillColor=#000000;strokeColor=#ff0000;" parent="2" vertex="1">
      <mxGeometry x="100" y="40" width="30" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="6" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;verticalAlign=bottom;endArrow=open;endSize=8;strokeColor=#FF0000;endFill=1;rounded=0" parent="2" source="5" target="7" edge="1">
      <mxGeometry x="100" y="40" as="geometry">
        <mxPoint x="115" y="110" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="7" value="idle" style="" parent="2" vertex="1">
      <mxGeometry x="60" y="110" width="110" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="8" value="user action" style="" parent="2" vertex="1">
      <mxGeometry x="60" y="220" width="110" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="9" value="" style="endArrow=open;strokeColor=#FF0000;endFill=1;rounded=0" parent="2" source="7" target="8" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="10" value="post command" style="" parent="2" vertex="1">
      <mxGeometry x="60" y="325" width="110" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="11" value="" style="endArrow=open;strokeColor=#FF0000;endFill=1;rounded=0" parent="2" source="8" target="10" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="12" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;strokeColor=#FF0000;endArrow=open;endFill=1;rounded=0" parent="2" source="10" target="7" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="160" y="290" as="sourcePoint"/>
        <mxPoint x="260" y="190" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="30" y="250"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="3" value="Thread 2" style="swimlane;whiteSpace=wrap" parent="1" vertex="1">
      <mxGeometry x="444.5" y="128" width="280" height="570" as="geometry"/>
    </mxCell>
    <mxCell id="13" value="" style="ellipse;shape=startState;fillColor=#000000;strokeColor=#ff0000;" parent="3" vertex="1">
      <mxGeometry x="60" y="40" width="30" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="14" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;verticalAlign=bottom;endArrow=open;endSize=8;strokeColor=#FF0000;endFill=1;rounded=0" parent="3" source="13" target="15" edge="1">
      <mxGeometry x="40" y="20" as="geometry">
        <mxPoint x="55" y="90" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="15" value="idle" style="" parent="3" vertex="1">
      <mxGeometry x="20" y="110" width="110" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="16" value="check for &#10;new commands" style="" parent="3" vertex="1">
      <mxGeometry x="20" y="220" width="110" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="17" value="" style="endArrow=open;strokeColor=#FF0000;endFill=1;rounded=0" parent="3" source="15" target="16" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="18" value="command queue" style="" parent="3" vertex="1">
      <mxGeometry x="20" y="325" width="110" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="19" value="" style="endArrow=open;strokeColor=#FF0000;endFill=1;rounded=0" parent="3" source="16" target="18" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="21" value="queue empty" style="rhombus;fillColor=#ffffc0;strokeColor=#ff0000;" parent="3" vertex="1">
      <mxGeometry x="150" y="225" width="80" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="22" value="yes" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;align=left;verticalAlign=bottom;endArrow=open;endSize=8;strokeColor=#FF0000;exitX=0.5;exitY=0;endFill=1;rounded=0;entryX=0.75;entryY=0.5;entryPerimeter=0" parent="3" source="21" target="25" edge="1">
      <mxGeometry x="-1" relative="1" as="geometry">
        <mxPoint x="160" y="150" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="190" y="180"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="23" value="no" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;align=left;verticalAlign=top;endArrow=open;endSize=8;strokeColor=#FF0000;endFill=1;rounded=0" parent="3" source="21" target="30" edge="1">
      <mxGeometry x="-1" relative="1" as="geometry">
        <mxPoint x="190" y="305" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="24" value="" style="endArrow=open;strokeColor=#FF0000;endFill=1;rounded=0" parent="3" source="16" target="21" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="25" value="" style="shape=line;strokeWidth=6;strokeColor=#ff0000;rotation=90" parent="3" vertex="1">
      <mxGeometry x="130" y="127.5" width="50" height="15" as="geometry"/>
    </mxCell>
    <mxCell id="26" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;verticalAlign=bottom;endArrow=open;endSize=8;strokeColor=#FF0000;endFill=1;rounded=0" parent="3" source="25" target="15" edge="1">
      <mxGeometry x="130" y="90" as="geometry">
        <mxPoint x="230" y="140" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="30" value="dispatch&#10;command&#10;worker thread" style="" parent="3" vertex="1">
      <mxGeometry x="140" y="325" width="110" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="31" value="critical&#10;section" style="shape=note;whiteSpace=wrap;size=17" parent="3" vertex="1">
      <mxGeometry x="105" y="490" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="32" value="" style="endArrow=none;strokeColor=#FF0000;endFill=0;rounded=0;dashed=1" parent="3" source="18" target="31" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="34" value="" style="whiteSpace=wrap;strokeColor=#FF0000;fillColor=#FF0000" parent="3" vertex="1">
      <mxGeometry x="245" y="395" width="5" height="45" as="geometry"/>
    </mxCell>
    <mxCell id="41" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;entryX=0;entryY=0.5;strokeColor=#FF0000;endArrow=open;endFill=1;rounded=0" parent="3" source="30" target="34" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="60" y="480" as="sourcePoint"/>
        <mxPoint x="160" y="380" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="195" y="400"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="4" value="Thread 3" style="swimlane;whiteSpace=wrap" parent="1" vertex="1">
      <mxGeometry x="724.5" y="128" width="280" height="570" as="geometry"/>
    </mxCell>
    <mxCell id="33" value="process&#10;command" style="" parent="4" vertex="1">
      <mxGeometry x="90" y="405" width="110" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="35" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;strokeColor=#FF0000;endArrow=open;endFill=1;rounded=0;entryX=0.25;entryY=0.5;entryPerimeter=0" parent="4" target="25" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="-30" y="410" as="sourcePoint"/>
        <mxPoint x="-120" y="120" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="-10" y="135"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="37" value="" style="edgeStyle=none;strokeColor=#FF0000;endArrow=open;endFill=1;rounded=0" parent="4" target="33" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="-30" y="429.5" as="sourcePoint"/>
        <mxPoint x="90" y="429.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="38" value="" style="ellipse;shape=endState;fillColor=#000000;strokeColor=#ff0000" parent="4" vertex="1">
      <mxGeometry x="130" y="500" width="30" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="39" value="" style="endArrow=open;strokeColor=#FF0000;endFill=1;rounded=0" parent="4" source="33" target="38" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="20" value="" style="endArrow=open;strokeColor=#FF0000;endFill=1;rounded=0" parent="1" source="10" target="18" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
