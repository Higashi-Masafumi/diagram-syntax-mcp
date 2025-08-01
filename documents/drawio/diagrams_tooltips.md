---
title: "Tooltips Flowchart"
description: "A flowchart diagram showing process flow and decision points"
category: "diagrams"
type: "flowchart"
source_file: "diagrams/tooltips_decoded.xml"
tags: ["diagram", "drawio", "documentation"]
---

# Tooltips Flowchart

A flowchart diagram showing process flow and decision points

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="741" dy="1160" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="826" pageHeight="1169" background="#ffffff" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="5" target="4" edge="1">
      <mxGeometry x="240" y="155" as="geometry"/>
    </mxCell>
    <mxCell id="3" value="Start" style="ellipse;whiteSpace=wrap;html=1;" parent="1" vertex="1">
      <mxGeometry x="50" y="130" width="60" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="4" value="Decision" style="rhombus;whiteSpace=wrap;html=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;fillColor=#ffffff;" parent="1" vertex="1">
      <mxGeometry x="280" y="120" width="80" height="70" as="geometry"/>
    </mxCell>
    <UserObject label="Task 1" tooltip="&lt;strong&gt;Task analysis&lt;/strong&gt; describes in a way that is definable, measurable and communicable the basic units of work that are performed in a job. The task as a part of the function, is defined as a action or sequence of actions that contributes significantly to the completion of a specific work objective." id="5">
      <mxCell style="whiteSpace=wrap;html=1;" parent="1" vertex="1">
        <mxGeometry x="150" y="130" width="90" height="50" as="geometry"/>
      </mxCell>
    </UserObject>
    <mxCell id="6" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="3" target="5" edge="1">
      <mxGeometry x="110" y="155" as="geometry">
        <mxPoint x="120" y="155" as="sourcePoint"/>
        <mxPoint x="320" y="230" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="7" value="End" style="ellipse;whiteSpace=wrap;html=1;" parent="1" vertex="1">
      <mxGeometry x="290" y="230" width="60" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="8" value="No" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="4" target="7" edge="1">
      <mxGeometry x="320" y="190" as="geometry"/>
    </mxCell>
    <UserObject label="Task 2" tooltip="&lt;strong&gt;Task analysis&lt;/strong&gt; describes in a way that is definable, measurable and communicable the basic units of work that are performed in a job. The task as a part of the function, is defined as a action or sequence of actions that contributes significantly to the completion of a specific work objective." id="9">
      <mxCell style="whiteSpace=wrap;html=1;" parent="1" vertex="1">
        <mxGeometry x="420" y="130" width="100" height="50" as="geometry"/>
      </mxCell>
    </UserObject>
    <mxCell id="10" value="Yes" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="4" target="9" edge="1">
      <mxGeometry x="360" y="155" as="geometry"/>
    </mxCell>
    <mxCell id="11" value="End" style="ellipse;whiteSpace=wrap;html=1;" parent="1" vertex="1">
      <mxGeometry x="571" y="130" width="59" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="12" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="9" target="11" edge="1">
      <mxGeometry x="520" y="155" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
