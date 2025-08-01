---
title: "Ibm Vcenter Server Platform Flowchart"
description: "A flowchart diagram showing process flow and decision points"
category: "templates/cloud"
type: "flowchart"
source_file: "templates/cloud/ibm_vcenter_server_platform_decoded.xml"
tags: ["cloud", "template", "architecture", "drawio", "infrastructure"]
---

# Ibm Vcenter Server Platform Flowchart

A flowchart diagram showing process flow and decision points

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=#4277BB;align=right;startSize=0;collapsible=0;strokeWidth=3;" parent="1" vertex="1">
      <mxGeometry x="178" y="74" width="813" height="680" as="geometry"/>
    </mxCell>
    <mxCell id="103" style="edgeStyle=elbowEdgeStyle;rounded=0;elbow=vertical;html=1;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;strokeWidth=2;fontSize=14;fontColor=#4277BB;" parent="2" source="76" target="77" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="105" style="edgeStyle=elbowEdgeStyle;rounded=0;elbow=vertical;html=1;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;strokeWidth=2;fontSize=14;fontColor=#4277BB;" parent="2" source="28" target="77" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="106" style="edgeStyle=elbowEdgeStyle;rounded=0;elbow=vertical;html=1;entryX=0;entryY=0.522;entryPerimeter=0;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;strokeWidth=2;fontSize=14;fontColor=#4277BB;" parent="2" source="77" target="79" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="104" style="edgeStyle=elbowEdgeStyle;rounded=0;elbow=vertical;html=1;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;strokeWidth=2;fontSize=14;fontColor=#4277BB;" parent="2" source="76" target="28" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="143" y="200" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="6" value="Application component" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#EBC01A;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="2" vertex="1">
      <mxGeometry x="21" y="530" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="7" value="Infrastructure services" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#8DC642;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="2" vertex="1">
      <mxGeometry x="21" y="550" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="8" value="Management" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#0DB39D;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="2" vertex="1">
      <mxGeometry x="21" y="570" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="9" value="Data store" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#335D81;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="2" vertex="1">
      <mxGeometry x="21" y="590" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="13" value="LEGEND" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=14;spacingLeft=0;" parent="2" vertex="1">
      <mxGeometry x="21" y="500" width="150" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="76" value="API&lt;div&gt;MANAGEMENT&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/management/api_management.svg;rounded=1;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=14;fontColor=#4277BB;spacingTop=3;" parent="2" vertex="1">
      <mxGeometry x="130" y="60" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="28" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=#4277BB;align=right;startSize=0;collapsible=0;strokeWidth=3;" parent="2" vertex="1">
      <mxGeometry x="100" y="190" width="120" height="280" as="geometry"/>
    </mxCell>
    <mxCell id="83" value="WORKLOADS" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/microservice.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="28" vertex="1">
      <mxGeometry x="19" y="38" width="82" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="84" value="WORKLOADS" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/microservice.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="28" vertex="1">
      <mxGeometry x="19" y="164" width="82" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="77" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=#4277BB;align=right;startSize=0;collapsible=0;strokeWidth=3;" parent="2" vertex="1">
      <mxGeometry x="315" y="57" width="137" height="483" as="geometry"/>
    </mxCell>
    <mxCell id="85" value="SOFTWARE&lt;div&gt;DEFINED&lt;/div&gt;&lt;div&gt;NETWORKING&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/infrastructure_services.svg;rounded=1;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=14;fontColor=#4277BB;" parent="77" vertex="1">
      <mxGeometry x="39" y="28" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="86" value="COMPUTE" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/dashboard.svg;rounded=1;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=14;fontColor=#4277BB;" parent="77" vertex="1">
      <mxGeometry x="39" y="181" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="87" value="SOFTWARE&lt;div&gt;DEFINED&lt;/div&gt;&lt;div&gt;STORAGE&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/data/data_services.svg;rounded=1;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=14;fontColor=#4277BB;" parent="77" vertex="1">
      <mxGeometry x="39" y="333" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="79" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=#4277BB;align=right;startSize=0;collapsible=0;strokeWidth=3;" parent="2" vertex="1">
      <mxGeometry x="563" y="57" width="137" height="483" as="geometry"/>
    </mxCell>
    <mxCell id="92" value="BARE METAL&#10;SERVERS" style="group;fontSize=14;fontColor=#4277BB;labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;labelBackgroundColor=#ffffff;" parent="79" vertex="1" connectable="0">
      <mxGeometry x="40" y="11" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="91" value="" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/miscellaneous/scalable.svg;rounded=1;labelBackgroundColor=none;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=14;fontColor=#4277BB;" parent="92" vertex="1">
      <mxGeometry width="15" height="15" as="geometry"/>
    </mxCell>
    <mxCell id="88" value="" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/data/file_repository.svg;rounded=1;labelBackgroundColor=none;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=14;fontColor=#4277BB;" parent="92" vertex="1">
      <mxGeometry width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="93" value="" style="group;fontSize=14;fontColor=#4277BB;labelBackgroundColor=#ffffff;" parent="79" vertex="1" connectable="0">
      <mxGeometry x="40" y="130" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="94" value="" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/miscellaneous/scalable.svg;rounded=1;labelBackgroundColor=none;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=14;fontColor=#4277BB;" parent="93" vertex="1">
      <mxGeometry width="15" height="15" as="geometry"/>
    </mxCell>
    <mxCell id="95" value="BARE METAL&lt;br&gt;SERVERS" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/data/file_repository.svg;rounded=1;labelBackgroundColor=none;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=14;fontColor=#4277BB;" parent="93" vertex="1">
      <mxGeometry width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="96" value="" style="group;fontSize=14;fontColor=#4277BB;labelBackgroundColor=#ffffff;" parent="79" vertex="1" connectable="0">
      <mxGeometry x="40" y="249" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="97" value="" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/miscellaneous/scalable.svg;rounded=1;labelBackgroundColor=none;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=14;fontColor=#4277BB;" parent="96" vertex="1">
      <mxGeometry width="15" height="15" as="geometry"/>
    </mxCell>
    <mxCell id="98" value="BARE METAL&lt;br&gt;SERVERS" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/data/file_repository.svg;rounded=1;labelBackgroundColor=none;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=14;fontColor=#4277BB;" parent="96" vertex="1">
      <mxGeometry width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="99" value="" style="group;fontSize=14;fontColor=#4277BB;labelBackgroundColor=#ffffff;" parent="79" vertex="1" connectable="0">
      <mxGeometry x="40" y="368" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="100" value="" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/miscellaneous/scalable.svg;rounded=1;labelBackgroundColor=none;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=14;fontColor=#4277BB;" parent="99" vertex="1">
      <mxGeometry width="15" height="15" as="geometry"/>
    </mxCell>
    <mxCell id="101" value="BARE METAL&lt;br&gt;SERVERS" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/data/file_repository.svg;rounded=1;labelBackgroundColor=none;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=14;fontColor=#4277BB;" parent="99" vertex="1">
      <mxGeometry width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="102" value="Scalable" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=left;shadow=0;image;image=img/lib/ibm/miscellaneous/scalable.svg;rounded=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#335D81;gradientColor=none;fontSize=12;fontColor=#4277BB;verticalAlign=middle;spacingLeft=7;labelPosition=right;verticalLabelPosition=middle;" parent="2" vertex="1">
      <mxGeometry x="24" y="608" width="15" height="15" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
