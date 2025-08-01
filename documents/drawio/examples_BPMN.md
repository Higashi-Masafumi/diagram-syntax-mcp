---
title: "Business Process Model Notation"
description: "A sequence diagram illustrating interactions between objects over time"
category: "examples"
type: "sequence"
source_file: "examples/BPMN_decoded.xml"
tags: ["bpmn", "business_process", "sample", "drawio", "example"]
---

# Business Process Model Notation

A sequence diagram illustrating interactions between objects over time

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1086" dy="613" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1.5" pageWidth="826" pageHeight="1169" background="#ffffff" math="0" shadow="0">
  <root>
    <mxCell id="0" style=";html=1;"/>
    <mxCell id="1" style=";html=1;" parent="0"/>
    <mxCell id="23" value="" style="rounded=1;fillColor=#f5f5f5;strokeWidth=2;html=1;strokeColor=#666666;" parent="1" vertex="1">
      <mxGeometry x="30" y="398.50000000000006" width="1660" height="301.49999999999994" as="geometry"/>
    </mxCell>
    <mxCell id="39" value="" style="rounded=1;fillColor=#f5f5f5;strokeWidth=2;html=1;strokeColor=#666666;" parent="1" vertex="1">
      <mxGeometry x="280" y="430" width="1220" height="230" as="geometry"/>
    </mxCell>
    <mxCell id="2" value="" style="rounded=1;fillColor=#f5f5f5;strokeWidth=2;html=1;strokeColor=#666666;" parent="1" vertex="1">
      <mxGeometry x="20" y="20" width="1660" height="180" as="geometry"/>
    </mxCell>
    <mxCell id="3" value="" style="edgeStyle=none;endArrow=none;startArrow=none;strokeWidth=2;html=1;" parent="1" edge="1">
      <mxGeometry x="125" y="-80.75" width="100" height="100" as="geometry">
        <mxPoint x="102.5" y="19.25" as="sourcePoint"/>
        <mxPoint x="102.5" y="199.25" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=standard;symbol=message;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=black;strokeWidth=2;fillColor=#B6D7A8;" parent="1" vertex="1">
      <mxGeometry x="170" y="85" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="5" value="Get Task" style="rounded=1;fillColor=#CFE2F3;strokeWidth=2;html=1;" parent="1" vertex="1">
      <mxGeometry x="320" y="78.5" width="160" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="6" value="Create Schedule" style="rounded=1;fillColor=#CFE2F3;strokeWidth=2;html=1;" parent="1" vertex="1">
      <mxGeometry x="590" y="78.5" width="210" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="7" value="Verify Schedule" style="rounded=1;fillColor=#CFE2F3;strokeWidth=2;html=1;" parent="1" vertex="1">
      <mxGeometry x="910" y="79.9" width="210" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="8" value="Commit Schedule" style="rounded=1;fillColor=#CFE2F3;strokeWidth=2;html=1;" parent="1" vertex="1">
      <mxGeometry x="1210" y="80" width="200" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="10" value="" style="edgeStyle=none;exitX=1;exitY=0.5;exitPerimeter=0;strokeWidth=2;html=1;" parent="1" source="4" target="5" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="11" value="" style="edgeStyle=none;strokeWidth=2;html=1;" parent="1" source="5" target="6" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="12" value="" style="edgeStyle=none;strokeWidth=2;html=1;" parent="1" source="6" target="7" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="13" value="" style="edgeStyle=none;strokeWidth=2;html=1;" parent="1" source="7" target="8" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="16" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=end;symbol=general;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=black;strokeWidth=2;fillColor=#B6D7A8;" parent="1" vertex="1">
      <mxGeometry x="1540" y="84.75000000000001" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="20" value="" style="edgeStyle=none;strokeWidth=2;html=1;" parent="1" source="8" target="16" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="21" value="Scheduling" style="text;horizontal=0;fontSize=18;fontStyle=1;html=1;" parent="1" vertex="1">
      <mxGeometry x="55" y="60" width="45" height="106" as="geometry"/>
    </mxCell>
    <mxCell id="22" value="Order list" style="shape=note;verticalLabelPosition=bottom;verticalAlign=top;strokeWidth=2;html=1;spacingLeft=35;align=left;" parent="1" vertex="1">
      <mxGeometry x="390" y="240" width="60" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="24" value="" style="edgeStyle=none;endArrow=none;startArrow=none;strokeWidth=2;html=1;" parent="1" edge="1">
      <mxGeometry x="126.75" y="298.50000000000006" width="100" height="100" as="geometry">
        <mxPoint x="104.25" y="398.50000000000006" as="sourcePoint"/>
        <mxPoint x="101.75" y="700" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="26" value="Compose Specification" style="rounded=1;fillColor=#CFE2F3;strokeWidth=2;html=1;" parent="1" vertex="1">
      <mxGeometry x="510" y="457" width="160" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="27" value="Check warehouse" style="rounded=1;fillColor=#CFE2F3;strokeWidth=2;html=1;" parent="1" vertex="1">
      <mxGeometry x="740" y="457.75000000000006" width="150" height="59.99999999999994" as="geometry"/>
    </mxCell>
    <mxCell id="29" value="Produce Goods" style="rounded=1;fillColor=#CFE2F3;strokeWidth=2;html=1;" parent="1" vertex="1">
      <mxGeometry x="1110" y="457.5" width="200" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="31" value="" style="edgeStyle=none;strokeWidth=2;html=1;" parent="1" source="26" target="27" edge="1">
      <mxGeometry x="10" y="378.50000000000006" width="100" height="100" as="geometry">
        <mxPoint x="10" y="478.50000000000006" as="sourcePoint"/>
        <mxPoint x="110" y="378.50000000000006" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="35" value="" style="edgeStyle=none;strokeWidth=2;html=1;" parent="1" source="29" target="46" edge="1">
      <mxGeometry x="10" y="378.50000000000006" width="100" height="100" as="geometry">
        <mxPoint x="10" y="478.50000000000006" as="sourcePoint"/>
        <mxPoint x="110" y="378.50000000000006" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="36" value="Factory" style="text;horizontal=0;fontSize=18;fontStyle=1;html=1;" parent="1" vertex="1">
      <mxGeometry x="65" y="490" width="35" height="104" as="geometry"/>
    </mxCell>
    <mxCell id="40" value="Available?" style="shape=mxgraph.bpmn.gateway;fillColor=#F4CCCC;strokeColor=black;strokeWidth=2;perimeter=ellipsePerimeter;html=1;" parent="1" vertex="1">
      <mxGeometry x="960" y="448.5" width="80" height="78.74999999999994" as="geometry"/>
    </mxCell>
    <mxCell id="41" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=eventInt;symbol=message;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=black;strokeWidth=2;fillColor=#B6D7A8;" parent="1" vertex="1">
      <mxGeometry x="975" y="570" width="49.99999999999997" height="49.80000000000001" as="geometry"/>
    </mxCell>
    <mxCell id="42" value="" style="edgeStyle=orthogonalEdgeStyle;strokeWidth=2;html=1;" parent="1" source="27" target="40" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="43" value="no" style="edgeStyle=orthogonalEdgeStyle;strokeWidth=2;html=1;labelBackgroundColor=none;align=left;" parent="1" source="40" target="41" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="44" value="yes" style="edgeStyle=orthogonalEdgeStyle;strokeWidth=2;html=1;labelBackgroundColor=none;verticalAlign=bottom;" parent="1" source="40" target="29" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="45" value="" style="edgeStyle=orthogonalEdgeStyle;strokeWidth=2;html=1;" parent="1" source="41" target="29" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="46" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=end;symbol=message;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=black;strokeWidth=2;fillColor=#B6D7A8;" parent="1" vertex="1">
      <mxGeometry x="1385" y="462.20000000000005" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="47" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=standard;symbol=general;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=black;strokeWidth=2;fillColor=#B6D7A8;" parent="1" vertex="1">
      <mxGeometry x="390" y="462.50000000000006" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="48" value="" style="edgeStyle=none;strokeWidth=2;html=1;" parent="1" source="47" target="26" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="49" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=eventInt;symbol=timer;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=black;strokeWidth=2;fillColor=#B6D7A8;" parent="1" vertex="1">
      <mxGeometry x="180.40000000000003" y="510" width="50" height="51" as="geometry"/>
    </mxCell>
    <mxCell id="50" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;strokeWidth=2;html=1;" parent="1" source="49" target="39" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="51" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=end;symbol=general;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=black;strokeWidth=2;fillColor=#B6D7A8;" parent="1" vertex="1">
      <mxGeometry x="1550" y="526.375" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="52" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;strokeWidth=2;html=1;" parent="1" source="39" target="51" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="53" value="Order Completed" style="edgeStyle=elbowEdgeStyle;elbow=vertical;dashed=1;rounded=1;strokeWidth=2;html=1;verticalAlign=bottom;" parent="1" source="46" target="6" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="56" value="" style="edgeStyle=none;dashed=1;strokeWidth=2;html=1;" parent="1" source="6" target="22" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="57" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;dashed=1;startArrow=classic;endArrow=classic;strokeWidth=2;html=1;" parent="1" source="22" target="39" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="61" value="" style="rounded=1;fillColor=#f5f5f5;strokeWidth=2;html=1;strokeColor=#666666;" parent="1" vertex="1">
      <mxGeometry x="30" y="920" width="1660" height="180" as="geometry"/>
    </mxCell>
    <mxCell id="62" value="" style="edgeStyle=none;endArrow=none;startArrow=none;strokeWidth=2;html=1;" parent="1" edge="1">
      <mxGeometry x="130.57" y="820" width="100" height="100" as="geometry">
        <mxPoint x="102.5" y="920" as="sourcePoint"/>
        <mxPoint x="102.5" y="1100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="63" value="Analysis" style="text;horizontal=0;fontSize=18;fontStyle=1;html=1;" parent="1" vertex="1">
      <mxGeometry x="55" y="950" width="35" height="104" as="geometry"/>
    </mxCell>
    <mxCell id="64" value="Quality Control" style="rounded=1;fillColor=#CFE2F3;strokeWidth=2;html=1;" parent="1" vertex="1">
      <mxGeometry x="419.99999999999994" y="985" width="160" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="65" value="Issue Revision" style="rounded=1;fillColor=#CFE2F3;strokeWidth=2;html=1;" parent="1" vertex="1">
      <mxGeometry x="715.0000000000001" y="985" width="160" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="66" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=eventInt;symbol=timer;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=black;strokeWidth=2;fillColor=#B6D7A8;" parent="1" vertex="1">
      <mxGeometry x="185" y="989.5" width="50" height="51" as="geometry"/>
    </mxCell>
    <mxCell id="67" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=end;symbol=general;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=black;strokeWidth=2;fillColor=#B6D7A8;" parent="1" vertex="1">
      <mxGeometry x="1020" y="990" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="68" value="" style="edgeStyle=none;dashed=1;strokeWidth=2;html=1;" parent="1" source="27" target="70" edge="1">
      <mxGeometry x="120.87110481586399" y="611.5" width="100" height="100" as="geometry">
        <mxPoint x="769.128895184136" y="750" as="sourcePoint"/>
        <mxPoint x="570.871104815864" y="877.2454545454545" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="69" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;dashed=1;startArrow=classic;endArrow=classic;strokeWidth=2;html=1;" parent="1" source="70" target="64" edge="1">
      <mxGeometry x="33.599999999999916" y="580" width="100" height="100" as="geometry">
        <mxPoint x="453.59999999999997" y="910" as="sourcePoint"/>
        <mxPoint x="453.59999999999997" y="1010" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="70" value="Planned&#10; Stock Balance" style="shape=note;verticalLabelPosition=bottom;verticalAlign=top;strokeWidth=2;html=1;align=left;spacingLeft=35;" parent="1" vertex="1">
      <mxGeometry x="440.00000000000006" y="780" width="60" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="71" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;strokeWidth=2;html=1;" parent="1" source="66" target="64" edge="1">
      <mxGeometry x="5" y="-65.00000000000023" width="100" height="100" as="geometry">
        <mxPoint x="5" y="34.99999999999977" as="sourcePoint"/>
        <mxPoint x="105" y="-65.00000000000023" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="72" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;strokeWidth=2;html=1;" parent="1" source="64" target="65" edge="1">
      <mxGeometry x="5" y="-65.00000000000023" width="100" height="100" as="geometry">
        <mxPoint x="5" y="34.99999999999977" as="sourcePoint"/>
        <mxPoint x="105" y="-65.00000000000023" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="73" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;strokeWidth=2;html=1;" parent="1" source="65" target="67" edge="1">
      <mxGeometry x="5" y="-65.00000000000023" width="100" height="100" as="geometry">
        <mxPoint x="5" y="34.99999999999977" as="sourcePoint"/>
        <mxPoint x="105" y="-65.00000000000023" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="74" value="Materials Delivered" style="edgeStyle=elbowEdgeStyle;elbow=vertical;dashed=1;strokeWidth=2;html=1;verticalAlign=bottom;" parent="1" source="65" target="41" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
  </root>
</mxGraphModel>

```
