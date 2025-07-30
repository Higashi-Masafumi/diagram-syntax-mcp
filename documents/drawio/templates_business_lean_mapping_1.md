---
title: "Lean Mapping 1 Database"
description: "A database diagram showing entity relationships and structure"
category: "templates/business"
type: "database"
source_file: "templates/business/lean_mapping_1_decoded.xml"
tags: ["process", "template", "business", "drawio", "workflow"]
---

# Lean Mapping 1 Database

A database diagram showing entity relationships and structure

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="113" style="edgeStyle=orthogonalEdgeStyle;shape=arrow;rounded=1;html=1;exitX=0.5;exitY=0;shadow=0;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=block;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontSize=16;fontColor=#000000;" parent="1" source="119" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="1199" y="370.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="114" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;shadow=0;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=block;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontSize=16;fontColor=#000000;shape=arrow;" parent="1" source="115" target="120" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="115" value="&lt;table style=&quot;width: 100%; height: 100%;&quot; cellspacing=&quot;0&quot; cellpadding=&quot;5&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td height=&quot;50%&quot;&gt;&amp;nbsp;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;center&quot; height=&quot;50%&quot;&gt;Supplier&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="strokeWidth=2;shape=mxgraph.lean_mapping.outside_sources;html=1;overflow=fill;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="387" y="299.5" width="100" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="116" value="Production&#10;Control" style="strokeWidth=2;shape=mxgraph.lean_mapping.schedule;html=1;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="767" y="169.5" width="100" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="117" value="&lt;table style=&quot;width: 100%; height: 100%;&quot; cellspacing=&quot;0&quot; cellpadding=&quot;5&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td height=&quot;50%&quot;&gt;&amp;nbsp;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;center&quot; height=&quot;50%&quot;&gt;Customer&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="strokeWidth=2;shape=mxgraph.lean_mapping.outside_sources;html=1;overflow=fill;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1147" y="299.5" width="100" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="118" value="Production&#10;Supervisor" style="strokeWidth=2;shape=mxgraph.lean_mapping.schedule;html=1;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="767" y="499.5" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="119" value="Ship" style="strokeWidth=2;shape=mxgraph.lean_mapping.schedule;html=1;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1167" y="619.5" width="60" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="120" value="&lt;table style=&quot;width: 100%; height: 100%;&quot; cellspacing=&quot;0&quot; cellpadding=&quot;0&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td height=&quot;0%&quot;&gt;Machine&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;center&quot; height=&quot;100%&quot;&gt;&amp;nbsp;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="strokeWidth=2;shape=mxgraph.lean_mapping.manufacturing_process;html=1;overflow=fill;verticalAlign=top;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="387" y="744.5" width="100" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="121" value="&lt;table style=&quot;width: 100%; height: 100%;&quot; cellspacing=&quot;0&quot; cellpadding=&quot;5&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;C/T=44 sec&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;C/O=60 min&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;Lat=1000 pc&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;Avail=27,600&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;&amp;nbsp;Uptime=87%&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="strokeWidth=2;shape=mxgraph.lean_mapping.data_box;fontSize=8;html=1;overflow=fill;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="397" y="814.5" width="80" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="122" value="&lt;table style=&quot;width: 100%; height: 100%;&quot; cellspacing=&quot;0&quot; cellpadding=&quot;0&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td height=&quot;0%&quot;&gt;Inspect&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;center&quot; height=&quot;100%&quot;&gt;&amp;nbsp;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="strokeWidth=2;shape=mxgraph.lean_mapping.manufacturing_process;html=1;overflow=fill;verticalAlign=top;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="577" y="744.5" width="100" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="123" value="&lt;table style=&quot;width: 100%; height: 100%;&quot; cellspacing=&quot;0&quot; cellpadding=&quot;0&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td height=&quot;0%&quot;&gt;Cln/Deburr&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;center&quot; height=&quot;100%&quot;&gt;&amp;nbsp;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="strokeWidth=2;shape=mxgraph.lean_mapping.manufacturing_process;html=1;overflow=fill;verticalAlign=top;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="767" y="744.5" width="100" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="124" value="&lt;table style=&quot;width: 100%; height: 100%;&quot; cellspacing=&quot;0&quot; cellpadding=&quot;0&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td height=&quot;0%&quot;&gt;Stock&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;center&quot; height=&quot;100%&quot;&gt;&amp;nbsp;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="strokeWidth=2;shape=mxgraph.lean_mapping.manufacturing_process;html=1;overflow=fill;verticalAlign=top;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="957" y="744.5" width="100" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="125" style="edgeStyle=orthogonalEdgeStyle;shape=arrow;rounded=1;html=1;exitX=0.5;exitY=0;shadow=0;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=block;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontSize=16;fontColor=#000000;" parent="1" source="126" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="1197" y="662.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="126" value="&lt;table style=&quot;width: 100%; height: 100%;&quot; cellspacing=&quot;0&quot; cellpadding=&quot;0&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td height=&quot;0%&quot;&gt;Package&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;center&quot; height=&quot;100%&quot;&gt;&amp;nbsp;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="strokeWidth=2;shape=mxgraph.lean_mapping.manufacturing_process;html=1;overflow=fill;verticalAlign=top;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1147" y="744.5" width="100" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="127" value="&lt;table style=&quot;width: 100%; height: 100%;&quot; cellspacing=&quot;0&quot; cellpadding=&quot;5&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;C/T=40 sec&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;C/O=5 min&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;Lat=1000 pc&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;Avail=27,600&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;&amp;nbsp;Uptime=99%&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="strokeWidth=2;shape=mxgraph.lean_mapping.data_box;fontSize=8;html=1;overflow=fill;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="587" y="814.5" width="80" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="128" value="&lt;table style=&quot;width: 100%; height: 100%;&quot; cellspacing=&quot;0&quot; cellpadding=&quot;5&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;C/T=5 sec&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;C/O=5 sec&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;Lat=1000 pc&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;Avail=27,600&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;&amp;nbsp;Uptime=80%&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="strokeWidth=2;shape=mxgraph.lean_mapping.data_box;fontSize=8;html=1;overflow=fill;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="777" y="814.5" width="80" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="129" value="&lt;table style=&quot;width: 100%; height: 100%;&quot; cellspacing=&quot;0&quot; cellpadding=&quot;5&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;C/T=30 sec&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;C/O=5 min&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;Lat=1000 pc&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;Avail=27.600&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;Uptime=99%&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="strokeWidth=2;shape=mxgraph.lean_mapping.data_box;fontSize=8;html=1;overflow=fill;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="967" y="814.5" width="80" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="130" value="&lt;table style=&quot;width: 100%; height: 100%;&quot; cellspacing=&quot;0&quot; cellpadding=&quot;5&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;C/T=10 sec&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;C/O=5 min&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;Lat=1000 pc&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;Avail=27,600&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;left&quot; height=&quot;20%&quot;&gt;Uptime=99% &lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="strokeWidth=2;shape=mxgraph.lean_mapping.data_box;fontSize=8;html=1;overflow=fill;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1157" y="814.5" width="80" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="131" value="" style="arrow;exitX=1;exitY=0.25;entryX=0;entryY=0.25;html=1;labelBackgroundColor=none;shadow=0;strokeWidth=2;fontColor=#000000;strokeColor=#000000;" parent="1" source="120" target="122" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="557" y="714.5" as="sourcePoint"/>
        <mxPoint x="657" y="614.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="132" value="" style="arrow;exitX=1;exitY=0.25;entryX=0;entryY=0.25;html=1;labelBackgroundColor=none;shadow=0;strokeWidth=2;fontColor=#000000;strokeColor=#000000;" parent="1" source="122" target="123" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="657" y="724.5" as="sourcePoint"/>
        <mxPoint x="747" y="724.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="133" value="" style="arrow;exitX=1;exitY=0.25;entryX=0;entryY=0.25;html=1;labelBackgroundColor=none;shadow=0;strokeWidth=2;fontColor=#000000;strokeColor=#000000;" parent="1" source="123" target="124" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="507" y="782" as="sourcePoint"/>
        <mxPoint x="597" y="782" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="134" value="" style="arrow;exitX=1;exitY=0.25;entryX=0;entryY=0.25;html=1;labelBackgroundColor=none;shadow=0;strokeWidth=2;fontColor=#000000;strokeColor=#000000;" parent="1" source="124" target="126" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="517" y="792" as="sourcePoint"/>
        <mxPoint x="607" y="792" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="135" value="&lt;table style=&quot;width: 60%; height: 100%;&quot; cellspacing=&quot;0&quot; cellpadding=&quot;0&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td align=&quot;center&quot; height=&quot;80%&quot;&gt;&lt;p&gt;(incoming&lt;/p&gt;&lt;p&gt;shipment)&lt;/p&gt;&lt;p&gt;Weekly&lt;/p&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;center&quot; height=&quot;20%&quot;&gt;&amp;nbsp;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="strokeWidth=2;shape=mxgraph.lean_mapping.truck_shipment;html=1;overflow=fill;verticalAlign=top;fontSize=10;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="392" y="469.5" width="100" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="136" value="&lt;table style=&quot;width: 60%; height: 100%;&quot; cellspacing=&quot;0&quot; cellpadding=&quot;0&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td align=&quot;center&quot; height=&quot;80%&quot;&gt;&lt;p&gt;(outgoing&lt;/p&gt;&lt;p&gt;shipment)&lt;/p&gt;&lt;p&gt;Daily&lt;/p&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;center&quot; height=&quot;20%&quot;&gt;&amp;nbsp;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="strokeWidth=2;shape=mxgraph.lean_mapping.truck_shipment;html=1;overflow=fill;verticalAlign=top;fontSize=10;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1152" y="469.5" width="100" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="137" value="(-4) 3360&lt;br&gt;(-6) 1680" style="strokeWidth=2;shape=mxgraph.lean_mapping.inventory_box;verticalAlign=top;verticalLabelPosition=bottom;fontStyle=3;html=1;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="507" y="784.5" width="40" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="138" value="2500" style="strokeWidth=2;shape=mxgraph.lean_mapping.inventory_box;verticalAlign=top;verticalLabelPosition=bottom;fontStyle=3;html=1;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="467" y="669.5" width="40" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="139" value="3500" style="strokeWidth=2;shape=mxgraph.lean_mapping.inventory_box;verticalAlign=top;verticalLabelPosition=bottom;fontStyle=3;html=1;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="707" y="784.5" width="40" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="140" value="2000" style="strokeWidth=2;shape=mxgraph.lean_mapping.inventory_box;verticalAlign=top;verticalLabelPosition=bottom;fontStyle=3;html=1;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="887" y="784.5" width="40" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="141" value="2000" style="strokeWidth=2;shape=mxgraph.lean_mapping.inventory_box;verticalAlign=top;verticalLabelPosition=bottom;fontStyle=3;html=1;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1077" y="784.5" width="40" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="142" value="2000" style="strokeWidth=2;shape=mxgraph.lean_mapping.inventory_box;verticalAlign=top;verticalLabelPosition=bottom;fontStyle=3;html=1;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1247" y="699.5" width="40" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="143" value="&lt;table style=&quot;width: 100%; height: 100%;&quot; cellspacing=&quot;0&quot; cellpadding=&quot;0&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td height=&quot;0%&quot;&gt;MAX=12&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td align=&quot;center&quot; height=&quot;100%&quot;&gt;&amp;nbsp;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="strokeWidth=2;shape=mxgraph.lean_mapping.fifo_lane;html=1;overflow=fill;verticalAlign=top;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="777" y="764.5" width="80" height="45" as="geometry"/>
    </mxCell>
    <mxCell id="144" value="" style="strokeWidth=2;shape=mxgraph.lean_mapping.timeline;mainText=0,,10,5 dy,20,45 sec,25,10 dy,20,40 sec,25,7 dy,20,5 sec,25,4 dy,20,30 sec,25,4 dy,20,10 sec,10,4 dy;html=1;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="367" y="939.5" width="920" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="145" value="1" style="strokeWidth=2;shape=mxgraph.lean_mapping.operator;align=right;labelPosition=left;fontSize=18;fontStyle=3;html=1;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="427" y="772.0833333333333" width="40" height="29.833333333333485" as="geometry"/>
    </mxCell>
    <mxCell id="146" value="1" style="strokeWidth=2;shape=mxgraph.lean_mapping.operator;align=right;labelPosition=left;fontSize=18;fontStyle=3;html=1;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="617" y="772.0833333333333" width="40" height="29.833333333333485" as="geometry"/>
    </mxCell>
    <mxCell id="147" value="1" style="strokeWidth=2;shape=mxgraph.lean_mapping.operator;align=right;labelPosition=left;fontSize=18;fontStyle=3;html=1;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="997" y="772.0833333333333" width="40" height="29.833333333333485" as="geometry"/>
    </mxCell>
    <mxCell id="148" value="1" style="strokeWidth=2;shape=mxgraph.lean_mapping.operator;align=right;labelPosition=left;fontSize=18;fontStyle=3;html=1;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1187" y="772.2499999999998" width="40" height="29.833333333333485" as="geometry"/>
    </mxCell>
    <mxCell id="149" value="1 shift/day (8.5 hrs)&#10;0.5 hr (lunch)&#10;0.5 hr (breaks)&#10;available time: 460 min/dy" style="strokeWidth=2;shape=mxgraph.lean_mapping.schedule;shadow=0;fontStyle=2;html=1;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1047" y="169.5" width="150" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="150" value="10,080 pcs/month&#10;(-4) 6,720&#10;(-6) 3,360&#10;504 pcs/day&#10;(-4) 336 pcs/day&#10;(-6) 168 pcs/day&#10;12 containers/day" style="strokeWidth=2;shape=mxgraph.lean_mapping.schedule;shadow=0;fontStyle=2;html=1;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="947" y="379.5" width="140" height="120" as="geometry"/>
    </mxCell>
    <mxCell id="151" value="lead time= 34 dy&#10;total cycle time= 130 sec&#10;total work time = 130 sec" style="strokeWidth=2;shape=mxgraph.lean_mapping.schedule;shadow=0;fontStyle=2;html=1;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="577" y="399.5" width="150" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="152" value="Production&#10;Plan" style="strokeWidth=2;shape=mxgraph.lean_mapping.schedule;html=1;shadow=0;strokeColor=#000000;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="767" y="349.5" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="153" value="Monthly&lt;div&gt;Forecast&lt;/div&gt;" style="shape=mxgraph.lean_mapping.electronic_info_flow_edge;html=1;endArrow=none;endFill=0;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontSize=12;fontColor=#000000;align=center;verticalAlign=bottom;spacingBottom=19;labelBackgroundColor=none;shadow=0;strokeColor=#000000;" parent="1" source="116" target="115" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="277" y="379.5" as="sourcePoint"/>
        <mxPoint x="377" y="279.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="154" value="Weekly&lt;div&gt;Orders&lt;/div&gt;" style="shape=mxgraph.lean_mapping.electronic_info_flow_edge;html=1;endArrow=none;endFill=0;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontSize=12;fontColor=#000000;align=center;verticalAlign=bottom;spacingBottom=12;labelBackgroundColor=none;shadow=0;strokeColor=#000000;" parent="1" source="115" target="152" edge="1">
      <mxGeometry x="527" y="231.16666666666663" width="100" height="100" as="geometry">
        <mxPoint x="817" y="231.16666666666663" as="sourcePoint"/>
        <mxPoint x="527" y="327.83333333333337" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="155" value="Monthly&lt;div&gt;Forecast&lt;/div&gt;" style="shape=mxgraph.lean_mapping.electronic_info_flow_edge;html=1;endArrow=none;endFill=0;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontSize=12;fontColor=#000000;align=center;verticalAlign=bottom;spacingBottom=19;labelBackgroundColor=none;shadow=0;strokeColor=#000000;" parent="1" source="116" target="117" edge="1">
      <mxGeometry x="527" y="231.16666666666663" width="100" height="100" as="geometry">
        <mxPoint x="817" y="231.16666666666663" as="sourcePoint"/>
        <mxPoint x="527" y="327.83333333333337" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="156" value="Weekly&lt;div&gt;Orders&lt;/div&gt;" style="shape=mxgraph.lean_mapping.electronic_info_flow_edge;html=1;endArrow=none;endFill=0;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontSize=12;fontColor=#000000;align=center;verticalAlign=bottom;spacingBottom=12;labelBackgroundColor=none;shadow=0;strokeColor=#000000;" parent="1" source="117" target="152" edge="1">
      <mxGeometry x="537" y="241.16666666666663" width="100" height="100" as="geometry">
        <mxPoint x="527" y="348.98717948717945" as="sourcePoint"/>
        <mxPoint x="817" y="375.01282051282055" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="157" value="Daily" style="shape=mxgraph.lean_mapping.manual_info_flow_edge;html=1;endArrow=none;endFill=0;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontSize=12;fontColor=#000000;align=left;labelBackgroundColor=none;spacingLeft=4;shadow=0;strokeColor=#000000;" parent="1" source="116" target="152" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="317" y="329.5" as="sourcePoint"/>
        <mxPoint x="417" y="229.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="158" value="Daily" style="shape=mxgraph.lean_mapping.manual_info_flow_edge;html=1;endArrow=none;endFill=0;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontSize=12;fontColor=#000000;align=left;labelBackgroundColor=none;spacingLeft=4;shadow=0;strokeColor=#000000;" parent="1" source="152" target="118" edge="1">
      <mxGeometry x="867" y="249.5" width="100" height="100" as="geometry">
        <mxPoint x="867" y="249.5" as="sourcePoint"/>
        <mxPoint x="867" y="359.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="159" value="" style="shape=mxgraph.lean_mapping.manual_info_flow_edge;html=1;endArrow=none;endFill=0;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontSize=12;fontColor=#000000;align=left;verticalAlign=top;labelBackgroundColor=none;shadow=0;strokeColor=#000000;" parent="1" source="118" target="120" edge="1">
      <mxGeometry x="697" y="409.5" width="100" height="100" as="geometry">
        <mxPoint x="687" y="549.5" as="sourcePoint"/>
        <mxPoint x="687" y="659.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="160" value="Daily" style="text;html=1;resizable=0;points=[];align=center;verticalAlign=middle;labelBackgroundColor=#ffffff;fontSize=12;fontColor=#000000;" parent="159" vertex="1" connectable="0">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="14" y="-14" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="161" value="" style="shape=mxgraph.lean_mapping.manual_info_flow_edge;html=1;endArrow=none;endFill=0;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontSize=12;fontColor=#000000;align=left;verticalAlign=top;labelBackgroundColor=none;shadow=0;strokeColor=#000000;" parent="1" source="118" target="122" edge="1">
      <mxGeometry x="707" y="419.5" width="100" height="100" as="geometry">
        <mxPoint x="834.6923076923076" y="549.5" as="sourcePoint"/>
        <mxPoint x="497" y="758.547619047619" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="162" value="Daily&lt;br&gt;" style="text;html=1;resizable=0;points=[];align=center;verticalAlign=middle;labelBackgroundColor=#ffffff;fontSize=12;fontColor=#000000;" parent="161" vertex="1" connectable="0">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="10" y="-13.766199889010977" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="163" value="" style="shape=mxgraph.lean_mapping.manual_info_flow_edge;html=1;endArrow=none;endFill=0;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontSize=12;fontColor=#000000;align=left;verticalAlign=top;labelBackgroundColor=none;shadow=0;strokeColor=#000000;" parent="1" source="118" target="123" edge="1">
      <mxGeometry x="717" y="429.5" width="100" height="100" as="geometry">
        <mxPoint x="844.6923076923076" y="559.5" as="sourcePoint"/>
        <mxPoint x="507" y="768.547619047619" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="164" value="Daily" style="text;html=1;resizable=0;points=[];align=center;verticalAlign=middle;labelBackgroundColor=#ffffff;fontSize=12;fontColor=#000000;" parent="163" vertex="1" connectable="0">
      <mxGeometry relative="1" as="geometry">
        <mxPoint y="-14.227527362257888" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="165" value="" style="shape=mxgraph.lean_mapping.manual_info_flow_edge;html=1;endArrow=none;endFill=0;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontSize=12;fontColor=#000000;align=left;verticalAlign=bottom;labelBackgroundColor=none;shadow=0;strokeColor=#000000;" parent="1" source="118" target="124" edge="1">
      <mxGeometry x="727" y="439.5" width="100" height="100" as="geometry">
        <mxPoint x="854.6923076923076" y="569.5" as="sourcePoint"/>
        <mxPoint x="517" y="778.547619047619" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="166" value="Daily" style="text;html=1;resizable=0;points=[];align=center;verticalAlign=middle;labelBackgroundColor=#ffffff;fontSize=12;fontColor=#000000;" parent="165" vertex="1" connectable="0">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="-9" y="-13.766199889010977" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="167" value="" style="shape=mxgraph.lean_mapping.manual_info_flow_edge;html=1;endArrow=none;endFill=0;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontSize=12;fontColor=#000000;align=left;verticalAlign=bottom;labelBackgroundColor=none;shadow=0;strokeColor=#000000;spacing=20;" parent="1" source="118" target="126" edge="1">
      <mxGeometry x="737" y="449.5" width="100" height="100" as="geometry">
        <mxPoint x="864.6923076923076" y="579.5" as="sourcePoint"/>
        <mxPoint x="527" y="788.547619047619" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="168" value="Daily" style="text;html=1;resizable=0;points=[];align=center;verticalAlign=middle;labelBackgroundColor=#ffffff;fontSize=12;fontColor=#000000;" parent="167" vertex="1" connectable="0">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="-13" y="-14" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="169" style="edgeStyle=orthogonalEdgeStyle;shape=arrow;rounded=1;jumpStyle=none;html=1;exitX=0.5;exitY=0;entryX=0.5;entryY=0;shadow=0;labelBackgroundColor=none;startArrow=none;startFill=0;endArrow=block;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#000000;" parent="1" source="123" target="123" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
