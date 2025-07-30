---
title: "Sipoc Diagram Flowchart"
description: "A flowchart diagram showing process flow and decision points"
category: "templates/business"
type: "flowchart"
source_file: "templates/business/sipoc_diagram_decoded.xml"
tags: ["logic", "process", "template", "venn", "business", "drawio", "workflow"]
---

# Sipoc Diagram Flowchart

A flowchart diagram showing process flow and decision points

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="619" value="&lt;br style=&quot;font-size: 12px;&quot;&gt;Manufacturer&lt;br style=&quot;font-size: 12px;&quot;&gt;&lt;br style=&quot;font-size: 12px;&quot;&gt;Car Dealer&lt;br style=&quot;font-size: 12px;&quot;&gt;&lt;br style=&quot;font-size: 12px;&quot;&gt;Gas/Recharging&lt;br style=&quot;font-size: 12px;&quot;&gt;Station&lt;br style=&quot;font-size: 12px;&quot;&gt;&lt;br style=&quot;font-size: 12px;&quot;&gt;Car Wash" style="html=1;labelBackgroundColor=none;strokeColor=none;fillColor=#BAC8D3;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;labelPosition=center;verticalLabelPosition=middle;verticalAlign=top;opacity=30;whiteSpace=wrap;spacingLeft=10;spacingRight=10;fontStyle=0;spacingTop=-5;" parent="1" vertex="1">
      <mxGeometry x="62.5" y="208.5" width="162" height="460" as="geometry"/>
    </mxCell>
    <mxCell id="620" value="INPUTS" style="shape=step;whiteSpace=wrap;strokeColor=none;fillColor=#23445D;fontColor=#FFFFFF;fontStyle=0;html=1;fontSize=14;size=0.1" parent="1" vertex="1">
      <mxGeometry x="235.5" y="158.5" width="180" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="621" value="PROCESS" style="shape=step;whiteSpace=wrap;strokeColor=none;fillColor=#23445D;fontColor=#FFFFFF;fontStyle=0;html=1;fontSize=14;size=0.1" parent="1" vertex="1">
      <mxGeometry x="408.5000000000002" y="158.49999999999994" width="180" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="622" value="OUTPUTS" style="shape=step;whiteSpace=wrap;strokeColor=none;fillColor=#23445D;fontColor=#FFFFFF;fontStyle=0;html=1;fontSize=14;size=0.1" parent="1" vertex="1">
      <mxGeometry x="581.5" y="158.5" width="180" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="623" value="CUSTOMERS" style="shape=step;whiteSpace=wrap;strokeColor=none;fillColor=#23445D;fontColor=#FFFFFF;fontStyle=0;html=1;fontSize=14;size=0.1;" parent="1" vertex="1">
      <mxGeometry x="754.5" y="158.5" width="180" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="624" value="REQUIREMENTS" style="shape=step;whiteSpace=wrap;strokeColor=none;fillColor=#23445D;fontColor=#FFFFFF;fontStyle=0;html=1;fontSize=14;size=0.1" parent="1" vertex="1">
      <mxGeometry x="927.5" y="158.5" width="179" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="625" value="&lt;span style=&quot;font-weight: normal&quot;&gt;&lt;font style=&quot;font-size: 14px;&quot;&gt;SUPPLIER&lt;/font&gt;&lt;/span&gt;" style="shape=step;whiteSpace=wrap;strokeColor=none;fillColor=#23445D;fontColor=#FFFFFF;fontStyle=0;html=1;fontSize=14;size=0.1" parent="1" vertex="1">
      <mxGeometry x="62.5" y="158.5" width="180" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="626" style="edgeStyle=orthogonalEdgeStyle;curved=1;jumpSize=0;html=1;exitX=0.75;exitY=0;entryX=0.75;entryY=0;labelBackgroundColor=none;endArrow=open;endFill=0;jettySize=auto;orthogonalLoop=1;strokeColor=#23445D;strokeWidth=1;fillColor=#2F5B7C;fontFamily=Helvetica;fontSize=14;fontColor=#23445D;" parent="1" source="625" target="625" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="627" value="&#10;Vehicles&#10;&#10;Optional Packages&#10;&#10;Fuel Type&#10;&#10;Gas/Recharging&#10; Sations" style="text;spacingTop=-5;fontSize=12;fontFamily=Helvetica;fontColor=#23445D;fontStyle=0;html=1;align=center;fillColor=#BAC8D3;opacity=30;whiteSpace=wrap;spacingLeft=10;spacingRight=10;" parent="1" vertex="1">
      <mxGeometry x="235.5" y="208.5" width="162" height="460" as="geometry"/>
    </mxCell>
    <mxCell id="628" value="&lt;br style=&quot;font-size: 12px;&quot;&gt;New Customer Account&lt;br style=&quot;font-size: 12px;&quot;&gt;&lt;br style=&quot;font-size: 12px;&quot;&gt;Registration Document&lt;br style=&quot;font-size: 12px;&quot;&gt;&lt;br style=&quot;font-size: 12px;&quot;&gt;Sales Invoice&lt;br style=&quot;font-size: 12px;&quot;&gt;&lt;br style=&quot;font-size: 12px;&quot;&gt;Purchase Order&lt;br style=&quot;font-size: 12px;&quot;&gt;&lt;br style=&quot;font-size: 12px;&quot;&gt;Payment&lt;br style=&quot;font-size: 12px;&quot;&gt;&lt;br style=&quot;font-size: 12px;&quot;&gt;Service Contract&lt;br style=&quot;font-size: 12px;&quot;&gt;&lt;br style=&quot;font-size: 12px;&quot;&gt;Service Booklet" style="text;spacingTop=-5;fontSize=12;fontFamily=Helvetica;fontColor=#23445D;fontStyle=0;html=1;align=center;fillColor=#BAC8D3;opacity=30;whiteSpace=wrap;spacingLeft=10;spacingRight=10;" parent="1" vertex="1">
      <mxGeometry x="581.5" y="208.5" width="162" height="460" as="geometry"/>
    </mxCell>
    <mxCell id="629" value="&lt;br style=&quot;font-size: 12px;&quot;&gt;Car Buyer&lt;br style=&quot;font-size: 12px;&quot;&gt;&lt;br style=&quot;font-size: 12px;&quot;&gt;Dealerhip&lt;br style=&quot;font-size: 12px;&quot;&gt;&lt;br style=&quot;font-size: 12px;&quot;&gt;Department of Motor&lt;br style=&quot;font-size: 12px;&quot;&gt;Vehicles&lt;br style=&quot;font-size: 12px;&quot;&gt;&lt;br style=&quot;font-size: 12px;&quot;&gt;Service Department" style="text;spacingTop=-5;fontSize=12;fontFamily=Helvetica;fontColor=#23445D;fontStyle=0;html=1;align=center;fillColor=#BAC8D3;opacity=30;whiteSpace=wrap;spacingLeft=10;spacingRight=10;" parent="1" vertex="1">
      <mxGeometry x="754.5" y="208.5" width="162" height="460" as="geometry"/>
    </mxCell>
    <mxCell id="630" value="&lt;br style=&quot;font-size: 12px;&quot;&gt;Color Selection&lt;br style=&quot;font-size: 12px;&quot;&gt;&lt;br style=&quot;font-size: 12px;&quot;&gt;Build To Order&lt;br style=&quot;font-size: 12px;&quot;&gt;&lt;br style=&quot;font-size: 12px;&quot;&gt;Paperwork Filed&lt;br style=&quot;font-size: 12px;&quot;&gt;&lt;br style=&quot;font-size: 12px;&quot;&gt;Money Orders" style="text;spacingTop=-5;fontSize=12;fontFamily=Helvetica;fontColor=#23445D;fontStyle=0;html=1;align=center;fillColor=#BAC8D3;opacity=30;whiteSpace=wrap;spacingLeft=10;spacingRight=10;" parent="1" vertex="1">
      <mxGeometry x="927.5" y="208.5" width="162" height="460" as="geometry"/>
    </mxCell>
    <mxCell id="631" value="Meet Customer" style="whiteSpace=wrap;html=1;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;fillColor=#BAC8D3;strokeColor=none;spacing=5;opacity=30;" parent="1" vertex="1">
      <mxGeometry x="408.70731707317077" y="208.5" width="162" height="59.26829268292683" as="geometry"/>
    </mxCell>
    <mxCell id="632" value="Understand Customer Needs" style="whiteSpace=wrap;html=1;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;fillColor=#BAC8D3;strokeColor=none;spacing=5;opacity=30;" parent="1" vertex="1">
      <mxGeometry x="408.70731707317077" y="288.5" width="162" height="59.26829268292683" as="geometry"/>
    </mxCell>
    <mxCell id="633" value="" style="endArrow=classic;html=1;strokeColor=#23445D;endFill=1;fontColor=#23445D;" parent="1" source="631" target="632" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="634" value="Present Vehicles Mathing Clients Needs" style="whiteSpace=wrap;html=1;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;fillColor=#BAC8D3;strokeColor=none;opacity=30;" parent="1" vertex="1">
      <mxGeometry x="408.70731707317077" y="368.5" width="162" height="59.26829268292683" as="geometry"/>
    </mxCell>
    <mxCell id="635" value="" style="endArrow=classic;html=1;strokeColor=#23445D;endFill=1;fontColor=#23445D;" parent="1" source="632" target="634" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="636" value="Present Optional Packages for Vehicle" style="whiteSpace=wrap;html=1;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;fillColor=#BAC8D3;strokeColor=none;spacing=5;opacity=30;" parent="1" vertex="1">
      <mxGeometry x="408.70731707317077" y="448.5" width="162" height="59.26829268292683" as="geometry"/>
    </mxCell>
    <mxCell id="637" value="" style="endArrow=classic;html=1;strokeColor=#23445D;endFill=1;fontColor=#23445D;" parent="1" source="634" target="636" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="638" value="Test Drive Vehicle" style="whiteSpace=wrap;html=1;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;fillColor=#BAC8D3;strokeColor=none;spacing=5;opacity=30;" parent="1" vertex="1">
      <mxGeometry x="408.70731707317077" y="528.5" width="162" height="59.26829268292683" as="geometry"/>
    </mxCell>
    <mxCell id="639" value="" style="endArrow=classic;html=1;strokeColor=#23445D;endFill=1;fontColor=#23445D;" parent="1" source="636" target="638" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="640" value="Sign Paperwork &#10;and Give Keys" style="whiteSpace=wrap;html=1;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;fillColor=#BAC8D3;strokeColor=none;spacing=5;opacity=30;" parent="1" vertex="1">
      <mxGeometry x="408.5" y="608.5" width="162" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="641" value="" style="endArrow=classic;html=1;strokeColor=#23445D;endFill=1;fontColor=#23445D;" parent="1" source="638" target="640" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
