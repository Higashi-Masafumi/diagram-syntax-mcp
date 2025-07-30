---
title: "State Machine 1 Floorplan"
description: "A floor plan diagram showing spatial layout"
category: "templates/uml"
type: "floorplan"
source_file: "templates/uml/state_machine_1_decoded.xml"
---

# State Machine 1 Floorplan

A floor plan diagram showing spatial layout

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1.5" pageWidth="826" pageHeight="1169" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="193" value="" style="fillColor=#FFF2CC" parent="1" vertex="1">
      <mxGeometry x="10" y="200" width="1550" height="510" as="geometry"/>
    </mxCell>
    <mxCell id="124" value="waiting for &#10;hotel response" style="rounded=1;fillColor=#A2C4C9" parent="1" vertex="1">
      <mxGeometry x="710" y="440" width="140" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="126" value="Created" style="rounded=1;fillColor=#A2C4C9" parent="1" vertex="1">
      <mxGeometry x="715.0000000000001" y="40.000000000000014" width="140" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="127" value="hotel room &#10;confirmed" style="rounded=1;fillColor=#A2C4C9" parent="1" vertex="1">
      <mxGeometry x="710.0000000000001" y="610" width="140" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="128" value="no answer&#10;to hotel request" style="rounded=1;fillColor=#A2C4C9" parent="1" vertex="1">
      <mxGeometry x="540" y="610" width="140" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="129" value="lodging not&#10;available" style="rounded=1;fillColor=#A2C4C9" parent="1" vertex="1">
      <mxGeometry x="880" y="609.9999999999999" width="140" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="132" value="flights not&#10;available" style="rounded=1;fillColor=#A2C4C9" parent="1" vertex="1">
      <mxGeometry x="360" y="610" width="140" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="133" value="flights &#10;confirmed" style="rounded=1;fillColor=#A2C4C9" parent="1" vertex="1">
      <mxGeometry x="200" y="610" width="140" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="134" value="no answer&#10;to flight&#10;request" style="rounded=1;fillColor=#A2C4C9" parent="1" vertex="1">
      <mxGeometry x="40" y="610" width="140" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="135" value="waiting for &#10;airline response" style="rounded=1;fillColor=#A2C4C9" parent="1" vertex="1">
      <mxGeometry x="200" y="440" width="140" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="136" value="no answer&#10;to activity&#10;request" style="rounded=1;fillColor=#A2C4C9" parent="1" vertex="1">
      <mxGeometry x="1060" y="610" width="140" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="137" value="activities&#10;booking&#10;confirmed" style="rounded=1;fillColor=#A2C4C9" parent="1" vertex="1">
      <mxGeometry x="1220" y="610" width="140" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="138" value="activity not&#10;available" style="rounded=1;fillColor=#A2C4C9" parent="1" vertex="1">
      <mxGeometry x="1380" y="609.9999999999999" width="140" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="139" value="waiting for &#10;activity sup.&#10;response" style="rounded=1;fillColor=#A2C4C9" parent="1" vertex="1">
      <mxGeometry x="1220" y="440" width="140" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="140" value="" style="shape=mxgraph.bpmn.terminate;fillColor=white;strokeColor=black;strokeWidth=2;perimeter=ellipsePerimeter;" parent="1" vertex="1">
      <mxGeometry x="1115.0000000000002" y="60.000000000000014" width="30" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="141" value="" style="ellipse;fillColor=#000000;strokeColor=none" parent="1" vertex="1">
      <mxGeometry x="415.0000000000002" y="60.000000000000014" width="30" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="142" value="" style="ellipse;fillColor=#000000;strokeColor=none" parent="1" vertex="1">
      <mxGeometry x="300" y="290" width="30" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="143" value="" style="ellipse;fillColor=#000000;strokeColor=none" parent="1" vertex="1">
      <mxGeometry x="810" y="290" width="30" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="146" value="" style="ellipse;fillColor=#000000;strokeColor=none" parent="1" vertex="1">
      <mxGeometry x="1310" y="290" width="30" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="147" value="user places order" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="141" target="126" edge="1">
      <mxGeometry x="2.2737367544323206e-13" y="-60" width="100" height="100" as="geometry">
        <mxPoint x="2.2737367544323206e-13" y="40" as="sourcePoint"/>
        <mxPoint x="100.00000000000023" y="-60" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="148" value="credit card charge not &#10;authorized / email customer" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="126" target="140" edge="1">
      <mxGeometry x="2.2737367544323206e-13" y="-60" width="100" height="100" as="geometry">
        <mxPoint x="2.2737367544323206e-13" y="40" as="sourcePoint"/>
        <mxPoint x="100.00000000000023" y="-60" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="151" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal" parent="1" source="142" target="135" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="152" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal" parent="1" source="143" target="124" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="153" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal" parent="1" source="146" target="139" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="155" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="135" target="132" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="430" y="470"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="156" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="135" target="134" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="110" y="475"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="157" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="135" target="133" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="158" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="124" target="127" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="159" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="124" target="128" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="610" y="475"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="160" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="124" target="129" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="950" y="475"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="161" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="139" target="137" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="162" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="139" target="136" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1130" y="480"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="163" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="139" target="138" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1450" y="475"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="164" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="135" target="142" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="230" y="305"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="165" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="124" target="143" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="740" y="305"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="166" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="139" target="146" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1240" y="305"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="167" value="a supplier &#10;could not &#10;fill the order" style="rounded=1;fillColor=#A2C4C9" parent="1" vertex="1">
      <mxGeometry x="710.0000000000001" y="850" width="140" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="170" value="completed&#10;successfully" style="rounded=1;fillColor=#A2C4C9" parent="1" vertex="1">
      <mxGeometry x="920" y="780" width="140" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="171" value="canceled&#10;by user" style="rounded=1;fillColor=#A2C4C9" parent="1" vertex="1">
      <mxGeometry x="1380" y="850" width="140" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="172" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="134" target="167" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="173" value="[activities and flights confirmed]" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="133" target="170" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="640" y="815"/>
        </Array>
        <mxPoint x="-5" y="82.5" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="174" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="132" target="167" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="175" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="128" target="167" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="176" value="[activities and hotel confirmed]" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="127" target="170" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="177" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="129" target="167" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="178" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="136" target="167" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="179" value="[flights and hotel confirmed]" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="137" target="170" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="180" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="138" target="167" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="181" value="automatic transition" style="text;align=center" parent="1" vertex="1">
      <mxGeometry x="705.0000000000002" y="780" width="149.9999999999999" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="182" value="user&#10;canceled&#10;order" style="edgeStyle=elbowEdgeStyle;elbow=vertical" parent="1" source="170" target="171" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="183" value="[#retries &gt; 3]&#10;timeout" style="text;align=center" parent="1" vertex="1">
      <mxGeometry x="180" y="335" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="184" value="[#retries &gt; 3]&#10;timeout" style="text;align=center" parent="1" vertex="1">
      <mxGeometry x="690" y="335" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="185" value="[#retries &gt; 3]&#10;timeout" style="text;align=center" parent="1" vertex="1">
      <mxGeometry x="1190" y="335" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="186" value="book flight&#10;request sent" style="text;align=center" parent="1" vertex="1">
      <mxGeometry x="270" y="360" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="189" value="book hotel&#10;request sent" style="text;align=center" parent="1" vertex="1">
      <mxGeometry x="780" y="360" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="190" value="book activities&#10;request sent" style="text;align=center" parent="1" vertex="1">
      <mxGeometry x="1280" y="360" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="192" value="" style="edgeStyle=none;endArrow=none" parent="1" edge="1">
      <mxGeometry x="100.00000000000001" y="183.59999999999997" width="100" height="100" as="geometry">
        <mxPoint x="10.000000000000018" y="233.6" as="sourcePoint"/>
        <mxPoint x="1560" y="233.6" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="194" value="Filling Order" style="text;align=center" parent="1" vertex="1">
      <mxGeometry x="10" y="200" width="1550" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="196" value="" style="edgeStyle=none" parent="1" source="126" target="193" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="197" value="[#retries &gt; 3]&#10;timeout" style="text;align=center" parent="1" vertex="1">
      <mxGeometry x="60" y="520" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="198" value="[#retries &gt; 3]&#10;timeout" style="text;align=center" parent="1" vertex="1">
      <mxGeometry x="560" y="520" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="199" value="[#retries &gt; 3]&#10;timeout" style="text;align=center" parent="1" vertex="1">
      <mxGeometry x="1080.0000000000002" y="520" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="200" value="flight booking&#10;confirmation&#10;received" style="text;align=center" parent="1" vertex="1">
      <mxGeometry x="220" y="530" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="201" value="airline&#10;replies&#10;denying&#10;request" style="text;align=center" parent="1" vertex="1">
      <mxGeometry x="380.0000000000002" y="500" width="100" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="202" value="hotel booking&#10;confirmation&#10;received" style="text;align=center" parent="1" vertex="1">
      <mxGeometry x="730" y="530" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="204" value="hotel&#10;replies&#10;denying&#10;request" style="text;align=center" parent="1" vertex="1">
      <mxGeometry x="900" y="505" width="100" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="205" value="activity booking&#10;confirmation&#10;received" style="text;align=center" parent="1" vertex="1">
      <mxGeometry x="1240" y="530" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="206" value="activity sup.&#10;replies&#10;denying&#10;request" style="text;align=center" parent="1" vertex="1">
      <mxGeometry x="1400" y="505" width="100" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="207" value="user&#10;canceled&#10;order" style="edgeStyle=elbowEdgeStyle;elbow=horizontal" parent="1" source="193" target="171" edge="1">
      <mxGeometry x="1580" y="700" width="100" height="100" as="geometry">
        <mxPoint x="1580" y="800" as="sourcePoint"/>
        <mxPoint x="1680" y="700" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1480" y="780"/>
        </Array>
      </mxGeometry>
    </mxCell>
  </root>
</mxGraphModel>

```
