---
title: "Entity Relationship 5 Class"
description: "A UML class diagram showing class relationships and structure"
category: "templates/software"
type: "class"
source_file: "templates/software/entity_relationship_5_decoded.xml"
tags: ["development", "software", "database", "template", "architecture", "erd", "drawio", "data"]
---

# Entity Relationship 5 Class

A UML class diagram showing class relationships and structure

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="850" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2ec13a14cca0a23-1" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="80" y="145" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-2" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="180" y="95" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-3" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="310" y="70" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-4" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="385" y="140" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-7" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERzeroToOne;endFill=1;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-5" target="2ec13a14cca0a23-1" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-8" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERmany;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-5" target="2ec13a14cca0a23-2" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-9" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERzeroToMany;endFill=1;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-5" target="2ec13a14cca0a23-3" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-10" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERmandOne;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-5" target="2ec13a14cca0a23-4" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-11" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=none;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-5" target="2ec13a14cca0a23-6" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-23" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=openThin;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-22" target="2ec13a14cca0a23-5" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-35" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=none;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-5" target="2ec13a14cca0a23-32" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-36" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=openThin;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-31" target="2ec13a14cca0a23-5" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-5" value="Object" style="whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="240" y="220" width="90" height="45" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-21" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=none;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-6" target="2ec13a14cca0a23-20" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-6" value="&lt;span&gt;Relation&lt;/span&gt;" style="rhombus;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="500" y="210" width="80" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-12" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="900" y="360" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-13" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="750" y="98" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-14" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="880" y="73" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-15" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="955" y="143" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-16" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERzeroToMany;endFill=1;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-20" target="2ec13a14cca0a23-12" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-17" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERmany;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-20" target="2ec13a14cca0a23-13" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-18" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERmany;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-20" target="2ec13a14cca0a23-14" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-19" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERzeroToOne;endFill=1;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-20" target="2ec13a14cca0a23-15" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-30" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=openThin;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-29" target="2ec13a14cca0a23-20" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-62" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=openThin;endFill=0;fontFamily=Verdana;fontSize=12;exitX=0.6;exitY=0.938;exitPerimeter=0;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-59" target="2ec13a14cca0a23-20" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-63" style="edgeStyle=none;html=1;entryX=0.89;entryY=0.631;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=openThin;endFill=0;fontFamily=Verdana;fontSize=12;entryPerimeter=0;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-20" target="2ec13a14cca0a23-59" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-20" value="&lt;span&gt;Object&lt;/span&gt;" style="whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="810" y="223" width="90" height="45" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-24" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=none;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-22" target="2ec13a14cca0a23-20" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-22" value="&lt;span&gt;Relation&lt;/span&gt;" style="rhombus;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="510" y="290" width="80" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-26" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERoneToMany;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-20" target="2ec13a14cca0a23-25" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-25" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="955" y="218" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-28" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERzeroToOne;endFill=1;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-20" target="2ec13a14cca0a23-27" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-27" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="950" y="295" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-42" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=none;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-29" target="2ec13a14cca0a23-41" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-29" value="&lt;span&gt;Relation&lt;/span&gt;" style="rhombus;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="750" y="365" width="80" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-39" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=none;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-31" target="2ec13a14cca0a23-37" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-31" value="&lt;span&gt;Relation&lt;/span&gt;" style="rhombus;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="360" y="340" width="80" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-34" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERone;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-32" target="2ec13a14cca0a23-33" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-38" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=none;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-32" target="2ec13a14cca0a23-37" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-32" value="&lt;span&gt;Relation&lt;/span&gt;" style="rhombus;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="218" y="345" width="80" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-33" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="100" y="355" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-49" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERoneToMany;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-37" target="2ec13a14cca0a23-48" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-50" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERone;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-37" target="2ec13a14cca0a23-45" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-51" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERzeroToOne;endFill=1;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-37" target="2ec13a14cca0a23-46" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-52" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERmandOne;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-37" target="2ec13a14cca0a23-47" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-37" value="&lt;span&gt;Object&lt;/span&gt;" style="whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="250" y="490" width="90" height="45" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-44" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=openThin;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-40" target="2ec13a14cca0a23-37" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-40" value="&lt;span&gt;Relation&lt;/span&gt;" style="rhombus;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="550" y="460" width="80" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-43" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=none;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-41" target="2ec13a14cca0a23-40" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-60" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=openThin;endFill=0;fontFamily=Verdana;fontSize=12;exitX=0;exitY=0;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-58" target="2ec13a14cca0a23-41" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-61" style="edgeStyle=none;html=1;entryX=0;entryY=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=openThin;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-41" target="2ec13a14cca0a23-58" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-64" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERzeroToMany;endFill=1;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-41" target="2ec13a14cca0a23-53" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-65" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERzeroToOne;endFill=1;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-41" target="2ec13a14cca0a23-54" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-66" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERone;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-41" target="2ec13a14cca0a23-56" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-67" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERone;endFill=0;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-41" target="2ec13a14cca0a23-57" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-41" value="&lt;span&gt;Object&lt;/span&gt;" style="whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="740" y="490" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-45" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="118" y="550" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-46" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="218" y="590" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-47" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="340" y="590" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-48" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="105" y="460" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-53" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="630" y="590" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-54" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="735" y="640" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-70" style="edgeStyle=none;html=1;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=ERzeroToMany;endFill=1;fontFamily=Verdana;fontSize=12;endSize=8;startSize=8;" parent="1" source="2ec13a14cca0a23-37" target="2ec13a14cca0a23-55" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-55" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="440" y="545" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-56" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="840" y="645" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-57" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="940" y="635" width="75" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-58" value="&lt;span&gt;Relation&lt;/span&gt;" style="rhombus;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="913" y="485" width="80" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="2ec13a14cca0a23-59" value="Relation" style="rhombus;whiteSpace=wrap;html=1;rounded=0;shadow=1;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="655" y="120" width="80" height="60" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
