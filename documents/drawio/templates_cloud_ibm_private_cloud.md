---
title: "Ibm Private Cloud Flowchart"
description: "A flowchart diagram showing process flow and decision points"
category: "templates/cloud"
type: "flowchart"
source_file: "templates/cloud/ibm_private_cloud_decoded.xml"
tags: ["cloud", "template", "architecture", "drawio", "infrastructure"]
---

# Ibm Private Cloud Flowchart

A flowchart diagram showing process flow and decision points

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="63" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=none;align=right;startSize=0;collapsible=0;noLabel=1;strokeWidth=3;" parent="1" vertex="1">
      <mxGeometry x="37" y="110" width="1580" height="951" as="geometry"/>
    </mxCell>
    <mxCell id="98" value="" style="swimlane;shadow=0;labelBackgroundColor=#007FFF;strokeColor=#4277BB;fillColor=none;gradientColor=none;fontColor=#000000;align=right;collapsible=0;startSize=0;strokeWidth=3;" parent="63" vertex="1">
      <mxGeometry x="838" y="771" width="142" height="159" as="geometry"/>
    </mxCell>
    <mxCell id="180" value="PROVISION" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/devops/provision.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="98" vertex="1">
      <mxGeometry x="42" y="44" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="184" value="INFRASTRUCTURE&lt;div&gt;AUTOMATION&lt;/div&gt;" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=12;spacingLeft=5;" parent="98" vertex="1">
      <mxGeometry x="7" y="10" width="123" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="102" value="PUBLIC CLOUD" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=16;spacingLeft=5;" parent="63" vertex="1">
      <mxGeometry y="10" width="150" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="103" value="" style="line;strokeWidth=3;direction=south;html=1;shadow=0;labelBackgroundColor=none;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;align=right;strokeColor=#4277BB;" parent="63" vertex="1">
      <mxGeometry x="175" y="1" width="10" height="169" as="geometry"/>
    </mxCell>
    <mxCell id="106" value="" style="line;strokeWidth=3;direction=south;html=1;shadow=0;labelBackgroundColor=none;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;align=right;strokeColor=#4277BB;" parent="63" vertex="1">
      <mxGeometry x="1410" width="10" height="430" as="geometry"/>
    </mxCell>
    <mxCell id="107" value="IBM CLOUD PRIVATE" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=16;spacingLeft=5;" parent="63" vertex="1">
      <mxGeometry x="190" y="10" width="150" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="108" value="ENTERPRISE" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=16;spacingLeft=5;" parent="63" vertex="1">
      <mxGeometry x="1420" y="10" width="140" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="109" value="Application component" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#EBC01A;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="63" vertex="1">
      <mxGeometry x="15" y="781" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="110" value="Infrastructure services" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#8DC642;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="63" vertex="1">
      <mxGeometry x="15" y="801" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="111" value="Management" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#0DB39D;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="63" vertex="1">
      <mxGeometry x="15" y="821" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="112" value="Data store" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#335D81;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="63" vertex="1">
      <mxGeometry x="15" y="841" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="113" value="Analytics" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#744399;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="63" vertex="1">
      <mxGeometry x="15" y="861" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="114" value="Device capabilities" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#A72870;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="63" vertex="1">
      <mxGeometry x="15" y="881" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="115" value="Security" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="63" vertex="1">
      <mxGeometry x="15" y="901" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="117" value="LEGEND" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=14;spacingLeft=0;" parent="63" vertex="1">
      <mxGeometry x="15" y="751" width="150" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="189" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;strokeWidth=2;fontSize=12;fontColor=#4277BB;" parent="63" target="119" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="270" y="219.71428571428578" as="sourcePoint"/>
        <Array as="points">
          <mxPoint x="250" y="220"/>
          <mxPoint x="250" y="220"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="123" value="" style="swimlane;shadow=0;labelBackgroundColor=#007FFF;strokeColor=#4277BB;fillColor=none;gradientColor=none;fontColor=#000000;align=right;collapsible=0;startSize=0;strokeWidth=3;" parent="63" vertex="1">
      <mxGeometry x="270" y="70" width="880" height="300" as="geometry"/>
    </mxCell>
    <mxCell id="125" value="" style="swimlane;shadow=0;labelBackgroundColor=#007FFF;strokeColor=#4277BB;fillColor=none;gradientColor=none;fontColor=#000000;align=right;collapsible=0;startSize=0;strokeWidth=3;" parent="123" vertex="1">
      <mxGeometry x="10" y="50" width="220" height="240" as="geometry"/>
    </mxCell>
    <mxCell id="192" style="rounded=0;html=1;labelBackgroundColor=#ffffff;startArrow=none;startFill=0;startSize=4;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;strokeWidth=2;fontSize=12;fontColor=#4277BB;endArrow=none;endFill=0;" parent="125" source="120" target="127" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="193" style="edgeStyle=none;rounded=0;html=1;labelBackgroundColor=#ffffff;startArrow=none;startFill=0;startSize=4;endArrow=none;endFill=0;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;strokeWidth=2;fontSize=12;fontColor=#4277BB;" parent="125" source="120" target="128" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="120" value="MICROSERVICE" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/enterprise_applications.svg;labelBackgroundColor=#ffffff;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=10;fontColor=#4277BB;verticalAlign=top;" parent="125" vertex="1">
      <mxGeometry x="45" y="94" width="30" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="194" style="edgeStyle=none;rounded=0;html=1;labelBackgroundColor=#ffffff;startArrow=none;startFill=0;startSize=4;endArrow=none;endFill=0;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;strokeWidth=2;fontSize=12;fontColor=#4277BB;" parent="125" source="128" target="127" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="128" value="MICROSERVICE" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/enterprise_applications.svg;labelBackgroundColor=#ffffff;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=10;fontColor=#4277BB;verticalAlign=top;" parent="125" vertex="1">
      <mxGeometry x="153" y="146" width="30" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="127" value="MICROSERVICE" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/enterprise_applications.svg;labelBackgroundColor=#ffffff;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=10;fontColor=#4277BB;verticalAlign=top;" parent="125" vertex="1">
      <mxGeometry x="153" y="39" width="30" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="140" value="CLOUD NATIVE" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=12;spacingLeft=5;" parent="125" vertex="1">
      <mxGeometry x="6" y="8.00000000000025" width="150" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="126" value="" style="swimlane;shadow=0;labelBackgroundColor=#007FFF;strokeColor=#4277BB;fillColor=none;gradientColor=none;fontColor=#000000;align=right;collapsible=0;startSize=0;strokeWidth=3;" parent="123" vertex="1">
      <mxGeometry x="242" y="50" width="236" height="240" as="geometry"/>
    </mxCell>
    <mxCell id="122" value="APP&lt;div&gt;SERVER&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/app_server.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;verticalAlign=top;" parent="126" vertex="1">
      <mxGeometry x="39" y="37" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="121" value="BLOCKCHAIN" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/blockchain/blockchain.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;verticalAlign=top;" parent="126" vertex="1">
      <mxGeometry x="148" y="37" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="131" value="TRANSFORMATION&lt;div&gt;&amp;amp; CONNECTIVITY&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/transformation_connectivity.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;verticalAlign=top;" parent="126" vertex="1">
      <mxGeometry x="39" y="138" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="132" value="OTHER&lt;div&gt;WORKLOADS&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/data/data_services.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;verticalAlign=top;" parent="126" vertex="1">
      <mxGeometry x="148" y="138" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="141" value="CONTAINERIZED MIDDLEWARE" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=12;spacingLeft=5;" parent="126" vertex="1">
      <mxGeometry x="5" y="8" width="195" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="130" value="" style="swimlane;shadow=0;labelBackgroundColor=#007FFF;strokeColor=#4277BB;fillColor=none;gradientColor=none;fontColor=#000000;align=right;collapsible=0;startSize=0;strokeWidth=3;" parent="123" vertex="1">
      <mxGeometry x="491" y="50" width="159" height="240" as="geometry"/>
    </mxCell>
    <mxCell id="133" value="CACHES" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/data/caches.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="130" vertex="1">
      <mxGeometry x="9" y="37" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="134" value="DATABASES" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/data/data_services.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="130" vertex="1">
      <mxGeometry x="89" y="37" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="135" value="ANALYTICS" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/analytics/analytics.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="130" vertex="1">
      <mxGeometry x="47" y="138" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="142" value="DATA WORKLOADS" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=12;spacingLeft=5;" parent="130" vertex="1">
      <mxGeometry x="7" y="8" width="150" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="187" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;exitX=0.75;exitY=0;entryX=0.75;entryY=0;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#EDC11C;strokeWidth=2;fontSize=12;fontColor=#4277BB;" parent="130" source="142" target="142" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="136" value="" style="swimlane;shadow=0;labelBackgroundColor=#007FFF;strokeColor=#4277BB;fillColor=none;gradientColor=none;fontColor=#000000;align=right;collapsible=0;startSize=0;strokeWidth=3;" parent="123" vertex="1">
      <mxGeometry x="661" y="50" width="199" height="240" as="geometry"/>
    </mxCell>
    <mxCell id="137" value="AUTOMATION&lt;div&gt;TOOLS&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/automation_tools.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="136" vertex="1">
      <mxGeometry x="27" y="37" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="138" value="OPENSOURCE&lt;div&gt;TOOLS&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/open_source_tools.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="136" vertex="1">
      <mxGeometry x="119" y="37" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="143" value="DEVOPS &amp;amp; TOOLS" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=12;spacingLeft=5;" parent="136" vertex="1">
      <mxGeometry x="7" y="8" width="150" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="186" value="WORKLOADS" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=14;spacingLeft=5;" parent="123" vertex="1">
      <mxGeometry x="20" y="11" width="150" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="118" value="COGNITIVE&lt;div&gt;SERVICES&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;image;image=img/lib/ibm/miscellaneous/cognitive_services.svg;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#808080;gradientColor=none;fontSize=12;fontColor=#4277BB;rounded=0;verticalAlign=top;spacingLeft=5;" parent="63" vertex="1">
      <mxGeometry x="45" y="190.00000000000006" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="188" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;strokeWidth=2;fontSize=12;fontColor=#4277BB;" parent="63" source="119" target="118" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="119" value="EDGE&lt;div&gt;SERVICES&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;image;image=img/lib/ibm/infrastructure/edge_services.svg;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#808080;gradientColor=none;fontSize=12;fontColor=#4277BB;rounded=0;verticalAlign=top;spacingLeft=5;" parent="63" vertex="1">
      <mxGeometry x="150" y="190" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="144" value="" style="swimlane;shadow=0;labelBackgroundColor=#007FFF;strokeColor=#4277BB;fillColor=none;gradientColor=none;fontColor=#000000;align=right;collapsible=0;startSize=0;strokeWidth=3;" parent="63" vertex="1">
      <mxGeometry x="1165" y="69" width="205" height="301" as="geometry"/>
    </mxCell>
    <mxCell id="145" value="DEVELOPER AUTOMATION" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=14;spacingLeft=5;" parent="144" vertex="1">
      <mxGeometry x="6" y="12" width="194" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="146" value="SERVICE&lt;div&gt;BROKER&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/service_broker.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="144" vertex="1">
      <mxGeometry x="107" y="61" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="148" value="PROVISION" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/devops/provision.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="144" vertex="1">
      <mxGeometry x="32" y="132" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="149" value="CONTAINER&lt;div&gt;CATALOG&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/management/content_management.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="144" vertex="1">
      <mxGeometry x="107" y="197" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="150" value="ENTERPRISE&lt;div&gt;MIDDLEWARE&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/enterprise_applications.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="63" vertex="1">
      <mxGeometry x="1490" y="377" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="151" value="TRANSFORMATION&lt;div&gt;&amp;amp; CONNECTIVITY&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/transformation_connectivity.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="63" vertex="1">
      <mxGeometry x="1385" y="445" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="152" value="ENTERPRISE&lt;div&gt;DATA&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/data/enterprise_data.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="63" vertex="1">
      <mxGeometry x="1490" y="527" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="159" value="IBM&lt;div&gt;PUBLIC&lt;/div&gt;&lt;div&gt;CLOUD&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;image;image=img/lib/ibm/miscellaneous/ibm_public_cloud.svg;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#808080;gradientColor=none;fontSize=12;fontColor=#4277BB;rounded=0;verticalAlign=top;spacingLeft=5;" parent="63" vertex="1">
      <mxGeometry x="45" y="370" width="60" height="46" as="geometry"/>
    </mxCell>
    <mxCell id="160" value="IoT&lt;div&gt;CLOUD&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;image;image=img/lib/ibm/miscellaneous/ibm_public_cloud.svg;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#808080;gradientColor=none;fontSize=12;fontColor=#4277BB;rounded=0;verticalAlign=top;spacingLeft=5;labelPosition=center;verticalLabelPosition=bottom;" parent="63" vertex="1">
      <mxGeometry x="45" y="474" width="60" height="46" as="geometry"/>
    </mxCell>
    <mxCell id="161" value="SERVICES" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;image;image=img/lib/ibm/blockchain/services.svg;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#808080;gradientColor=none;fontSize=12;fontColor=#4277BB;rounded=0;verticalAlign=top;spacingLeft=5;" parent="63" vertex="1">
      <mxGeometry x="45" y="590" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="162" value="" style="swimlane;shadow=1;labelBackgroundColor=#007FFF;strokeColor=#4277BB;fillColor=none;gradientColor=none;fontColor=#000000;align=right;collapsible=0;startSize=0;strokeWidth=3;swimlaneFillColor=#ffffff;" parent="63" vertex="1">
      <mxGeometry x="280" y="580" width="190" height="140" as="geometry"/>
    </mxCell>
    <mxCell id="163" value="RUNTIME" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/runtime_services.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="162" vertex="1">
      <mxGeometry x="18" y="35" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="164" value="SERVICES" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/blockchain/services.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="162" vertex="1">
      <mxGeometry x="103" y="35" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="181" value="PaaS (Platform as a Service)" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=12;spacingLeft=5;" parent="162" vertex="1">
      <mxGeometry x="5" y="7" width="150" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="165" value="" style="swimlane;shadow=1;labelBackgroundColor=#007FFF;strokeColor=#4277BB;fillColor=none;gradientColor=none;fontColor=#000000;align=right;collapsible=0;startSize=0;strokeWidth=3;swimlaneFillColor=#ffffff;" parent="63" vertex="1">
      <mxGeometry x="581" y="580" width="680" height="140" as="geometry"/>
    </mxCell>
    <mxCell id="168" value="CONTAINER&lt;div&gt;ORCHESTRATION&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/devops/release_management.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="165" vertex="1">
      <mxGeometry x="30" y="34" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="169" value="CLUSTER&lt;div&gt;MANAGEMENT&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/management/cluster_management.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="165" vertex="1">
      <mxGeometry x="127" y="34" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="170" value="CONTAINER&lt;div&gt;SECURITY&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/blockchain/certificate_authority.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="165" vertex="1">
      <mxGeometry x="220" y="34" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="171" value="IMAGE&lt;div&gt;REPOSITORY&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/data/file_repository.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="165" vertex="1">
      <mxGeometry x="320" y="34" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="172" value="ROUTING&lt;div&gt;SERVICES&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/load_balancing_routing.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="165" vertex="1">
      <mxGeometry x="415" y="34" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="173" value="MICROSERVICES&lt;div&gt;MESH&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/microservices_mesh.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="165" vertex="1">
      <mxGeometry x="530" y="34.00000000000006" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="182" value="CaaS (Container as a Service)" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=14;spacingLeft=5;" parent="165" vertex="1">
      <mxGeometry x="52" y="7" width="150" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="174" value="" style="swimlane;shadow=0;labelBackgroundColor=#007FFF;strokeColor=#4277BB;fillColor=none;gradientColor=none;fontColor=#000000;align=right;collapsible=0;startSize=0;strokeWidth=3;" parent="63" vertex="1">
      <mxGeometry x="275" y="771" width="475" height="159" as="geometry"/>
    </mxCell>
    <mxCell id="175" value="EXISTING&lt;div&gt;ENTERPRISE&lt;/div&gt;&lt;div&gt;SYSTEMS&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/blockchain/existing_enterprise_systems.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="174" vertex="1">
      <mxGeometry x="20" y="44" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="176" value="INFRASTRUCTURE&lt;div&gt;SERVICES&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/infrastructure_services.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="174" vertex="1">
      <mxGeometry x="113" y="44" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="177" value="DATA&lt;div&gt;SOURCES&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/data/data_sources.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="174" vertex="1">
      <mxGeometry x="205" y="44" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="178" value="ROUTING&lt;div&gt;SERVICES&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/load_balancing_routing.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="174" vertex="1">
      <mxGeometry x="298" y="44" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="179" value="CONTAINER&lt;div&gt;SECURITY&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/blockchain/certificate_authority.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="174" vertex="1">
      <mxGeometry x="390" y="44" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="183" value="INFRASTRUCTURE" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=12;spacingLeft=5;" parent="174" vertex="1">
      <mxGeometry x="8" y="5" width="150" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="185" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;exitX=0.75;exitY=0;entryX=0.75;entryY=0;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#EDC11C;strokeWidth=2;fontSize=12;fontColor=#4277BB;" parent="63" source="118" target="118" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="190" value="" style="line;strokeWidth=3;direction=south;html=1;shadow=0;labelBackgroundColor=none;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;align=right;strokeColor=#4277BB;" parent="63" vertex="1">
      <mxGeometry x="175" y="300" width="10" height="650" as="geometry"/>
    </mxCell>
    <mxCell id="153" value="" style="swimlane;shadow=0;labelBackgroundColor=#007FFF;strokeColor=#4277BB;fillColor=none;gradientColor=none;fontColor=#000000;align=right;collapsible=0;startSize=0;strokeWidth=3;" parent="63" vertex="1">
      <mxGeometry x="280" y="407" width="850" height="133" as="geometry"/>
    </mxCell>
    <mxCell id="154" value="NEXT GENERATION MANAGEMENT" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=12;spacingLeft=5;" parent="153" vertex="1">
      <mxGeometry x="6" y="10" width="245" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="155" value="CLOUD&lt;div&gt;MANAGEMENT&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/management/cloud_management.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="153" vertex="1">
      <mxGeometry x="237" y="24" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="156" value="LOGGING" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/monitoring_logging.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="153" vertex="1">
      <mxGeometry x="334" y="24" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="157" value="MONITORING" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/monitoring.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="153" vertex="1">
      <mxGeometry x="431" y="24" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="158" value="DASHBOARD" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/dashboard.svg;labelBackgroundColor=none;strokeColor=#4277BB;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;" parent="153" vertex="1">
      <mxGeometry x="528" y="24" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="197" style="edgeStyle=none;rounded=0;html=1;entryX=0;entryY=0.5;labelBackgroundColor=#ffffff;startArrow=none;startFill=0;startSize=4;endArrow=none;endFill=0;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;strokeWidth=2;fontSize=12;fontColor=#4277BB;" parent="63" source="195" target="196" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="195" value="" style="shape=partialRectangle;whiteSpace=wrap;html=1;left=0;right=1;top=1;bottom=1;fillColor=none;routingCenterX=-0.5;shadow=0;labelBackgroundColor=#ffffff;strokeColor=#4277BB;strokeWidth=2;fontSize=12;fontColor=#4277BB;align=center;" parent="63" vertex="1">
      <mxGeometry x="460" y="570" width="20" height="160" as="geometry"/>
    </mxCell>
    <mxCell id="196" value="" style="shape=partialRectangle;whiteSpace=wrap;html=1;left=1;right=0;top=1;bottom=1;fillColor=none;routingCenterX=-0.5;shadow=0;labelBackgroundColor=#ffffff;strokeColor=#4277BB;strokeWidth=2;fontSize=12;fontColor=#4277BB;align=center;" parent="63" vertex="1">
      <mxGeometry x="569" y="570" width="21" height="160" as="geometry"/>
    </mxCell>
    <mxCell id="198" style="edgeStyle=elbowEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;startArrow=none;startFill=0;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;strokeWidth=2;fontSize=12;fontColor=#4277BB;entryX=1.003;entryY=0.464;entryPerimeter=0;elbow=vertical;" parent="63" source="180" target="174" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="780" y="871" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="199" style="edgeStyle=elbowEdgeStyle;rounded=0;elbow=vertical;html=1;entryX=1.002;entryY=0.472;entryPerimeter=0;labelBackgroundColor=#ffffff;startArrow=none;startFill=0;startSize=4;endArrow=classic;endFill=1;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;strokeWidth=2;fontSize=12;fontColor=#4277BB;" parent="63" source="148" target="136" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="200" value="" style="line;strokeWidth=3;direction=south;html=1;shadow=0;labelBackgroundColor=none;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;align=right;strokeColor=#4277BB;" parent="63" vertex="1">
      <mxGeometry x="1410" y="546" width="10" height="404" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
