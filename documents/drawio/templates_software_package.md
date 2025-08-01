---
title: "Package Network"
description: "A network topology diagram showing infrastructure components"
category: "templates/software"
type: "network"
source_file: "templates/software/package_decoded.xml"
tags: ["development", "software", "template", "architecture", "drawio"]
---

# Package Network

A network topology diagram showing infrastructure components

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1.5" pageWidth="826" pageHeight="1169" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="37" value="Abstraction layer" style="swimlane;fillColor=#66B2FF" parent="1" vertex="1">
      <mxGeometry x="170" y="100" width="1140" height="430" as="geometry">
        <mxRectangle x="170" y="100" width="140" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="40" value="" style="strokeWidth=1" parent="37" vertex="1">
      <mxGeometry y="23" width="1140" height="407" as="geometry"/>
    </mxCell>
    <mxCell id="3" value="&lt;&lt;namespace&gt;&gt;&#10;System" style="shape=folder;fontStyle=0;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;shadow=1;verticalAlign=top;fillColor=#FF9933;gradientColor=#FFE6CC;gradientDirection=north" parent="37" vertex="1">
      <mxGeometry x="56" y="58" width="200" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="6" value="&lt;&lt;namespace&gt;&gt;&#10;Ajax" style="shape=folder;fontStyle=0;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;shadow=1;verticalAlign=top;fillColor=#FF9933;gradientColor=#FFE6CC;gradientDirection=north" parent="37" vertex="1">
      <mxGeometry x="576" y="58" width="200" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="15" value="&lt;&lt;namespace&gt;&gt;&#10;JavaScript" style="shape=folder;fontStyle=0;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;shadow=1;verticalAlign=top;fillColor=#FF9933;gradientColor=#FFE6CC;gradientDirection=north" parent="37" vertex="1">
      <mxGeometry x="826" y="160.00000000000006" width="200" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="16" value="&lt;&lt;namespace&gt;&gt;&#10;Apache Server" style="shape=folder;fontStyle=0;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;shadow=1;verticalAlign=top;fillColor=#FF9933;gradientColor=#FFE6CC;gradientDirection=north" parent="37" vertex="1">
      <mxGeometry x="576" y="160.00000000000006" width="200" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="17" value="&lt;&lt;namespace&gt;&gt;&#10;Protocol" style="shape=folder;fontStyle=0;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;shadow=1;verticalAlign=top;fillColor=#FF9933;gradientColor=#FFE6CC;gradientDirection=north" parent="37" vertex="1">
      <mxGeometry x="56" y="175.00000000000006" width="200" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="18" value="&lt;&lt;namespace&gt;&gt;&#10;P2P" style="shape=folder;fontStyle=0;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;shadow=1;verticalAlign=top;fillColor=#FF9933;gradientColor=#FFE6CC;gradientDirection=north" parent="37" vertex="1">
      <mxGeometry x="56" y="315.00000000000006" width="200" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="19" value="&lt;&lt;namespace&gt;&gt;&#10;HTTP" style="shape=folder;fontStyle=0;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;shadow=1;verticalAlign=top;fillColor=#FF9933;gradientColor=#FFE6CC;gradientDirection=north" parent="37" vertex="1">
      <mxGeometry x="316" y="315.00000000000006" width="200" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="28" value="" style="edgeStyle=none;dashed=1;endArrow=open" parent="37" source="16" target="22" edge="1">
      <mxGeometry x="-154" y="-124.99999999999994" width="100" height="100" as="geometry">
        <mxPoint x="-154" y="-24.999999999999943" as="sourcePoint"/>
        <mxPoint x="-54" y="-124.99999999999994" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="29" value="" style="shape=mxgraph.basic.x;fillColor=#990000;strokeColor=black;strokeWidth=1" parent="37" vertex="1">
      <mxGeometry x="236" y="78" width="16" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="30" value="" style="shape=mxgraph.basic.x;fillColor=#990000;strokeColor=black;strokeWidth=1" parent="37" vertex="1">
      <mxGeometry x="756" y="78" width="16" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="31" value="" style="shape=mxgraph.basic.tick;fillColor=#006600;strokeColor=black;strokeWidth=1" parent="37" vertex="1">
      <mxGeometry x="236" y="191.3888888888889" width="16" height="23.611111111111143" as="geometry"/>
    </mxCell>
    <mxCell id="32" value="" style="shape=mxgraph.basic.tick;fillColor=#006600;strokeColor=black;strokeWidth=1" parent="37" vertex="1">
      <mxGeometry x="236" y="338.1944444444445" width="16" height="23.611111111111143" as="geometry"/>
    </mxCell>
    <mxCell id="33" value="" style="shape=mxgraph.basic.tick;fillColor=#006600;strokeColor=black;strokeWidth=1" parent="37" vertex="1">
      <mxGeometry x="756" y="179.58333333333337" width="16" height="23.611111111111143" as="geometry"/>
    </mxCell>
    <mxCell id="34" value="" style="shape=mxgraph.basic.tick;fillColor=#006600;strokeColor=black;strokeWidth=1" parent="37" vertex="1">
      <mxGeometry x="1006" y="179.58333333333337" width="16" height="23.611111111111143" as="geometry"/>
    </mxCell>
    <mxCell id="35" value="" style="shape=mxgraph.basic.x;fillColor=#990000;strokeColor=black;strokeWidth=1" parent="37" vertex="1">
      <mxGeometry x="756" y="315.0000000000001" width="16" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="36" value="" style="shape=mxgraph.basic.x;fillColor=#990000;strokeColor=black;strokeWidth=1" parent="37" vertex="1">
      <mxGeometry x="496" y="335.0000000000001" width="16" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="27" value="" style="edgeStyle=none;dashed=1;endArrow=open" parent="37" source="6" target="15" edge="1">
      <mxGeometry x="-154" y="-124.99999999999994" width="100" height="100" as="geometry">
        <mxPoint x="-154" y="-24.999999999999943" as="sourcePoint"/>
        <mxPoint x="-54" y="-124.99999999999994" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="26" value="" style="edgeStyle=none;dashed=1;endArrow=open" parent="37" source="6" target="16" edge="1">
      <mxGeometry x="-154" y="-124.99999999999994" width="100" height="100" as="geometry">
        <mxPoint x="-154" y="-24.999999999999943" as="sourcePoint"/>
        <mxPoint x="-54" y="-124.99999999999994" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="25" value="" style="edgeStyle=none;dashed=1;endArrow=open" parent="37" source="17" target="19" edge="1">
      <mxGeometry x="-154" y="-124.99999999999994" width="100" height="100" as="geometry">
        <mxPoint x="-154" y="-24.999999999999943" as="sourcePoint"/>
        <mxPoint x="-54" y="-124.99999999999994" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="24" value="" style="edgeStyle=none;dashed=1;endArrow=open" parent="37" source="17" target="18" edge="1">
      <mxGeometry x="-154" y="-124.99999999999994" width="100" height="100" as="geometry">
        <mxPoint x="-154" y="-24.999999999999943" as="sourcePoint"/>
        <mxPoint x="-54" y="-124.99999999999994" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="23" value="" style="edgeStyle=none;dashed=1;endArrow=open" parent="37" source="3" target="17" edge="1">
      <mxGeometry x="-154" y="-124.99999999999994" width="100" height="100" as="geometry">
        <mxPoint x="-154" y="-24.999999999999943" as="sourcePoint"/>
        <mxPoint x="-54" y="-124.99999999999994" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="22" value="&lt;&lt;namespace&gt;&gt;&#10;Tomcat" style="shape=folder;fontStyle=0;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;shadow=1;verticalAlign=top;fillColor=#FF9933;gradientColor=#FFE6CC;gradientDirection=north" parent="37" vertex="1">
      <mxGeometry x="576" y="295.00000000000006" width="200" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="42" value="" style="shape=mxgraph.basic.x;fillColor=#990000;strokeColor=black;strokeWidth=1" parent="37" vertex="1">
      <mxGeometry x="756" y="315.0000000000001" width="16" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="43" value="Implementation layer" style="swimlane;fillColor=#66B2FF" parent="1" vertex="1">
      <mxGeometry x="170" y="530" width="1140" height="430" as="geometry">
        <mxRectangle x="170" y="530" width="140" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="44" value="" style="strokeWidth=1" parent="43" vertex="1">
      <mxGeometry y="23" width="1140" height="407" as="geometry"/>
    </mxCell>
    <mxCell id="45" value="Presentation Logic" style="shape=folder;fontStyle=0;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;shadow=1;verticalAlign=top;fillColor=#FF9933;gradientColor=#FFE6CC;gradientDirection=north" parent="43" vertex="1">
      <mxGeometry x="56" y="58" width="200" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="46" value="Communication" style="shape=folder;fontStyle=0;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;shadow=1;verticalAlign=top;fillColor=#FF9933;gradientColor=#FFE6CC;gradientDirection=north" parent="43" vertex="1">
      <mxGeometry x="576" y="58" width="200" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="47" value="Security" style="shape=folder;fontStyle=0;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;shadow=1;verticalAlign=top;fillColor=#FF9933;gradientColor=#FFE6CC;gradientDirection=north" parent="43" vertex="1">
      <mxGeometry x="826" y="160.00000000000006" width="200" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="48" value="Data Access" style="shape=folder;fontStyle=0;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;shadow=1;verticalAlign=top;fillColor=#FF9933;gradientColor=#FFE6CC;gradientDirection=north" parent="43" vertex="1">
      <mxGeometry x="576" y="160.00000000000006" width="200" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="49" value="User Interface" style="shape=folder;fontStyle=0;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;shadow=1;verticalAlign=top;fillColor=#FF9933;gradientColor=#FFE6CC;gradientDirection=north" parent="43" vertex="1">
      <mxGeometry x="56" y="175.00000000000006" width="200" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="50" value="Menu subsystem" style="shape=folder;fontStyle=0;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;shadow=1;verticalAlign=top;fillColor=#FF9933;gradientColor=#FFE6CC;gradientDirection=north" parent="43" vertex="1">
      <mxGeometry x="56" y="315.00000000000006" width="200" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="51" value="Action Linking" style="shape=folder;fontStyle=0;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;shadow=1;verticalAlign=top;fillColor=#FF9933;gradientColor=#FFE6CC;gradientDirection=north" parent="43" vertex="1">
      <mxGeometry x="316" y="315.00000000000006" width="200" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="52" value="" style="edgeStyle=none;dashed=1;endArrow=open" parent="43" source="48" target="66" edge="1">
      <mxGeometry x="-154" y="-124.99999999999994" width="100" height="100" as="geometry">
        <mxPoint x="-154" y="-24.999999999999943" as="sourcePoint"/>
        <mxPoint x="-54" y="-124.99999999999994" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="59" value="" style="shape=mxgraph.basic.x;fillColor=#990000;strokeColor=black;strokeWidth=1" parent="43" vertex="1">
      <mxGeometry x="756" y="315.0000000000001" width="16" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="61" value="" style="edgeStyle=none;dashed=1;endArrow=open" parent="43" source="46" target="47" edge="1">
      <mxGeometry x="-154" y="-124.99999999999994" width="100" height="100" as="geometry">
        <mxPoint x="-154" y="-24.999999999999943" as="sourcePoint"/>
        <mxPoint x="-54" y="-124.99999999999994" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="62" value="" style="edgeStyle=none;dashed=1;endArrow=open" parent="43" source="46" target="48" edge="1">
      <mxGeometry x="-154" y="-124.99999999999994" width="100" height="100" as="geometry">
        <mxPoint x="-154" y="-24.999999999999943" as="sourcePoint"/>
        <mxPoint x="-54" y="-124.99999999999994" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="63" value="" style="edgeStyle=none;dashed=1;endArrow=open" parent="43" source="49" target="51" edge="1">
      <mxGeometry x="-154" y="-124.99999999999994" width="100" height="100" as="geometry">
        <mxPoint x="-154" y="-24.999999999999943" as="sourcePoint"/>
        <mxPoint x="-54" y="-124.99999999999994" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="64" value="" style="edgeStyle=none;dashed=1;endArrow=open" parent="43" source="49" target="50" edge="1">
      <mxGeometry x="-154" y="-124.99999999999994" width="100" height="100" as="geometry">
        <mxPoint x="-154" y="-24.999999999999943" as="sourcePoint"/>
        <mxPoint x="-54" y="-124.99999999999994" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="65" value="" style="edgeStyle=none;dashed=1;endArrow=open" parent="43" source="45" target="49" edge="1">
      <mxGeometry x="-154" y="-124.99999999999994" width="100" height="100" as="geometry">
        <mxPoint x="-154" y="-24.999999999999943" as="sourcePoint"/>
        <mxPoint x="-54" y="-124.99999999999994" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="66" value="Data Sources" style="shape=folder;fontStyle=0;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;shadow=1;verticalAlign=top;fillColor=#FF9933;gradientColor=#FFE6CC;gradientDirection=north" parent="43" vertex="1">
      <mxGeometry x="576" y="295.00000000000006" width="200" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="68" value="Help subsystem" style="shape=folder;fontStyle=0;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;shadow=1;verticalAlign=top;fillColor=#FF9933;gradientColor=#FFE6CC;gradientDirection=north" parent="43" vertex="1">
      <mxGeometry x="316" y="175" width="200" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="69" value="" style="edgeStyle=none;dashed=1;endArrow=open" parent="43" source="45" target="68" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
  </root>
</mxGraphModel>

```
