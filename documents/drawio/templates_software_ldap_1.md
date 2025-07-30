---
title: "Ldap 1 Flowchart"
description: "A flowchart diagram showing process flow and decision points"
category: "templates/software"
type: "flowchart"
source_file: "templates/software/ldap_1_decoded.xml"
---

# Ldap 1 Flowchart

A flowchart diagram showing process flow and decision points

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="850" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="5d0233d4081636b3-5" value="LDAP&amp;nbsp;&lt;div&gt;Functional&amp;nbsp;&lt;/div&gt;&lt;div&gt;Model&lt;/div&gt;" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=none;startArrow=block;startFill=1;endArrow=block;endFill=1;strokeColor=#000000;strokeWidth=2;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" source="5d0233d4081636b3-1" target="5d0233d4081636b3-2" edge="1">
      <mxGeometry x="0.0909" y="-40" relative="1" as="geometry">
        <mxPoint as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="5d0233d4081636b3-1" value="LDAP Client" style="whiteSpace=wrap;html=1;rounded=1;shadow=0;comic=0;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="220" y="360" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="5d0233d4081636b3-7" value="DAP" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=none;startArrow=block;startFill=1;endArrow=block;endFill=1;strokeColor=#000000;strokeWidth=2;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" source="5d0233d4081636b3-2" target="5d0233d4081636b3-3" edge="1">
      <mxGeometry x="-0.1429" y="10" relative="1" as="geometry">
        <mxPoint as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="5d0233d4081636b3-8" value="Information&lt;div&gt;Model&lt;/div&gt;" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=none;startArrow=block;startFill=1;endArrow=block;endFill=1;strokeColor=#000000;strokeWidth=2;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" source="5d0233d4081636b3-2" edge="1">
      <mxGeometry y="40" relative="1" as="geometry">
        <mxPoint x="510" y="480" as="targetPoint"/>
        <mxPoint as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="5d0233d4081636b3-10" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=none;startArrow=block;startFill=1;endArrow=block;endFill=1;strokeColor=#000000;strokeWidth=2;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" source="5d0233d4081636b3-2" target="5d0233d4081636b3-9" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="620" y="410"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="5d0233d4081636b3-2" value="LDAP Server" style="whiteSpace=wrap;html=1;rounded=1;shadow=0;comic=0;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="450" y="360" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="5d0233d4081636b3-3" value="X.500&lt;div&gt;DSA&lt;/div&gt;" style="whiteSpace=wrap;html=1;rounded=1;shadow=0;comic=0;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="640" y="360" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="5d0233d4081636b3-4" value="Remote LDAP Server" style="whiteSpace=wrap;html=1;rounded=1;shadow=0;comic=0;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="640" y="240" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="5d0233d4081636b3-6" value="Referral" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=none;startArrow=block;startFill=1;endArrow=block;endFill=1;strokeColor=#000000;strokeWidth=2;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" source="5d0233d4081636b3-1" target="5d0233d4081636b3-4" edge="1">
      <mxGeometry x="0.1905" y="10" relative="1" as="geometry">
        <mxPoint x="350" y="400.0000000000001" as="sourcePoint"/>
        <mxPoint x="460" y="400.0000000000001" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="400" y="390"/>
          <mxPoint x="400" y="270"/>
        </Array>
        <mxPoint as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="5d0233d4081636b3-9" value="Back-End&lt;div&gt;Database&lt;/div&gt;" style="shape=cylinder;whiteSpace=wrap;html=1;rounded=1;shadow=0;comic=0;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" parent="1" vertex="1">
      <mxGeometry x="590" y="480" width="60" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="5d0233d4081636b3-11" value="LDIF&lt;div&gt;Import&lt;/div&gt;&lt;div&gt;Export&lt;/div&gt;" style="text;html=1;resizable=0;points=[];autosize=1;align=center;verticalAlign=top;spacingTop=-4;fontFamily=Verdana;" parent="1" vertex="1">
      <mxGeometry x="480" y="490" width="60" height="40" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
