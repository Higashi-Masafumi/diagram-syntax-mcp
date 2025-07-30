---
title: "Lean Mapping 3 Diagram"
description: "A diagram diagram template"
category: "templates/business"
type: "diagram"
source_file: "templates/business/lean_mapping_3_decoded.xml"
---

# Lean Mapping 3 Diagram

A diagram diagram template

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="850" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="62062f0c37465949-1" value="&lt;div&gt;Production planning&lt;/div&gt;" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.manufacturing_process;fontSize=12;verticalAlign=middle;html=1;align=center;whiteSpace=wrap;rounded=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="878" y="45" width="130" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="62062f0c37465949-2" value="Sales &amp;amp; Ops. Planning" style="text;fontSize=12;spacingLeft=2;verticalAlign=top;html=1;align=center;spacingTop=-5;resizeWidth=1;fillColor=#ffffff;fontColor=#000000;strokeColor=#000000;strokeWidth=2;" parent="62062f0c37465949-1" vertex="1">
      <mxGeometry width="130" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="62062f0c37465949-3" value="Suppliers" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.outside_sources;whiteSpace=wrap;align=center;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;strokeColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="103" y="110" width="100" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="62062f0c37465949-4" value="Customers" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.outside_sources;whiteSpace=wrap;align=center;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;strokeColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1649" y="112" width="100" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="62062f0c37465949-5" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.manufacturing_process;fontSize=12;verticalAlign=middle;html=1;align=center;whiteSpace=wrap;rounded=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="453" y="365" width="110" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="62062f0c37465949-6" value="Pole Form" style="text;fontSize=12;spacingLeft=2;verticalAlign=top;html=1;align=center;spacingTop=-5;resizeWidth=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;strokeWidth=2;" parent="62062f0c37465949-5" vertex="1">
      <mxGeometry width="110.00000000000001" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-52" value="2" style="verticalLabelPosition=middle;html=1;verticalAlign=middle;strokeWidth=2;shape=mxgraph.lean_mapping.operator;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=right;strokeColor=#000000;labelPosition=left;" parent="62062f0c37465949-5" vertex="1">
      <mxGeometry x="43" y="30" width="25" height="21" as="geometry"/>
    </mxCell>
    <mxCell id="62062f0c37465949-22" value="" style="html=1;shadow=0;dashed=0;align=center;verticalAlign=middle;shape=mxgraph.arrows2.arrow;dy=0.6;dx=33.71;direction=south;notch=0;rounded=1;strokeColor=#000000;strokeWidth=2;fillColor=#ffffff;fontFamily=Verdana;fontSize=14;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="141" y="190" width="30" height="160" as="geometry"/>
    </mxCell>
    <mxCell id="62062f0c37465949-26" value="1 / week" style="shape=mxgraph.signs.transportation.truck_1;html=1;fillColor=#ffffff;strokeColor=#000000;verticalLabelPosition=bottom;verticalAlign=top;align=center;rounded=1;fontFamily=Verdana;fontSize=8;fontColor=#000000;flipH=1;labelPosition=center;spacing=0;spacingTop=-2;" parent="1" vertex="1">
      <mxGeometry x="82" y="240" width="59" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="62062f0c37465949-30" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.inventory_box;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=14;fontColor=#000000;align=center;strokeColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="101" y="289" width="34" height="31" as="geometry"/>
    </mxCell>
    <mxCell id="62062f0c37465949-31" value="Monthly" style="shape=mxgraph.lean_mapping.electronic_info_flow_edge;html=1;startSize=5;endSize=5;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Verdana;fontSize=14;fontColor=#000000;fillColor=#ffffff;" parent="1" source="62062f0c37465949-1" target="62062f0c37465949-3" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="553" y="140" as="sourcePoint"/>
        <mxPoint x="263" y="160" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="62062f0c37465949-32" value="Weekly" style="shape=mxgraph.lean_mapping.electronic_info_flow_edge;html=1;startSize=5;endSize=5;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Verdana;fontSize=14;fontColor=#000000;fillColor=#ffffff;" parent="1" source="62062f0c37465949-4" target="62062f0c37465949-1" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="1013" y="130" as="sourcePoint"/>
        <mxPoint x="713" y="140" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="62062f0c37465949-33" value="Daily" style="shape=mxgraph.lean_mapping.manual_info_flow_edge;html=1;startSize=5;endSize=5;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Verdana;fontSize=14;fontColor=#000000;fillColor=#ffffff;" parent="1" source="62062f0c37465949-1" target="504260f35e674a68-26" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="373" y="330" as="sourcePoint"/>
        <mxPoint x="473" y="230" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="62062f0c37465949-34" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.timeline2;dx1=0;dy1=0;dx2=110.125;dy2=0.866;dx3=316.792;dy3=0;dx4=458.458;dy4=1;dx5=550.958;dy5=0;dy6=1;rounded=1;fillColor=none;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="103" y="590" width="660" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-4" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.push_arrow;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="221" y="390.00000000000006" width="222" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-6" value="" style="html=1;shadow=0;dashed=0;align=center;verticalAlign=middle;shape=mxgraph.arrows2.arrow;dy=0.6;dx=33.71;direction=south;notch=0;rounded=1;strokeColor=#000000;strokeWidth=2;fillColor=#ffffff;fontFamily=Verdana;fontSize=14;fontColor=#000000;rotation=-180;" parent="1" vertex="1">
      <mxGeometry x="1684" y="192" width="30" height="160" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-7" value="3 / week" style="shape=mxgraph.signs.transportation.truck_1;html=1;fillColor=#ffffff;strokeColor=#000000;verticalLabelPosition=bottom;verticalAlign=top;align=center;rounded=1;fontFamily=Verdana;fontSize=8;fontColor=#000000;flipH=1;labelPosition=center;spacing=0;spacingTop=-2;" parent="1" vertex="1">
      <mxGeometry x="1714" y="262" width="59" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-16" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.data_box;html=1;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="126" y="445" width="60" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-17" value="C/T= 30 s" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="283523e09561b2f7-16" vertex="1">
      <mxGeometry width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-18" value="C/O= 5 s" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="283523e09561b2f7-16" vertex="1">
      <mxGeometry y="20" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-19" value="Batch= 10" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="283523e09561b2f7-16" vertex="1">
      <mxGeometry y="40" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-20" value="Avail= 80%" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="283523e09561b2f7-16" vertex="1">
      <mxGeometry y="60" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-21" value="" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="283523e09561b2f7-16" vertex="1">
      <mxGeometry y="80" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-40" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.timeline2;dx1=0;dy1=0.991;dx2=91.792;dy2=0;dx3=200.125;dy3=1;dx4=291.792;dy4=0;dx5=400.125;dy5=0.928;dy6=0;rounded=1;fillColor=none;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="763" y="590" width="490" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-42" value="5" style="text;html=1;resizable=0;points=[];autosize=1;align=center;verticalAlign=top;spacingTop=-4;fontSize=12;fontFamily=Verdana;fontColor=#000000;fillColor=none;strokeColor=none;labelBackgroundColor=none;" parent="1" vertex="1">
      <mxGeometry x="146" y="570" width="20" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-43" value="30240" style="text;html=1;resizable=0;points=[];autosize=1;align=center;verticalAlign=top;spacingTop=-4;fontSize=12;fontFamily=Verdana;fontColor=#000000;fillColor=none;strokeColor=none;labelBackgroundColor=none;" parent="1" vertex="1">
      <mxGeometry x="289" y="610" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-45" value="70" style="text;html=1;resizable=0;points=[];autosize=1;align=center;verticalAlign=top;spacingTop=-4;fontSize=12;fontFamily=Verdana;fontColor=#000000;fillColor=none;strokeColor=none;labelBackgroundColor=none;" parent="1" vertex="1">
      <mxGeometry x="488" y="570" width="30" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-46" value="180" style="text;html=1;resizable=0;points=[];autosize=1;align=center;verticalAlign=top;spacingTop=-4;fontSize=12;fontFamily=Verdana;fontColor=#000000;fillColor=none;strokeColor=none;labelBackgroundColor=none;" parent="1" vertex="1">
      <mxGeometry x="588" y="610" width="40" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-47" value="90" style="text;html=1;resizable=0;points=[];autosize=1;align=center;verticalAlign=top;spacingTop=-4;fontSize=12;fontFamily=Verdana;fontColor=#000000;fillColor=none;strokeColor=none;labelBackgroundColor=none;" parent="1" vertex="1">
      <mxGeometry x="693" y="570" width="30" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-48" value="0" style="text;html=1;resizable=0;points=[];autosize=1;align=center;verticalAlign=top;spacingTop=-4;fontSize=12;fontFamily=Verdana;fontColor=#000000;fillColor=none;strokeColor=none;labelBackgroundColor=none;" parent="1" vertex="1">
      <mxGeometry x="798" y="610" width="20" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-49" value="0" style="text;html=1;resizable=0;points=[];autosize=1;align=center;verticalAlign=top;spacingTop=-4;fontSize=12;fontFamily=Verdana;fontColor=#000000;fillColor=none;strokeColor=none;labelBackgroundColor=none;" parent="1" vertex="1">
      <mxGeometry x="899" y="570" width="20" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-50" value="180" style="text;html=1;resizable=0;points=[];autosize=1;align=center;verticalAlign=top;spacingTop=-4;fontSize=12;fontFamily=Verdana;fontColor=#000000;fillColor=none;strokeColor=none;labelBackgroundColor=none;" parent="1" vertex="1">
      <mxGeometry x="988" y="610" width="40" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="283523e09561b2f7-51" value="240" style="text;html=1;resizable=0;points=[];autosize=1;align=center;verticalAlign=top;spacingTop=-4;fontSize=12;fontFamily=Verdana;fontColor=#000000;fillColor=none;strokeColor=none;labelBackgroundColor=none;" parent="1" vertex="1">
      <mxGeometry x="1088" y="570" width="40" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-1" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.manufacturing_process;fontSize=12;verticalAlign=middle;html=1;align=center;whiteSpace=wrap;rounded=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="101" y="365" width="110" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-2" value="Cut Splits" style="text;fontSize=12;spacingLeft=2;verticalAlign=top;html=1;align=center;spacingTop=-5;resizeWidth=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;strokeWidth=2;" parent="504260f35e674a68-1" vertex="1">
      <mxGeometry width="110.00000000000001" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-3" value="2" style="verticalLabelPosition=middle;html=1;verticalAlign=middle;strokeWidth=2;shape=mxgraph.lean_mapping.operator;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=right;strokeColor=#000000;labelPosition=left;" parent="504260f35e674a68-1" vertex="1">
      <mxGeometry x="43" y="30" width="25" height="21" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-4" value="" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;rounded=1;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="77" y="288" width="24" height="16" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-6" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.manufacturing_process;fontSize=12;verticalAlign=middle;html=1;align=center;whiteSpace=wrap;rounded=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="258" y="235" width="110" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-7" value="CE Press" style="text;fontSize=12;spacingLeft=2;verticalAlign=top;html=1;align=center;spacingTop=-5;resizeWidth=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;strokeWidth=2;" parent="504260f35e674a68-6" vertex="1">
      <mxGeometry width="110.00000000000001" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-8" value="3" style="verticalLabelPosition=middle;html=1;verticalAlign=middle;strokeWidth=2;shape=mxgraph.lean_mapping.operator;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=right;strokeColor=#000000;labelPosition=left;" parent="504260f35e674a68-6" vertex="1">
      <mxGeometry x="43" y="30" width="25" height="21" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-9" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.manufacturing_process;fontSize=12;verticalAlign=middle;html=1;align=center;whiteSpace=wrap;rounded=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="453" y="233" width="110" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-10" value="GO Punch" style="text;fontSize=12;spacingLeft=2;verticalAlign=top;html=1;align=center;spacingTop=-5;resizeWidth=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;strokeWidth=2;" parent="504260f35e674a68-9" vertex="1">
      <mxGeometry width="110.00000000000001" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-11" value="2" style="verticalLabelPosition=middle;html=1;verticalAlign=middle;strokeWidth=2;shape=mxgraph.lean_mapping.operator;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=right;strokeColor=#000000;labelPosition=left;" parent="504260f35e674a68-9" vertex="1">
      <mxGeometry x="43" y="30" width="25" height="21" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-12" value="Daily" style="shape=mxgraph.lean_mapping.manual_info_flow_edge;html=1;startSize=5;endSize=5;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Verdana;fontSize=14;fontColor=#000000;fillColor=#ffffff;" parent="1" source="62062f0c37465949-1" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="622.2679028132993" y="145" as="sourcePoint"/>
        <mxPoint x="243" y="210" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="504260f35e674a68-13" value="Daily" style="shape=mxgraph.lean_mapping.manual_info_flow_edge;html=1;startSize=5;endSize=5;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Verdana;fontSize=14;fontColor=#000000;fillColor=#ffffff;" parent="1" target="504260f35e674a68-1" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="253" y="200" as="sourcePoint"/>
        <mxPoint x="273" y="210" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="504260f35e674a68-14" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.push_arrow;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;rotation=-40;" parent="1" vertex="1">
      <mxGeometry x="213" y="335" width="89" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-15" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.push_arrow;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;rotation=-20;" parent="1" vertex="1">
      <mxGeometry x="254" y="332" width="188" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-16" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.push_arrow;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;rotation=0;" parent="1" vertex="1">
      <mxGeometry x="373" y="258" width="70" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-17" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.push_arrow;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;rotation=90;" parent="1" vertex="1">
      <mxGeometry x="486" y="321" width="45" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-18" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.inventory_box;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=14;fontColor=#000000;align=center;strokeColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="296" y="414" width="34" height="31" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-19" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.data_box;html=1;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="478" y="445" width="60" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-20" value="C/T= 80 s" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-19" vertex="1">
      <mxGeometry width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-21" value="C/O= 70 s" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-19" vertex="1">
      <mxGeometry y="20" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-22" value="Batch= 10" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-19" vertex="1">
      <mxGeometry y="40" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-23" value="Avail= 80%" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-19" vertex="1">
      <mxGeometry y="60" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-24" value="" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-19" vertex="1">
      <mxGeometry y="80" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-25" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.push_arrow;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;rotation=0;" parent="1" vertex="1">
      <mxGeometry x="573" y="390.00000000000006" width="70" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-26" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.manufacturing_process;fontSize=12;verticalAlign=middle;html=1;align=center;whiteSpace=wrap;rounded=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="653" y="364.9999999999999" width="110" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-27" value="Single Seam Weld" style="text;fontSize=12;spacingLeft=2;verticalAlign=top;html=1;align=center;spacingTop=-5;resizeWidth=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;strokeWidth=2;" parent="504260f35e674a68-26" vertex="1">
      <mxGeometry width="110.00000000000001" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-28" value="4" style="verticalLabelPosition=middle;html=1;verticalAlign=middle;strokeWidth=2;shape=mxgraph.lean_mapping.operator;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=right;strokeColor=#000000;labelPosition=left;" parent="504260f35e674a68-26" vertex="1">
      <mxGeometry x="43" y="30" width="25" height="21" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-29" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.push_arrow;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;rotation=0;" parent="1" vertex="1">
      <mxGeometry x="773" y="389.99999999999983" width="70" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-30" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.manufacturing_process;fontSize=12;verticalAlign=middle;html=1;align=center;whiteSpace=wrap;rounded=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="853" y="365" width="110" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-31" value="Weld Repair" style="text;fontSize=12;spacingLeft=2;verticalAlign=top;html=1;align=center;spacingTop=-5;resizeWidth=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;strokeWidth=2;" parent="504260f35e674a68-30" vertex="1">
      <mxGeometry width="110.00000000000001" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-32" value="2" style="verticalLabelPosition=middle;html=1;verticalAlign=middle;strokeWidth=2;shape=mxgraph.lean_mapping.operator;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=right;strokeColor=#000000;labelPosition=left;" parent="504260f35e674a68-30" vertex="1">
      <mxGeometry x="43" y="30" width="25" height="21" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-33" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.push_arrow;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;rotation=0;" parent="1" vertex="1">
      <mxGeometry x="973" y="390" width="70" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-34" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.manufacturing_process;fontSize=12;verticalAlign=middle;html=1;align=center;whiteSpace=wrap;rounded=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1053" y="365" width="110" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-35" value="GO Finishing" style="text;fontSize=12;spacingLeft=2;verticalAlign=top;html=1;align=center;spacingTop=-5;resizeWidth=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;strokeWidth=2;" parent="504260f35e674a68-34" vertex="1">
      <mxGeometry width="110.00000000000001" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-36" value="3" style="verticalLabelPosition=middle;html=1;verticalAlign=middle;strokeWidth=2;shape=mxgraph.lean_mapping.operator;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=right;strokeColor=#000000;labelPosition=left;" parent="504260f35e674a68-34" vertex="1">
      <mxGeometry x="43" y="30" width="25" height="21" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-37" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.push_arrow;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;rotation=0;" parent="1" vertex="1">
      <mxGeometry x="1173" y="390" width="70" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-38" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.manufacturing_process;fontSize=12;verticalAlign=middle;html=1;align=center;whiteSpace=wrap;rounded=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1253" y="365" width="110" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-39" value="Base Weld" style="text;fontSize=12;spacingLeft=2;verticalAlign=top;html=1;align=center;spacingTop=-5;resizeWidth=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;strokeWidth=2;" parent="504260f35e674a68-38" vertex="1">
      <mxGeometry width="110.00000000000001" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-40" value="4" style="verticalLabelPosition=middle;html=1;verticalAlign=middle;strokeWidth=2;shape=mxgraph.lean_mapping.operator;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=right;strokeColor=#000000;labelPosition=left;" parent="504260f35e674a68-38" vertex="1">
      <mxGeometry x="43" y="30" width="25" height="21" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-41" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.push_arrow;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;rotation=0;" parent="1" vertex="1">
      <mxGeometry x="1369" y="390.00000000000006" width="70" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-42" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.manufacturing_process;fontSize=12;verticalAlign=middle;html=1;align=center;whiteSpace=wrap;rounded=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1449" y="365" width="110" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-43" value="Galv Out" style="text;fontSize=12;spacingLeft=2;verticalAlign=top;html=1;align=center;spacingTop=-5;resizeWidth=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;strokeWidth=2;" parent="504260f35e674a68-42" vertex="1">
      <mxGeometry width="110.00000000000001" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-44" value="2" style="verticalLabelPosition=middle;html=1;verticalAlign=middle;strokeWidth=2;shape=mxgraph.lean_mapping.operator;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=right;strokeColor=#000000;labelPosition=left;" parent="504260f35e674a68-42" vertex="1">
      <mxGeometry x="43" y="30" width="25" height="21" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-45" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.push_arrow;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;rotation=0;" parent="1" vertex="1">
      <mxGeometry x="1563" y="390" width="70" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-46" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.manufacturing_process;fontSize=12;verticalAlign=middle;html=1;align=center;whiteSpace=wrap;rounded=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1643" y="365" width="110" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-47" value="Galv In" style="text;fontSize=12;spacingLeft=2;verticalAlign=top;html=1;align=center;spacingTop=-5;resizeWidth=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;strokeWidth=2;" parent="504260f35e674a68-46" vertex="1">
      <mxGeometry width="110.00000000000001" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-48" value="3" style="verticalLabelPosition=middle;html=1;verticalAlign=middle;strokeWidth=2;shape=mxgraph.lean_mapping.operator;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=right;strokeColor=#000000;labelPosition=left;" parent="504260f35e674a68-46" vertex="1">
      <mxGeometry x="43" y="30" width="25" height="21" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-49" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.manufacturing_process;fontSize=12;verticalAlign=middle;html=1;align=center;whiteSpace=wrap;rounded=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1253" y="230" width="110" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-50" value="Base Weld" style="text;fontSize=12;spacingLeft=2;verticalAlign=top;html=1;align=center;spacingTop=-5;resizeWidth=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-49" vertex="1">
      <mxGeometry width="110.00000000000001" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-51" value="2" style="verticalLabelPosition=middle;html=1;verticalAlign=middle;strokeWidth=2;shape=mxgraph.lean_mapping.operator;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=right;strokeColor=#000000;labelPosition=left;" parent="504260f35e674a68-49" vertex="1">
      <mxGeometry x="43" y="30" width="25" height="21" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-52" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.push_arrow;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;rotation=90;" parent="1" vertex="1">
      <mxGeometry x="1285" y="322" width="45" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-53" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.push_arrow;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;rotation=-35;" parent="1" vertex="1">
      <mxGeometry x="1121" y="304" width="119" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-54" value="Daily" style="shape=mxgraph.lean_mapping.manual_info_flow_edge;html=1;startSize=5;endSize=5;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Verdana;fontSize=14;fontColor=#000000;fillColor=#ffffff;" parent="1" source="62062f0c37465949-1" target="504260f35e674a68-34" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="927.135220125786" y="125" as="sourcePoint"/>
        <mxPoint x="743.8647798742136" y="372.9999999999998" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="504260f35e674a68-55" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.inventory_box;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=14;fontColor=#000000;align=center;strokeColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="591" y="418" width="34" height="31" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-57" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=2;shape=mxgraph.lean_mapping.timeline2;dx1=0;dy1=0;dx2=107.357;dy2=1;dx3=197.286;dy3=0;dx4=305.286;dy4=0.868;dx5=391.571;dy5=0;dy6=0;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1254" y="590" width="499" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-62" value="2" style="text;html=1;resizable=0;points=[];autosize=1;align=center;verticalAlign=top;spacingTop=-4;fontSize=12;fontFamily=Verdana;fontColor=#000000;strokeColor=none;labelBackgroundColor=none;" parent="1" vertex="1">
      <mxGeometry x="1688" y="570" width="20" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-63" value="10080" style="text;html=1;resizable=0;points=[];autosize=1;align=center;verticalAlign=top;spacingTop=-4;fontSize=12;fontFamily=Verdana;fontColor=#000000;fillColor=none;strokeColor=none;labelBackgroundColor=none;" parent="1" vertex="1">
      <mxGeometry x="1568" y="610" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-64" value="180" style="text;html=1;resizable=0;points=[];autosize=1;align=center;verticalAlign=top;spacingTop=-4;fontSize=12;fontFamily=Verdana;fontColor=#000000;fillColor=none;strokeColor=none;labelBackgroundColor=none;" parent="1" vertex="1">
      <mxGeometry x="1188" y="610" width="40" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-65" value="240" style="text;html=1;resizable=0;points=[];autosize=1;align=center;verticalAlign=top;spacingTop=-4;fontSize=12;fontFamily=Verdana;fontColor=#000000;fillColor=none;strokeColor=none;labelBackgroundColor=none;" parent="1" vertex="1">
      <mxGeometry x="1384" y="610" width="40" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-66" value="0" style="text;html=1;resizable=0;points=[];autosize=1;align=center;verticalAlign=top;spacingTop=-4;fontSize=12;fontFamily=Verdana;fontColor=#000000;fillColor=none;strokeColor=none;labelBackgroundColor=none;" parent="1" vertex="1">
      <mxGeometry x="1497" y="570" width="20" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-67" value="600" style="text;html=1;resizable=0;points=[];autosize=1;align=center;verticalAlign=top;spacingTop=-4;fontSize=12;fontFamily=Verdana;fontColor=#000000;fillColor=none;strokeColor=none;labelBackgroundColor=none;" parent="1" vertex="1">
      <mxGeometry x="1288" y="570" width="40" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-70" value="" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=2;fontFamily=Verdana;fontSize=12;fontColor=#000000;verticalAlign=top;fillColor=#ffffff;labelBackgroundColor=none;" parent="1" edge="1">
      <mxGeometry width="50" height="50" relative="1" as="geometry">
        <mxPoint x="30" y="629" as="sourcePoint"/>
        <mxPoint x="102.99999999999977" y="629" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="504260f35e674a68-71" value="" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=2;fontFamily=Verdana;fontSize=12;fontColor=#000000;verticalAlign=top;fillColor=#ffffff;entryX=0.001;entryY=0.03;entryPerimeter=0;labelBackgroundColor=none;" parent="1" target="62062f0c37465949-34" edge="1">
      <mxGeometry width="50" height="50" relative="1" as="geometry">
        <mxPoint x="104" y="630" as="sourcePoint"/>
        <mxPoint x="112.99999999999977" y="639" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="504260f35e674a68-72" value="20160" style="text;html=1;resizable=0;points=[];autosize=1;align=center;verticalAlign=top;spacingTop=-4;fontSize=12;fontFamily=Verdana;fontColor=#000000;fillColor=none;strokeColor=none;labelBackgroundColor=none;" parent="1" vertex="1">
      <mxGeometry x="40" y="610" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-73" value="" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;rounded=1;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="390" y="359" width="24" height="16" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-74" value="" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;rounded=1;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="433" y="517" width="24" height="16" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-75" value="" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;rounded=1;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="596" y="337" width="24" height="16" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-76" value="" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;rounded=1;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="1390.5714285714284" y="329" width="24" height="16" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-79" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.data_box;html=1;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="678" y="445" width="60" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-80" value="C/T= 90 s" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-79" vertex="1">
      <mxGeometry width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-81" value="C/O= 90 s" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-79" vertex="1">
      <mxGeometry y="20" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-82" value="Batch= 10" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-79" vertex="1">
      <mxGeometry y="40" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-83" value="Avail= 80%" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-79" vertex="1">
      <mxGeometry y="60" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-84" value="" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-79" vertex="1">
      <mxGeometry y="80" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-85" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.data_box;html=1;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="879" y="445" width="60" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-86" value="C/T= 2 min" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-85" vertex="1">
      <mxGeometry width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-87" value="C/O= 0" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-85" vertex="1">
      <mxGeometry y="20" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-88" value="Batch= 10" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-85" vertex="1">
      <mxGeometry y="40" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-89" value="Avail= 80%" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-85" vertex="1">
      <mxGeometry y="60" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-90" value="" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-85" vertex="1">
      <mxGeometry y="80" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-91" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.data_box;html=1;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1078" y="445" width="60" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-92" value="C/T= 4 min" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-91" vertex="1">
      <mxGeometry width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-93" value="C/O= 4 min" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-91" vertex="1">
      <mxGeometry y="20" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-94" value="Batch= 10" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-91" vertex="1">
      <mxGeometry y="40" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-95" value="Avail= 80%" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-91" vertex="1">
      <mxGeometry y="60" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-96" value="" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-91" vertex="1">
      <mxGeometry y="80" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-97" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.data_box;html=1;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1278" y="445" width="60" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-98" value="C/T= 10 min" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-97" vertex="1">
      <mxGeometry width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-99" value="C/O= 10 min" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-97" vertex="1">
      <mxGeometry y="20" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-100" value="Batch= 10" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-97" vertex="1">
      <mxGeometry y="40" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-101" value="Avail= 80%" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-97" vertex="1">
      <mxGeometry y="60" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-102" value="" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-97" vertex="1">
      <mxGeometry y="80" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-103" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.data_box;html=1;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1475" y="445" width="60" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-104" value="C/T= 0" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-103" vertex="1">
      <mxGeometry width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-105" value="C/O= 0" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-103" vertex="1">
      <mxGeometry y="20" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-106" value="Batch= 10" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-103" vertex="1">
      <mxGeometry y="40" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-107" value="Avail= 80%" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-103" vertex="1">
      <mxGeometry y="60" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-108" value="" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-103" vertex="1">
      <mxGeometry y="80" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-109" value="" style="strokeWidth=2;html=1;shape=mxgraph.lean_mapping.data_box;html=1;rounded=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;align=center;strokeColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1668" y="445" width="60" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-110" value="C/T= 30 min" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-109" vertex="1">
      <mxGeometry width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-111" value="C/O= 2 min" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-109" vertex="1">
      <mxGeometry y="20" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-112" value="Batch= 10" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-109" vertex="1">
      <mxGeometry y="40" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-113" value="Avail= 80%" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-109" vertex="1">
      <mxGeometry y="60" width="60" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="504260f35e674a68-114" value="" style="text;fontSize=8;spacingLeft=2;verticalAlign=middle;html=1;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" parent="504260f35e674a68-109" vertex="1">
      <mxGeometry y="80" width="60" height="20" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
