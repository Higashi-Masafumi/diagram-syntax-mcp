---
title: "Entity Relationship 1 Class"
description: "A UML class diagram showing class relationships and structure"
category: "templates/software"
type: "class"
source_file: "templates/software/entity_relationship_1_decoded.xml"
---

# Entity Relationship 1 Class

A UML class diagram showing class relationships and structure

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="826" pageHeight="1169" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2" value="League" style="strokeWidth=2;shape=mxgraph.er.entity;fontColor=#000000;buttonStyle=rect;fillColor=#ffffff;buttonText=;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="576" y="146.21739130434776" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="4" value="Manager" style="strokeWidth=2;shape=mxgraph.er.entity;fontColor=#000000;buttonStyle=rect;fillColor=#ffffff;buttonText=;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="150" y="390" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="5" value="State" style="strokeWidth=2;shape=mxgraph.er.entity;fontColor=#000000;buttonStyle=rect;fillColor=#ffffff;buttonText=;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="130" y="141" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="6" value="Club" style="strokeWidth=2;shape=mxgraph.er.entity;fontColor=#000000;buttonStyle=rect;fillColor=#ffffff;buttonText=;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="576" y="390" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="7" value="has" style="strokeWidth=2;shape=mxgraph.er.has;buttonText=;fontSize=10;buttonStyle=rhombus;fontColor=#999999;fontStyle=0" parent="1" vertex="1">
      <mxGeometry x="601" y="281" width="70" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="8" value="has" style="strokeWidth=2;shape=mxgraph.er.has;buttonText=;fontSize=10;buttonStyle=rhombus;fontColor=#999999;fontStyle=0" parent="1" vertex="1">
      <mxGeometry x="350" y="156.21739130434776" width="70" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="9" value="has" style="strokeWidth=2;shape=mxgraph.er.has;buttonText=;fontSize=10;buttonStyle=rhombus;fontColor=#999999;fontStyle=0" parent="1" vertex="1">
      <mxGeometry x="360" y="400" width="70" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="10" value="" style="edgeStyle=none;endArrow=ERmany;endFill=1;noEdgeStyle=1" parent="1" source="8" target="5" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="30" y="370" as="sourcePoint"/>
        <mxPoint x="130" y="270" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="11" value="" style="edgeStyle=none;endArrow=none;noEdgeStyle=1" parent="1" source="8" target="2" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="556" y="211" as="sourcePoint"/>
        <mxPoint x="415" y="45.21739130434776" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="12" value="" style="edgeStyle=none;endArrow=ERmany;endFill=1;noEdgeStyle=1" parent="1" source="7" target="2" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="250" y="320" as="sourcePoint"/>
        <mxPoint x="250" y="380" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="13" value="" style="edgeStyle=none;endArrow=none;noEdgeStyle=1" parent="1" source="7" target="6" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="574.75" y="360" as="sourcePoint"/>
        <mxPoint x="545" y="279" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="14" value="" style="edgeStyle=none;endArrow=ERmany;endFill=1;noEdgeStyle=1" parent="1" source="9" target="6" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="380" y="200" as="sourcePoint"/>
        <mxPoint x="520" y="240" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="15" value="" style="edgeStyle=none;endArrow=none;noEdgeStyle=1" parent="1" source="9" target="4" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="450" y="200" as="sourcePoint"/>
        <mxPoint x="450" y="350" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="16" value="id" style="strokeWidth=2;shape=mxgraph.er.entity;fontColor=#007FFF;buttonStyle=round;fillColor=#ffffff;buttonText=;fontStyle=4" parent="1" vertex="1">
      <mxGeometry x="666" y="66.21739130434776" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="17" value="name" style="strokeWidth=2;shape=mxgraph.er.entity;fontColor=#007FFF;buttonStyle=round;fillColor=#ffffff;buttonText=;" parent="1" vertex="1">
      <mxGeometry x="526" y="36.21739130434776" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="18" value="class" style="strokeWidth=2;shape=mxgraph.er.entity;fontColor=#007FFF;buttonStyle=round;fillColor=#ffffff;buttonText=;" parent="1" vertex="1">
      <mxGeometry x="420" y="96.21739130434776" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="19" value="id" style="strokeWidth=2;shape=mxgraph.er.entity;fontColor=#007FFF;buttonStyle=round;fillColor=#ffffff;buttonText=;fontStyle=4" parent="1" vertex="1">
      <mxGeometry x="301" y="490" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="20" value="name" style="strokeWidth=2;shape=mxgraph.er.entity;fontColor=#007FFF;buttonStyle=round;fillColor=#ffffff;buttonText=;" parent="1" vertex="1">
      <mxGeometry x="10" y="470" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="21" value="salary" style="strokeWidth=2;shape=mxgraph.er.entity;fontColor=#007FFF;buttonStyle=round;fillColor=#ffffff;buttonText=;" parent="1" vertex="1">
      <mxGeometry x="180" y="510" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="22" value="id" style="strokeWidth=2;shape=mxgraph.er.entity;fontColor=#007FFF;buttonStyle=round;fillColor=#ffffff;buttonText=;fontStyle=4" parent="1" vertex="1">
      <mxGeometry x="696" y="490" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="23" value="rating" style="strokeWidth=2;shape=mxgraph.er.entity;fontColor=#007FFF;buttonStyle=round;fillColor=#ffffff;buttonText=;" parent="1" vertex="1">
      <mxGeometry x="526" y="490" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="24" value="name" style="strokeWidth=2;shape=mxgraph.er.entity;fontColor=#007FFF;buttonStyle=round;fillColor=#ffffff;buttonText=;" parent="1" vertex="1">
      <mxGeometry x="150" y="291" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="25" value="id" style="strokeWidth=2;shape=mxgraph.er.entity;fontColor=#007FFF;buttonStyle=round;fillColor=#ffffff;buttonText=;fontStyle=4" parent="1" vertex="1">
      <mxGeometry x="280" y="261" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="26" value="continent" style="strokeWidth=2;shape=mxgraph.er.entity;fontColor=#007FFF;buttonStyle=round;fillColor=#ffffff;buttonText=;" parent="1" vertex="1">
      <mxGeometry x="240" y="41" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="27" value="rating" style="strokeWidth=2;shape=mxgraph.er.entity;fontColor=#007FFF;buttonStyle=round;fillColor=#ffffff;buttonText=;" parent="1" vertex="1">
      <mxGeometry x="100" y="56.21739130434776" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="28" value="cups" style="strokeWidth=2;shape=mxgraph.er.entity;fontColor=#007FFF;buttonStyle=round;fillColor=#ffffff;buttonText=;" parent="1" vertex="1">
      <mxGeometry x="30" y="241" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="42" value="pro" style="strokeWidth=2;shape=mxgraph.er.entity;fontColor=#007FFF;buttonStyle=round;fillColor=#ffffff;buttonText=;" parent="1" vertex="1">
      <mxGeometry x="696" y="251" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="44" value="" style="edgeStyle=none;endArrow=ERzeroToMany;endFill=1;" parent="1" source="5" target="28" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="70" y="190" as="sourcePoint"/>
        <mxPoint x="100" y="110" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="46" value="" style="edgeStyle=none;endArrow=ERmandOne;" parent="1" source="5" target="24" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="170" y="250" as="sourcePoint"/>
        <mxPoint x="100" y="120" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="47" value="" style="edgeStyle=none;endArrow=ERmandOne;" parent="1" source="5" target="25" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="330" y="210" as="sourcePoint"/>
        <mxPoint x="202.1428571428571" y="211" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="48" value="" style="edgeStyle=none;endArrow=ERmandOne;" parent="1" source="5" target="26" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="314.5454545454545" y="271" as="sourcePoint"/>
        <mxPoint x="310" y="120" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="49" value="" style="edgeStyle=none;endArrow=ERmandOne;" parent="1" source="5" target="27" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="281.81818181818176" y="91" as="sourcePoint"/>
        <mxPoint x="190" y="110" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="50" value="" style="edgeStyle=none;endArrow=ERmandOne;" parent="1" source="2" target="18" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="440" y="310" as="sourcePoint"/>
        <mxPoint x="530" y="210" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="51" value="" style="edgeStyle=none;endArrow=ERmandOne;" parent="1" source="2" target="17" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="530" y="144.2896804609743" as="sourcePoint"/>
        <mxPoint x="560" y="110" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="52" value="" style="edgeStyle=none;endArrow=ERmandOne;" parent="1" source="2" target="16" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="596" y="86.21739130434776" as="sourcePoint"/>
        <mxPoint x="636" y="110" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="53" value="" style="edgeStyle=none;endArrow=ERmandOne;" parent="1" source="2" target="42" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="750" y="200" as="sourcePoint"/>
        <mxPoint x="672.6666666666667" y="156.21739130434776" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="54" value="" style="edgeStyle=none;endArrow=ERmandOne;" parent="1" source="6" target="22" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="740" y="430" as="sourcePoint"/>
        <mxPoint x="680.8165137614678" y="216.21739130434776" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="55" value="" style="edgeStyle=none;endArrow=ERmandOne;" parent="1" source="6" target="23" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="520" y="470" as="sourcePoint"/>
        <mxPoint x="731.5555555555557" y="500" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="56" value="" style="edgeStyle=none;endArrow=ERmandOne;" parent="1" source="4" target="19" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="310" y="440" as="sourcePoint"/>
        <mxPoint x="410" y="540" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="57" value="" style="edgeStyle=none;endArrow=ERmandOne;" parent="1" source="4" target="20" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="320" y="650" as="sourcePoint"/>
        <mxPoint x="90" y="400" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="58" value="" style="edgeStyle=none;endArrow=ERzeroToOne;endFill=1;" parent="1" source="4" target="21" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="30" y="640" as="sourcePoint"/>
        <mxPoint x="130" y="580" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
  </root>
</mxGraphModel>

```
