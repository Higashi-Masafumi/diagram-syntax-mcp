---
title: "Flowchart 2 Flowchart"
description: "A flowchart diagram showing process flow and decision points"
category: "templates/flowcharts"
type: "flowchart"
source_file: "templates/flowcharts/flowchart_2_decoded.xml"
tags: ["process", "flowchart", "template", "flowcharts", "drawio", "workflow"]
---

# Flowchart 2 Flowchart

A flowchart diagram showing process flow and decision points

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2" value="start" style="shape=mxgraph.flowchart.terminator;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="260" y="60" width="120" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="3" value="analyse project&#10; documentation" style="shape=mxgraph.flowchart.data;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="240.5" y="130" width="159" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="4" value="create&#10;material&#10;specification" style="shape=mxgraph.flowchart.data;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="240.5" y="510" width="159" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="5" value="check for&#10;obscurities" style="shape=mxgraph.flowchart.data;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="240.5" y="250" width="159" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="6" value="obscurities?" style="shape=mxgraph.flowchart.decision;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="271" y="390" width="98" height="57" as="geometry"/>
    </mxCell>
    <mxCell id="7" style="fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="2" target="3" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="8" style="fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="3" target="5" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="9" style="entryX=0.5;entryY=0;entryPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="5" target="6" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="10" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;entryX=0.5;entryY=0.91;entryPerimeter=0;exitX=1;exitY=0.5;exitPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="6" target="51" edge="1">
      <mxGeometry x="381" y="28.5" width="100" height="100" as="geometry">
        <mxPoint x="750" y="447" as="sourcePoint"/>
        <mxPoint x="765.395" y="318.5" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="545" y="400"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="11" value="yes" style="text;fontColor=#001933;fontStyle=0;html=1;strokeColor=none;gradientColor=none;fillColor=none;strokeWidth=2;" parent="1" vertex="1">
      <mxGeometry x="370" y="390" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="12" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="6" target="4" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="13" value="order material" style="shape=mxgraph.flowchart.data;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="240.5" y="640" width="159" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="14" value="no" style="text;fontColor=#001933;fontStyle=0;html=1;strokeColor=none;gradientColor=none;fillColor=none;strokeWidth=2;align=center;" parent="1" vertex="1">
      <mxGeometry x="320" y="447" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="15" value="final project" style="shape=mxgraph.flowchart.document;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="480" y="515" width="140" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="16" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;exitX=0.905;exitY=0.5;exitPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="4" target="15" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="17" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="4" target="13" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="18" value="material&#10;balance" style="shape=mxgraph.flowchart.predefined_process;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="480" y="635" width="190" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="19" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;exitX=0.905;exitY=0.5;exitPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="13" target="18" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="20" value="organize &#10;workforce" style="shape=mxgraph.flowchart.manual_input;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="242" y="780" width="158" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="21" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;entryX=0.5;entryY=0.195;entryPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="13" target="20" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="22" value="create Gantt&#10;diagram" style="shape=mxgraph.flowchart.document;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="240.5" y="920" width="159" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="23" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;exitX=0.5;exitY=1;exitPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="20" target="22" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="24" value="late&#10;project&#10;changes?" style="shape=mxgraph.flowchart.decision;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="261.5" y="1080" width="119" height="78.5" as="geometry"/>
    </mxCell>
    <mxCell id="25" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;exitX=0.5;exitY=0.9;exitPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="22" target="24" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="26" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;exitX=0;exitY=0.5;exitPerimeter=0;entryX=0;entryY=0.5;entryPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="28" target="6" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="160" y="850"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="27" value="yes" style="text;fontColor=#001933;fontStyle=0;html=1;strokeColor=none;gradientColor=none;fillColor=none;strokeWidth=2;" parent="1" vertex="1">
      <mxGeometry x="280" y="1158.5" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="28" value="investor&#10;disapproves&#10; investment?" style="shape=mxgraph.flowchart.decision;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="255" y="1210" width="130" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="29" value="agreement?" style="shape=mxgraph.flowchart.decision;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="510" y="1210" width="130" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="30" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;exitX=0.5;exitY=1;exitPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="24" target="28" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="31" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;exitX=1;exitY=0.5;exitPerimeter=0;entryX=0;entryY=0.5;entryPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="28" target="29" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="32" value="terminate&#10;contract&#10;" style="shape=mxgraph.flowchart.merge_or_storage;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="760" y="1300" width="130" height="80.5" as="geometry"/>
    </mxCell>
    <mxCell id="33" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;entryX=0.5;entryY=0;entryPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="29" target="32" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="740" y="1260"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="34" value="create&#10;status&#10;report" style="shape=mxgraph.flowchart.data;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="240.5" y="1490" width="159" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="35" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.5;exitY=1;exitPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="28" target="34" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="36" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.5;exitY=1;exitPerimeter=0;entryX=0.5;entryY=0;entryPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="29" target="34" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="37" value="project&#10;complete?" style="shape=mxgraph.flowchart.decision;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="271" y="1621.5" width="98" height="57" as="geometry"/>
    </mxCell>
    <mxCell id="38" value="create&#10;final&#10;report" style="shape=mxgraph.flowchart.data;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="240.5" y="1730" width="159" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="39" value="issue&#10;bill of works" style="shape=mxgraph.flowchart.predefined_process;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="560" y="1725" width="190" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="40" value="end" style="shape=mxgraph.flowchart.terminator;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="260" y="1910" width="120" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="41" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.5;exitY=1;exitPerimeter=0;entryX=0.5;entryY=0;entryPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="34" target="37" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="42" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.5;exitY=1;exitPerimeter=0;entryX=0.5;entryY=0;entryPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="37" target="38" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="43" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.5;exitY=1;exitPerimeter=0;entryX=0.5;entryY=0;entryPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="38" target="40" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="44" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.905;exitY=0.5;exitPerimeter=0;entryX=0;entryY=0.5;entryPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="38" target="39" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="45" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;exitX=1;exitY=0.5;exitPerimeter=0;entryX=0.905;entryY=0.5;entryPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="24" target="34" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="950" y="1320"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="46" value="no" style="text;fontColor=#001933;fontStyle=0;html=1;strokeColor=none;gradientColor=none;fillColor=none;strokeWidth=2;" parent="1" vertex="1">
      <mxGeometry x="380.5" y="1093.25" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="47" value="yes" style="text;fontColor=#001933;fontStyle=0;html=1;strokeColor=none;gradientColor=none;fillColor=none;strokeWidth=2;" parent="1" vertex="1">
      <mxGeometry x="385" y="1234" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="48" value="no" style="text;fontColor=#001933;fontStyle=0;html=1;strokeColor=none;gradientColor=none;fillColor=none;strokeWidth=2;align=center;" parent="1" vertex="1">
      <mxGeometry x="320" y="1310" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="49" value="yes" style="text;fontColor=#001933;fontStyle=0;html=1;strokeColor=none;gradientColor=none;fillColor=none;strokeWidth=2;align=center;" parent="1" vertex="1">
      <mxGeometry x="575" y="1310" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="50" value="no" style="text;fontColor=#001933;fontStyle=0;html=1;strokeColor=none;gradientColor=none;fillColor=none;strokeWidth=2;" parent="1" vertex="1">
      <mxGeometry x="640" y="1234" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="51" value="iron out&#10;obscurities &#10;with investor" style="shape=mxgraph.flowchart.paper_tape;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;gradientColor=none;gradientDirection=north;fontColor=#001933;fontStyle=0;html=1;" parent="1" vertex="1">
      <mxGeometry x="470" y="300" width="150" height="81" as="geometry"/>
    </mxCell>
    <mxCell id="52" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;exitX=0.5;exitY=0.09;exitPerimeter=0;entryX=0.905;entryY=0.5;entryPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="51" target="5" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="545" y="300"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="53" value="yes" style="text;fontColor=#001933;fontStyle=0;html=1;strokeColor=none;gradientColor=none;fillColor=none;strokeWidth=2;align=center;" parent="1" vertex="1">
      <mxGeometry x="321" y="1680" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="54" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;exitX=0;exitY=0.5;exitPerimeter=0;entryX=0.095;entryY=0.5;entryPerimeter=0;fontColor=#001933;fontStyle=1;strokeColor=#003366;strokeWidth=1;html=1;" parent="1" source="37" target="5" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="120" y="970"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="55" value="no" style="text;fontColor=#001933;fontStyle=0;html=1;strokeColor=none;gradientColor=none;fillColor=none;strokeWidth=2;" parent="1" vertex="1">
      <mxGeometry x="235" y="1624" width="40" height="26" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
