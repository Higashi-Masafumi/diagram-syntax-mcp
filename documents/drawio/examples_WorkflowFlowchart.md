---
title: "Workflowflowchart Flowchart"
description: "A flowchart diagram showing process flow and decision points"
category: "examples"
type: "flowchart"
source_file: "examples/WorkflowFlowchart_decoded.xml"
tags: ["process", "flowchart", "sample", "drawio", "example"]
---

# Workflowflowchart Flowchart

A flowchart diagram showing process flow and decision points

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1086" dy="613" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1" pageWidth="826" pageHeight="1169" background="#ffffff" math="0" shadow="0">
  <root>
    <mxCell id="0" style=";html=1;"/>
    <mxCell id="1" style=";html=1;" parent="0"/>
    <mxCell id="2" value="&lt;font color=&quot;#23497d&quot;&gt;Inside Sales Rep&lt;/font&gt;" style="swimlane;whiteSpace=wrap;fillColor=#D4E1F5;swimlaneFillColor=#D4E1F5;fontColor=#660000;fontFamily=Tahoma;html=1;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="20" y="20" width="160" height="610" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="8" value="Customer Management" style="whiteSpace=wrap;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;plain-purple;strokeColor=none;fillColor=#23497D;gradientColor=none;" parent="2" vertex="1">
      <mxGeometry x="10" y="100" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="9" value="Credit Management" style="whiteSpace=wrap;strokeColor=none;fillColor=#23497D;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;" parent="2" vertex="1">
      <mxGeometry x="20" y="375" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="10" value="Price Management" style="whiteSpace=wrap;strokeColor=none;fillColor=#23497D;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;" parent="2" vertex="1">
      <mxGeometry x="20" y="485" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="34" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="2" source="9" target="10" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="170" y="397.5" as="sourcePoint"/>
        <mxPoint x="270" y="472.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="33" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="2" source="8" target="9" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="160" y="110" as="sourcePoint"/>
        <mxPoint x="260" y="185" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="3" value="&lt;font color=&quot;#23497d&quot;&gt;Inside Sales Manager&lt;/font&gt;" style="swimlane;whiteSpace=wrap;fillColor=#E6EFFF;swimlaneFillColor=#E6EFFF;fontColor=#660000;fontFamily=Tahoma;html=1;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="820" y="20" width="160" height="610" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="21" value="Sales Contract" style="shape=document;whiteSpace=wrap;verticalAlign=top;strokeColor=none;fillColor=#67B1E1;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;" parent="3" vertex="1">
      <mxGeometry x="20" y="50" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="22" value="Bills" style="shape=document;whiteSpace=wrap;verticalAlign=top;strokeColor=none;fillColor=#67B1E1;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;" parent="3" vertex="1">
      <mxGeometry x="20" y="500" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="23" value="Cost Allocation" style="whiteSpace=wrap;strokeColor=none;fillColor=#23497D;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;" parent="3" vertex="1">
      <mxGeometry x="20" y="305" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="4" value="&lt;font color=&quot;#23497d&quot;&gt;VP Sales&lt;/font&gt;" style="swimlane;whiteSpace=wrap;fillColor=#D4E1F5;swimlaneFillColor=#D4E1F5;fontColor=#660000;fontFamily=Tahoma;html=1;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="660" y="20" width="160" height="610" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="19" value="Outbound Accounting" style="whiteSpace=wrap;fillColor=#23497D;strokeColor=none;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;" parent="4" vertex="1">
      <mxGeometry x="20" y="160" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="20" value="Account Processing" style="whiteSpace=wrap;strokeColor=none;fillColor=#23497D;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;" parent="4" vertex="1">
      <mxGeometry x="20" y="420" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="5" value="&lt;font color=&quot;#23497d&quot;&gt;Sales Admin&lt;/font&gt;" style="swimlane;whiteSpace=wrap;fillColor=#E6EFFF;swimlaneFillColor=#E6EFFF;fontColor=#660000;fontFamily=Tahoma;html=1;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="180" y="20" width="160" height="610" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="11" value="Material Requirements Planning Operation" style="whiteSpace=wrap;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;plain-purple;strokeColor=none;fillColor=#23497D;gradientColor=none;" parent="5" vertex="1">
      <mxGeometry x="20" y="165" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="12" value="&lt;font color=&quot;#ffffff&quot;&gt;Facilities Procurement&lt;br&gt;Application&lt;/font&gt;&lt;br&gt; " style="shape=document;whiteSpace=wrap;verticalAlign=top;strokeColor=none;fillColor=#67B1E1;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;" parent="5" vertex="1">
      <mxGeometry x="20" y="265" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="32" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="5" source="11" target="12" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="-10" y="100" as="sourcePoint"/>
        <mxPoint x="90" y="175" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="6" value="&lt;font color=&quot;#23497d&quot;&gt;Sales Representative&lt;/font&gt;" style="swimlane;whiteSpace=wrap;fillColor=#D4E1F5;swimlaneFillColor=#D4E1F5;fontColor=#660000;fontFamily=Tahoma;html=1;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="340" y="20" width="160" height="610" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="13" value="Product Quotations" style="shape=document;whiteSpace=wrap;verticalAlign=top;strokeColor=none;fillColor=#67B1E1;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;" parent="6" vertex="1">
      <mxGeometry x="20" y="50" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="14" value="Orders" style="shape=document;whiteSpace=wrap;verticalAlign=top;strokeColor=none;fillColor=#67B1E1;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;" parent="6" vertex="1">
      <mxGeometry x="20" y="225" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="15" value="Product Delivery Notification" style="shape=document;whiteSpace=wrap;strokeColor=none;fillColor=#67B1E1;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;verticalAlign=top;" parent="6" vertex="1">
      <mxGeometry x="20" y="400" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="16" value="Invoice" style="shape=document;whiteSpace=wrap;verticalAlign=top;strokeColor=none;fillColor=#67B1E1;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;" parent="6" vertex="1">
      <mxGeometry x="20" y="490" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="40" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="6" source="15" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="-80" y="375" as="sourcePoint"/>
        <mxPoint x="60" y="490" as="targetPoint"/>
        <Array as="points"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="7" value="&lt;font color=&quot;#23497d&quot;&gt;Sales Manager&lt;/font&gt;" style="swimlane;whiteSpace=wrap;fillColor=#E6EFFF;swimlaneFillColor=#E6EFFF;fontColor=#660000;fontFamily=Tahoma;html=1;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="500" y="20" width="160" height="610" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="17" value="Inventory Control" style="whiteSpace=wrap;strokeColor=none;fillColor=#23497D;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;" parent="7" vertex="1">
      <mxGeometry x="20" y="160" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="18" value="Product Delivery" style="whiteSpace=wrap;strokeColor=none;fillColor=#23497D;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;" parent="7" vertex="1">
      <mxGeometry x="20" y="315" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="24" value="Director" style="swimlane;whiteSpace=wrap;fillColor=#D4E1F5;swimlaneFillColor=#D4E1F5;fontColor=#23497D;fontFamily=Tahoma;html=1;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="980" y="20" width="160" height="610" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="25" value="Outbounding Management" style="shape=document;whiteSpace=wrap;verticalAlign=top;strokeColor=none;fillColor=#67B1E1;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;" parent="24" vertex="1">
      <mxGeometry x="20" y="130" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="27" value="Resources Allocation" style="whiteSpace=wrap;strokeColor=none;fillColor=#23497D;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;" parent="24" vertex="1">
      <mxGeometry x="20" y="255" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="28" value="Long Term Strategy" style="whiteSpace=wrap;strokeColor=none;fillColor=#23497D;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=1;html=1;fontSize=12;" parent="24" vertex="1">
      <mxGeometry x="20" y="400" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="53" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="24" source="27" target="28" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="30" y="570" as="sourcePoint"/>
        <mxPoint x="130" y="470" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="56" value="" style="edgeStyle=segmentEdgeStyle;entryX=0.25;entryY=0;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="24" source="25" target="27" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="-120" y="260" as="sourcePoint"/>
        <mxPoint x="-20" y="160" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="31" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="1" source="8" target="11" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="220" y="180" as="sourcePoint"/>
        <mxPoint x="320" y="80" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="35" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="1" source="12" target="9" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="270" y="255" as="sourcePoint"/>
        <mxPoint x="270" y="295" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="230" y="425"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="36" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="1" source="8" target="13" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="170" y="120" as="sourcePoint"/>
        <mxPoint x="270" y="195" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="37" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="1" source="12" target="15" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="380" y="750" as="sourcePoint"/>
        <mxPoint x="480" y="650" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="230" y="460"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="42" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="1" source="16" target="22" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="540" y="550" as="sourcePoint"/>
        <mxPoint x="640" y="450" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="43" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="1" source="11" target="14" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="450" y="230" as="sourcePoint"/>
        <mxPoint x="550" y="130" as="targetPoint"/>
        <Array as="points"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="44" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="1" source="13" target="17" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="440" y="180" as="sourcePoint"/>
        <mxPoint x="540" y="80" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="45" value="" style="edgeStyle=none;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="1" source="17" target="19" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="680" y="390" as="sourcePoint"/>
        <mxPoint x="780" y="290" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="46" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="1" source="14" target="18" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="520" y="420" as="sourcePoint"/>
        <mxPoint x="620" y="320" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="400" y="370"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="47" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="1" source="18" target="19" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="640" y="370" as="sourcePoint"/>
        <mxPoint x="740" y="270" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="48" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="1" source="18" target="20" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="510" y="520" as="sourcePoint"/>
        <mxPoint x="610" y="420" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="49" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="1" source="19" target="21" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="860" y="310" as="sourcePoint"/>
        <mxPoint x="960" y="210" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="740" y="110"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="50" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="1" source="19" target="23" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="850" y="320" as="sourcePoint"/>
        <mxPoint x="950" y="220" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="51" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="1" source="20" target="22" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="880" y="510" as="sourcePoint"/>
        <mxPoint x="980" y="410" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="52" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="1" source="23" target="28" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="1090" y="430" as="sourcePoint"/>
        <mxPoint x="1190" y="330" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="54" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#23497D;strokeWidth=2;html=1;endArrow=open;endFill=1;" parent="1" source="21" target="25" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="850" y="280" as="sourcePoint"/>
        <mxPoint x="950" y="180" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
  </root>
</mxGraphModel>

```
