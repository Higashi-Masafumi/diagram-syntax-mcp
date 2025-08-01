---
title: "Ibm Microservices Flowchart"
description: "A flowchart diagram showing process flow and decision points"
category: "templates/cloud"
type: "flowchart"
source_file: "templates/cloud/ibm_microservices_decoded.xml"
tags: ["cloud", "template", "architecture", "drawio", "infrastructure"]
---

# Ibm Microservices Flowchart

A flowchart diagram showing process flow and decision points

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=#4277BB;align=right;startSize=0;collapsible=0;strokeWidth=3;" parent="1" vertex="1">
      <mxGeometry x="247" y="140" width="1160" height="890" as="geometry"/>
    </mxCell>
    <mxCell id="3" value="PUBLIC NETWORK" style="text;html=1;align=left;verticalAlign=top;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=16;spacingLeft=5;" parent="2" vertex="1">
      <mxGeometry width="170" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="4" value="" style="line;strokeWidth=3;direction=south;html=1;shadow=0;labelBackgroundColor=none;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;align=right;strokeColor=#4277BB;" parent="2" vertex="1">
      <mxGeometry x="205" width="10" height="250" as="geometry"/>
    </mxCell>
    <mxCell id="5" value="PROVIDER CLOUD" style="text;html=1;align=left;verticalAlign=top;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=16;spacingLeft=5;" parent="2" vertex="1">
      <mxGeometry x="210" width="180" height="35" as="geometry"/>
    </mxCell>
    <mxCell id="6" value="Application component" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#EBC01A;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="2" vertex="1">
      <mxGeometry x="10" y="730" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="7" value="Infrastructure services" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#8DC642;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="2" vertex="1">
      <mxGeometry x="10" y="750" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="8" value="Management" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#0DB39D;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="2" vertex="1">
      <mxGeometry x="10" y="770" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="9" value="Data store" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#335D81;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="2" vertex="1">
      <mxGeometry x="10" y="790" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="10" value="Analytics" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#744399;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="2" vertex="1">
      <mxGeometry x="10" y="810" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="11" value="Device capabilities" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#A72870;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="2" vertex="1">
      <mxGeometry x="10" y="830" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="12" value="Security" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="2" vertex="1">
      <mxGeometry x="10" y="850" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="13" value="LEGEND" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=14;spacingLeft=0;" parent="2" vertex="1">
      <mxGeometry x="10" y="700" width="150" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="14" value="Users" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="2" vertex="1">
      <mxGeometry x="10" y="870" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="16" value="" style="line;strokeWidth=3;direction=south;html=1;shadow=0;labelBackgroundColor=none;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;align=right;strokeColor=#4277BB;" parent="2" vertex="1">
      <mxGeometry x="205" y="370" width="10" height="520" as="geometry"/>
    </mxCell>
    <mxCell id="17" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=#4277BB;align=right;startSize=0;collapsible=0;strokeWidth=3;" parent="2" vertex="1">
      <mxGeometry x="394" y="780" width="516" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="18" value="CLOUD SECURITY" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=left;shadow=0;dashed=0;image;image=img/lib/ibm/blockchain/certificate_authority.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;" parent="17" vertex="1">
      <mxGeometry x="34" y="15" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="19" style="edgeStyle=orthogonalEdgeStyle;rounded=0;comic=0;html=1;exitX=1;exitY=0.5;entryX=0;entryY=0.25;startArrow=classic;startFill=1;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#4378BB;strokeWidth=2;fontFamily=Helvetica;fontSize=19;fontColor=#CC99FF;endSize=4;startSize=4;" parent="2" source="20" target="26" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="155" y="106"/>
          <mxPoint x="155" y="283"/>
          <mxPoint x="180" y="283"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="20" value="CLOUD&lt;div&gt;USER&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/users/user.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="2" vertex="1">
      <mxGeometry x="55" y="76" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="21" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#4378BB;strokeWidth=2;fontSize=19;fontColor=#CC99FF;" parent="2" source="22" target="26" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="135" y="216"/>
          <mxPoint x="135" y="296"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="22" value="DEVICES" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/users/device.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="2" vertex="1">
      <mxGeometry x="55" y="186" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="23" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#4378BB;strokeWidth=2;fontSize=19;fontColor=#CC99FF;" parent="2" source="24" target="26" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="155" y="400"/>
          <mxPoint x="155" y="306"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="24" value="CLOUD" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/data/cloud.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="2" vertex="1">
      <mxGeometry x="55" y="370" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="25" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#4378BB;strokeWidth=2;fontSize=19;fontColor=#CC99FF;" parent="2" source="26" target="28" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="26" value="EDGE&lt;div&gt;SERVICES&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/edge_services.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="2" vertex="1">
      <mxGeometry x="180" y="266" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="27" style="edgeStyle=elbowEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#4378BB;strokeWidth=2;fontSize=19;fontColor=#CC99FF;elbow=vertical;" parent="2" source="28" target="35" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="380" y="296" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="376" y="296"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="28" value="CLOUD" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/management/api_management.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="2" vertex="1">
      <mxGeometry x="295" y="266" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="29" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=#4277BB;align=right;startSize=0;collapsible=0;strokeWidth=3;" parent="2" vertex="1">
      <mxGeometry x="394" y="44" width="516" height="141" as="geometry"/>
    </mxCell>
    <mxCell id="30" value="COLLABORATIVE&lt;div&gt;DEVELOPMENT&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/devops/collaborative_development.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="29" vertex="1">
      <mxGeometry x="34" y="32" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="31" value="CONTINUOUS&lt;div&gt;DEPLOY&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/devops/continuous_deploy.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="29" vertex="1">
      <mxGeometry x="162" y="32" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="32" value="CONFIGURATION&lt;div&gt;MANAGEMENT&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/devops/configuration_management.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="29" vertex="1">
      <mxGeometry x="289" y="32" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="33" value="CONTINUOUS&lt;div&gt;TESTING&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/devops/continuous_testing.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="29" vertex="1">
      <mxGeometry x="417" y="32" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="34" value="DevOps" style="text;html=1;align=left;verticalAlign=top;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=0;fontSize=14;spacingLeft=5;" parent="29" vertex="1">
      <mxGeometry width="90" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="35" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=#4277BB;align=right;startSize=0;collapsible=0;strokeWidth=3;" parent="2" vertex="1">
      <mxGeometry x="394" y="200" width="516" height="380" as="geometry"/>
    </mxCell>
    <mxCell id="52" value="CLOUD RUNTIME SERVICES" style="text;html=1;align=left;verticalAlign=top;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=0;fontSize=14;spacingLeft=5;" parent="35" vertex="1">
      <mxGeometry x="2" width="231" height="24" as="geometry"/>
    </mxCell>
    <mxCell id="84" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0;entryY=0.5;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#EEC11B;strokeWidth=2;fontSize=14;fontColor=#4277BB;" parent="35" source="65" target="68" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="90" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0.5;entryY=0;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#EEC11B;strokeWidth=2;fontSize=14;fontColor=#4277BB;" parent="35" source="65" target="72" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="65" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=#4277BB;align=right;startSize=0;collapsible=0;strokeWidth=3;" parent="35" vertex="1">
      <mxGeometry x="25" y="40" width="100" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="66" value="" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/microservice.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="65" vertex="1">
      <mxGeometry x="9" y="10" width="82" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="85" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0;entryY=0.5;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#EEC11B;strokeWidth=2;fontSize=14;fontColor=#4277BB;" parent="35" source="68" target="70" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="93" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0.5;entryY=0;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#EEC11B;strokeWidth=2;fontSize=14;fontColor=#4277BB;" parent="35" source="68" target="74" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="68" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=#4277BB;align=right;startSize=0;collapsible=0;strokeWidth=3;" parent="35" vertex="1">
      <mxGeometry x="209" y="40" width="100" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="69" value="" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/microservice.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="68" vertex="1">
      <mxGeometry x="9" y="10" width="82" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="94" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0.5;entryY=0;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#EEC11B;strokeWidth=2;fontSize=14;fontColor=#4277BB;" parent="35" source="70" target="76" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="70" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=#4277BB;align=right;startSize=0;collapsible=0;strokeWidth=3;" parent="35" vertex="1">
      <mxGeometry x="386" y="40" width="100" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="71" value="" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/microservice.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="70" vertex="1">
      <mxGeometry x="9" y="10" width="82" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="86" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0;entryY=0.5;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#EEC11B;strokeWidth=2;fontSize=14;fontColor=#4277BB;" parent="35" source="72" target="74" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="91" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0.5;entryY=0;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#EEC11B;strokeWidth=2;fontSize=14;fontColor=#4277BB;" parent="35" source="72" target="78" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="72" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=#4277BB;align=right;startSize=0;collapsible=0;strokeWidth=3;" parent="35" vertex="1">
      <mxGeometry x="24.99999999999996" y="160" width="100" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="73" value="" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/microservice.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="72" vertex="1">
      <mxGeometry x="9" y="10" width="82" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="87" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0;entryY=0.5;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#EEC11B;strokeWidth=2;fontSize=14;fontColor=#4277BB;" parent="35" source="74" target="76" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="92" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0.5;entryY=0;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#EEC11B;strokeWidth=2;fontSize=14;fontColor=#4277BB;" parent="35" source="74" target="80" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="74" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=#4277BB;align=right;startSize=0;collapsible=0;strokeWidth=3;" parent="35" vertex="1">
      <mxGeometry x="208.99999999999977" y="160" width="100" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="75" value="" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/microservice.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="74" vertex="1">
      <mxGeometry x="9" y="10" width="82" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="95" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0.5;entryY=0;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#EEC11B;strokeWidth=2;fontSize=14;fontColor=#4277BB;" parent="35" source="76" target="82" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="76" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=#4277BB;align=right;startSize=0;collapsible=0;strokeWidth=3;" parent="35" vertex="1">
      <mxGeometry x="386.00000000000017" y="160" width="100" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="77" value="" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/microservice.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="76" vertex="1">
      <mxGeometry x="9" y="10" width="82" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="88" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0;entryY=0.5;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#EEC11B;strokeWidth=2;fontSize=14;fontColor=#4277BB;" parent="35" source="78" target="80" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="78" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=#4277BB;align=right;startSize=0;collapsible=0;strokeWidth=3;" parent="35" vertex="1">
      <mxGeometry x="24.99999999999996" y="280" width="100" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="79" value="" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/microservice.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="78" vertex="1">
      <mxGeometry x="9" y="10" width="82" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="89" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0;entryY=0.5;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#EEC11B;strokeWidth=2;fontSize=14;fontColor=#4277BB;" parent="35" source="80" target="82" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="80" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=#4277BB;align=right;startSize=0;collapsible=0;strokeWidth=3;" parent="35" vertex="1">
      <mxGeometry x="208.99999999999977" y="280" width="100" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="81" value="" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/microservice.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="80" vertex="1">
      <mxGeometry x="9" y="10" width="82" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="82" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=#4277BB;align=right;startSize=0;collapsible=0;strokeWidth=3;" parent="35" vertex="1">
      <mxGeometry x="386.00000000000017" y="280" width="100" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="83" value="" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/microservice.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="82" vertex="1">
      <mxGeometry x="9" y="10" width="82" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="55" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=#4277BB;align=right;startSize=0;collapsible=0;strokeWidth=3;" parent="2" vertex="1">
      <mxGeometry x="394" y="596" width="516" height="164" as="geometry"/>
    </mxCell>
    <mxCell id="56" value="MONITORING &amp;amp;&lt;div&gt;LOGGING&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/monitoring_logging.svg;labelBackgroundColor=none;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="55" vertex="1">
      <mxGeometry x="34" y="44" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="57" value="SERVICE&lt;div&gt;REGISTRATION /&amp;nbsp;&lt;/div&gt;&lt;div&gt;DISCOVERY&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/service_discovery_configuration.svg;labelBackgroundColor=none;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="55" vertex="1">
      <mxGeometry x="162" y="44" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="58" value="LOAD&amp;nbsp;&lt;span&gt;BALANCING&lt;/span&gt;&lt;div&gt;ROUTING&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/load_balancing_routing.svg;labelBackgroundColor=none;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="55" vertex="1">
      <mxGeometry x="289" y="44" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="59" value="INTERSERVICE&lt;div&gt;COMMUNICATION&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/interservice_communication.svg;labelBackgroundColor=none;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="55" vertex="1">
      <mxGeometry x="417" y="44" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="60" value="INFRASTRUCTURE SERVICES" style="text;html=1;align=left;verticalAlign=top;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=0;fontSize=14;spacingLeft=5;" parent="55" vertex="1">
      <mxGeometry x="1" width="231" height="24" as="geometry"/>
    </mxCell>
    <mxCell id="61" style="edgeStyle=elbowEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#4378BB;strokeWidth=2;fontSize=19;fontColor=#CC99FF;elbow=vertical;" parent="2" source="62" target="35" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="930" y="330" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="982" y="322"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="62" value="TRANSFORMATION &amp;amp;&lt;div&gt;CONNECTIVITY&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/transformation_connectivity.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="2" vertex="1">
      <mxGeometry x="1051" y="290" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="63" style="edgeStyle=elbowEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#4378BB;strokeWidth=2;fontSize=19;fontColor=#CC99FF;elbow=vertical;" parent="2" source="64" target="35" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="930" y="438" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="981" y="438"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="64" value="CLOUD DATA&lt;div&gt;SERVICES&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/data/enterprise_data.svg;labelBackgroundColor=#ffffff;strokeColor=#666666;strokeWidth=3;fillColor=#C2952D;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="2" vertex="1">
      <mxGeometry x="1051" y="408" width="60" height="60" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
