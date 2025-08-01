---
title: "Swimlane Flowchart"
description: "A flowchart diagram showing process flow and decision points"
category: "templates/business"
type: "flowchart"
source_file: "templates/business/swimlane_decoded.xml"
tags: ["process", "template", "business", "drawio", "workflow"]
---

# Swimlane Flowchart

A flowchart diagram showing process flow and decision points

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="170" value="&lt;font color=&quot;#23497d&quot;&gt;Inside Sales Rep&lt;/font&gt;" style="swimlane;whiteSpace=wrap;fillColor=none;swimlaneFillColor=#BAC8D3;fontColor=#2F5B7C;fontFamily=Tahoma;html=1;strokeColor=none;opacity=50;" parent="1" vertex="1">
      <mxGeometry x="24.5" y="88.5" width="160" height="650" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="171" value="Customer Management" style="whiteSpace=wrap;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;plain-purple;strokeColor=none;fillColor=#2f5b7c;gradientColor=none;spacing=6;verticalAlign=middle;" parent="170" vertex="1">
      <mxGeometry x="20" y="60" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="172" value="Credit Management" style="whiteSpace=wrap;strokeColor=none;fillColor=#2f5b7c;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;spacing=6;verticalAlign=middle;" parent="170" vertex="1">
      <mxGeometry x="20" y="375" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="173" value="Price Management" style="whiteSpace=wrap;strokeColor=none;fillColor=#2f5b7c;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;spacing=6;verticalAlign=middle;" parent="170" vertex="1">
      <mxGeometry x="20" y="485" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="174" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#2F5B7C;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="170" source="172" target="173" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="170" y="397.5" as="sourcePoint"/>
        <mxPoint x="270" y="472.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="175" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#2F5B7C;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="170" source="171" target="172" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="160" y="110" as="sourcePoint"/>
        <mxPoint x="260" y="185" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="176" value="&lt;font color=&quot;#23497d&quot;&gt;Inside Sales Manager&lt;/font&gt;" style="swimlane;whiteSpace=wrap;fillColor=none;swimlaneFillColor=#BAC8D3;fontColor=#2F5B7C;fontFamily=Tahoma;html=1;strokeColor=none;opacity=25;" parent="1" vertex="1">
      <mxGeometry x="824.5" y="88.5" width="160" height="650" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="177" value="Sales Contract" style="shape=document;whiteSpace=wrap;verticalAlign=middle;strokeColor=none;fillColor=#12aab5;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;spacing=6;spacingBottom=22;" parent="176" vertex="1">
      <mxGeometry x="20" y="50" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="178" value="Bills" style="shape=document;whiteSpace=wrap;verticalAlign=middle;strokeColor=none;fillColor=#12aab5;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;spacing=6;spacingBottom=22;" parent="176" vertex="1">
      <mxGeometry x="20" y="530" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="179" value="Cost Allocation" style="whiteSpace=wrap;strokeColor=none;fillColor=#2f5b7c;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;spacing=6;verticalAlign=middle;" parent="176" vertex="1">
      <mxGeometry x="20" y="305" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="180" value="&lt;font color=&quot;#23497d&quot;&gt;VP Sales&lt;/font&gt;" style="swimlane;whiteSpace=wrap;fillColor=none;swimlaneFillColor=#BAC8D3;fontColor=#2F5B7C;fontFamily=Tahoma;html=1;strokeColor=none;opacity=50;" parent="1" vertex="1">
      <mxGeometry x="664.5" y="88.5" width="160" height="650" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="181" value="Outbound Accounting" style="whiteSpace=wrap;fillColor=#2f5b7c;strokeColor=none;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;spacing=6;verticalAlign=middle;" parent="180" vertex="1">
      <mxGeometry x="20" y="160" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="182" value="Account Processing" style="whiteSpace=wrap;strokeColor=none;fillColor=#2f5b7c;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;spacing=6;verticalAlign=middle;" parent="180" vertex="1">
      <mxGeometry x="20" y="420" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="183" value="&lt;font color=&quot;#23497d&quot;&gt;Sales Admin&lt;/font&gt;" style="swimlane;whiteSpace=wrap;fillColor=none;swimlaneFillColor=#BAC8D3;fontColor=#2F5B7C;fontFamily=Tahoma;html=1;strokeColor=none;opacity=25;" parent="1" vertex="1">
      <mxGeometry x="184.5" y="88.5" width="160" height="650" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="184" value="Material Requirements Planning Operation" style="whiteSpace=wrap;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;plain-purple;strokeColor=none;fillColor=#2f5b7c;gradientColor=none;spacing=6;verticalAlign=middle;" parent="183" vertex="1">
      <mxGeometry x="20" y="165" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="185" value="&lt;font color=&quot;#ffffff&quot;&gt;Facilities Procurement&lt;br&gt;Application&lt;/font&gt;&lt;br&gt; " style="shape=document;whiteSpace=wrap;verticalAlign=middle;strokeColor=none;fillColor=#12aab5;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;spacing=6;spacingBottom=22;" parent="183" vertex="1">
      <mxGeometry x="20" y="265" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="186" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#2F5B7C;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="183" source="184" target="185" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="-10" y="100" as="sourcePoint"/>
        <mxPoint x="90" y="175" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="187" value="&lt;font color=&quot;#23497d&quot;&gt;Sales Representative&lt;/font&gt;" style="swimlane;whiteSpace=wrap;fillColor=none;swimlaneFillColor=#BAC8D3;fontColor=#2F5B7C;fontFamily=Tahoma;html=1;strokeColor=none;opacity=50;" parent="1" vertex="1">
      <mxGeometry x="344.5" y="88.5" width="160" height="650" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="188" value="Product Quotations" style="shape=document;whiteSpace=wrap;verticalAlign=middle;strokeColor=none;fillColor=#12aab5;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;spacing=6;spacingBottom=22;" parent="187" vertex="1">
      <mxGeometry x="20" y="50" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="189" value="Orders" style="shape=document;whiteSpace=wrap;verticalAlign=middle;strokeColor=none;fillColor=#12aab5;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;spacing=6;spacingBottom=22;" parent="187" vertex="1">
      <mxGeometry x="20" y="225" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="190" value="Product Delivery Notification" style="shape=document;whiteSpace=wrap;strokeColor=none;fillColor=#12aab5;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;verticalAlign=middle;spacing=6;spacingBottom=22;" parent="187" vertex="1">
      <mxGeometry x="20" y="400" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="191" value="Invoice" style="shape=document;whiteSpace=wrap;verticalAlign=middle;strokeColor=none;fillColor=#12aab5;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;spacing=6;spacingBottom=22;" parent="187" vertex="1">
      <mxGeometry x="20" y="520" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="192" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#12AAB5;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="187" source="190" target="191" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="-80" y="375" as="sourcePoint"/>
        <mxPoint x="60" y="490" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="53" y="501"/>
          <mxPoint x="53" y="501"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="193" value="&lt;font color=&quot;#23497d&quot;&gt;Sales Manager&lt;/font&gt;" style="swimlane;whiteSpace=wrap;fillColor=none;swimlaneFillColor=#BAC8D3;fontColor=#2F5B7C;fontFamily=Tahoma;html=1;strokeColor=none;opacity=25;" parent="1" vertex="1">
      <mxGeometry x="504.5" y="88.5" width="160" height="650" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="194" value="Inventory Control" style="whiteSpace=wrap;strokeColor=none;fillColor=#2f5b7c;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;spacing=6;verticalAlign=middle;" parent="193" vertex="1">
      <mxGeometry x="20" y="160" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="195" value="Product Delivery" style="whiteSpace=wrap;strokeColor=none;fillColor=#2f5b7c;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;spacing=6;verticalAlign=middle;" parent="193" vertex="1">
      <mxGeometry x="20" y="315" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="196" value="Director" style="swimlane;whiteSpace=wrap;fillColor=none;swimlaneFillColor=#BAC8D3;fontColor=#2F5B7C;fontFamily=Tahoma;html=1;strokeColor=none;opacity=50;" parent="1" vertex="1">
      <mxGeometry x="984.5" y="88.5" width="160" height="650" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="197" value="Outbounding Management" style="shape=document;whiteSpace=wrap;verticalAlign=middle;strokeColor=none;fillColor=#12aab5;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;spacing=6;spacingBottom=22;" parent="196" vertex="1">
      <mxGeometry x="20" y="130" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="198" value="Resources Allocation" style="whiteSpace=wrap;strokeColor=none;fillColor=#2f5b7c;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;spacing=6;verticalAlign=middle;" parent="196" vertex="1">
      <mxGeometry x="20" y="255" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="199" value="Long Term Strategy" style="whiteSpace=wrap;strokeColor=none;fillColor=#2f5b7c;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;spacing=6;verticalAlign=middle;" parent="196" vertex="1">
      <mxGeometry x="20" y="400" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="200" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#2F5B7C;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="196" source="198" target="199" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="30" y="570" as="sourcePoint"/>
        <mxPoint x="130" y="470" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="201" value="" style="edgeStyle=segmentEdgeStyle;entryX=0.25;entryY=0;strokeColor=#12AAB5;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="196" source="197" target="198" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="-120" y="260" as="sourcePoint"/>
        <mxPoint x="-20" y="160" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="202" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#2F5B7C;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="1" source="171" target="184" edge="1">
      <mxGeometry x="164.5" y="178.5" width="100" height="100" as="geometry">
        <mxPoint x="224.5" y="248.5" as="sourcePoint"/>
        <mxPoint x="324.5" y="148.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="203" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#12AAB5;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="1" source="185" target="172" edge="1">
      <mxGeometry x="164.5" y="433.5" width="100" height="100" as="geometry">
        <mxPoint x="274.5" y="323.5" as="sourcePoint"/>
        <mxPoint x="274.5" y="363.5" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="234.5" y="493.5"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="204" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#2F5B7C;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="1" source="171" target="188" edge="1">
      <mxGeometry x="164.5" y="178.5" width="100" height="100" as="geometry">
        <mxPoint x="174.5" y="188.5" as="sourcePoint"/>
        <mxPoint x="274.5" y="263.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="205" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#12AAB5;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="1" source="185" target="190" edge="1">
      <mxGeometry x="234.5" y="433.5" width="100" height="100" as="geometry">
        <mxPoint x="384.5" y="818.5" as="sourcePoint"/>
        <mxPoint x="484.5" y="718.5" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="234.5" y="528.5"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="206" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;strokeColor=#12AAB5;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="1" source="191" target="178" edge="1">
      <mxGeometry x="484.5" y="623.5" width="100" height="100" as="geometry">
        <mxPoint x="544.5" y="618.5" as="sourcePoint"/>
        <mxPoint x="644.5" y="518.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="207" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#2F5B7C;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="1" source="184" target="189" edge="1">
      <mxGeometry x="324.5" y="283.5" width="100" height="100" as="geometry">
        <mxPoint x="454.5" y="298.5" as="sourcePoint"/>
        <mxPoint x="554.5" y="198.5" as="targetPoint"/>
        <Array as="points"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="208" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#12AAB5;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="1" source="188" target="194" edge="1">
      <mxGeometry x="484.5" y="178.5" width="100" height="100" as="geometry">
        <mxPoint x="444.5" y="248.5" as="sourcePoint"/>
        <mxPoint x="544.5" y="148.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="209" value="" style="edgeStyle=none;strokeColor=#2F5B7C;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="1" source="194" target="181" edge="1">
      <mxGeometry x="644.5" y="278.5" width="100" height="100" as="geometry">
        <mxPoint x="684.5" y="458.5" as="sourcePoint"/>
        <mxPoint x="784.5" y="358.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="210" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#12AAB5;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="1" source="189" target="195" edge="1">
      <mxGeometry x="404.5" y="393.5" width="100" height="100" as="geometry">
        <mxPoint x="524.5" y="488.5" as="sourcePoint"/>
        <mxPoint x="624.5" y="388.5" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="404.5" y="438.5"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="211" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#2F5B7C;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="1" source="195" target="181" edge="1">
      <mxGeometry x="644.5" y="308.5" width="100" height="100" as="geometry">
        <mxPoint x="644.5" y="438.5" as="sourcePoint"/>
        <mxPoint x="744.5" y="338.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="212" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#2F5B7C;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="1" source="195" target="182" edge="1">
      <mxGeometry x="644.5" y="433.5" width="100" height="100" as="geometry">
        <mxPoint x="514.5" y="588.5" as="sourcePoint"/>
        <mxPoint x="614.5" y="488.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="213" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#2F5B7C;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="1" source="181" target="177" edge="1">
      <mxGeometry x="744.5" y="178.5" width="100" height="100" as="geometry">
        <mxPoint x="864.5" y="378.5" as="sourcePoint"/>
        <mxPoint x="964.5" y="278.5" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="744.5" y="178.5"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="214" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#2F5B7C;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="1" source="181" target="179" edge="1">
      <mxGeometry x="804.5" y="278.5" width="100" height="100" as="geometry">
        <mxPoint x="854.5" y="388.5" as="sourcePoint"/>
        <mxPoint x="954.5" y="288.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="215" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#2F5B7C;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="1" source="182" target="178" edge="1">
      <mxGeometry x="804.5" y="538.5" width="100" height="100" as="geometry">
        <mxPoint x="884.5" y="578.5" as="sourcePoint"/>
        <mxPoint x="984.5" y="478.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="216" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#2F5B7C;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="1" source="179" target="199" edge="1">
      <mxGeometry x="964.5" y="423.5" width="100" height="100" as="geometry">
        <mxPoint x="1094.5" y="498.5" as="sourcePoint"/>
        <mxPoint x="1194.5" y="398.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="217" value="" style="edgeStyle=segmentEdgeStyle;strokeColor=#12AAB5;strokeWidth=3;html=1;endArrow=block;endFill=1;" parent="1" source="177" target="197" edge="1">
      <mxGeometry x="964.5" y="178.5" width="100" height="100" as="geometry">
        <mxPoint x="854.5" y="348.5" as="sourcePoint"/>
        <mxPoint x="954.5" y="248.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
  </root>
</mxGraphModel>

```
