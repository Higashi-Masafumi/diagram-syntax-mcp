---
title: "Azure 1 Network"
description: "A network topology diagram showing infrastructure components"
category: "templates/cloud"
type: "network"
source_file: "templates/cloud/azure_1_decoded.xml"
tags: ["cloud", "template", "architecture", "drawio", "infrastructure"]
---

# Azure 1 Network

A network topology diagram showing infrastructure components

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1.5" pageWidth="1169" pageHeight="826" background="#184380" math="0" shadow="0">
  <root>
    <mxCell id="0" style=";html=1;"/>
    <mxCell id="1" style=";html=1;" parent="0"/>
    <mxCell id="23046e2b9bb16c14-116" value="Azure Group" style="whiteSpace=wrap;html=1;rounded=1;shadow=0;strokeColor=none;strokeWidth=2;fillColor=#009BFF;fontSize=20;fontColor=#FFFFFF;align=center;arcSize=3;verticalAlign=top;spacingTop=4;" parent="1" vertex="1">
      <mxGeometry x="287" y="217" width="1180" height="550" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-64" value="Web role instances" style="rounded=1;whiteSpace=wrap;html=1;shadow=0;strokeWidth=2;fillColor=#0072BC;fontSize=12;fontColor=#FFFFFF;align=center;strokeColor=none;arcSize=3;verticalAlign=top;" parent="1" vertex="1">
      <mxGeometry x="1286" y="291" width="150" height="420" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-27" value="" style="rounded=1;whiteSpace=wrap;html=1;shadow=0;strokeWidth=2;fillColor=#8BC63E;fontSize=12;fontColor=#000000;align=center;strokeColor=none;arcSize=3;" parent="1" vertex="1">
      <mxGeometry x="726" y="291" width="530" height="420" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-2" value="" style="rounded=1;whiteSpace=wrap;html=1;shadow=0;strokeWidth=2;fillColor=none;fontSize=12;fontColor=#000000;align=center;strokeColor=#FFFFFF;arcSize=10;" parent="1" vertex="1">
      <mxGeometry x="876" y="420" width="160" height="241" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-54" value="Availability set" style="rounded=1;whiteSpace=wrap;html=1;shadow=0;strokeWidth=2;fillColor=none;fontSize=11;fontColor=#FFFFFF;align=center;strokeColor=#FFFFFF;dashed=1;verticalAlign=top;" parent="1" vertex="1">
      <mxGeometry x="956" y="441" width="70" height="211" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-28" value="On-premises networks" style="rounded=1;whiteSpace=wrap;html=1;shadow=0;strokeWidth=2;fillColor=#F04D22;fontSize=12;fontColor=#FFFFFF;align=center;strokeColor=none;arcSize=6;verticalAlign=top;" parent="1" vertex="1">
      <mxGeometry x="466" y="378" width="230" height="330" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-49" value="" style="rounded=1;whiteSpace=wrap;html=1;shadow=0;strokeWidth=2;fillColor=none;fontSize=12;fontColor=#000000;align=center;strokeColor=#FFFFFF;" parent="1" vertex="1">
      <mxGeometry x="486" y="410" width="80" height="218" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-1" value="" style="rounded=1;whiteSpace=wrap;html=1;shadow=0;strokeWidth=2;fillColor=none;fontSize=12;fontColor=#000000;align=center;strokeColor=#FFFFFF;" parent="1" vertex="1">
      <mxGeometry x="746" y="420" width="110" height="221" as="geometry"/>
    </mxCell>
    <mxCell id="24964f25f45c63f1-1" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeColor=none;fillColor=#FFFFFF;shape=mxgraph.azure.computer;rounded=0;shadow=0;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="501" y="424" width="50" height="45" as="geometry"/>
    </mxCell>
    <mxCell id="24964f25f45c63f1-2" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeColor=none;fillColor=#FFFFFF;shape=mxgraph.azure.computer;rounded=0;shadow=0;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="501" y="494" width="50" height="45" as="geometry"/>
    </mxCell>
    <mxCell id="24964f25f45c63f1-3" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeColor=none;fillColor=#FFFFFF;shape=mxgraph.azure.computer;rounded=0;shadow=0;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="501" y="564" width="50" height="45" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-73" style="html=1;startArrow=none;startFill=0;startSize=10;endArrow=none;endFill=0;endSize=10;strokeWidth=3;fontSize=11;fontColor=#FFFFFF;strokeColor=#FFFFFF;rounded=0;" parent="1" source="24964f25f45c63f1-5" target="23046e2b9bb16c14-7" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="24964f25f45c63f1-5" value="Gateway" style="shadow=0;dashed=0;html=1;strokeColor=none;shape=mxgraph.mscae.enterprise.gateway;fillColor=#FFFFFF;rounded=0;fontSize=12;fontColor=#FFFFFF;align=center;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;" parent="1" vertex="1">
      <mxGeometry x="773" y="541" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="24964f25f45c63f1-6" value="" style="shadow=0;dashed=0;html=1;strokeColor=none;shape=mxgraph.mscae.enterprise.lock;fillColor=#FFFFFF;rounded=0;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="896" y="436" width="39" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-7" value="" style="shadow=0;dashed=0;html=1;strokeColor=none;labelPosition=center;verticalLabelPosition=bottom;verticalAlign=top;shape=mxgraph.mscae.cloud.azure_load_balancer_feature;fillColor=#FFFFFF;rounded=1;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="891" y="541" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-75" style="html=1;startArrow=none;startFill=0;startSize=10;endArrow=none;endFill=0;endSize=10;strokeWidth=3;fontSize=11;fontColor=#FFFFFF;entryX=0.793;entryY=0.26;entryPerimeter=0;strokeColor=#FFFFFF;rounded=0;" parent="1" source="23046e2b9bb16c14-29" target="23046e2b9bb16c14-7" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-29" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeColor=none;fillColor=#FFFFFF;shape=mxgraph.azure.virtual_machine;rounded=1;shadow=0;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="966" y="493" width="50" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-76" style="html=1;entryX=1.016;entryY=0.509;entryPerimeter=0;startArrow=none;startFill=0;startSize=10;endArrow=none;endFill=0;endSize=10;strokeWidth=3;fontSize=11;fontColor=#FFFFFF;strokeColor=#FFFFFF;rounded=0;" parent="1" source="23046e2b9bb16c14-30" target="23046e2b9bb16c14-7" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-30" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeColor=none;fillColor=#FFFFFF;shape=mxgraph.azure.virtual_machine;rounded=1;shadow=0;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="966" y="546" width="50" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-77" style="html=1;entryX=0.802;entryY=0.762;entryPerimeter=0;startArrow=none;startFill=0;startSize=10;endArrow=none;endFill=0;endSize=10;strokeWidth=3;fontSize=11;fontColor=#FFFFFF;strokeColor=#FFFFFF;rounded=0;" parent="1" source="23046e2b9bb16c14-31" target="23046e2b9bb16c14-7" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-31" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeColor=none;fillColor=#FFFFFF;shape=mxgraph.azure.virtual_machine;rounded=1;shadow=0;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="966" y="598" width="50" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-48" value="Azure Vnet" style="shadow=0;dashed=0;html=1;strokeColor=none;fillColor=#FFFFFF;labelPosition=center;verticalLabelPosition=bottom;verticalAlign=top;shape=mxgraph.office.clouds.azure;rounded=1;fontSize=12;fontColor=#FFFFFF;align=center;" parent="1" vertex="1">
      <mxGeometry x="756" y="311" width="83" height="53" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-50" value="" style="rounded=1;whiteSpace=wrap;html=1;shadow=0;strokeWidth=2;fillColor=none;fontSize=12;fontColor=#000000;align=center;strokeColor=#FFFFFF;" parent="1" vertex="1">
      <mxGeometry x="596" y="409" width="80" height="218" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-51" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeColor=none;fillColor=#FFFFFF;shape=mxgraph.azure.computer;rounded=0;shadow=0;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="611" y="423" width="50" height="45" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-52" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeColor=none;fillColor=#FFFFFF;shape=mxgraph.azure.computer;rounded=0;shadow=0;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="611" y="493" width="50" height="45" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-53" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeColor=none;fillColor=#FFFFFF;shape=mxgraph.azure.computer;rounded=0;shadow=0;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="611" y="563" width="50" height="45" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-71" style="edgeStyle=orthogonalEdgeStyle;html=1;startArrow=none;startFill=0;startSize=10;endArrow=none;endFill=0;endSize=10;strokeWidth=3;fontSize=11;fontColor=#FFFFFF;strokeColor=#FFFFFF;dashed=1;rounded=0;" parent="1" source="24964f25f45c63f1-4" target="24964f25f45c63f1-5" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="581" y="730"/>
          <mxPoint x="798" y="730"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="24964f25f45c63f1-4" value="Gateway" style="shadow=0;dashed=0;html=1;strokeColor=none;shape=mxgraph.mscae.enterprise.gateway;fillColor=#FFFFFF;rounded=0;fontSize=12;fontColor=#FFFFFF;align=center;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;" parent="1" vertex="1">
      <mxGeometry x="556" y="648" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-55" value="" style="rounded=1;whiteSpace=wrap;html=1;shadow=0;strokeWidth=2;fillColor=none;fontSize=12;fontColor=#000000;align=center;strokeColor=#FFFFFF;arcSize=9;" parent="1" vertex="1">
      <mxGeometry x="1071" y="420" width="160" height="241" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-56" value="&lt;span&gt;Availability set&lt;/span&gt;" style="rounded=1;whiteSpace=wrap;html=1;shadow=0;strokeWidth=2;fillColor=none;fontSize=11;fontColor=#FFFFFF;align=center;strokeColor=#FFFFFF;dashed=1;verticalAlign=top;" parent="1" vertex="1">
      <mxGeometry x="1151" y="441" width="70" height="211" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-57" value="" style="shadow=0;dashed=0;html=1;strokeColor=none;shape=mxgraph.mscae.enterprise.lock;fillColor=#FFFFFF;rounded=0;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="1091" y="436" width="39" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-74" style="html=1;startArrow=none;startFill=0;startSize=10;endArrow=none;endFill=0;endSize=10;strokeWidth=3;fontSize=11;fontColor=#FFFFFF;strokeColor=#FFFFFF;rounded=0;edgeStyle=elbowEdgeStyle;elbow=vertical;" parent="1" source="23046e2b9bb16c14-58" target="23046e2b9bb16c14-2" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-78" style="edgeStyle=orthogonalEdgeStyle;html=1;startArrow=none;startFill=0;startSize=10;endArrow=none;endFill=0;endSize=10;strokeWidth=3;fontSize=11;fontColor=#FFFFFF;strokeColor=#FFFFFF;rounded=0;" parent="1" source="23046e2b9bb16c14-58" target="23046e2b9bb16c14-60" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-79" style="html=1;startArrow=none;startFill=0;startSize=10;endArrow=none;endFill=0;endSize=10;strokeWidth=3;fontSize=11;fontColor=#FFFFFF;strokeColor=#FFFFFF;rounded=0;exitX=0.796;exitY=0.241;exitPerimeter=0;" parent="1" source="23046e2b9bb16c14-58" target="23046e2b9bb16c14-59" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-80" style="html=1;startArrow=none;startFill=0;startSize=10;endArrow=none;endFill=0;endSize=10;strokeWidth=3;fontSize=11;fontColor=#FFFFFF;strokeColor=#FFFFFF;rounded=0;exitX=0.789;exitY=0.767;exitPerimeter=0;" parent="1" source="23046e2b9bb16c14-58" target="23046e2b9bb16c14-61" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-58" value="" style="shadow=0;dashed=0;html=1;strokeColor=none;labelPosition=center;verticalLabelPosition=bottom;verticalAlign=top;shape=mxgraph.mscae.cloud.azure_load_balancer_feature;fillColor=#FFFFFF;rounded=1;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="1086" y="541" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-59" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeColor=none;fillColor=#FFFFFF;shape=mxgraph.azure.virtual_machine;rounded=1;shadow=0;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="1161" y="493" width="50" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-60" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeColor=none;fillColor=#FFFFFF;shape=mxgraph.azure.virtual_machine;rounded=1;shadow=0;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="1161" y="546" width="50" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-61" value="" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeColor=none;fillColor=#FFFFFF;shape=mxgraph.azure.virtual_machine;rounded=1;shadow=0;fontSize=12;fontColor=#000000;align=center;" parent="1" vertex="1">
      <mxGeometry x="1161" y="598" width="50" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-69" style="edgeStyle=orthogonalEdgeStyle;html=1;startArrow=none;startFill=0;startSize=10;endArrow=none;endFill=0;endSize=10;strokeWidth=3;fontSize=11;fontColor=#FFFFFF;strokeColor=#FFFFFF;dashed=1;rounded=0;" parent="1" source="23046e2b9bb16c14-62" target="23046e2b9bb16c14-63" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-62" value="Firewall" style="shadow=0;dashed=0;html=1;strokeColor=none;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;shape=mxgraph.office.concepts.firewall;fillColor=#FFFFFF;rounded=1;fontSize=11;fontColor=#FFFFFF;align=left;spacingLeft=5;" parent="1" vertex="1">
      <mxGeometry x="328" y="475" width="47" height="43" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-70" style="edgeStyle=orthogonalEdgeStyle;html=1;startArrow=none;startFill=0;startSize=10;endArrow=none;endFill=0;endSize=10;strokeWidth=3;fontSize=11;fontColor=#FFFFFF;strokeColor=#FFFFFF;dashed=1;rounded=0;" parent="1" source="24964f25f45c63f1-4" target="23046e2b9bb16c14-68" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="606" y="730" as="sourcePoint"/>
        <Array as="points">
          <mxPoint x="581" y="730"/>
          <mxPoint x="1361" y="730"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-72" style="edgeStyle=orthogonalEdgeStyle;html=1;startArrow=none;startFill=0;startSize=10;endArrow=none;endFill=0;endSize=10;strokeWidth=3;fontSize=11;fontColor=#FFFFFF;strokeColor=#FFFFFF;dashed=1;rounded=0;" parent="1" source="23046e2b9bb16c14-63" target="24964f25f45c63f1-4" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="351" y="730"/>
          <mxPoint x="581" y="730"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-63" value="Windows&lt;div&gt;Azure&lt;/div&gt;&lt;div&gt;Load&lt;/div&gt;&lt;div&gt;Balancer&lt;/div&gt;" style="verticalLabelPosition=middle;html=1;verticalAlign=middle;strokeColor=none;fillColor=#FFFFFF;shape=mxgraph.azure.azure_load_balancer;rounded=1;shadow=0;dashed=1;fontSize=11;fontColor=#FFFFFF;align=left;labelPosition=right;spacingLeft=5;" parent="1" vertex="1">
      <mxGeometry x="326" y="593" width="50" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-65" value="" style="shadow=0;dashed=0;html=1;strokeColor=none;shape=mxgraph.mscae.enterprise.web;fillColor=#FFFFFF;rounded=1;fontSize=11;fontColor=#FFFFFF;align=center;" parent="1" vertex="1">
      <mxGeometry x="1336" y="531" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-66" value="" style="shadow=0;dashed=0;html=1;strokeColor=none;shape=mxgraph.mscae.enterprise.web;fillColor=#FFFFFF;rounded=1;fontSize=11;fontColor=#FFFFFF;align=center;" parent="1" vertex="1">
      <mxGeometry x="1336" y="450" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-67" value="" style="shadow=0;dashed=0;html=1;strokeColor=none;shape=mxgraph.mscae.enterprise.web;fillColor=#FFFFFF;rounded=1;fontSize=11;fontColor=#FFFFFF;align=center;" parent="1" vertex="1">
      <mxGeometry x="1336" y="370" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-117" style="edgeStyle=orthogonalEdgeStyle;rounded=0;elbow=vertical;html=1;startArrow=none;startFill=0;startSize=10;endArrow=none;endFill=0;endSize=10;strokeColor=#FFFFFF;strokeWidth=3;fontSize=20;fontColor=#FFFFFF;entryX=0.004;entryY=0.516;entryPerimeter=0;" parent="1" source="23046e2b9bb16c14-68" target="23046e2b9bb16c14-65" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="1520" y="590" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1326" y="673"/>
          <mxPoint x="1326" y="557"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-119" style="edgeStyle=orthogonalEdgeStyle;rounded=0;elbow=vertical;html=1;entryX=-0.002;entryY=0.494;entryPerimeter=0;startArrow=none;startFill=0;startSize=10;endArrow=none;endFill=0;endSize=10;strokeColor=#FFFFFF;strokeWidth=3;fontSize=20;fontColor=#FFFFFF;" parent="1" source="23046e2b9bb16c14-68" target="23046e2b9bb16c14-67" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="1326" y="673"/>
          <mxPoint x="1326" y="395"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-68" value="Gateway" style="shadow=0;dashed=0;html=1;strokeColor=none;shape=mxgraph.mscae.enterprise.gateway;fillColor=#FFFFFF;rounded=0;fontSize=12;fontColor=#FFFFFF;align=center;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;" parent="1" vertex="1">
      <mxGeometry x="1336" y="648" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-81" value="A" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;shadow=0;fontSize=11;fontColor=#FFFFFF;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="666" y="678" width="20" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-82" value="B" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;shadow=0;fontSize=11;fontColor=#FFFFFF;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="1226" y="678" width="20" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-83" value="C" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;shadow=0;fontSize=11;fontColor=#FFFFFF;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="1406" y="680" width="20" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-84" value="" style="rounded=0;whiteSpace=wrap;html=1;shadow=0;strokeWidth=2;fillColor=#F04D22;fontSize=12;fontColor=#FFFFFF;align=center;strokeColor=none;arcSize=6;verticalAlign=top;" parent="1" vertex="1">
      <mxGeometry x="326" y="820" width="300" height="102" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-85" value="" style="rounded=0;whiteSpace=wrap;html=1;shadow=0;strokeWidth=2;fillColor=#8BC63E;fontSize=12;fontColor=#FFFFFF;align=center;strokeColor=none;arcSize=6;verticalAlign=top;" parent="1" vertex="1">
      <mxGeometry x="626" y="820" width="400" height="102" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-86" value="" style="rounded=0;whiteSpace=wrap;html=1;shadow=0;strokeWidth=2;fillColor=#0072BC;fontSize=12;fontColor=#FFFFFF;align=center;strokeColor=none;arcSize=3;verticalAlign=top;" parent="1" vertex="1">
      <mxGeometry x="1026" y="820" width="390" height="102" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-87" value="A" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;shadow=0;fontSize=30;fontColor=#FFFFFF;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="326" y="853" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-88" value="B" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;shadow=0;fontSize=30;fontColor=#FFFFFF;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="626" y="853" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-89" value="C" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;shadow=0;fontSize=30;fontColor=#FFFFFF;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="1026" y="853" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-90" value="Computer" style="verticalLabelPosition=top;html=1;verticalAlign=bottom;strokeColor=none;fillColor=#FFFFFF;shape=mxgraph.azure.computer;rounded=0;shadow=0;fontSize=10;fontColor=#FFFFFF;align=center;labelPosition=center;" parent="1" vertex="1">
      <mxGeometry x="393" y="860" width="50" height="45" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-91" value="VHD" style="shadow=0;html=1;strokeColor=none;fillColor=#FFFFFF;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;shape=mxgraph.azure.vhd;rounded=0;fontSize=10;fontColor=#FFFFFF;align=center;" parent="1" vertex="1">
      <mxGeometry x="483" y="857" width="40" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-92" value="+" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;shadow=0;fontSize=30;fontColor=#FFFFFF;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="443" y="865" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-93" value="+" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;shadow=0;fontSize=30;fontColor=#FFFFFF;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="523" y="865" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-94" value="Server&lt;div&gt;Directory&lt;/div&gt;" style="shadow=0;html=1;strokeColor=none;shape=mxgraph.mscae.enterprise.server_directory;fillColor=#FFFFFF;rounded=0;fontSize=10;fontColor=#FFFFFF;align=center;verticalAlign=bottom;labelPosition=center;verticalLabelPosition=top;" parent="1" vertex="1">
      <mxGeometry x="563" y="858" width="36" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-95" value="VM Feature" style="shadow=0;html=1;strokeColor=none;fillColor=#FFFFFF;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;shape=mxgraph.azure.virtual_machine_feature;rounded=0;fontSize=10;fontColor=#FFFFFF;align=center;" parent="1" vertex="1">
      <mxGeometry x="684" y="861" width="50" height="45" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-96" value="+" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;shadow=0;fontSize=30;fontColor=#FFFFFF;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="734" y="866" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-97" value="VHD" style="shadow=0;html=1;strokeColor=none;fillColor=#FFFFFF;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;shape=mxgraph.azure.vhd;rounded=0;fontSize=10;fontColor=#FFFFFF;align=center;" parent="1" vertex="1">
      <mxGeometry x="774" y="858" width="40" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-98" value="3rd Party&lt;div&gt;Integration&lt;/div&gt;" style="shadow=0;html=1;strokeColor=none;fillColor=#FFFFFF;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;shape=mxgraph.office.communications.3rd_party_integration;rounded=0;fontSize=10;fontColor=#FFFFFF;align=center;" parent="1" vertex="1">
      <mxGeometry x="854" y="856" width="54" height="55" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-99" value="+" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;shadow=0;fontSize=30;fontColor=#FFFFFF;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="814" y="866" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-100" value="+" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;shadow=0;fontSize=30;fontColor=#FFFFFF;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="908" y="866" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-101" value="Data Migration&lt;div&gt;Wizard&lt;/div&gt;" style="shadow=0;html=1;strokeColor=none;shape=mxgraph.mscae.intune.data_migration_wizard;fillColor=#FFFFFF;rounded=0;fontSize=10;fontColor=#FFFFFF;align=center;verticalAlign=bottom;labelPosition=center;verticalLabelPosition=top;" parent="1" vertex="1">
      <mxGeometry x="948" y="859" width="50" height="48" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-102" value="VM Feature" style="shadow=0;html=1;strokeColor=none;fillColor=#FFFFFF;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;shape=mxgraph.azure.virtual_machine_feature;rounded=0;fontSize=10;fontColor=#FFFFFF;align=center;" parent="1" vertex="1">
      <mxGeometry x="1086" y="861" width="50" height="45" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-103" value="" style="line;strokeWidth=2;direction=south;html=1;rounded=0;shadow=0;fillColor=none;fontSize=30;fontColor=#FFFFFF;align=center;strokeColor=#FFFFFF;" parent="1" vertex="1">
      <mxGeometry x="366" y="820" width="10" height="102" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-104" value="" style="line;strokeWidth=2;direction=south;html=1;rounded=0;shadow=0;fillColor=none;fontSize=30;fontColor=#FFFFFF;align=center;strokeColor=#FFFFFF;" parent="1" vertex="1">
      <mxGeometry x="666" y="820" width="10" height="102" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-105" value="" style="line;strokeWidth=2;direction=south;html=1;rounded=0;shadow=0;fillColor=none;fontSize=30;fontColor=#FFFFFF;align=center;strokeColor=#FFFFFF;" parent="1" vertex="1">
      <mxGeometry x="1066" y="820" width="10" height="102" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-106" value="+" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;shadow=0;fontSize=30;fontColor=#FFFFFF;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="1136" y="866" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-107" value="Azure&lt;div&gt;Website&lt;/div&gt;" style="verticalLabelPosition=top;html=1;verticalAlign=bottom;strokeColor=none;fillColor=#FFFFFF;shape=mxgraph.azure.azure_website;rounded=0;shadow=0;fontSize=10;fontColor=#FFFFFF;align=center;labelPosition=center;" parent="1" vertex="1">
      <mxGeometry x="1176" y="858" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-108" value="+" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;shadow=0;fontSize=30;fontColor=#FFFFFF;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="1226" y="866" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-109" value="MySQL&lt;div&gt;Database&lt;/div&gt;" style="verticalLabelPosition=top;html=1;verticalAlign=bottom;strokeColor=none;fillColor=#FFFFFF;shape=mxgraph.azure.mysql_database;rounded=0;shadow=0;fontSize=10;fontColor=#FFFFFF;align=center;labelPosition=center;" parent="1" vertex="1">
      <mxGeometry x="1266" y="859" width="37.5" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-110" value="+" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;shadow=0;fontSize=30;fontColor=#FFFFFF;fontStyle=1" parent="1" vertex="1">
      <mxGeometry x="1304" y="866" width="40" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-111" value="Azure&lt;div&gt;Storage&lt;/div&gt;" style="shadow=0;html=1;strokeColor=none;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;shape=mxgraph.mscae.cloud.azure_storage;fillColor=#FFFFFF;rounded=0;fontSize=10;fontColor=#FFFFFF;align=center;" parent="1" vertex="1">
      <mxGeometry x="1344" y="862" width="50" height="43" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-113" value="Title" style="text;strokeColor=none;fillColor=none;html=1;fontSize=24;fontStyle=1;verticalAlign=middle;align=center;rounded=0;shadow=0;fontColor=#FFFFFF;" parent="1" vertex="1">
      <mxGeometry x="120" y="40" width="1510" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-114" value="Subtitle" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;shadow=0;fontSize=10;fontColor=#009BFF;" parent="1" vertex="1">
      <mxGeometry x="114" y="90" width="1526" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-115" value="&lt;h1&gt;Heading&lt;/h1&gt;&lt;p&gt;Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.&lt;/p&gt;" style="text;html=1;strokeColor=none;fillColor=none;spacing=5;spacingTop=-20;whiteSpace=wrap;overflow=hidden;rounded=0;shadow=0;fontSize=10;fontColor=#FFFFFF;align=left;" parent="1" vertex="1">
      <mxGeometry x="323" y="952" width="1041" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="23046e2b9bb16c14-118" style="edgeStyle=orthogonalEdgeStyle;rounded=0;elbow=vertical;html=1;startArrow=none;startFill=0;startSize=10;endArrow=none;endFill=0;endSize=10;strokeColor=#FFFFFF;strokeWidth=3;fontSize=20;fontColor=#FFFFFF;entryX=-0.009;entryY=0.502;entryPerimeter=0;" parent="1" source="23046e2b9bb16c14-68" target="23046e2b9bb16c14-66" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="1346.3333333333333" y="566.6666666666666" as="targetPoint"/>
        <mxPoint x="1371" y="658" as="sourcePoint"/>
        <Array as="points">
          <mxPoint x="1326" y="673"/>
          <mxPoint x="1326" y="475"/>
        </Array>
      </mxGeometry>
    </mxCell>
  </root>
</mxGraphModel>

```
