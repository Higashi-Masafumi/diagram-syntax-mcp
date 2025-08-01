---
title: "Plc Ladder Diagram"
description: "A diagram diagram template"
category: "templates/engineering"
type: "diagram"
source_file: "templates/engineering/plc_ladder_decoded.xml"
tags: ["engineering", "template", "technical", "electrical", "drawio"]
---

# Plc Ladder Diagram

A diagram diagram template

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1.5" pageWidth="826" pageHeight="1169" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="67" value="light_a" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="300" y="80" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="74" value="" parent="1" vertex="1">
      <mxGeometry x="60" y="10" width="10" height="1990" as="geometry"/>
    </mxCell>
    <mxCell id="76" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="67" target="74" edge="1">
      <mxGeometry x="50" width="100" height="100" as="geometry">
        <mxPoint x="50" y="100" as="sourcePoint"/>
        <mxPoint x="150" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="77" value="in_1" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="300" y="180" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="78" value="in_2" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="300" y="280" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="79" value="in_3" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="300" y="380" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="80" value="no_conflict" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="300" y="480" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="82" value="vehicle1_sensor" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="230" y="580" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="83" value="vehicle2_sensor" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="390" y="580" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="84" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;entryX=1;entryY=0.5;entryPerimeter=0;rounded=0;endArrow=none" parent="1" source="83" target="82" edge="1">
      <mxGeometry x="50" width="100" height="100" as="geometry">
        <mxPoint x="50" y="100" as="sourcePoint"/>
        <mxPoint x="150" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="87" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="82" target="88" edge="1">
      <mxGeometry x="150" y="220" width="100" height="100" as="geometry">
        <mxPoint x="150" y="320" as="sourcePoint"/>
        <mxPoint x="160" y="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="180" y="605"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="88" value="" style="strokeColor=none;fillColor=none" parent="1" vertex="1">
      <mxGeometry x="160" y="70" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="89" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="80" target="88" edge="1">
      <mxGeometry x="50" width="100" height="100" as="geometry">
        <mxPoint x="50" y="100" as="sourcePoint"/>
        <mxPoint x="150" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="250" y="505"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="90" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="79" target="88" edge="1">
      <mxGeometry x="50" width="100" height="100" as="geometry">
        <mxPoint x="50" y="100" as="sourcePoint"/>
        <mxPoint x="150" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="180" y="405"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="91" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="78" target="88" edge="1">
      <mxGeometry x="50" width="100" height="100" as="geometry">
        <mxPoint x="50" y="100" as="sourcePoint"/>
        <mxPoint x="150" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="180" y="305"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="92" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="77" target="88" edge="1">
      <mxGeometry x="50" width="100" height="100" as="geometry">
        <mxPoint x="50" y="100" as="sourcePoint"/>
        <mxPoint x="150" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="180" y="205"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="93" value="" parent="1" vertex="1">
      <mxGeometry x="1060" y="10" width="10" height="1990" as="geometry"/>
    </mxCell>
    <mxCell id="94" value="critical_stop" style="shape=mxgraph.electrical.plc_ladder.not_contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="660" y="80" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="95" value="enable" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="660" y="180" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="96" value="" style="strokeColor=none;fillColor=none" parent="1" vertex="1">
      <mxGeometry x="610" y="70" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="97" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="95" target="96" edge="1">
      <mxGeometry x="150" width="100" height="100" as="geometry">
        <mxPoint x="150" y="100" as="sourcePoint"/>
        <mxPoint x="250" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="630" y="205"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="98" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;entryX=1;entryY=0.5;entryPerimeter=0;rounded=0;endArrow=none" parent="1" source="94" target="67" edge="1">
      <mxGeometry x="150" width="100" height="100" as="geometry">
        <mxPoint x="150" y="100" as="sourcePoint"/>
        <mxPoint x="500" y="105" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="99" value="" style="strokeColor=none;fillColor=none" parent="1" vertex="1">
      <mxGeometry x="540" y="70" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="100" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="77" target="99" edge="1">
      <mxGeometry x="150" width="100" height="100" as="geometry">
        <mxPoint x="500" y="205" as="sourcePoint"/>
        <mxPoint x="250" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="560" y="205"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="101" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;entryX=0;entryY=0.5;entryPerimeter=0;rounded=0;endArrow=none" parent="1" source="94" target="109" edge="1">
      <mxGeometry x="50" width="100" height="100" as="geometry">
        <mxPoint x="50" y="100" as="sourcePoint"/>
        <mxPoint x="150" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="102" value="" style="strokeColor=none;fillColor=none" parent="1" vertex="1">
      <mxGeometry x="800" y="70" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="103" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="95" target="102" edge="1">
      <mxGeometry x="150" width="100" height="100" as="geometry">
        <mxPoint x="150" y="100" as="sourcePoint"/>
        <mxPoint x="250" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="820" y="205"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="104" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="78" target="99" edge="1">
      <mxGeometry x="50" width="100" height="100" as="geometry">
        <mxPoint x="50" y="100" as="sourcePoint"/>
        <mxPoint x="150" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="560" y="305"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="105" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="79" target="99" edge="1">
      <mxGeometry x="50" width="100" height="100" as="geometry">
        <mxPoint x="50" y="100" as="sourcePoint"/>
        <mxPoint x="150" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="560" y="405"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="106" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="80" target="99" edge="1">
      <mxGeometry x="50" width="100" height="100" as="geometry">
        <mxPoint x="50" y="100" as="sourcePoint"/>
        <mxPoint x="150" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="560" y="505"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="107" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="83" target="99" edge="1">
      <mxGeometry x="50" width="100" height="100" as="geometry">
        <mxPoint x="50" y="100" as="sourcePoint"/>
        <mxPoint x="150" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="560" y="605"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="108" value="1" style="text" parent="1" vertex="1">
      <mxGeometry x="10" y="92" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="109" value="ramp_1" style="shape=mxgraph.electrical.plc_ladder.output_1;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="920" y="80" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="110" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="109" target="93" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="111" value="light_b" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="300" y="690" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="112" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="111" edge="1">
      <mxGeometry x="50" y="610" width="100" height="100" as="geometry">
        <mxPoint x="50" y="710" as="sourcePoint"/>
        <mxPoint x="70" y="715" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="113" value="in_1" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="300" y="790" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="114" value="in_2" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="300" y="890" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="115" value="in_3" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="300" y="990" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="116" value="no_conflict" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="300" y="1090" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="117" value="vehicle3_sensor" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="230" y="1190" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="118" value="vehicle4_sensor" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="390" y="1190" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="119" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;entryX=1;entryY=0.5;entryPerimeter=0;rounded=0;endArrow=none" parent="1" source="118" target="117" edge="1">
      <mxGeometry x="50" y="610" width="100" height="100" as="geometry">
        <mxPoint x="50" y="710" as="sourcePoint"/>
        <mxPoint x="150" y="610" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="120" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="117" target="121" edge="1">
      <mxGeometry x="150" y="830" width="100" height="100" as="geometry">
        <mxPoint x="150" y="930" as="sourcePoint"/>
        <mxPoint x="160" y="710" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="180" y="1215"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="121" value="" style="strokeColor=none;fillColor=none" parent="1" vertex="1">
      <mxGeometry x="160" y="680" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="122" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="116" target="121" edge="1">
      <mxGeometry x="50" y="610" width="100" height="100" as="geometry">
        <mxPoint x="50" y="710" as="sourcePoint"/>
        <mxPoint x="150" y="610" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="250" y="1115"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="123" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="115" target="121" edge="1">
      <mxGeometry x="50" y="610" width="100" height="100" as="geometry">
        <mxPoint x="50" y="710" as="sourcePoint"/>
        <mxPoint x="150" y="610" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="180" y="1015"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="124" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="114" target="121" edge="1">
      <mxGeometry x="50" y="610" width="100" height="100" as="geometry">
        <mxPoint x="50" y="710" as="sourcePoint"/>
        <mxPoint x="150" y="610" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="180" y="915"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="125" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="113" target="121" edge="1">
      <mxGeometry x="50" y="610" width="100" height="100" as="geometry">
        <mxPoint x="50" y="710" as="sourcePoint"/>
        <mxPoint x="150" y="610" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="180" y="815"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="126" value="critical_stop" style="shape=mxgraph.electrical.plc_ladder.not_contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="660" y="690" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="127" value="enable" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="660" y="790" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="128" value="" style="strokeColor=none;fillColor=none" parent="1" vertex="1">
      <mxGeometry x="610" y="680" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="129" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="127" target="128" edge="1">
      <mxGeometry x="150" y="610" width="100" height="100" as="geometry">
        <mxPoint x="150" y="710" as="sourcePoint"/>
        <mxPoint x="250" y="610" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="630" y="815"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="130" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;entryX=1;entryY=0.5;entryPerimeter=0;rounded=0;endArrow=none" parent="1" source="126" target="111" edge="1">
      <mxGeometry x="150" y="610" width="100" height="100" as="geometry">
        <mxPoint x="150" y="710" as="sourcePoint"/>
        <mxPoint x="500" y="715" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="131" value="" style="strokeColor=none;fillColor=none" parent="1" vertex="1">
      <mxGeometry x="540" y="680" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="132" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="113" target="131" edge="1">
      <mxGeometry x="150" y="610" width="100" height="100" as="geometry">
        <mxPoint x="500" y="815" as="sourcePoint"/>
        <mxPoint x="250" y="610" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="560" y="815"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="133" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;entryX=0;entryY=0.5;entryPerimeter=0;rounded=0;endArrow=none" parent="1" source="126" target="141" edge="1">
      <mxGeometry x="50" y="610" width="100" height="100" as="geometry">
        <mxPoint x="50" y="710" as="sourcePoint"/>
        <mxPoint x="150" y="610" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="134" value="" style="strokeColor=none;fillColor=none" parent="1" vertex="1">
      <mxGeometry x="800" y="680" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="135" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="127" target="134" edge="1">
      <mxGeometry x="150" y="610" width="100" height="100" as="geometry">
        <mxPoint x="150" y="710" as="sourcePoint"/>
        <mxPoint x="250" y="610" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="820" y="815"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="136" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="114" target="131" edge="1">
      <mxGeometry x="50" y="610" width="100" height="100" as="geometry">
        <mxPoint x="50" y="710" as="sourcePoint"/>
        <mxPoint x="150" y="610" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="560" y="915"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="137" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="115" target="131" edge="1">
      <mxGeometry x="50" y="610" width="100" height="100" as="geometry">
        <mxPoint x="50" y="710" as="sourcePoint"/>
        <mxPoint x="150" y="610" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="560" y="1015"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="138" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="116" target="131" edge="1">
      <mxGeometry x="50" y="610" width="100" height="100" as="geometry">
        <mxPoint x="50" y="710" as="sourcePoint"/>
        <mxPoint x="150" y="610" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="560" y="1115"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="139" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="118" target="131" edge="1">
      <mxGeometry x="50" y="610" width="100" height="100" as="geometry">
        <mxPoint x="50" y="710" as="sourcePoint"/>
        <mxPoint x="150" y="610" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="560" y="1215"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="140" value="2" style="text" parent="1" vertex="1">
      <mxGeometry x="10" y="702" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="141" value="ramp_2" style="shape=mxgraph.electrical.plc_ladder.output_1;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="920" y="690" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="142" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="141" edge="1">
      <mxGeometry y="610" width="100" height="100" as="geometry">
        <mxPoint y="710" as="sourcePoint"/>
        <mxPoint x="1060" y="715" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="145" value="critical_stop" style="shape=mxgraph.electrical.plc_ladder.not_contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="200" y="1320" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="146" value="alarm_light" style="shape=mxgraph.electrical.plc_ladder.output_1;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="920" y="1320" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="147" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="146" target="93" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="148" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="145" target="74" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="149" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;entryX=0;entryY=0.5;entryPerimeter=0;rounded=0;endArrow=none" parent="1" source="145" target="146" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="150" value="vehicle1_sensor" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="200" y="1460" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="152" value="vehicle2_sensor" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="200" y="1560" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="153" value="vehicle3_sensor" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="200" y="1660" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="154" value="vehicle4_sensor" style="shape=mxgraph.electrical.plc_ladder.contact;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="200" y="1760" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="155" value="passage_light" style="shape=mxgraph.electrical.plc_ladder.output_1;fillColor=white;strokeColor=black;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="920" y="1460" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="156" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="155" target="93" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="157" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="150" target="155" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="158" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="150" target="74" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="159" value="" style="strokeColor=none;fillColor=none" parent="1" vertex="1">
      <mxGeometry x="135" y="1450" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="160" value="" style="strokeColor=none;fillColor=none" parent="1" vertex="1">
      <mxGeometry x="540" y="1450" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="161" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="152" target="159" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="155" y="1585"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="162" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="153" target="159" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="155" y="1685"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="163" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="154" target="159" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="155" y="1785"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="164" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="152" target="160" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="430" y="1585"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="165" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="153" target="160" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="430" y="1685"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="166" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;rounded=0;endArrow=none" parent="1" source="154" target="160" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="420" y="1785"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="167" value="3" style="text" parent="1" vertex="1">
      <mxGeometry x="10" y="1332" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="168" value="4" style="text" parent="1" vertex="1">
      <mxGeometry x="10" y="1472" width="40" height="26" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
