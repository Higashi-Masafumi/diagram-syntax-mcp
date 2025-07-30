---
title: "Mmo Simracing Service Flowchart"
description: "A flowchart diagram showing process flow and decision points"
category: "templates/software"
type: "flowchart"
source_file: "templates/software/mmo_simracing_service_decoded.xml"
tags: ["development", "software", "template", "architecture", "drawio"]
---

# Mmo Simracing Service Flowchart

A flowchart diagram showing process flow and decision points

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="826" pageHeight="1169" background="#006666" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2" value="user logs in" style="shape=mxgraph.flowchart.start_1;fillColor=#FF8000;strokeColor=#FF3333;strokeWidth=2;gradientColor=#FFFF33;gradientDirection=north" parent="1" vertex="1">
      <mxGeometry x="50" y="90" width="140" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="3" value="user history is evaluated" style="shape=mxgraph.flowchart.process;fillColor=#003366;strokeColor=#003366;strokeWidth=2;whiteSpace=wrap;gradientColor=#99CCFF;gradientDirection=north;fontColor=#FFFFFF;fontStyle=1;fontFamily=Tahoma" parent="1" vertex="1">
      <mxGeometry x="55" y="250" width="130" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="4" value="user chooses simrace category" style="shape=mxgraph.flowchart.process;fillColor=#003366;strokeColor=#003366;strokeWidth=2;whiteSpace=wrap;gradientColor=#99CCFF;gradientDirection=north;fontColor=#FFFFFF;fontStyle=1;fontFamily=Tahoma" parent="1" vertex="1">
      <mxGeometry x="55" y="350" width="130" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="5" value="" style="shape=mxgraph.flowchart.or;fillColor=#B3B3B3;strokeColor=#FFFFFF;strokeWidth=2" parent="1" vertex="1">
      <mxGeometry x="102.5" y="185" width="35" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="7" value="evaluate &#10;simracer&#10; pool" style="shape=mxgraph.flowchart.data;fillColor=#006600;strokeColor=#000000;strokeWidth=2;gradientColor=#009900;gradientDirection=north;fontColor=#FFFFFF;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="210" y="350" width="98" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="8" value="" style="shape=mxgraph.flowchart.decision;fillColor=#FF3333;strokeColor=#CC0000;strokeWidth=2;gradientColor=#FF9999;gradientDirection=north" parent="1" vertex="1">
      <mxGeometry x="320" y="340" width="80" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="9" value="Is league too small?" style="text;spacingTop=-5;fontColor=#66FFFF;fontStyle=3" parent="1" vertex="1">
      <mxGeometry x="400" y="340" width="91" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="10" value="" style="shape=mxgraph.flowchart.decision;fillColor=#FF3333;strokeColor=#CC0000;strokeWidth=2;gradientColor=#FF9999;gradientDirection=north" parent="1" vertex="1">
      <mxGeometry x="530" y="340" width="80" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="11" value="Is league too big?" style="text;spacingTop=-5;fontColor=#66FFFF;fontStyle=3" parent="1" vertex="1">
      <mxGeometry x="610" y="340" width="91" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="12" value="" style="endArrow=block;strokeColor=#FFFFFF;strokeWidth=3" parent="1" source="2" target="5" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="13" value="" style="endArrow=block;strokeColor=#FFFFFF;strokeWidth=3" parent="1" source="5" target="3" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="14" value="" style="endArrow=block;strokeColor=#FFFFFF;strokeWidth=3" parent="1" source="3" target="4" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="15" value="" style="endArrow=block;entryX=0.095;entryY=0.5;entryPerimeter=0;strokeColor=#FFFFFF;strokeWidth=3" parent="1" source="4" target="7" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="16" value="" style="endArrow=block;exitX=0.905;exitY=0.5;exitPerimeter=0;strokeColor=#FFFFFF;strokeWidth=3" parent="1" source="7" target="8" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="18" value="" style="endArrow=block;strokeColor=#FFFFFF;strokeWidth=3" parent="1" source="8" target="10" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="20" value="" style="shape=mxgraph.flowchart.merge_or_storage;fillColor=#808080;strokeColor=#FFFFFF;strokeWidth=2" parent="1" vertex="1">
      <mxGeometry x="420" y="500.5" width="95" height="61" as="geometry"/>
    </mxCell>
    <mxCell id="21" value="" style="edgeStyle=orthogonalEdgeStyle;entryX=1;entryY=0.5;entryPerimeter=0;strokeColor=#FFFFFF;strokeWidth=3;endArrow=block" parent="1" source="8" target="5" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="280" y="270" as="sourcePoint"/>
        <mxPoint x="380" y="170" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="360" y="200"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="23" value="split league" style="shape=mxgraph.flowchart.process;fillColor=#003366;strokeColor=#003366;strokeWidth=2;whiteSpace=wrap;gradientColor=#99CCFF;gradientDirection=north;fontColor=#FFFFFF;fontStyle=1;fontFamily=Tahoma" parent="1" vertex="1">
      <mxGeometry x="730" y="350" width="130" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="24" value="" style="edgeStyle=orthogonalEdgeStyle;entryX=1;entryY=0.5;entryPerimeter=0;exitX=0.5;exitY=0;exitPerimeter=0;strokeColor=#FFFFFF;strokeWidth=3;endArrow=block" parent="1" source="23" target="5" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="762.5" y="325" as="sourcePoint"/>
        <mxPoint x="540" y="185" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="795" y="200"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="25" value="" style="endArrow=block;strokeColor=#FFFFFF;strokeWidth=3" parent="1" source="10" target="23" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="26" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.5;exitY=1;exitPerimeter=0;strokeColor=#FFFFFF;strokeWidth=3;endArrow=block" parent="1" source="10" target="20" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="160" y="620" as="sourcePoint"/>
        <mxPoint x="260" y="520" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="27" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;strokeColor=#FFFFFF;strokeWidth=3;endArrow=block" parent="1" source="8" target="20" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="170" y="630" as="sourcePoint"/>
        <mxPoint x="270" y="530" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="28" value="add user to the lobby" style="shape=mxgraph.flowchart.process;fillColor=#003366;strokeColor=#003366;strokeWidth=2;whiteSpace=wrap;gradientColor=#99CCFF;gradientDirection=north;fontColor=#FFFFFF;fontStyle=1;fontFamily=Tahoma" parent="1" vertex="1">
      <mxGeometry x="402.5" y="590" width="130" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="29" value="" style="endArrow=block;strokeColor=#FFFFFF;strokeWidth=3" parent="1" source="20" target="28" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="30" value="Yes" style="text;spacingTop=-5;fontColor=#66FFFF;fontStyle=3" parent="1" vertex="1">
      <mxGeometry x="402.5" y="360" width="67.5" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="31" value="Yes" style="text;spacingTop=-5;fontColor=#66FFFF;fontStyle=3" parent="1" vertex="1">
      <mxGeometry x="610" y="360" width="67.5" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="32" value="No" style="text;spacingTop=-5;fontColor=#66FFFF;fontStyle=3" parent="1" vertex="1">
      <mxGeometry x="368.75" y="420" width="67.5" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="33" value="No" style="text;spacingTop=-5;fontColor=#66FFFF;fontStyle=3" parent="1" vertex="1">
      <mxGeometry x="580" y="420" width="67.5" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="34" value="race" style="shape=mxgraph.flowchart.process;fillColor=#003366;strokeColor=#003366;strokeWidth=2;whiteSpace=wrap;gradientColor=#99CCFF;gradientDirection=north;fontColor=#FFFFFF;fontStyle=1;fontFamily=Tahoma" parent="1" vertex="1">
      <mxGeometry x="405" y="700" width="130" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="35" value="race evaluation" style="shape=mxgraph.flowchart.process;fillColor=#003366;strokeColor=#003366;strokeWidth=2;whiteSpace=wrap;gradientColor=#99CCFF;gradientDirection=north;fontColor=#FFFFFF;fontStyle=1;fontFamily=Tahoma" parent="1" vertex="1">
      <mxGeometry x="405" y="810" width="130" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="36" value="display race stats" style="shape=mxgraph.flowchart.process;fillColor=#003366;strokeColor=#003366;strokeWidth=2;whiteSpace=wrap;gradientColor=#99CCFF;gradientDirection=north;fontColor=#FFFFFF;fontStyle=1;fontFamily=Tahoma" parent="1" vertex="1">
      <mxGeometry x="405" y="900" width="130" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="38" value="End" style="shape=mxgraph.flowchart.terminator;fillColor=#FF8000;strokeColor=#FF3333;strokeWidth=2;gradientColor=#FFFF33;gradientDirection=north" parent="1" vertex="1">
      <mxGeometry x="421" y="1100" width="98" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="43" value="User logged out?" style="text;spacingTop=-5;fontColor=#66FFFF;fontStyle=3" parent="1" vertex="1">
      <mxGeometry x="510" y="990" width="91" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="44" value="No" style="text;spacingTop=-5;fontColor=#66FFFF;fontStyle=3" parent="1" vertex="1">
      <mxGeometry x="510" y="1010" width="67.5" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="45" value="Yes" style="text;spacingTop=-5;fontColor=#66FFFF;fontStyle=3" parent="1" vertex="1">
      <mxGeometry x="480" y="1070" width="67.5" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="46" value="" style="endArrow=block;strokeColor=#FFFFFF;strokeWidth=3" parent="1" source="28" target="34" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="47" value="" style="endArrow=block;strokeColor=#FFFFFF;strokeWidth=3" parent="1" source="34" target="35" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="48" value="" style="endArrow=block;strokeColor=#FFFFFF;strokeWidth=3" parent="1" source="35" target="36" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="49" value="" style="endArrow=block;strokeColor=#FFFFFF;strokeWidth=3" parent="1" source="36" target="52" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="380" y="990" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="50" value="" style="endArrow=block;strokeColor=#FFFFFF;strokeWidth=3" parent="1" source="52" target="38" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="290" y="1040" as="sourcePoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="51" value="" style="edgeStyle=orthogonalEdgeStyle;strokeColor=#FFFFFF;strokeWidth=3;endArrow=block" parent="1" source="52" target="5" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="510" y="1030" as="sourcePoint"/>
        <mxPoint x="900" y="200.0000000000001" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="901" y="1030"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="52" value="" style="shape=mxgraph.flowchart.decision;fillColor=#FF3333;strokeColor=#CC0000;strokeWidth=2;gradientColor=#FF9999;gradientDirection=north" parent="1" vertex="1">
      <mxGeometry x="430" y="990" width="80" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="53" value="myRacing Massively Multiplayer Online Racing Service" style="text;spacingTop=-5;fontColor=#FFFF33;fontSize=18;fontStyle=3;fontFamily=Verdana" parent="1" vertex="1">
      <mxGeometry x="40" y="31" width="703" height="20" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
