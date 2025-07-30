---
title: "Metadata Diagram"
description: "A diagram diagram template"
category: "diagrams"
type: "diagram"
source_file: "diagrams/metadata_decoded.xml"
---

# Metadata Diagram

A diagram diagram template

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="773" dy="1215" grid="0" gridSize="10" guides="1" tooltips="1" connect="0" arrows="1" fold="1" page="1" pageScale="1" pageWidth="826" pageHeight="1169" background="#ffffff" math="0" shadow="0">
  <root>
    <UserObject label="" author="John Doe" revision="v1.0" id="0">
      <mxCell/>
    </UserObject>
    <mxCell id="1" parent="0"/>
    <mxCell id="9" value="" style="group;strokeColor=#000000;" parent="1" vertex="1" connectable="0">
      <mxGeometry x="120" y="125" width="180" height="50" as="geometry"/>
    </mxCell>
    <object label="John Doe" placeholders="1" placeholder="author" id="4">
      <mxCell style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;overflow=hidden;fontStyle=1" parent="9" vertex="1">
        <mxGeometry x="78" y="5" width="62" height="20" as="geometry"/>
      </mxCell>
    </object>
    <mxCell id="5" value="Author:" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;overflow=hidden;" parent="9" vertex="1">
      <mxGeometry x="8" y="5" width="60" height="20" as="geometry"/>
    </mxCell>
    <object label="v1.0" placeholders="1" placeholder="revision" id="7">
      <mxCell style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;overflow=hidden;fontStyle=1" parent="9" vertex="1">
        <mxGeometry x="78" y="25" width="32" height="20" as="geometry"/>
      </mxCell>
    </object>
    <mxCell id="8" value="Revision:" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;overflow=hidden;" parent="9" vertex="1">
      <mxGeometry x="8" y="25" width="60" height="20" as="geometry"/>
    </mxCell>
    <object label="This diagram was created by %author%.&lt;br&gt;Current revision is %revision%." placeholders="1" id="10">
      <mxCell style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;overflow=hidden;fontSize=12;" parent="1" vertex="1">
        <mxGeometry x="140" y="195" width="242" height="40" as="geometry"/>
      </mxCell>
    </object>
    <mxCell id="12" value="Direct Reference:" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;overflow=hidden;fontSize=12;" parent="1" vertex="1">
      <mxGeometry x="138" y="265" width="102" height="20" as="geometry"/>
    </mxCell>
    <object label="John Doe" placeholders="1" placeholder="author" id="13">
      <mxCell style="text;html=1;strokeColor=#000000;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;overflow=hidden;fontStyle=1" parent="1" vertex="1">
        <mxGeometry x="240" y="265" width="84" height="20" as="geometry"/>
      </mxCell>
    </object>
    <mxCell id="14" value="Edit and&lt;br&gt;press Ctrl+M" style="edgeStyle=elbowEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;fontSize=11;startArrow=classicThin;startFill=1;elbow=vertical;endArrow=classicThin;endFill=1;" parent="1" source="4" target="13" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="400" y="135"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="15" style="edgeStyle=elbowEdgeStyle;rounded=0;html=1;entryX=0.773;entryY=0.125;entryPerimeter=0;startArrow=classicThin;startFill=1;jettySize=auto;orthogonalLoop=1;fontSize=12;dashed=1;dashPattern=1 1;endArrow=none;endFill=0;" parent="1" source="4" target="10" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="327" y="145"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="18" value="reference" style="text;html=1;resizable=0;points=[];align=center;verticalAlign=middle;labelBackgroundColor=#ffffff;fontSize=11;fontStyle=2" parent="15" vertex="1" connectable="0">
      <mxGeometry x="0.4188" y="2" relative="1" as="geometry">
        <mxPoint as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="16" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0.479;entryY=0.925;entryPerimeter=0;startArrow=classicThin;startFill=1;jettySize=auto;orthogonalLoop=1;fontSize=12;dashed=1;dashPattern=1 1;endArrow=none;endFill=0;" parent="1" source="7" target="10" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="280" y="160"/>
          <mxPoint x="280" y="190"/>
          <mxPoint x="130" y="190"/>
          <mxPoint x="130" y="255"/>
          <mxPoint x="256" y="255"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="17" value="reference" style="text;html=1;resizable=0;points=[];align=center;verticalAlign=middle;labelBackgroundColor=#ffffff;fontSize=11;fontStyle=2" parent="16" vertex="1" connectable="0">
      <mxGeometry x="0.4693" y="-1" relative="1" as="geometry">
        <mxPoint x="-3" y="-11" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="19" value="Using Metadata (Ctrl+M)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;overflow=hidden;fontSize=16;fontStyle=1;fontFamily=Helvetica;" parent="1" vertex="1">
      <mxGeometry x="120" y="80" width="280" height="30" as="geometry"/>
    </mxCell>
    <UserObject label="%name% Data Text (Select and press Ctrl+M)" placeholders="1" name="Variable" id="21">
      <mxCell style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;overflow=hidden;" parent="1" vertex="1">
        <mxGeometry x="120" y="300" width="249" height="20" as="geometry"/>
      </mxCell>
    </UserObject>
    <mxCell id="22" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;entryX=0.089;entryY=0.95;entryPerimeter=0;endArrow=none;endFill=0;startArrow=classicThin;startFill=1;dashed=1;dashPattern=1 1;" parent="1" source="21" target="21" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="367" y="323" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="399" y="310"/>
          <mxPoint x="399" y="360"/>
          <mxPoint x="142" y="360"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="23" value="reference to metadata" style="text;html=1;resizable=0;points=[];align=center;verticalAlign=middle;labelBackgroundColor=#ffffff;fontSize=11;fontStyle=2" parent="22" vertex="1" connectable="0">
      <mxGeometry x="0.3228" y="1" relative="1" as="geometry">
        <mxPoint x="50" y="-11" as="offset"/>
      </mxGeometry>
    </mxCell>
  </root>
</mxGraphModel>

```
